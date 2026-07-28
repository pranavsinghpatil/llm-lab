from tokenizer.vocabulary import Vocabulary

class CharacterTokenizer:
    def __init__(self):
        """
        Initialize the tokenizer.
        You might need structures to map characters to integers and vice-versa.
        """
        self.char_to_int = {}
        self.int_to_char = {}
        self.unk_token = "<UNK>"
        self.vocab = Vocabulary(special_tokens=[self.unk_token])

    def fit(self, text: str):
        """
        Build the vocabulary from the given text.
        Hint: Find all unique characters in the text, sort them, 
        and assign a unique integer ID to each.
        """
        unique_char = sorted(set(text))
        self.vocab.add_tokens(unique_char)

    def encode(self, text: str) -> list[int]:
        """
        Convert a string into a list of integers based on the vocabulary.
        """
        if text is None:
            return []
        return [self.vocab.lookup_id(ch, default_token=self.unk_token) for ch in text]

    def decode(self, tokens: list[int]) -> str:
        """
        Convert a list of integers back into a string.
        """
        if tokens is None:
            return ""
        return ''.join(self.vocab.lookup_token(token) for token in tokens)

    @property
    def vocab_size(self) -> int:
        """
        Return the size of the vocabulary.
        """
        return len(self.vocab)
