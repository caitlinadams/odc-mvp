s2_layer = {
    "title": "Australia",
    "abstract": "DE Australia Data",
    "layers": [
        {
            "name": "ga_s2am_ard_3",
            "title": "GA (Sentinel-2)",
            "abstract": "Geoscience Australia Sentinel-2",
            "product_name": "ga_s2am_ard_3",
            "native_crs": "EPSG:3577",
            "native_resolution": [10.0, -10.0],
            "bands": {
                "nbart_coastal_aerosol": [
                    "nbart_coastal_aerosol",
                    "coastal_aerosol",
                    "nbart_narrow_blue",
                    "narrow_blue",
                ],
                "nbart_blue": ["nbart_blue", "blue"],
                "nbart_green": ["nbart_green", "green"],
                "nbart_red": ["nbart_red", "red"],
                "nbart_red_edge_1": ["nbart_red_edge_1", "red_edge_1"],
                "nbart_red_edge_2": ["nbart_red_edge_2", "red_edge_2"],
                "nbart_red_edge_3": ["nbart_red_edge_3", "red_edge_3"],
                "nbart_nir_1": ["nbart_nir_1", "nir", "nir_1", "nbart_near_infrared_1"],
                "nbart_nir_2": ["nbart_nir_2", "nir_2", "nbart_near_infrared_2"],
                "nbart_swir_2": [
                    "nbart_swir_2",
                    "swir_2",
                    "nbart_shortwave_infrared_2",
                ],
                "nbart_swir_3": [
                    "nbart_swir_3",
                    "swir_3",
                    "nbart_shortwave_infrared_3",
                ],
                "oa_fmask": ["oa_fmask", "fmask"],
                "oa_s2cloudless_mask": ["oa_s2cloudless_mask", "s2cloudless_mask"],
                "oa_s2cloudless_prob": ["oa_s2cloudless_prob", "s2cloudless_prob"],
            },
            "resource_limits": {
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "min_zoom_level": 8.0,
                "max_datasets": 12,
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": [
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {"red": 1.0},
                            "green": {"green": 1.0},
                            "blue": {"blue": 1.0},
                        },
                        "scale_range": [0.0, 3000.0],
                    },
                ],
            },
        }
    ],
}
