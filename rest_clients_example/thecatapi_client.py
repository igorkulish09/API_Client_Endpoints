import httpx


class TheCatAPIClient:
    def __init__(self, base_url: str = "https://api.thecatapi.com/v1"):
        self.base_url = base_url

    async def get_random_cat_image(self) -> dict:
        endpoint = f"{self.base_url}/images/search"

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return {}


# Пример использования:
async def main():
    thecatapi_client = TheCatAPIClient()

    # Получить случайное изображение кота
    cat_image = await thecatapi_client.get_random_cat_image()
    print("Cat Image URL:", cat_image.get("url", "N/A"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
