HH = {
    "name": "HH",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "components": {
        "red": {"HH": 1},
        "green": {"HH": 1},
        "blue": {"HH": 1},
    },
    "scale_range": [0.02, 0.4],
}

VV = {
    "name": "VV",
    "title": "Backscatter VV",
    "abstract": "Backscatter VV",
    "components": {
        "red": {"VV_gamma0": 1},
        "green": {"VV_gamma0": 1},
        "blue": {"VV_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
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
