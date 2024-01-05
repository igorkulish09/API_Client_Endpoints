from typing import List, Optional
import httpx


class JSONPlaceholderClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    async def get_posts(self) -> List[dict]:
        endpoint = f"{self.base_url}/posts"

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    async def get_comments(self) -> List[dict]:
        endpoint = f"{self.base_url}/comments"

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            return []


# Пример использования:
async def main():
    jsonplaceholder_client = JSONPlaceholderClient()

    # Получить список постов
    posts = await jsonplaceholder_client.get_posts()
    print("Posts:", posts)

    # Получить список комментариев
    comments = await jsonplaceholder_client.get_comments()
    print("Comments:", comments)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
