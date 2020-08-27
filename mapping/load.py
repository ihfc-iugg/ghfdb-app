import os
from django.contrib.gis.utils import LayerMapping
from .models import Country, Continent, Sea, Margin, Basin, Political


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))


world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'poly' : 'MULTIPOLYGON',
}

world_dir = os.path.join(DATA_DIR,'TM_WORLD_BORDERS-0.3','TM_WORLD_BORDERS-0.3.shp')

def world_borders(verbose=True):
    lm = LayerMapping(Country, world_dir, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


continents_dir = os.path.join(DATA_DIR,'continents','World_Continents.shp')

continents_mapping = {
    'objectid': 'OBJECTID',
    'name': 'CONTINENT',
    'sqmi': 'SQMI',
    'sqkm': 'SQKM',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'poly': 'MULTIPOLYGON',
}

def continents(verbose=True):
    lm = LayerMapping(Continent, continents_dir, continents_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


world_seas_dir = os.path.join(DATA_DIR,'seas','World_Seas_IHO_v3.shp')

seas_mapping = {
    'name': 'NAME',
    'id': 'ID',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'min_x': 'min_X',
    'min_y': 'min_Y',
    'max_x': 'max_X',
    'max_y': 'max_Y',
    'area': 'area',
    'mrgid': 'MRGID',
    'poly': 'MULTIPOLYGON',
}

def seas(verbose=True):
    lm = LayerMapping(Sea, world_seas_dir, seas_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

margin_dir = os.path.join(DATA_DIR,'margins','ContinentalMargins.shp')

margin_mapping = {
    'id': 'Uniq_ID',
    'area': 'Area',
    'perimetre': 'PERIMETRE',
    'superficie': 'SUPERFICIE',
    'poly': 'MULTIPOLYGON',
}

def margins(verbose=True):
    lm = LayerMapping(Margin, margin_dir, margin_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)




basin_dir = os.path.join(DATA_DIR,'basins','basins.shp')
basin_mapping = {
    'id': 'OBJECTID',
    'name': 'BASIN_NAME',
    'region': 'BASINS_AND',
    'province': 'PROVINCE_N',
    'max_fill': 'MAX_FILL_K',
    'exploration_status': 'EXP_STATUS',
    'location': 'LOCATION',
    'sub_regime_group': 'SUB_REGIME',
    'sub_regime': 'SUB_REGI_1',
    'petsys_status': 'PET_SYS_ST',
    'poly': 'MULTIPOLYGON',
}
def basins(verbose=True):
    lm = LayerMapping(Basin, basin_dir, basin_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


political_dir = os.path.join(DATA_DIR,'political','EEZ_Land_v3_202030.shp')
political_mapping = {
    'name': 'UNION',

    'territory': 'TERRITORY1',
    'iso_territory': 'ISO_TER1',
    'un_territory': 'UN_TER1',

    'sovereign': 'SOVEREIGN1',
    'iso_sovereign': 'ISO_SOV1',
    'un_sovereign': 'UN_SOV1',

    'area_km2': 'AREA_KM2',
    'geom': 'MULTIPOLYGON',
}

def political(verbose=True):
    lm = LayerMapping(Political, political_dir, political_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)