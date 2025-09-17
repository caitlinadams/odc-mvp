datacube system init

# ADD required product metadata
datacube metadata add /src/dea-config/product_metadata/eo3_s1_nrb.odc-type.yaml 

# S1 Test Data
datacube product add /src/dea-config/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_vv_vh_0.odc-product.yaml

# Existing scene from Australian Continental run, no changes to metadata
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/local_production_environment_data/ga_s1_nrb_iw_vv_vh_0/t147_314936_iw2/2025/06/*/ga_s1a_nrb_0-1-0_T147-314936-IW2_20250619T191840Z_stac-item.json ga_s1_nrb_iw_vv_vh_0

# sleep infinity