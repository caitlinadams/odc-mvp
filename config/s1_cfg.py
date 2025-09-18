from general_cfg import resource_limits, image_processing
from s1_styles import VV

vv_vh_0_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_0",
    "title": "Sentinel-1 NRB IW (VV+VH)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV+VH)",
    "product_name": "ga_s1_nrb_iw_vv_vh_0",
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
        "styles": [VV],
    },
}

s1_layer_group = {
    "title": "Antarctic and Australian S1 NRB",
    "abstract": "Sentinel-1 Radar Backscatter products for Antarctica and Australia",
    "layers": [vv_vh_0_layer],
}
