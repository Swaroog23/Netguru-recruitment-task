import json
import requests


def get_all_makes():
    makes = requests.get(
        "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
    ).json()
    return makes


def get_models_for_make(requested_make):
    try:
        all_makes_response = get_all_makes()
        for make in all_makes_response["Results"]:
            if make["Make_Name"] == requested_make.upper():
                models = requests.get(
                    f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{requested_make}?format=json"
                ).json()
                return models

    except Exception as ex:
        return ex