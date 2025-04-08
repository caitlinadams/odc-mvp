datacube system init

datacube-ows-update --schema

datacube product add /src/products/sentinel1/s1_pyrosar_gamma_backscatter.yml

for dir in /src/data/sentinel1/pyrosar/gamma/*/; do find "$dir" -type f -name "*.yaml"; done | while read -r file; do datacube dataset add https://deant-data-public-dev.s3.ap-southeast-2.amazonaws.com/experimental/pyrosar-ew-rtc/${file#/src/data/sentinel1/pyrosar/gamma/}; done

datacube spindex create 3031

datacube spindex update 3031

datacube-ows-update

flask run --host=0.0.0.0 --port=8000