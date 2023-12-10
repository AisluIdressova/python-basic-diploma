import json
from typing import Dict

import requests


def _make_response(url: str, headers: Dict, querystring: Dict,
                   city: str, timeout: int):
    querystring["query"] = city

    response = requests.get(
        url=url,
        headers=headers,
        params=querystring,
        timeout=timeout
    )

    list_airports = []

    if response.status_code == 200:
        response = json.loads(response.text)
        for item in response:
            list_airports.append(item["display_name"])

        response = '\n'.join(list_airports)

        return response



def _airport_data(url: str, headers: Dict, querystring: Dict, city: str, func=_make_response):
    response = func(url, headers, querystring, city, 20)

    return response

class SiteApiInterface:
    @staticmethod
    def get_info():
        return _airport_data


if __name__ == '__main__':
    _make_response()
    _airport_data()
    SiteApiInterface()
