from tokenizer.vocabulary import Vocabulary

def test_vocabulary_add_and_lookup():
    vocab = Vocabulary(special_tokens=["<UNK>"])
    
    # Add tokens
    vocab.add_token("a")
    vocab.add_token("b")
    
    # Lookup IDs
    assert vocab.lookup_id("a") == 1
    assert vocab.lookup_id("b") == 2
    assert vocab.lookup_id("<UNK>") == 0
    
    # Lookup tokens
    assert vocab.lookup_token(1) == "a"
    assert vocab.lookup_token(2) == "b"
    assert vocab.lookup_token(0) == "<UNK>"