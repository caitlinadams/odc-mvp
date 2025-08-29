# def linear_vv_vh_ratio(data):
#     unscaled = data["VV"] / data["VH"]
#     normalised = (unscaled - min(unscaled)) / (max(unscaled) - min(unscaled))
#     scaled = normalised * 255

#     return scaled

from general_cfg import resource_limits, image_processing

hh_c0_layer = {
    "name": "ga_s1_iw_hh_c0",
    "title": "GA S1 IW HH C0",
    "abstract": "Robinson Ridge Data",
    "product_name": "ga_s1_iw_hh_c0",
    "native_crs": "EPSG:3031",
    "native_resolution": [20, -20],
    "bands": {
        "HH": ["HH"],
        "mask": ["mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
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
}

s1_layer_group = {
    "title": "Antarctic and Australian S1 NRB",
    "abstract": "Sentinel-1 Radar Backscatter products for Antarctica and Australia",
    "layers": [hh_c0_layer],
}
