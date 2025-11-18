from general_cfg import resource_limits, image_processing
from s1_styles import (
    vv_linear,
    vv_db,
    vh_linear,
    vh_db,
    hh_linear,
    hh_db,
    hv_linear,
    hv_db,
    vv_vh_false_colour_linear,
    mask,
)


vv_1_layer = {
    "name": "ga_s1_nrb_iw_vv_1",
    "title": "Sentinel-1 NRB IW (VV)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV)",
    "product_name": "ga_s1_nrb_iw_vv_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "vv_gamma0": ["vv_gamma0"],
        "mask": ["oa_layover_shadow_mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "vv_linear",
        "styles": [vv_linear, vv_db, mask],
    },
}

vv_vh_1_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_1",
    "title": "Sentinel-1 NRB IW (VV+VH)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV+VH)",
    "product_name": "ga_s1_nrb_iw_vv_vh_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "vv_gamma0": ["vv_gamma0"],
        "vh_gamma0": ["vh_gamma0"],
        "mask": ["oa_layover_shadow_mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "vv_vh_false_colour_linear",
        "styles": [vv_vh_false_colour_linear, vv_linear, vh_linear, vv_db, vh_db, mask],
    },
}

hh_1_layer = {
    "name": "ga_s1_nrb_iw_hh_1",
    "title": "Sentinel-1 NRB IW (HH)",
    "abstract": "Experimental Sentinel-1 backscatter data (HH)",
    "product_name": "ga_s1_nrb_iw_hh_1",
    "native_crs": "EPSG:3031",
    "native_resolution": [20, -20],
    "bands": {
        "hh_gamma0": ["hh_gamma0"],
        "mask": ["oa_layover_shadow_mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "hh_linear",
        "styles": [hh_linear, hh_db, mask],
    },
}

hh_hv_1_layer = {
    "name": "ga_s1_nrb_iw_hh_hv_1",
    "title": "Sentinel-1 NRB IW (HH+HV)",
    "abstract": "Experimental Sentinel-1 backscatter data (HH+HV)",
    "product_name": "ga_s1_nrb_iw_hh_hv_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": {
        "hh_gamma0": ["hh_gamma0"],
        "hv_gamma0": ["hv_gamma0"],
        "mask": ["oa_layover_shadow_mask"],
    },
    "resource_limits": resource_limits,
    "image_processing": image_processing,
    "styling": {
        "default_style": "hh_linear",
        "styles": [hh_linear, hv_linear, hh_db, hv_db, mask],
    },
}

s1_layer_group = {
    "title": "Antarctic and Australian S1 NRB",
    "abstract": "Sentinel-1 Radar Backscatter products for Antarctica and Australia",
    "layers": [vv_vh_1_layer, hh_1_layer],
}
