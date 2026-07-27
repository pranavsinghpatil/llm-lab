class CharacterTokenizer:
    def __init__(self):
        """
        Initialize the tokenizer.
        You might need structures to map characters to integers and vice-versa.
        """
        self.char_to_int = {}
        self.int_to_char = {}
        self.vocab_size = None

    def fit(self, text: str):
        """
        Build the vocabulary from the given text.
        
        Hint: Find all unique characters in the text, sort them, 
        and assign a unique integer ID to each.
        """
        unique_char = sorted(set(text))
        self.vocab_size = len(unique_char)
        for i, ch in enumerate(unique_char):
            self.char_to_int[ch] = i
            self.int_to_char[i] = ch

        # return [self.char_to_int[ch] for ch in text]

    def encode(self, text: str) -> list[int]:
        """
        Convert a string into a list of integers based on the vocabulary.
        """
        return [self.char_to_int[ch] for ch in text]

    def decode(self, tokens: list[int]) -> str:
        """
        Convert a list of integers back into a string.
        """
        return ''.join(self.int_to_char[token] for token in tokens)
