from rest_framework.renderers import ParseError


def validate_post_car_request_data(request_data):
    if "make" not in request_data.keys() and "model" not in request_data.keys():
        raise ParseError(detail="Wrong body data provided", code=400)
    validate_request_data_is_not_null(request_data)
    validate_request_make_is_not_numeric(request_data["make"])


def validate_list_of_models_exists(list_of_models):
    if not list_of_models:
        raise ParseError(detail="Wrong body data provided", code=400)


def validate_request_make_is_not_numeric(request_make):
    if request_make.isnumeric():
        raise ParseError(detail="Wrong body data provided", code=400)


def validate_request_rating_is_number(request_rating):
    if not isinstance(request_rating, int):
        raise ParseError(detail="Wrong body data provided", code=400)


def validate_request_rating(request_rating):
    validate_request_rating_is_number(request_rating)
    if not 5 >= request_rating >= 1:
        raise ParseError(detail="Wrong body data provided", code=400)


def validate_post_rate_request_data(request_data):
    if not "rating" in request_data.keys() and not "car_id" in request_data.keys():
        raise ParseError(detail="Wrong body data provided", code=400)
    validate_request_rating(request_data["rating"])


def validate_request_data_is_not_null(request_data):
    if request_data["make"] is None and request_data["model"] is None:
        raise ParseError(detail="Request data cannot be null", code=400)
