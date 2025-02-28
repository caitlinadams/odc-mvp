# OWS

If using the [ODC + OWS](../odc_ows_dockercompose.md) instructions, you can create webservices for your indexed data. 

Ensure you have indexed the following products using their instructions:

* [S1 RTC Backscatter for Australia (COMPASS+ISCE3)](../indexing/compass_isce3.md)
* [S1 RTC Backscatter for Antarctica (PyroSAR+GAMMA)](../indexing/pyrosar_gamma.md)

### Exec into OWS containter
To run `datacube` commands, exec into the ows container (see [docker compose instructions](../odc_ows_dockercompose.md))

## Create OWS schema
```
datacube-ows-update --schema
datacube-ows-update
```

## Restart the service and launch the OWS app
```
docker compose restart ows
```

To view the WMS Config, launch `http://localhost:8000/?service=wms&request=getcapabilities`

## Add to Terria
Press upload > my data > web data, and past the above URL.
