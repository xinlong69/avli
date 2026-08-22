import httpx
from bs4 import BeautifulSoup


async def scrape_target(url: str) -> str:
    async with httpx.AsyncClient(follow_redirects=True, timeout=20.0) as client:
        response = await client.get(url)
        response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    # Strip scripts, styles, and navigational junk
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.extract()

    return soup.get_text(separator=" ", strip=True)
