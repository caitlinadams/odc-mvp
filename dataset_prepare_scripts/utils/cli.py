import click
import boto3
from mypy_boto3_s3 import S3Client
from typing import cast

from dataset_prepare_scripts.utils.aws_s3 import (
    copy_file,
    get_static_href,
    update_stac_href,
)


@click.command()
@click.argument("data-prefix", type=str)
@click.option("--source-bucket", type=str, default="deant-data-public-dev")
@click.option("--source-project-prefix", type=str, default="experimental/for_zhengshu/")
@click.option("--destination-bucket", type=str, default="deant-data-public-dev")
@click.option(
    "--destination-project-prefix",
    type=str,
    default="experimental/local_production_environment_data/",
)
@click.option("--copy-static", default=False, is_flag=True)
def copy_and_update_burst(
    source_bucket: str,
    source_project_prefix: str,
    destination_bucket: str,
    destination_project_prefix: str,
    data_prefix: str,
    copy_static: bool,
):
    # Set up boto3 client
    s3 = cast(S3Client, boto3.client("s3"))

    # List objects in source data folder
    source_data_prefix = "".join([source_project_prefix, data_prefix])
    response = s3.list_objects_v2(Bucket=source_bucket, Prefix=source_data_prefix)

    # Iterate through each object in the source data folder
    print("Copying NRB layers")
    for obj in response.get("Contents", []):

        # Update the destination key for the object. Same as the source key, but with the project prefix changed
        source_key = obj.get("Key", None)
        if source_key is not None:
            destination_key = source_key.replace(
                source_project_prefix, destination_project_prefix
            )
        else:
            raise KeyError("'Key' not found in object contents")

        # Destination file name
        source_file_name = source_key.rpartition("/")[-1]
        destination_file_name = destination_key.rpartition("/")[-1]

        # Copy the file
        copy_file(s3, source_bucket, source_key, destination_bucket, destination_key)

        # Check if the object is a stac item, if so, check if static layers should be copied
        if ("stac-item.json" in source_file_name) and (copy_static):
            print("Copying static layers")
            (
                static_layer_bucket,
                static_layer_project_prefix,
                static_layer_data_prefix,
            ) = get_static_href(s3, source_bucket, source_key)

            # List objects in static layer data folder
            static_layer_prefix = "".join(
                [static_layer_project_prefix, static_layer_data_prefix]
            )
            static_layer_response = s3.list_objects_v2(
                Bucket=static_layer_bucket, Prefix=static_layer_prefix
            )

            # Iterate through each object in the source data folder
            for obj in static_layer_response.get("Contents", []):

                # Update the destination key for the object. Same as the source key, but with the project prefix changed
                static_source_key = obj.get("Key", None)
                if static_source_key is not None:
                    static_destination_key = static_source_key.replace(
                        static_layer_project_prefix, destination_project_prefix
                    )
                else:
                    raise KeyError("'Key' not found in object contents")

                # Destination file name
                static_source_file_name = static_source_key.rpartition("/")[-1]
                static_destination_file_name = static_destination_key.rpartition("/")[
                    -1
                ]

                # Copy the file
                copy_file(
                    s3,
                    static_layer_bucket,
                    static_source_key,
                    destination_bucket,
                    static_destination_key,
                )

                if "stac-item.json" in static_destination_file_name:
                    print("Updating hrefs in static layer json")
                    update_stac_href(
                        s3,
                        destination_bucket,
                        static_destination_key,
                        target_string=static_layer_project_prefix,
                        replacement_string=destination_project_prefix,
                    )

        # Check if the object is a stac item, if so, update the asset hrefs
        if "stac-item.json" in destination_file_name:
            print("Updating hrefs in NRB json")
            update_stac_href(
                s3,
                destination_bucket,
                destination_key,
                target_string=source_project_prefix,
                replacement_string=destination_project_prefix,
            )


if __name__ == "__main__":
    copy_and_update_burst()
