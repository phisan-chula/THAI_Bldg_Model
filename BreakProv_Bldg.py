#
#
#
import pandas as pd
import geopandas as gpd
from zipfile import ZipFile
from pathlib import Path
import sys,time

def Read_Glob_Bldg( country_geojson ):
    CACHE = './PICKLE'
    DIR = Path( '/home/phisan/GeoData/GlobML_BldgFP' )
    GEOJSON = DIR.joinpath( country_geojson ) 

    STEM = GEOJSON.stem
    PICKLE = GEOJSON.parents[0].joinpath( CACHE, STEM+'.bz2' ) 

    if PICKLE.is_file(): 
        print( f'Reading cached "{PICKLE}"...' )
        df = pd.read_pickle( PICKLE )
    else:
        print( f'Reading "{GEOJSON}" might take time ...' )
        df = gpd.read_file( GEOJSON )
        print( f'Writing cache "{PICKLE}"...')
        df.to_pickle( PICKLE, compression='infer' )
    return df

def Read_GADM( SYMB ):
    ''' SYMB =   THA | LAO '''
    SHP = f'/home/phisan/GeoData/GADM/{SYMB}/gadm40_{SYMB}_1.shp'
    df = gpd.read_file( SHP )
    return df
    #import pdb; pdb.set_trace()

def MakeCentroid( dfBLDG, SYMB ):
    FILE_CEN = Path(f'CACHE/dfCENTR_{SYMB}.bz2')
    if FILE_CEN.is_file():
        print( f'Reading cached "{FILE_CEN}"...' )
        dfCENTR = pd.read_pickle( FILE_CEN )
    else:
        print( f'Caculate centroid ...' )
        dfCENTR = dfBLDG[['geometry']].copy()
        dfCENTR['geometry'] = dfCENTR['geometry'].centroid
        print( f'Writing "{FILE_CEN}" ...' )
        dfCENTR.to_pickle( FILE_CEN, compression='infer' )
    return dfCENTR

#################################################################
#################################################################
#################################################################
FR,TO = int(sys.argv[1]) , int(sys.argv[2])

COUNTRY = 'Thailand.geojsonl', 'THA'
#COUNTRY = 'Laos.geojsonl', 'LAO'
dfADM =  Read_GADM( COUNTRY[1] )
for i in range(FR,TO): 
    PROV = dfADM.iloc[i:i+1]
    print( f'Check processing {i}  {PROV.iloc[0].NAME_1} ok...' )
#import pdb; pdb.set_trace()

dfBLDG = Read_Glob_Bldg( COUNTRY[0] )
dfCENTR = MakeCentroid( dfBLDG, COUNTRY[1] )
for i in range(FR,TO): 
    print( '===========================================')
    BEG = time.time()
    PROV = dfADM.iloc[i:i+1]
    print( f'Processing {i}  {PROV.iloc[0].NAME_1} ' )
    PROV_NAME = PROV.iloc[0].NAME_1
    xmin,ymin,xmax,ymax = PROV.total_bounds
    dfCENTR_ = dfCENTR.cx[xmin:xmax, ymin:ymax].copy()
    #import pdb; pdb.set_trace()
    df_bldg_prov = gpd.sjoin( dfCENTR_, PROV, how='inner', predicate='intersects' )  
    if len(df_bldg_prov)>0:
        df_bldg_prov.to_file( f'CACHE/{i}_{PROV_NAME}.gpkg', driver='GPKG', 
                                layer='Bldg_Centroid' )
        dfBLDG.loc[df_bldg_prov.index].to_file( f'CACHE/{i}_{PROV_NAME}.gpkg', 
                                driver='GPKG', layer='Bldg_Polygon' )
    SUM_PROV = len( df_bldg_prov )
    print( f'Buildings in province : {SUM_PROV:,} ...' )
    END = time.time(); ELAP = END-BEG; print( f'{ELAP:,.0f} sec')


print( '=================== Finish ====================')
