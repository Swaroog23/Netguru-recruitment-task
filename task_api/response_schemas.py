car_view_schema = {
    "type": "array",
    "properties": {
        "id": {"type": "number"},
        "avg_rating": {"type": "number"},
        "make": {"type": "string"},
        "model": {"type": "string"},
    },
    "required": ["id", "avg_rating", "make", "model"],
}

popular_view_schema = {
    "type": "array",
    "properties": {
        "id": {"type": "number"},
        "rates_number": {"type": "number"},
        "make": {"type": "string"},
        "model": {"type": "string"},
    },
    "required": ["id", "rates_number", "make", "model"],
}
