# MVP for Digital Earth Antarctica Open Data Cube

## Clone repository and set up required repos
```
mkdir deant-mvp
cd deant-mvp
git clone https://github.com/caitlinadams/odc-mvp.git
```
### Set up required folders and other codebases
```
mkdir codebases
cd codebases
git clone https://github.com/opendatacube/datacube-core.git
git clone https://github.com/opendatacube/eo-datasets.git
cd ..
```
## Conda environment
```
cd odc-mvp
micromamba create -f environment.yml
micromamba activate deantmvp
cd ../
```
### Install codebases
#### Open Data Cube
```
cd codebases/datacube-core
git checkout 1.9.0-rc11
pip install --upgrade '.[test]'
./check-code.sh
cd ../
```
#### eo-datasets
```
cd eo-datasets
git checkout integrate-1.9
pip install .
cd ../../odc-mvp
```

## PostGIS Container

This repository uses PostGIS as the database. 
In a new terminal, run `docker compose up` from the `odc-mvp` directory to start the database.

## Open Data Cube

Create a local Open Data Cube (using the 1.9 release candidate)

### Update datacube conf file to point at postgis database
```
vim ~/.datacube.conf
```
Add the following:
```
[default]
db_hostname:localhost
db_database: antarctica
index_driver: postgis
db_username: ant
db_password: antarcticapassword
```
These values are chosen to match the configuration for the PostGIS database that are contained in the `compose.yml` file.

### Initialise and check the system
```
datacube system init
datacube system check
```

### Add the product definition
```
datacube product add ./products/sentinel1/s1_compass_isce3_backscatter.yml
```

### Create the dataset metadata 
#### Copy the data file
Download `OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY.tif` from [DEAnt Public Bucket](https://deant-data-public-dev.s3.ap-southeast-2.amazonaws.com/index.html?prefix=experimental/COMPASS-ISCE3/glo_30/S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185/)

Then add the file to 
```
odc-mvp/data/sentinel1/compass/isce3/OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY.tif
```

#### Produce the dataset metadata document
```
python dataset_prepare_scripts/prepare_s1_compass_isce3_backscatter.py 
```

#### Add dataset document to ODC
```
datacube dataset add data/sentinel1/compass/isce3/OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY-odc-metadata.yaml
```

### Run notebook to check if product add and dataset add successful