def get_formatted_location(city_name, country_name, population=0):
    """Generate a neatly formatted location"""
    if population:
        formatted_location = f"{city_name.title()}, {country_name.title()} - population: {population}"
    else:
        formatted_location = f"{city_name.title()}, {country_name.title()}"
    return formatted_location