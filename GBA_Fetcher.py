#!/usr/bin/env python3
"""
BldgFetch.py

Fetch GlobalBuildingAtlas buildings from GeoServer WFS by geohash or lat/lng,
and show a 3x3 geohash neighborhood map in Markdown.

CLI:
  -g / --geohash  <gh>                  Fetch by geohash and write <gh>.gpkg
  -l / --latlng   "precision,lat,lng"   Encode lat/lng to geohash (precision digits), then fetch + write
  -z / --zorder   <gh>                  DO NOT fetch. Print 3x3 neighborhood geohash grid (Markdown, no headers)

Examples:
  python BldgFetch.py -g w4rqpt
  python BldgFetch.py -l "6,14.0000,99.0000"
  python BldgFetch.py -z w4rqpt
"""

import argparse
from functools import singledispatchmethod
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pygeohash as pgh
import requests
from pyproj import Transformer
from shapely.geometry import box


class BuildingDataFetcher:
    WFS_URL = "https://tubvsig-so2sat-vm1.srv.mwn.de/geoserver/ows"

    def __init__(self, output_dir: str = "./RESULT/GBA_2019"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # EPSG:4326 (lon/lat) -> EPSG:3857 (meters)
        self.transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)

    @singledispatchmethod
    def fetch(self, arg, *args, **kwargs):
        raise TypeError(f"Unsupported type {type(arg)}")

    @fetch.register
    def _(self, ghash: str):
        ghash = ghash.strip()
        lat_c, lon_c, lat_e, lon_e = pgh.decode_exactly(ghash)
        ghash_poly_4326 = box(lon_c - lon_e, lat_c - lat_e, lon_c + lon_e, lat_c + lat_e)
        self._execute_workflow(ghash, ghash_poly_4326)

    @fetch.register
    def _(self, lat: float, lng: float, precision: int = 6):
        target_ghash = pgh.encode(lat, lng, precision=precision)
        lat_c, lon_c, lat_e, lon_e = pgh.decode_exactly(target_ghash)
        ghash_poly_4326 = box(lon_c - lon_e, lat_c - lat_e, lon_c + lon_e, lat_c + lat_e)
        self._execute_workflow(target_ghash, ghash_poly_4326)

    def _execute_workflow(self, ghash: str, ghash_poly_4326):
        # 1) Project geohash cell bounds to EPSG:3857 for WFS bbox
        minx, miny, maxx, maxy = ghash_poly_4326.bounds
        x1, y1 = self.transformer.transform(minx, miny)
        x2, y2 = self.transformer.transform(maxx, maxy)
        bbox_3857 = f"{x1},{y1},{x2},{y2},EPSG:3857"
        print(f"WxH = {(x2 - x1):,.0f} x {(y2 - y1):,.0f} m")

        params = {
            "service": "WFS",
            "version": "2.0.0",
            "request": "GetFeature",
            "typeNames": "global3D:lod1_global",
            "srsName": "EPSG:3857",
            "bbox": bbox_3857,
            "outputFormat": "application/json",
        }

        try:
            print(f"Fetching {ghash} ...")
            r = requests.get(self.WFS_URL, params=params, timeout=60)
            r.raise_for_status()

            data = r.json()
            feats = data.get("features", [])
            if not feats:
                print(f"*** No buildings in {ghash}")
                return

            gdf = gpd.GeoDataFrame.from_features(feats)

            # GeoServer returns coords in EPSG:3857 because srsName=EPSG:3857
            gdf = gdf.set_crs(epsg=3857, allow_override=True)

            if len(gdf) >= 100_000:
                print(f"*** Overflow: too many buildings in {ghash} ({len(gdf):,})")
                return

            # 2) Centroids in 3857 -> 4326, for within test on geohash cell in 4326
            cent_3857 = gdf.geometry.centroid
            cent_4326 = gpd.GeoSeries(cent_3857, crs="EPSG:3857").to_crs("EPSG:4326")

            # 3) Convert all geometries to 4326 for output
            gdf_4326 = gdf.to_crs(epsg=4326)

            # 4) Spatial filter: keep features whose centroid is within the geohash cell polygon
            mask = cent_4326.within(ghash_poly_4326)
            filtered = gdf_4326.loc[mask].copy()

            # 5) Save
            out = self.output_dir / f"{ghash}.gpkg"
            filtered.to_file(out, driver="GPKG")
            print(f"Success: {len(filtered):,} buildings -> {out}")

        except Exception as e:
            print(f"Error processing {ghash}: {e}")


def parse_latlng(s: str):
    """
    Parse -l/--latlng "precision,lat,lng"
    Example: "6,14.0000,99.0000"
    """
    try:
        parts = [p.strip() for p in s.split(",")]
        if len(parts) != 3:
            raise ValueError("Expected: precision,lat,lng")
        precision = int(parts[0])
        lat = float(parts[1])
        lng = float(parts[2])

        if not (1 <= precision <= 12):
            raise ValueError("precision must be in [1..12]")
        if not (-90.0 <= lat <= 90.0):
            raise ValueError("lat must be in [-90..90]")
        if not (-180.0 <= lng <= 180.0):
            raise ValueError("lng must be in [-180..180]")

        return precision, lat, lng
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid --latlng '{s}': {e}")


def geohash_grid3x3(center: str):
    """
    Return 3x3 grid around center:
      [NW, N, NE]
      [ W, C,  E]
      [SW, S, SE]
    """
    c = center.strip()
    n = pgh.get_adjacent(c, "top")
    s = pgh.get_adjacent(c, "bottom")
    e = pgh.get_adjacent(c, "right")
    w = pgh.get_adjacent(c, "left")
    ne = pgh.get_adjacent(n, "right")
    nw = pgh.get_adjacent(n, "left")
    se = pgh.get_adjacent(s, "right")
    sw = pgh.get_adjacent(s, "left")

    return [
        [nw, n, ne],
        [w,  c, e],
        [sw, s, se],
    ]


def print_geohash_grid_md(center: str):
    grid = geohash_grid3x3(center)
    for row in grid:
        print("| " + " | ".join(row) + " |")


def build_argparser():
    p = argparse.ArgumentParser(
        prog="BldgFetch.py",
        description="Fetch GlobalBuildingAtlas buildings by geohash/latlng; or print a 3x3 geohash neighborhood map.",
    )

    p.add_argument(
        "-o",
        "--outdir",
        default="./RESULT/GBA_2019",
        help="Output directory for .gpkg results (default: ./RESULT/GBA_2019)",
    )

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("-g", "--geohash", help="Fetch by geohash and write <geohash>.gpkg")
    g.add_argument("-l", "--latlng", type=parse_latlng, help='Input "precision,lat,lng" e.g. "6,14.0000,99.0000"')
    g.add_argument("-z", "--zorder", help="Show 3x3 neighborhood geohash map (NO fetch)")

    return p


def main(argv=None) -> int:
    args = build_argparser().parse_args(argv)

    if args.zorder:
        print_geohash_grid_md(args.zorder)
        return 0

    worker = BuildingDataFetcher(output_dir=args.outdir)

    if args.geohash:
        worker.fetch(args.geohash)
        return 0

    if args.latlng:
        precision, lat, lng = args.latlng
        gh = pgh.encode(lat, lng, precision=precision)
        print(f"lat,lng -> geohash: {lat},{lng} (precision={precision}) => {gh}")
        worker.fetch(lat, lng, precision=precision)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

