from tokenizer.bpe import BPETokenizer

def test_bpe_tokenizer():
    tokenizer = BPETokenizer()
    text = "low lower lowest"
    tokenizer.fit(text, num_merges=2)

    # Test encoding
    encoded = tokenizer.encode(text)
    assert isinstance(encoded, list)
    assert all(isinstance(i, int) for i in encoded)

    # Test decoding
    decoded = tokenizer.decode(encoded)
    assert isinstance(decoded, str)
    assert decoded == text

    # Test unknown token handling
    unknown_text = "unknown words"
    encoded_unknown = tokenizer.encode(unknown_text)
    assert all(token == tokenizer.vocab.lookup_id(tokenizer.unk_token) for token in encoded_unknown if token not in tokenizer.vocab.token_to_id)