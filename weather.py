#weather.py

from pprint import pprint

import requests


def get_weather(city):
    url = "https://open-weather13.p.rapidapi.com/city/" + city

    headers = {
        "X-RapidAPI-Key": "69bc405e5bmsh2f4565ba236cd4bp1ea962jsne4eb459bbc5c",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    # print(response.json())
    return response.json()


if __name__ == '__main__':
    pprint(get_weather("London"))