import asyncio
from rest_clients_example.jsonplaceholder_client import JSONPlaceholderClient
from rest_clients_example.thecatapi_client import TheCatAPIClient
from rest_clients_example.email_verification_service import EmailVerificationService


async def main_async():
    # Инициализация экземпляров клиентов и сервиса
    jsonplaceholder_client = JSONPlaceholderClient()
    thecatapi_client = TheCatAPIClient()
    email_verification_service = EmailVerificationService()

    # Методы клиентов и сервиса
    posts = await jsonplaceholder_client.get_posts()
    print(f"All Posts: {posts}")

    cat_image = await thecatapi_client.get_random_cat_image()
    print(f"Random Cat Image: {cat_image}")

    email = "example@email.com"
    verification_result = email_verification_service.verify_email(email)
    print(f"Email Verification Result: {verification_result}")

    all_results = email_verification_service.get_all_results()
    print(f"All Email Verification Results: {all_results}")

if __name__ == "__main__":
    asyncio.run(main_async())
