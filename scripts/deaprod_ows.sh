datacube-ows-update --schema --role sar --views

datacube-ows-update

exec gunicorn -b 0.0.0.0:8080 --workers 2 --timeout 120 datacube_ows.wsgi:application