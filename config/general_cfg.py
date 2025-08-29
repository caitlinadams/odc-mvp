resource_limits = {
    "zoomed_out_fill_colour": [150, 180, 200, 160],
    "min_zoom_level": 8.0,
    "max_datasets": 12,
}

image_processing = {
    "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
    "always_fetch_bands": [],
    "manual_merge": False,
}
