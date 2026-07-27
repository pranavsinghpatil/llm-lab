from tokenizer.implementation import CharacterTokenizer


def test_character_tokenizer_round_trip():
    text = "banana"

    tokenizer = CharacterTokenizer()
    tokenizer.fit(text)

    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)

    assert decoded == text

def test_unknown_characters():
    text = "banana"
    unknown_text = "bandana"

    tokenizer = CharacterTokenizer()
    tokenizer.fit(text)

    tokens = tokenizer.encode(unknown_text)
    decoded = tokenizer.decode(tokens)

    assert decoded != unknown_text
    assert decoded.count("<UNK>") == unknown_text.count("d") + unknown_text.count(" ")