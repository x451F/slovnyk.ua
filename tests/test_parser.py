from pathlib import Path
from bot.services.parser import parse_word_page


def test_parse_alpha_page_extracts_basic_word_info():
    html = Path("tests/fixtures/slovnyk/alpha.html").read_text(encoding="utf-8")

    result = parse_word_page(
        html, query="альфа", source_url="https://slovnyk.ua/index.php?swrd=альфа")

    assert result is not None
    assert result.title == "альфа"
    assert "іменник" in result.grammar
    assert "жіночий рід" in result.grammar
    assert "неістота" in result.grammar
    assert result.definitions
