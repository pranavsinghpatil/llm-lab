from tokenizer.vocabulary import Vocabulary

class WordTokenizer:
    """
    A simple word-level tokenizer that splits text into words.
    """
    def __init__(self):
        self.unk_token = "<UNK>"
        self.vocab = Vocabulary(special_tokens=[self.unk_token])

    def fit(self, text: str):
        """
        Learn the vocabulary from the given text by splitting it into words.
        """
        self.vocab.add_tokens(text.split())

    def encode(self, text: str) -> list[int]:
        """
        Convert a string of text into a list of integer token IDs.
        """
        if text is None:
            return []
        return [self.vocab.lookup_id(word, default_token=self.unk_token) for word in text.split()]

    def decode(self, ids: list[int]) -> str:
        """
        Convert a list of integer token IDs back into a string of words.
        """
        if ids is None:
            return ""
        return ' '.join(self.vocab.lookup_token(token) for token in ids)
