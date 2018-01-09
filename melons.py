melon_tracking = {
    "Honeydew": {
        "price": 0.99,
        "seedless": True,
        "flesh_color": "Green",
        "rind_color": "Light Green",
        "weight": "Medium",
    },

    "Crenshaw": {
        "price": 2.00,
        "seedless": False,
        "flesh_color": "Green",
        "rind_color": "Green",
        "weight": "Low",
    },

    "Crane": {
        "price": 2.50,
        "seedless": False,
        "flesh_color": "Red",
        "rind_color": "Green",
        "weight": "Low",
    },

    "Casaba": {
        "price": 2.50,
        "seedless": False,
        "flesh_color": "Yellow",
        "rind_color": "Yellow",
        "weight": "High",
    },

    "Cantaloupe": {
        "price": 0.99,
        "seedless": False,
        "flesh_color": "Orange",
        "rind_color": "Taupe",
        "weight": "High",
    }
}

def add_melon_attribute():
    """adds new tracked attributes (as type str) for each melon type"""

    new_key = raw_input("type the new attribute: ")
    
    for melon, nested_melon_dict in melon_tracking.items():
        new_value = raw_input("type the value for {} {}: ".format(melon, new_key))
        nested_melon_dict[new_key] = new_value

