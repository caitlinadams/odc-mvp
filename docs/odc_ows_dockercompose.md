# ODC + OWS

## Docker compose
The `compose.yml` file describes two services:

* `postgres` - container for the database
* `ows` - container for OWS application and running ODC commands

## Launch the services
In a new terminal, run 
```
docker compose up
```

This will launch both services.

## Initialising the ODC
If running for the first time, the ODC won't be initialised.
You may see the warning:
```
ows-1      | [2025-02-27 02:06:55,415] [ERROR] ODC initialisation of env default failed: 
ows-1      | 
ows-1      | No DB schema exists. Have you run init?
```

If so, you will need to initialise the ODC. 
This can be done by entering the OWS service container.
In a new terminal, run
```
docker compose exec ows bash
```

Once the container has loaded, run
```
datacube system init
datacube system check
```

Exit, and restart the OWS service by running
```
docker compose restart ows
```

## Add products and index datasets

* [Antarctica: pyroSAR+GAMMA](indexing/pyrosar_gamma.md)
* [Australia: COMPASS+ISCE3](indexing/compass_isce3.md)