from datetime import datetime
from pathlib import Path
from typing import Optional
import os

from eodatasets3 import DatasetPrepare


def prepare_dataset(linear_tile: Path, db_tile: Path, output_path: str):

    # Hardcode any metadata for now, but ideally use the tile/file structure to get necessary metadata
    dataset_datetime = datetime(2022, 10, 6, 19, 14, 22)

    with DatasetPrepare(metadata_path=output_path) as p:
        p.product_name = "s1_compass_isce3_backscatter"  # Must match the product name in product definition
        p.datetime = dataset_datetime
        p.processed_now()

        p.properties["odc:file_format"] = (
            "GeoTIFF"  # Got a warning if this wasn't included
        )

        p.note_measurement(
            "backscatter_linear", path=linear_tile
        )  # First arg must match measurement in product definition
        p.note_measurement(
            "backscatter_db", path=db_tile
        )  # First arg must match measurement in product definition

        p.done()


def main():

    script_dir = Path(__file__).parent
    repo_dir = script_dir.parent
    data_dir = repo_dir.joinpath("data")
    collection_path = data_dir.joinpath("sentinel1/compass/isce3")
    linear_tiles = collection_path.glob("*LINEAR.tif")
    db_tiles = collection_path.glob("*DB.tif")

    for linear_tile, db_tile in zip(linear_tiles, db_tiles):

        common_prefix = os.path.commonprefix([linear_tile.stem, db_tile.stem])
        output_file = collection_path / f"{common_prefix}-odc-metadata.yaml"

        prepare_dataset(linear_tile, db_tile, output_path=output_file)


if __name__ == "__main__":
    main()
