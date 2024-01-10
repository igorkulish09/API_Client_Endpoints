"""Module for interacting with the Cat API."""

# Third-party imports
import aiohttp  # noqa: I003,I005
from typing import List, Dict  # noqa: I001

CAT_API_BASE_URL = 'https://api.thecatapi.com/v1'


async def async_get_random_cats(limit: int = 5) -> List[Dict]:
    """
    Get random cats from The Cat API.

    Args:
        limit (int): The number of cats to retrieve (default is 5).

    Returns:
        List[Dict]: A list of dictionaries, each containing information about a random cat.
    """
    url = f'{CAT_API_BASE_URL}/images/search'  # noqa: WPS305
    query_parameters = {'limit': limit}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=query_parameters) as response:
            return await response.json()


async def async_get_cat_by_id(cat_id: str) -> Dict:
    """
    Retrieve cat information by its ID.

    Args:
        cat_id (str): The ID of the cat.

    Returns:
        Dict: A dictionary containing cat information.
    """
    url = f'{CAT_API_BASE_URL}/images/{cat_id}'  # noqa: WPS305

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
