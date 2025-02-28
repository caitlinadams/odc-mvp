# Indexing example data over Antarctica

## Running `datacube` commands
The following steps require you to run `datacube` commands.
Depending on how you are using the `datacube` library, you may need to take one of the following additional steps:

### In a conda environment
If using the conda environment, activate the environment (see [Conda instructions](../odc_conda.md))

### Using docker compose
If using docker compose, exec into the ows container (see [docker compose instructions](../odc_ows_dockercompose.md))

## Add the product definition
```
datacube product add /src/products/sentinel1/s1_pyrosar_gamma_backscatter.yml
```

## Create the dataset metadata 
### Copy the data file
Download the following scene folders from [DEAnt Public Bucket](https://ap-southeast-2.console.aws.amazon.com/s3/buckets/deant-data-public-dev?region=ap-southeast-2&bucketType=general&prefix=experimental/pyrosar-ew-rtc/&showversions=false)

* S1A_EW_GRDM_1SDH_20210701T150428_20210701T150533_038585_048D91_23E6	
* S1A_EW_GRDM_1SDH_20210806T150430_20210806T150535_039110_049D7D_84BD
* S1A_EW_GRDM_1SDH_20210704T152833_20210704T152942_038629_048EE8_D41F	
* S1A_EW_GRDM_1SDH_20210809T152835_20210809T152939_039154_049F07_CCCC
* S1A_EW_GRDM_1SDH_20210706T151222_20210706T151326_038658_048FD4_8688	
* S1A_EW_GRDM_1SDH_20210811T151224_20210811T151328_039183_049FFD_C9FA
* S1A_EW_GRDM_1SDH_20210708T145617_20210708T145724_038687_0490BA_D480	
* S1A_EW_GRDM_1SDH_20210813T145619_20210813T145724_039212_04A110_8248
* S1A_EW_GRDM_1SDH_20210709T153644_20210709T153749_038702_04912E_7C93	
* S1A_EW_GRDM_1SDH_20210814T153646_20210814T153751_039227_04A198_2620
* S1A_EW_GRDM_1SDH_20210711T152028_20210711T152132_038731_049202_3EA9	
* S1A_EW_GRDM_1SDH_20210816T152030_20210816T152134_039256_04A28A_3D14
* S1A_EW_GRDM_1SDH_20210713T150429_20210713T150533_038760_0492E0_CE10	
* S1A_EW_GRDM_1SDH_20210818T150431_20210818T150535_039285_04A391_1DB0
* S1A_EW_GRDM_1SDH_20210716T152833_20210716T152943_038804_049427_4ED6	
* S1A_EW_GRDM_1SDH_20210821T152835_20210821T152940_039329_04A511_DA41
* S1A_EW_GRDM_1SDH_20210720T145618_20210720T145642_038862_0495FA_0777	
* S1A_EW_GRDM_1SDH_20210823T151225_20210823T151329_039358_04A609_D5F1
* S1A_EW_GRDM_1SDH_20210721T153645_20210721T153749_038877_04966E_C8C0	
* S1A_EW_GRDM_1SDH_20210825T145620_20210825T145724_039387_04A70D_5A57
* S1A_EW_GRDM_1SDH_20210723T152028_20210723T152105_038906_04973E_D3BB	
* S1A_EW_GRDM_1SDH_20210826T153647_20210826T153751_039402_04A790_B049
* S1A_EW_GRDM_1SDH_20210725T150430_20210725T150518_038935_04981C_DBDB	
* S1A_EW_GRDM_1SDH_20210828T152030_20210828T152135_039431_04A87D_C04A
* S1A_EW_GRDM_1SDH_20210728T152834_20210728T152943_038979_04995F_1B28	
* S1A_EW_GRDM_1SDH_20210830T150432_20210830T150536_039460_04A980_A5A0
* S1A_EW_GRDM_1SDH_20210804T152029_20210804T152133_039081_049C87_C251	
* S1A_EW_GRDM_1SDH_20210902T152836_20210902T152940_039504_04AB07_C582

Then add the backsatter tifs in each folder to their respective folder in
```
odc-mvp/data/sentinel1/pyrosar/gamma/
```

If running ODC in the `ows` docker compose service, restart the service using `docker compose restart ows`.

### Produce the dataset metadata document
These should already come with the repository, but if you need to recreate them, run

```
python dataset_prepare_scripts/prepare_s1_pyrosar_gamma_backscatter.py
```

### Add dataset document to ODC
Add the dataset documents recursively:
```
for dir in /src/data/sentinel1/pyrosar/gamma/*/; do find "$dir" -type f -name "*.yaml"; done | while read -r file; do datacube dataset add "$file"; done
```

### Add alternative spatial index
When working with Antarctica data in EPSG:3031, it is valuable to add an extra spatial index to support querying.
```
datacube spindex create 3031
datacube spindex update 3031
```