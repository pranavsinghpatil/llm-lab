from tokenizer.implementation import CharacterTokenizer


def test_character_tokenizer_round_trip():
    text = "banana"

    tokenizer = CharacterTokenizer()
    tokenizer.fit(text)

    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)

    assert decoded == text
