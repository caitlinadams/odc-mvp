datacube system init

ADD required product metadata
datacube metadata add /src/dea-config/product_metadata/eo3_s1_ard.odc-type.yaml

# S1 Test Data -- HH from Robinson Ridge
datacube product add /src/dea-config/products/baseline_satellite_data/s1_gamma0/ga_s1_iw_hh_c0.odc-product.yaml
s3-to-dc --stac --no-sign-request s3://deant-data-public-dev/experimental/stac_for_ows/ga_s1_iw_hh_c0/t099_212227_iw2/2022/12/*/metadata.json ga_s1_iw_hh_c0