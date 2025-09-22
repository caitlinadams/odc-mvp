# Docker compose for local Digital Earth Australia production and development ODC environments.

This repository contains docker compose files and accompanying scripts and notebooks to create a local instance of Digital Earth Australia's production or development Open Data Cube (ODC) environments.
The purpose is to support simple testing of new products prior to integrating these fully into development or production.

> **_NOTE:_** Production-like docker compose has been well-tested. Development-like docker compose is still under construction.

## Set up

1. Ensure you have `docker` and `docker-compose` installed
1. Clone this repository
1. Set up a Python virtual environment
    * Option 1: use `conda` to install the appropriate `environment.yaml` file
    * Option 2: use `pixi` to install the project (provides access to additional functionality)

## Simple launch with docker-compose
There are two docker compose files:
* Production-like environment: [docker-compose-dea-prod.yml](docker-compose-dea-prod.yml)
* Development-like environment: [docker-compose-dea-dev.yml](docker-compose-dea-dev.yml)

Each environment contains:
* A postgres+postgis database
* A service for indexing data
* A service for OWS
* A service for Explorer

If indexing from AWS, you may need to log into AWS on your command line.

### Launch the production-like environment
run `docker compose -f docker-compose-dea-prod.yml up` to start all services.
Alternatively, if using [pixi](https://pixi.sh/latest/) you can run `pixi run prod-up`.

Versions of services are as follows:
* Database: [postgis/postgis:16-3.4](https://hub.docker.com/layers/postgis/postgis/16-3.4/images/sha256-fdabb7985ea8963bbc0256807e8ca5e9b86b85f35d9fbe683aff57fcce09cc98)
* Indexing: [opendatacube/datacube-index:0.2.1](https://hub.docker.com/layers/opendatacube/datacube-index/0.2.1/images/sha256-9baa74025f93ce054f1ec377fd65a93949f7d9f4df93c02e61537946254c48ca)
* OWS: [opendatacube/ows:1.8.42](https://hub.docker.com/layers/opendatacube/ows/1.8.42/images/sha256-ffa15513107eb8b7d1b82a354fe3ed075acf89571d292f20a671e98990f697cc)
* Explorer: [opendatacube/explorer:2.12.4](https://hub.docker.com/layers/opendatacube/explorer/2.12.4/images/sha256-ff1885b7e7936d7af38d2468f314f580fa1dd21d50f31b02608987b932894f53)

### Launch the development-like environment
> **_NOTE:_** UNDER CONSTRUCTION
run `docker compose -f docker-compose-dea-dev.yml up` to start all services.
Alternatively, if using [pixi](https://pixi.sh/latest/) you can run `pixi run dev-up`.

* Database: [postgis/postgis:16-3.4](https://hub.docker.com/layers/postgis/postgis/16-3.4/images/sha256-fdabb7985ea8963bbc0256807e8ca5e9b86b85f35d9fbe683aff57fcce09cc98)
* Indexing: [opendatacube/datacube-index:latest](https://hub.docker.com/layers/opendatacube/datacube-index/latest/images/sha256-d9947d2a6f60fdeba3e859c636b0ee0ea3c9a70ac7af7e2375f68a03464b097c)
* OWS: [opendatacube/ows:latest](https://hub.docker.com/layers/opendatacube/ows/latest/images/sha256-668cbb41473c4abdb5eb30a0f32328c34ef9fcfceb312371217c5f17de7319c4)
* Explorer: [opendatacube/explorer:3.0.1](https://hub.docker.com/layers/opendatacube/explorer/3.0.1/images/sha256-604cdb5aee26c258a79a8d46ad9cd261c01b011ab6bd581bf052c1ccf99d70da)

### Ports
Port mapping specified as follows:
* Database: 5432:5432
* OWS: 8080:8080 (http://localhost:8080/?service=wms&request=getcapabilities)
* Explorer: 8000:8000 (http://localhost:8000)

### Shut down
When you are finished, we recommend doing a complete shutdown and removing volumes by running `docker compose -f docker-compose-dea-<prod/dev>.yml down -v`.
Alternatively, if using [pixi](https://pixi.sh/latest/) you can run `pixi run prod-down` or `pixi run dev-down`.

## Customising indexing and OWS

The dataube-index, datacube-ows, and datacube-explorer services all have an associated shell script that is called as their command on launch. 

### Indexing script
