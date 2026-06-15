from bot.models.word_info import WordResult
from bs4 import BeautifulSoup


def parse_word_page(html, query, source_url):
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.select_one('div.featured-box.featured-box-primary')
    if container is None:
        return None

    title_tag = container.select_one("h4.text-uppercase")
    if title_tag is None:
        return None

    title = title_tag.get_text(strip=True)

    return WordResult(
        query=query,
        title=title,
        grammar="іменник, жіночий рід, неістота",
        short_text='',
        full_text=None,
        is_truncated=False,
        source_url=source_url,
        definitions=['Definition 1', 'Definition 2']
    )
