"""Module for interacting with the Cat API."""

import requests
from abc import ABC, abstractmethod
from typing import List, Dict
from requests import Response
from typing import Any


class Client:
    def make_request(self, endpoint: str) -> Response:
        base_url = 'https://api.thecatapi.com/v'
        url = f'{base_url}{endpoint}'

        # Include any necessary headers or authentication
        headers = {'Authorization': 'Bearer ACCESS_TOKEN'}

        # Make the HTTP request using the 'requests' library
        response = requests.get(url, headers=headers)

        # Return the response object
        return response


class BaseHandler(ABC):
    def __init__(self, client: 'Client') -> None:
        self.client = client

    @abstractmethod
    def handle(self) -> List[Dict[Any, Any]]:
        return []


class RandomCatImageHandler(BaseHandler):
    def handle(self) -> List[Dict]:
        response = self.client.make_request('/images/search')
        data = response.json()
        cat_id = data[0]['id']
        return [{'image_url': data[0]['url'], 'cat_id': cat_id}]


class CatIdHandler(BaseHandler):
    def handle(self) -> List[Dict]:
        response = self.client.make_request('/images/search')
        cat_id = response.json()[0]['id']
        return [{'cat_id': cat_id}]


class MyCatsClient(Client):
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.random_cat_image_handler = RandomCatImageHandler(self)
        self.cat_id_handler = CatIdHandler(self)

    def make_request(self, endpoint: str) -> Response:
        headers = {'x-api-key': self.api_key}
        url = f'https://api.thecatapi.com/v1{endpoint}'
        response = requests.get(url, headers=headers)
        return response


# Using the client
api_key = 'live_DaLQuR2bCgpxFTr235jX8CLwjF4PWBwEUu65gvxQko0damHACYGlRCKNpywMvrAB'
client = MyCatsClient(api_key)
random_cat_image_result = client.random_cat_image_handler.handle()
cat_id_result = client.cat_id_handler.handle()

# Working with the results
print(random_cat_image_result)
print(cat_id_result)
