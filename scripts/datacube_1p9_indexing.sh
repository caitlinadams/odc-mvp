datacube system init

# ADD required product metadata
datacube metadata add /src/dea-config/product_metadata/eo3_s1_nrb.odc-type.yaml
datacube metadata add /src/dea-config/product_metadata/eo3_s1_ard.odc-type.yaml

# S1 Test Data -- HH with static layers
datacube product add /src/dea-config/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_hh_c0.odc-product.yaml
s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_nrb_iw_hh_c0/**/metadata.json
# s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_nrb_iw_hh_c0/t099_212227_iw2/2022/12/17/metadata.json

# S1 Test Data -- HH from Robinson Ridge
datacube product add /src/dea-config/products/baseline_satellite_data/s1_gamma0/ga_s1_iw_hh_c0.odc-product.yaml
# s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_iw_hh_c0/**/metadata.json
s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_iw_hh_c0/t099_212227_iw2/2022/12/17/metadata.json

# S1 Test Data -- HH from recent image
datacube product add /src/dea-config/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_hh_0.odc-product.yaml
s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows_recent_image/ga_s1_nrb_iw_hh_0/t002_003629_iw2/2025/4/16/ga_s1a_nrb_v0.1.0_T002-003629-IW2_20250416T204617Z.stac-item.json

# S1 Test Data -- VV+VH from Zheng-Shu run
datacube product add /src/dea-config/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_vv_vh_0.odc-product.yaml
s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/for_zhengshu/ga_s1_nrb_iw_vv_vh_0/t002_003297_iw3/2018/03/06/ga_s1a_nrb_0-1-0_T002-003297-IW3_20180306T203149Z_stac-item.json

# # S1 Test Data -- VV from Landcover
# datacube metadata add /src/dea-config/product_metadata/eo3_s1_ard.odc-type.yaml

# datacube product add /src/dea-config/products/baseline_satellite_data/s1_gamma0/ga_s1_iw_vv_c0.odc-product.yaml

# s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_iw_vv_c0/**/metadata.json

# # S2 GA product
# datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/master/product_metadata/eo3_sentinel_ard.odc-type.yaml

# datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/master/products/baseline_satellite_data/c3/ga_s2am_ard_3.odc-product.yaml

# s3-to-dc --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s2am_ard_3/ga_s2am_ard_3-2-1_49HFB_2022-10-28_nrt.odc-metadata.yaml

datacube spindex create 3031

datacube spindex update 3031