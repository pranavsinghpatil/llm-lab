from tokenizer.word import WordTokenizer

def test_word_tokenizer():
    tokenizer = WordTokenizer()
    text = "Hello world! This is a test."
    tokenizer.fit(text)

    # Test encoding
    encoded = tokenizer.encode(text)
    assert isinstance(encoded, list)
    assert all(isinstance(i, int) for i in encoded)

    # Test decoding
    decoded = tokenizer.decode(encoded)
    assert isinstance(decoded, str)
    assert decoded == text

    # Test unknown token handling
    unknown_text = "Unknown words here."
    encoded_unknown = tokenizer.encode(unknown_text)
    assert all(token == tokenizer.vocab.lookup_id(tokenizer.unk_token) for token in encoded_unknown if token not in tokenizer.vocab.token_to_id)