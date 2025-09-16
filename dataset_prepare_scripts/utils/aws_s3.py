from mypy_boto3_s3 import S3Client
import json
from urllib.parse import urlparse


def copy_file(
    s3_client: S3Client,
    source_bucket: str,
    source_key: str,
    destination_bucket: str,
    destination_key: str,
):

    # Copy if not already present, otherwise, skip
    try:
        s3_client.head_object(Bucket=destination_bucket, Key=destination_key)
        print(f"    Skipped {destination_key} (already exists)")
    except s3_client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print(
                f"    Copying {source_key} to {destination_key.rpartition("/")[0]+"/"}"
            )
            copy_source = "/".join([source_bucket, source_key])
            s3_client.copy_object(
                CopySource=copy_source,
                Bucket=destination_bucket,
                Key=destination_key,
            )
        else:
            raise


def get_static_href(s3_client: S3Client, source_bucket: str, source_key: str):
    # Get the object name from the destination key
    object_name = source_key.rpartition("/")[-1]

    # Confirm that the destination key being modified is the stac-item.json file
    if "stac-item.json" in object_name:

        source_stac_object = s3_client.get_object(Bucket=source_bucket, Key=source_key)
        source_stac_content = source_stac_object["Body"].read().decode("utf-8")

        source_stac_json_dict = json.loads(source_stac_content)

        static_layer_href = (
            source_stac_json_dict.get("assets", {})
            .get("number_of_looks", {})
            .get("href", None)
        )
        if static_layer_href is not None:
            parsed = urlparse(static_layer_href)
            bucket = parsed.netloc.split(".")[0]

            path_parts = parsed.path.lstrip("/").split("/")

            for i, part in enumerate(path_parts):
                if part.startswith("ga_s1_nrb_iw_"):
                    project_prefix = "/".join(path_parts[:i]) + "/"
                    data_prefix = "/".join(path_parts[i:-1]) + "/"
                    file = path_parts[-1]
                    break

            return bucket, project_prefix, data_prefix
        else:
            raise KeyError(
                "number_of_looks not found in asset list. There may be no static layers for this product"
            )

    else:
        raise ValueError(
            f"Object {object_name} is does not have the suffix 'stac-item.json' and will not be modified."
        )


def update_stac_href(
    s3_client: S3Client,
    destination_bucket: str,
    destination_key: str,
    target_string: str,
    replacement_string: str,
):

    # Get the object name from the destination key
    object_name = destination_key.rpartition("/")[-1]

    # Confirm that the destination key being modified is the stac-item.json file
    if "stac-item.json" in object_name:

        destination_stac_object = s3_client.get_object(
            Bucket=destination_bucket, Key=destination_key
        )
        destination_stac_content = (
            destination_stac_object["Body"].read().decode("utf-8")
        )

        updated_destination_stac_content = destination_stac_content.replace(
            target_string, replacement_string
        )

        s3_client.put_object(
            Bucket=destination_bucket,
            Key=destination_key,
            Body=updated_destination_stac_content.encode("utf-8"),
        )
    else:
        raise ValueError(
            f"Object {object_name} is does not have the suffix 'stac-item.json' and will not be modified."
        )
