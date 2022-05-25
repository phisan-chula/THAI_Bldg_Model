#
#
#
import pandas as pd
import geopandas as gpd
import subprocess as sp 
import numpy as np
from tabulate import tabulate
from io import StringIO
from pathlib import Path

def GetNumBldg( df ):
    numbld = list()
    CMD = '''ogrinfo -so "{}" Bldg_Centroid | grep "Feature Count:"'''
    folder = Path( 'BldgFtPrn_20142021' )
    df['NumBldg'] = 0
    for i in folder.glob('*.gpkg'):
        cmd = CMD.format( i )
        res = sp.run( cmd, shell=True, capture_output=True )
        res = res.stdout.decode('utf-8')
        PID = int(i.stem.split('_')[0])
        nbldg = int(res.split(' ')[2])
        df.loc[PID,'NumBldg'] = '{:9,d}'.format(nbldg)
    return df 

def ReadGDrive():
    GID = '1g4TLkb-WBeLPCkER3GcRfiRNDvc99Bjq'
    CMD = f'''gdrive list --max 1000 --query " '{GID}' in parents"'''
    res = sp.run( CMD, shell=True, capture_output=True )
    glist = StringIO( res.stdout.decode('utf-8') )
    df = pd.read_fwf( glist )
    return df 

######################################################################3
######################################################################3
######################################################################3
df = ReadGDrive()

def FmtTab(row):
    PID = int(row['Name'].split('_')[0])
    PNAME = row['Name'].split('_')[1][:-5]
    DNLD = f'[link](https://drive.google.com/file/d/'\
            f'{row.Id}/view?usp=sharing)'
    SIZE = '{:>9s}'.format(row.Size)
    #import pdb; pdb.set_trace()
    return PNAME,PID,SIZE,DNLD
df[['Name','PID','Size','LINK']] = df.apply( FmtTab , axis='columns', result_type='expand' )
df.sort_values( 'PID', ascending=True, inplace=True, ignore_index=True )

df = GetNumBldg( df )

TAB = df[['Name','NumBldg', 'Size', 'LINK' ]].copy()
with open( 'README.md', 'w', encoding='utf-8' ) as f:
    f.write( '#Research on Thai Building Modelling<br/>\n' )
    f.write( tabulate( TAB, headers=TAB.columns, tablefmt='github' ) )
    f.write( '\n<br/>\n' )
#import pdb; pdb.set_trace()
