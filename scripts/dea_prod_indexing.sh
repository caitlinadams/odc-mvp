datacube system init

# ADD required product metadata
datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c0/product_metadata/eo3_s1_nrb.odc-type.yaml

# ADD products
# vv+vh
datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c0/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_vv_vh_0.odc-product.yaml
# vv
datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c0/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_vv_0.odc-product.yaml
# hh+hv
datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c0/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_hh_hv_0.odc-product.yaml
# hh
datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/refs/heads/s1-nrb-c0/products/baseline_satellite_data/s1-nrb/ga_s1_nrb_iw_hh_0.odc-product.yaml

# Sentinel-1 test data
# Australia - VV+VH
# Harvey Bay 2025/03/02
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/for_zhengshu/ga_s1_nrb_iw_vv_vh_0/t147_314828_iw2/2025/03/27/ga_s1a_nrb_0-1-0_T147-314828-IW2_20250327T191344Z_stac-item.json ga_s1_nrb_iw_vv_vh_0
# Australia - VV
# Rockhampton 2024/07/04
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/for_zhengshu/ga_s1_nrb_iw_vv_0/t111_238273_iw2/2024/07/04/ga_s1a_nrb_0-1-0_T111-238273-IW2_20240704T083431Z_stac-item.json ga_s1_nrb_iw_vv_0
# Australia - HH
# Rockhampton 2024/07/16
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/for_zhengshu/ga_s1_nrb_iw_hh_0/t111_238273_iw2/2024/07/16/ga_s1a_nrb_0-1-0_T111-238273-IW2_20240716T083430Z_stac-item.json ga_s1_nrb_iw_hh_0
# Aurstralia - HH+HV
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/for_zhengshu/ga_s1_nrb_iw_hh_hv_0/t111_238269_iw3/2025/04/24/ga_s1a_nrb_0-1-0_T111-238269-IW3_20250424T083300Z_stac-item.json ga_s1_nrb_iw_hh_hv_0

# Antarctica - HH
# Amery 2021/04/24
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/baseline/antarctica/ga_s1_nrb_iw_hh_0/t072_154199_iw1/2021/04/24/ga_s1a_nrb_0-1-0_T072-154199-IW1_20210424T160916Z_stac-item.json ga_s1_nrb_iw_hh_0
# George VI 2018/02/22  
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/baseline/antarctica/ga_s1_nrb_iw_hh_0/t169_362391_iw2/2018/02/22/ga_s1a_nrb_0-1-0_T169-362391-IW2_20180222T073947Z_stac-item.json ga_s1_nrb_iw_hh_0
# Shackleton 2020/02/15
s3-to-dc --stac --convert-bools --no-sign-request s3://deant-data-public-dev/experimental/baseline/antarctica/ga_s1_nrb_iw_hh_0/t041_087655_iw1/2020/02/15/ga_s1a_nrb_0-1-0_T041-087655-IW1_20200215T131002Z_stac-item.json ga_s1_nrb_iw_hh_0



# sleep infinity