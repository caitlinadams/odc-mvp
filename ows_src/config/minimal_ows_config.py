ows_cfg = {
    "global": {
        "title": "Sample OGC WMS.",
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
    "layers": [
        {
            "title": "Antarctica",
            "abstract": "DE Antarctica Data",
            "layers": [
                {
                    "title": "RTC Backscatter",
                    "abstract": "RTC Backscatter produced with PyroSAR+GAMMA",
                    "name": "rtc_backscatter",
                    "product_name": "s1_pyrosar_gamma_backscatter",
                    "native_crs": "EPSG:3031",
                    "native_resolution": [40, -40],
                    "bands": {"hh": [], "hv": []},
                    "resource_limits": {
                        "zoomed_out_fill_colour": [150, 180, 200, 160],
                        "min_zoom_level": 7,
                        "max_datasets": 12,
                    },
                    "image_processing": {
                        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
                        "always_fetch_bands": [],
                        "manual_merge": False,
                    },
                    "styling": {
                        "default_style": "hh",
                        "styles": [
                            {
                                "name": "hh",
                                "title": "Backscatter HH",
                                "abstract": "Backscatter HH",
                                "components": {
                                    "red": {"hh": 1},
                                    "green": {"hh": 1},
                                    "blue": {"hh": 1},
                                },
                                "scale_range": [-26, 26],
                            },
                            {
                                "name": "hv",
                                "title": "Backscatter HV",
                                "abstract": "Backscatter HV",
                                "components": {
                                    "red": {"hv": 1},
                                    "green": {"hv": 1},
                                    "blue": {"hv": 1},
                                },
                                "scale_range": [-26, 26],
                            },
                        ],
                    },
                }
            ],
        },
    ],
}
