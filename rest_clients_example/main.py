"""This script initializes clients and services, performs various actions, and prints the results."""

# Standard Library imports
import asyncio

# Third-party imports
import aiohttp
from cat_viewer_client import async_get_cat_by_id, async_get_random_cats
# Local imports
from email_verification_service import EmailVerificationService
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


async def format_verification_results(verification_results: List[Dict]) -> None:
    """Format email verification results."""
    formatted_results = []
    for res_ult in verification_results:
        email = res_ult['email']
        is_valid = res_ult['is_valid']
        formatted_results.append(f'Email: {email}, Valid: {is_valid}')  # noqa: WPS305

    await some_async_function()


async def some_async_function() -> List[str]:
    return []


async def main() -> None:
    """Asynchronous main function."""
    async with aiohttp.ClientSession() as session:
        # Asynchronously retrieve random cats
        random_cats = await async_get_random_cats(session)
        logger.info('Random Cats: %s', random_cats)

        # Asynchronously retrieve a specific cat
        cat_id_to_get = 'g5'
        specific_cat = await async_get_cat_by_id(session, cat_id_to_get)
        logger.info('Specific Cat: %s', specific_cat)

        # Asynchronously verify an email
        email_service = EmailVerificationService()
        email_to_verify = 'test@example.com'
        await email_service.async_verify_email(email_to_verify)

        # Asynchronously retrieve email verification results
        verification_results = await email_service.async_get_verification_results()
        await format_verification_results(verification_results)

if __name__ == '__main__':
    asyncio.run(main())
