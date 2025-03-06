from datetime import datetime
from pathlib import Path
import re
import os

from eodatasets3 import DatasetPrepare


def parse_scene_file_dates(scene_id: str) -> tuple[datetime, datetime]:

    # Regex pattern to match the dates
    pattern = r"(?P<start_date>\d{8}T\d{6})_" r"(?P<stop_date>\d{8}T\d{6})_"

    match = re.search(pattern, scene_id)

    if not match:
        raise ValueError("The input string does not match the expected format.")

    start_date = datetime.strptime(match.group("start_date"), "%Y%m%dT%H%M%S")
    stop_date = datetime.strptime(match.group("stop_date"), "%Y%m%dT%H%M%S")

    return (start_date, stop_date)


def prepare_dataset(date: datetime, hh_tile: Path, hv_tile: Path, output_path: str):

    with DatasetPrepare(metadata_path=output_path) as p:
        p.product_name = "s1_pyrosar_gamma_backscatter"
        p.datetime = date
        p.processed_now()

        p.properties["odc:file_format"] = (
            "GeoTIFF"  # Got a warning if this wasn't included
        )

        p.note_measurement("hh", path=hh_tile)
        p.note_measurement("hv", path=hv_tile)

        p.done()


def main():

    script_dir = Path(__file__).parent
    repo_dir = script_dir.parent
    data_dir = repo_dir.joinpath("data")
    collection_path = data_dir.joinpath("sentinel1/pyrosar/gamma")

    tiles = [f for f in collection_path.iterdir() if f.is_dir()]

    for tile in tiles:
        tile_start_datetime, tile_end_datetime = parse_scene_file_dates(tile.stem)

        hh_file = None
        hv_file = None

        # Loop over files in the folder
        for file in tile.iterdir():
            if file.suffix == ".tif":
                if file.stem.endswith("_HH_grd_mli_gamma0-rtc_geo_db_3031"):
                    hh_file = file
                elif file.stem.endswith("_HV_grd_mli_gamma0-rtc_geo_db_3031"):
                    hv_file = file

        if hh_file and hv_file:
            common_prefix = hh_file.stem.removesuffix(
                "_HH_grd_mli_gamma0-rtc_geo_db_3031"
            )
            output_file = tile / f"{common_prefix}-odc-metadata.yaml"

            prepare_dataset(tile_start_datetime, hh_file, hv_file, output_file)
        else:
            print(f"didn't find files for tile: {tile.stem}")


if __name__ == "__main__":
    main()
