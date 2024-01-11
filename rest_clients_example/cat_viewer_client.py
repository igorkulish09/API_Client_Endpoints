"""Module for interacting with the Cat API."""

import asyncio
import logging
from typing import Dict, List

# Third-party imports
import aiohttp

CAT_API_BASE_URL = 'https://api.thecatapi.com/v1'


async def async_get_random_cats(session: aiohttp.ClientSession, limit: int = 5) -> List[Dict]:
    """
    Get random cats from The Cat API.

    Args:
        session (aiohttp.ClientSession): The aiohttp client session.
        limit (int): The number of cats to retrieve (default is 5).

    Returns:
        List[Dict]: A list of dictionaries, each containing information about a random cat.
    """
    url = f'{CAT_API_BASE_URL}/images/search'  # noqa: WPS305
    query_parameters = {'limit': limit}

    async with session.get(url, params=query_parameters) as response:
        return await response.json()


async def async_get_cat_by_id(session: aiohttp.ClientSession, cat_id: str) -> Dict:
    """
    Retrieve cat information by its ID.

    Args:
        session (aiohttp.ClientSession): The aiohttp client session.
        cat_id (str): The ID of the cat.

    Returns:
        Dict: A dictionary containing cat information.
    """
    url = f'{CAT_API_BASE_URL}/images/{cat_id}'  # noqa: WPS305

    async with session.get(url) as response:
        return await response.json()


logger = logging.getLogger(__name__)


async def main() -> None:
    """Asynchronous main function."""
    async with aiohttp.ClientSession() as session:
        cats = await async_get_random_cats(session)
        logger.info('Random Cats:')
        for cat in cats:
            logger.info(cat)


if __name__ == '__main__':
    asyncio.run(main())
