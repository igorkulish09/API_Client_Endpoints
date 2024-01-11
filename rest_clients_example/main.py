"""This script initializes clients and services, performs various actions, and prints the results."""

# Standard Library imports
import asyncio
import logging
from typing import Dict, List, Union

# Third-party imports
import aiohttp

# Local imports
from cat_viewer_client import async_get_cat_by_id, async_get_random_cats
from email_verification_service import EmailVerificationService

logger = logging.getLogger(__name__)


async def format_verification_results(verification_results: List[Dict[str, Union[str, bool]]]) -> None:
    """Format email verification results."""
    formatted_results = [
        f'Email: {res_ult["email"]}, Valid: {res_ult["is_valid"]}' for res_ult in verification_results
    ]
    await some_async_function(formatted_results)


async def some_async_function(formatted_results: List[str]) -> None:
    """Perform some asynchronous operation with the formatted results."""
    # Your asynchronous operations with formatted results go here


async def process_random_cats(session: aiohttp.ClientSession) -> None:
    """Asynchronously retrieve and process random cats."""
    random_cats = await async_get_random_cats(session)
    log_info('Random Cats', random_cats)


async def process_specific_cat(session: aiohttp.ClientSession) -> None:
    """Asynchronously retrieve and process a specific cat."""
    specific_cat = await async_get_cat_by_id(session, 'g5')
    log_info('Specific Cat', specific_cat)


async def process_email_verification(email_service: EmailVerificationService) -> None:
    """Asynchronously verify an email and retrieve verification results."""
    email_to_verify = 'test@example.com'
    await email_service.async_verify_email(email_to_verify)
    verification_results = await email_service.async_get_verification_results()
    await format_verification_results(verification_results)


def log_info(category: str, details: Union[str, Dict[str, str]]) -> None:
    """Log information."""
    logger.info(f'{category}: {details}')  # noqa: WPS305


async def main() -> None:
    """Asynchronous main function."""
    async with aiohttp.ClientSession() as session:
        email_service = EmailVerificationService()
        await process_random_cats(session)
        await process_random_cats(email_service)


if __name__ == '__main__':
    asyncio.run(main())
