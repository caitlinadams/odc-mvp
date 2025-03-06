# Indexing example data over Australia

## Running `datacube` commands
The following steps require you to run `datacube` commands.
Depending on how you are using the `datacube` library, you may need to take one of the following additional steps:

### In a conda environment
If using the conda environment, activate the environment (see [Conda instructions](../odc_conda.md))

### Using docker compose
If using docker compose, exec into the ows container (see [docker compose instructions](../odc_ows_dockercompose.md))

## Add the product definition
```
datacube product add /src/products/sentinel1/s1_compass_isce3_backscatter.yml
```

## Create the dataset metadata 
### Copy the data file
Download `OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY.tif` from [DEAnt Public Bucket](https://deant-data-public-dev.s3.ap-southeast-2.amazonaws.com/index.html?prefix=experimental/COMPASS-ISCE3/glo_30/S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185/)

Then add the file to 
```
odc-mvp/data/sentinel1/compass/isce3/OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY.tif
```

If running ODC in the `ows` docker compose service, restart the service using `docker compose restart ows`.

### Produce the dataset metadata document
These should already come with the repository, but if you need to recreate them, run

```
python dataset_prepare_scripts/prepare_s1_compass_isce3_backscatter.py 
```

### Add dataset document to ODC
```
datacube dataset add /src/data/sentinel1/compass/isce3/OPERA_L2_RTC-S1A_IW_SLC__1SDV_20220106T191355_20220106T191422_041344_04EA48_E185_CSLC_BACKSCATTER_TRY_-odc-metadata.yaml
```