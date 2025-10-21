hh_linear = {
    "name": "hh_linear",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "components": {
        "red": {"HH_gamma0": 1},
        "green": {"HH_gamma0": 1},
        "blue": {"HH_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

hh_db = {
    "name": "hh_db",
    "title": "Backscatter HH (dB)",
    "abstract": "Backscatter HH (dB)",
    "additional_bands": ["HH_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HH_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HH_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HH_gamma0",
                "scale_from": (-17, 6),
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
        "red": {"HV_gamma0": 1},
        "green": {"HV_gamma0": 1},
        "blue": {"HV_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

hv_db = {
    "name": "hv_db",
    "title": "Backscatter HV (dB)",
    "abstract": "Backscatter HV (dB)",
    "additional_bands": ["HV_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HV_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HV_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "HV_gamma0",
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
        "red": {"VV_gamma0": 1},
        "green": {"VV_gamma0": 1},
        "blue": {"VV_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

vv_db = {
    "name": "vv_db",
    "title": "Backscatter VV (dB)",
    "abstract": "Backscatter VV (dB)",
    "additional_bands": ["VV_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VV_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VV_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VV_gamma0",
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
        "red": {"VH_gamma0": 1},
        "green": {"VH_gamma0": 1},
        "blue": {"VH_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

vh_db = {
    "name": "vh_db",
    "title": "Backscatter VH (dB)",
    "abstract": "Backscatter VH (dB)",
    "additional_bands": ["VH_gamma0"],
    "components": {
        "red": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VH_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VH_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "s1_style_functions.db",
            "kwargs": {
                "band": "VH_gamma0",
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
    "additional_bands": ["VV_gamma0", "VH_gamma0"],
    "components": {
        "red": {
            "VV_gamma0": 1.0,
            "scale_range": [0.0, 0.28],
        },
        "green": {
            "VH_gamma0": 1.0,
            "scale_range": [0.0, 0.06],
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "VH_gamma0",
                "band2": "VV_gamma0",
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
        "red": {"mask": 1},
        "green": {"mask": 1},
        "blue": {"mask": 1},
    },
    "scale_range": [0, 3],
}
