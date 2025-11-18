hh_linear = {
    "name": "hh_linear",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "components": {
        "red": {"hh_gamma0": 1},
        "green": {"hh_gamma0": 1},
        "blue": {"hh_gamma0": 1},
    },
    "scale_range": [0.001, 0.4],
}

hh_db = {
    "name": "hh_db",
    "title": "Backscatter HH (dB)",
    "abstract": "Backscatter HH (dB)",
    "additional_bands": ["hh_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-30, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-30, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-30, 6),
                "scale_to": (0, 255),
            },
        },
    },
}

hv_linear = {
    "name": "hv_linear",
    "title": "Backscatter HV",
    "abstract": "Backscatter HV",
    "components": {
        "red": {"hv_gamma0": 1},
        "green": {"hv_gamma0": 1},
        "blue": {"hv_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

hv_db = {
    "name": "hv_db",
    "title": "Backscatter HV (dB)",
    "abstract": "Backscatter HV (dB)",
    "additional_bands": ["hv_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
    },
}

vv_linear = {
    "name": "vv_linear",
    "title": "Backscatter VV",
    "abstract": "Backscatter VV",
    "components": {
        "red": {"vv_gamma0": 1},
        "green": {"vv_gamma0": 1},
        "blue": {"vv_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

vv_db = {
    "name": "vv_db",
    "title": "Backscatter VV (dB)",
    "abstract": "Backscatter VV (dB)",
    "additional_bands": ["vv_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
    },
}

vh_linear = {
    "name": "vh_linear",
    "title": "Backscatter VH",
    "abstract": "Backscatter VH",
    "components": {
        "red": {"vh_gamma0": 1},
        "green": {"vh_gamma0": 1},
        "blue": {"vh_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

vh_db = {
    "name": "vh_db",
    "title": "Backscatter VH (dB)",
    "abstract": "Backscatter VH (dB)",
    "additional_bands": ["vh_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
    },
}

vv_vh_false_colour_linear = {
    "name": "vv_vh_false_colour_linear",
    "title": "VV+VH False Colour",
    "abstract": "VV+VH False Colour",
    "additional_bands": ["vv_gamma0", "vh_gamma0"],
    "components": {
        "red": {
            "vv_gamma0": 1.0,
            "scale_range": [0.0, 0.28],
        },
        "green": {
            "vh_gamma0": 1.0,
            "scale_range": [0.0, 0.06],
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "vh_gamma0",
                "band2": "vv_gamma0",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}

mask = {
    "name": "mask",
    "title": "Shadow Layover Mask",
    "abstract": "Shadow Layover Mask",
    "components": {
        "red": {"oa_layover_shadow_mask": 1},
        "green": {"oa_layover_shadow_mask": 1},
        "blue": {"oa_layover_shadow_mask": 1},
    },
    "scale_range": [0, 3],
}
