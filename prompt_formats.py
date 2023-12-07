prompt_hermes = """<|im_start|>system
    You are an helpful assistant who has access to functions calls to help the user. When you do not need function calls, just provide an answer.
   Here is an example of conversation with function calls:
   <|im_end|>
   <|im_start|>user
   Can you help me generate an anagram of the word "listen"?
   <|im_end|>
   <|im_start|>assistant
   <functioncall> {{"name":"generate_anagram", "arguments": {{"word": "listen"}}}}
   <|im_end|>
    <functionresp> {{"anagram": "silent"}}
    <|im_end|>
    <|im_start|>user
   Can you help me get the current day as a string?
   <|im_end|>
   <|im_start|>assistant
   <functioncall> {{"name":"get_current_day_str", "arguments": {{}}}}
   <|im_end|>
    <functionresp> {{"str": "Monday"}}
    <|im_end|>
    <|im_start|>user
    {input}
    <|im_start|>assistant
    """

prompt_raven = \
'''
Function:
def get_weather_data(coordinates):
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Args:
    coordinates (tuple): The latitude of the location.

    Returns:
    float: The current temperature in the coordinates you've asked for
    """

Function:
def get_coordinates_from_city(city_name):
    """
    Fetches the latitude and longitude of a given city name using the Maps.co Geocoding API.

    Args:
    city_name (str): The name of the city.

    Returns:
    tuple: The latitude and longitude of the city.
    """

User Query: {input}<human_end>
'''