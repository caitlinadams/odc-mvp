from general_cfg import resource_limits, image_processing
from s1_styles import VV, VH, HH, HV, mask

vv_0_layer = {
    "name": "ga_s1_nrb_iw_vv_0",
    "title": "Sentinel-1 NRB IW (VV)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV)",
    "product_name": "ga_s1_nrb_iw_vv_0",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "VV_gamma0": ["VV_gamma0"],
        "mask": ["mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "VV",
        "styles": [VV, mask],
    },
}

vv_vh_0_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_0",
    "title": "Sentinel-1 NRB IW (VV+VH)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV+VH)",
    "product_name": "ga_s1_nrb_iw_vv_vh_0",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "VV_gamma0": ["VV_gamma0"],
        "VH_gamma0": ["VH_gamma0"],
        "mask": ["mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "VV",
        "styles": [VV, VH, mask],
    },
}

hh_0_layer = {
    "name": "ga_s1_nrb_iw_hh_0",
    "title": "Sentinel-1 NRB IW (HH)",
    "abstract": "Experimental Sentinel-1 backscatter data (HH)",
    "product_name": "ga_s1_nrb_iw_hh_0",
    "native_crs": "EPSG:3031",
    "native_resolution": [20, -20],
    "bands": {
        "HH_gamma0": ["HH_gamma0"],
        "mask": ["mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "HH",
        "styles": [HH, mask],
    },
}

hh_hv_0_layer = {
    "name": "ga_s1_nrb_iw_hh_hv_0",
    "title": "Sentinel-1 NRB IW (HH+HV)",
    "abstract": "Experimental Sentinel-1 backscatter data (HH+HV)",
    "product_name": "ga_s1_nrb_iw_hh_hv_0",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "HH_gamma0": ["HH_gamma0"],
        "HV_gamma0": ["HV_gamma0"],
        "mask": ["mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "HH",
        "styles": [HH, HV, mask],
    },
}

s1_layer_group = {
    "title": "Antarctic and Australian S1 NRB",
    "abstract": "Sentinel-1 Radar Backscatter products for Antarctica and Australia",
    "layers": [vv_vh_0_layer, vv_0_layer, hh_0_layer, hh_hv_0_layer],
}
