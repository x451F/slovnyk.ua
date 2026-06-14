from bot.models.word_info import WordResult


def test_word_result_stores_data():
    word = WordResult(
        query="кущ",
        title="Кущ",
        grammar="noun",
        short_text="A bush or shrub.",
        full_text="A bush or shrub, typically with multiple stems and a dense growth habit.",
        is_truncated=False,
        source_url="https://slovnyk.ua/index.php?swrd=%D0%BA%D1%83%D1%89",
        definitions=["A bush or shrub.", "A dense growth of plants."]
    )

    assert word.query == "кущ"
    assert word.title == "Кущ"
    assert word.grammar == "noun"
    assert word.short_text == "A bush or shrub."
    assert word.full_text == "A bush or shrub, typically with multiple stems and a dense growth habit."
    assert word.is_truncated is False
    assert word.source_url == "https://slovnyk.ua/index.php?swrd=%D0%BA%D1%83%D1%89"
    assert word.definitions == [
        "A bush or shrub.", "A dense growth of plants."]
