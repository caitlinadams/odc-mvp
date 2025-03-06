# ODC Only

## Clone required code bases
These will be used to build from source.

```
mkdir codebases
cd codebases
git clone https://github.com/opendatacube/datacube-core.git
git clone https://github.com/opendatacube/eo-datasets.git
cd ..
```

## Conda environment
```
cd odc-mvp
micromamba create -f environment.yml
micromamba activate deantmvp
cd ../
```

### Install codebases
#### Open Data Cube
```
cd codebases/datacube-core
git checkout 1.9.0-rc11
pip install --upgrade '.[test]'
./check-code.sh
cd ../
```
#### eo-datasets
```
cd eo-datasets
git checkout integrate-1.9
pip install .
cd ../../odc-mvp
```

## PostGIS Container

This repository uses PostGIS as the database. 
In a new terminal:

```
cd odc-mvp
docker compose up postgis
```

This will start the database container.
If you want to run it in the background, instead run:

```
docker compose up -d postgis
```

## Open Data Cube

Create a local Open Data Cube (using the 1.9 release candidate)

### Update datacube conf file to point at postgis database
```
vim ~/.datacube.conf
```
Add the following:
```
[default]
db_hostname:localhost
db_database: antarctica
index_driver: postgis
db_username: ant
db_password: antarcticapassword
```
These values are chosen to match the configuration for the PostGIS database that are contained in the `compose.yml` file.

### Initialise and check the system
```
datacube system init
datacube system check
```

## Add products and index datasets

* [Antarctica: pyroSAR+GAMMA](indexing/pyrosar_gamma.md)
* [Australia: COMPASS+ISCE3](indexing/compass_isce3.md)