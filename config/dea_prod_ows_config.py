from s1_cfg import s1_layer_group

ows_cfg = {
    "global": {
        "title": "DEA Prod-Like OWS.",
        "info_url": "http://localhost",
        "services": {"wms": True, "wcs": False, "wmts": False},
        "response_headers": {"Access-Control-Allow-Origin": "*"},
        "allowed_urls": ["http://localhost"],
        "published_CRSs": {
            "EPSG:3857": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},
            "EPSG:32756": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3031": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
    },
    "wms": {"max_height": 512, "max_width": 512},
    "layers": [s1_layer_group],
}
