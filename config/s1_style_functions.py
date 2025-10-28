import numpy as np
import xarray as xr
from datacube_ows.band_utils import scalable


@scalable
def db(data: xr.Dataset, band: str):
    band_db = 10 * np.log10(data[band])
    band_db = band_db.where(np.isfinite(band_db))

    return band_db


@scalable
def db_difference(data, band1, band2):

    db_band1 = db(data, band1)
    db_band2 = db(data, band2)

    return db_band1 - db_band2
