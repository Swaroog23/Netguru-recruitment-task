import requests


def get_all_makes():
    makes = requests.get(
        "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
    ).json()
    return makes