datacube system init

# COLLECTION 1
# ADD required product metadata
datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c1/product_metadata/eo3_s1_nrb.odc-type.yaml

# ADD products
datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c1/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_vv_vh_1.odc-product.yaml

datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c1/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_hh_1.odc-product.yaml

# ADD test data
# Australia
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/baseline/collection_1_test_data/ga_s1_nrb_iw_vv_vh_1/t045_095837_iw1/2020/11/29/20201129T192619/ga_s1a_nrb_1-0-0_T045-095837-IW1_20201129T192619Z_stac-item.json ga_s1_nrb_iw_vv_vh_1

# Antarctica
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/baseline/collection_1_test_data/ga_s1_nrb_iw_hh_1/t070_149815_iw3/2022/01/01/20220101T124752/ga_s1a_nrb_1-0-0_T070-149815-IW3_20220101T124752Z_stac-item.json ga_s1_nrb_iw_hh_1