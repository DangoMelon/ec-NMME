import numpy as np
from dmelon import utils

import os

MODELS = {
    "CanCM4i": {"HINDCAST": {"members": 10}, "FORECAST": {"members": 10}},
    "NCEP-CFSv2": {
        "HINDCAST": {"members": 24},
        "FORECAST": {
            "members": 32,
            "prefix": ".EARLY_MONTH_SAMPLES/",
        },
    },
    "GEN-NEMO": {"HINDCAST": {"members": 10}, "FORECAST": {"members": 10}},
    "GFDL-CM2p1-aer04": {"base": {"members": 10}},
    "GFDL-CM2p5-FLOR-A06": {"base": {"members": 12}},
    "GFDL-CM2p5-FLOR-B01": {"base": {"members": 12}},
    "GFDL-SPEAR": {"HINDCAST": {"members": 15}, "FORECAST": {"members": 30}},
    "NASA-GEOSS2S": {"HINDCAST": {"members": 4}, "FORECAST": {"members": 10}},
}

BASE = "http://iridl.ldeo.columbia.edu/SOURCES/.Models/.NMME/.{MODEL_NAME}/.{TYPE}/{PREFIX}.MONTHLY/.sst/M/({MEMBER})VALUES/data.nc"
OUTPUT_DIR = "/data/users/grivera/NMME"

utils.check_folder("models")
utils.check_folder(OUTPUT_DIR)

for MODEL_NAME, values in MODELS.items():
    if "base" in values:
        continue
    for TYPE, _v in values.items():
        members = np.arange(1, _v["members"] + 1)
        PREFIX = _v["prefix"] if "prefix" in _v else ""
        with open(f"models/{MODEL_NAME}.{TYPE}.txt", "w") as f:
            for MEMBER in members:
                FILE_NAME = os.path.join(
                    OUTPUT_DIR, f"{MODEL_NAME}.{TYPE}.M{MEMBER}.nc"
                )
                URL = BASE.format(
                    MODEL_NAME=MODEL_NAME, TYPE=TYPE, PREFIX=PREFIX, MEMBER=MEMBER
                )
                print(FILE_NAME, URL)
                f.write(f"{FILE_NAME} {URL}\n")
