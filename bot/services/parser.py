from bot.models.word_info import WordResult
from bs4 import BeautifulSoup


def parse_word_page(html, query, source_url):
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.select_one('div.featured-box.featured-box-primary')
    if article is None:
        return None

    title_tag = article.select_one("h4.text-uppercase")
    if title_tag is None:
        return None

    title = title_tag.get_text(strip=True)

    grammar_tag = article.select_one("section.orfo")
    if grammar_tag is None:
        return None

    grammar = grammar_tag.get_text(" ", strip=True)
    print("\nTITLE:", title)
    print("GRAMMAR:", grammar)

    definition_tags = article.select("div.toggle.toggle-sum .toggle-content p")

    definitions = [tag.get_text(" ", strip=True) for tag in definition_tags]
    print("DEFINITIONS:", definitions)

    return WordResult(
        query=query,
        title=title,
        grammar=grammar,
        short_text='',
        full_text=None,
        is_truncated=False,
        source_url=source_url,
        definitions=definitions
    )
