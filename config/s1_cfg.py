def linear_vv_vh_ratio(data):
    unscaled = data["VV"] / data["VH"]
    normalised = (unscaled - min(unscaled)) / (max(unscaled) - min(unscaled))
    scaled = normalised * 255

    return scaled


s1_layer = {
    "title": "Antarctica",
    "abstract": "DE Antarctica Data",
    "layers": [
        {
            "name": "ga_s1_nrb_iw_vv_vh_0",
            "title": "Data from Zheng-Shu Run",
            "abstract": "Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW HH Collection 0 Updated",
            "product_name": "ga_s1_nrb_iw_vv_vh_0",
            "native_crs": "EPSG:3577",
            "native_resolution": [20, -20],
            "bands": {
                "VV_gamma0": ["VV_gamma0"],
                "VH_gamma0": ["VH_gamma0"],
                "mask": ["mask"],
                "number_of_looks": ["number_of_looks", "n_looks", "nlooks"],
                "gamma0_to_beta0_ratio": ["gamma0_to_beta0_ratio"],
                "gamma0_to_sigma0_ratio": ["gamma0_to_sigma0_ratio"],
                "local_incidence_angle": [
                    "local_incidence_angle",
                    "lia",
                    "LIA",
                ],
                "incidence_angle": ["incidence_angle", "ia", "IA"],
            },
            "resource_limits": {
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "min_zoom_level": 8.0,
                "max_datasets": 12,
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "VV_gamma0",
                "styles": [
                    {
                        "name": "VV_gamma0",
                        "title": "Backscatter VV",
                        "abstract": "Backscatter VV",
                        "components": {
                            "red": {"VV_gamma0": 1},
                            "green": {"VV_gamma0": 1},
                            "blue": {"VV_gamma0": 1},
                        },
                        "scale_range": [0.01, 0.3],
                    },
                    {
                        "name": "mask",
                        "title": "Shadow Layover Mask",
                        "abstract": "Shadow Layover Mask",
                        "components": {
                            "red": {"mask": 1},
                            "green": {"mask": 1},
                            "blue": {"mask": 1},
                        },
                        "scale_range": [0, 3],
                    },
                    {
                        "name": "local_incidence_angle",
                        "title": "LIA",
                        "abstract": "LIA",
                        "components": {
                            "red": {"local_incidence_angle": 1},
                            "green": {"local_incidence_angle": 1},
                            "blue": {"local_incidence_angle": 1},
                        },
                        "scale_range": [0, 90],
                    },
                ],
            },
        },
        {
            "name": "ga_s1_nrb_iw_hh_c0",
            "title": "New product",
            "abstract": "Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW HH Collection 0",
            "product_name": "ga_s1_nrb_iw_hh_c0",
            "native_crs": "EPSG:3031",
            "native_resolution": [20, -20],
            "bands": {
                "HH_gamma0": ["HH_gamma0"],
                "mask": ["mask"],
                "number_of_looks": ["number_of_looks", "n_looks", "nlooks"],
                "gamma0_to_beta0_ratio": ["gamma0_to_beta0_ratio"],
                "gamma0_to_sigma0_ratio": ["gamma0_to_sigma0_ratio"],
                "local_incidence_angle": [
                    "local_incidence_angle",
                    "lia",
                    "LIA",
                ],
                "incidence_angle": ["incidence_angle", "ia", "IA"],
            },
            "resource_limits": {
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "min_zoom_level": 8.0,
                "max_datasets": 12,
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "HH_gamma0",
                "styles": [
                    {
                        "name": "HH_gamma0",
                        "title": "Backscatter HH",
                        "abstract": "Backscatter HH",
                        "components": {
                            "red": {"HH_gamma0": 1},
                            "green": {"HH_gamma0": 1},
                            "blue": {"HH_gamma0": 1},
                        },
                        "scale_range": [0.02, 0.4],
                    },
                    {
                        "name": "mask",
                        "title": "Shadow Layover Mask",
                        "abstract": "Shadow Layover Mask",
                        "components": {
                            "red": {"mask": 1},
                            "green": {"mask": 1},
                            "blue": {"mask": 1},
                        },
                        "scale_range": [0, 3],
                    },
                    {
                        "name": "local_incidence_angle",
                        "title": "LIA",
                        "abstract": "LIA",
                        "components": {
                            "red": {"local_incidence_angle": 1},
                            "green": {"local_incidence_angle": 1},
                            "blue": {"local_incidence_angle": 1},
                        },
                        "scale_range": [0, 90],
                    },
                ],
            },
        },
        {
            "name": "ga_s1_nrb_iw_hh_0",
            "title": "New product - recent image",
            "abstract": "Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW HH Collection 0 Updated",
            "product_name": "ga_s1_nrb_iw_hh_0",
            "native_crs": "EPSG:3031",
            "native_resolution": [20, -20],
            "bands": {
                "HH_gamma0": ["HH_gamma0"],
                "mask": ["mask"],
                "number_of_looks": ["number_of_looks", "n_looks", "nlooks"],
                "gamma0_to_beta0_ratio": ["gamma0_to_beta0_ratio"],
                "gamma0_to_sigma0_ratio": ["gamma0_to_sigma0_ratio"],
                "local_incidence_angle": [
                    "local_incidence_angle",
                    "lia",
                    "LIA",
                ],
                "incidence_angle": ["incidence_angle", "ia", "IA"],
            },
            "resource_limits": {
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "min_zoom_level": 8.0,
                "max_datasets": 12,
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "HH_gamma0",
                "styles": [
                    {
                        "name": "HH_gamma0",
                        "title": "Backscatter HH",
                        "abstract": "Backscatter HH",
                        "components": {
                            "red": {"HH_gamma0": 1},
                            "green": {"HH_gamma0": 1},
                            "blue": {"HH_gamma0": 1},
                        },
                        "scale_range": [0.02, 0.4],
                    },
                    {
                        "name": "mask",
                        "title": "Shadow Layover Mask",
                        "abstract": "Shadow Layover Mask",
                        "components": {
                            "red": {"mask": 1},
                            "green": {"mask": 1},
                            "blue": {"mask": 1},
                        },
                        "scale_range": [0, 3],
                    },
                    {
                        "name": "local_incidence_angle",
                        "title": "LIA",
                        "abstract": "LIA",
                        "components": {
                            "red": {"local_incidence_angle": 1},
                            "green": {"local_incidence_angle": 1},
                            "blue": {"local_incidence_angle": 1},
                        },
                        "scale_range": [0, 90],
                    },
                ],
            },
        },
        {
            "name": "ga_s1_iw_hh_c0",
            "title": "Old product",
            "abstract": "Old Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW HH Collection 0",
            "product_name": "ga_s1_iw_hh_c0",
            "native_crs": "EPSG:3031",
            "native_resolution": [20, -20],
            "bands": {
                "HH": ["HH", "hh", "hh_gamma0"],
                "mask": ["mask"],
            },
            "resource_limits": {
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "min_zoom_level": 8.0,
                "max_datasets": 12,
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "HH",
                "styles": [
                    {
                        "name": "HH",
                        "title": "Backscatter HH",
                        "abstract": "Backscatter HH",
                        "components": {
                            "red": {"HH": 1},
                            "green": {"HH": 1},
                            "blue": {"HH": 1},
                        },
                        "scale_range": [0.02, 0.4],
                    },
                    {
                        "name": "mask",
                        "title": "Shadow Layover Mask",
                        "abstract": "Shadow Layover Mask",
                        "components": {
                            "red": {"mask": 1},
                            "green": {"mask": 1},
                            "blue": {"mask": 1},
                        },
                        "scale_range": [0, 3],
                    },
                ],
            },
        },
        # {
        #     "name": "ga_s1_iw_vv_c0",
        #     "title": "GA Normalised Radar Backscatter IW VV (Sentinel-1)",
        #     "abstract": "Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW VV Collection 0",
        #     "product_name": "ga_s1_iw_vv_c0",
        #     "native_crs": "EPSG:3577",
        #     "native_resolution": [20, -20],
        #     "bands": {
        #         "VV": ["VV", "vv", "vv_gamma0"],
        #         "mask": ["mask"],
        #     },
        #     "resource_limits": {
        #         "zoomed_out_fill_colour": [150, 180, 200, 160],
        #         "min_zoom_level": 8.0,
        #         "max_datasets": 12,
        #     },
        #     "image_processing": {
        #         "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        #         "always_fetch_bands": [],
        #         "manual_merge": False,
        #     },
        #     "styling": {
        #         "default_style": "VV",
        #         "styles": [
        #             {
        #                 "name": "VV",
        #                 "title": "Backscatter VV",
        #                 "abstract": "Backscatter VV",
        #                 "components": {
        #                     "red": {"VV": 1},
        #                     "green": {"VV": 1},
        #                     "blue": {"VV": 1},
        #                 },
        #                 "scale_range": [0.01, 0.3],
        #             },
        #             {
        #                 "name": "mask",
        #                 "title": "Shadow Layover Mask",
        #                 "abstract": "Shadow Layover Mask",
        #                 "components": {
        #                     "red": {"mask": 1},
        #                     "green": {"mask": 1},
        #                     "blue": {"mask": 1},
        #                 },
        #                 "scale_range": [0, 3],
        #             },
        #         ],
        #     },
        # },
        # {
        #     "name": "ga_s1_iw_vv_vh_c0",
        #     "title": "GA Normalised Radar Backscatter IW VV+VH (Sentinel-1)",
        #     "abstract": "Geoscience Australia Sentinel-1 Normalised Radar Backscatter IW VV+VH Collection 0",
        #     "product_name": "ga_s1_iw_vv_vh_c0",
        #     "native_crs": "EPSG:3577",
        #     "native_resolution": [20, -20],
        #     "bands": {
        #         "VV": ["VV", "vv", "vv_gamma0"],
        #         "VH": ["VH", "vh", "vh_gamma0"],
        #         "mask": ["mask"],
        #     },
        #     "resource_limits": {
        #         "zoomed_out_fill_colour": [150, 180, 200, 160],
        #         "min_zoom_level": 8.0,
        #         "max_datasets": 12,
        #     },
        #     "image_processing": {
        #         "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        #         "always_fetch_bands": [],
        #         "manual_merge": False,
        #     },
        #     "styling": {
        #         "default_style": "VV",
        #         "styles": [
        #             {
        #                 "name": "VV",
        #                 "title": "Backscatter VV",
        #                 "abstract": "Backscatter VV",
        #                 "components": {
        #                     "red": {"VV": 1},
        #                     "green": {"VV": 1},
        #                     "blue": {"VV": 1},
        #                 },
        #                 "scale_range": [0.01, 0.3],
        #             },
        #             {
        #                 "name": "VH",
        #                 "title": "Backscatter VH",
        #                 "abstract": "Backscatter VH",
        #                 "components": {
        #                     "red": {"VH": 1},
        #                     "green": {"VH": 1},
        #                     "blue": {"VH": 1},
        #                 },
        #                 "scale_range": [0.01, 0.3],
        #             },
        #             {
        #                 "name": "mask",
        #                 "title": "Shadow Layover Mask",
        #                 "abstract": "Shadow Layover Mask",
        #                 "components": {
        #                     "red": {"mask": 1},
        #                     "green": {"mask": 1},
        #                     "blue": {"mask": 1},
        #                 },
        #                 "scale_range": [0, 3],
        #             },
        #         ],
        #     },
        # },
    ],
}
