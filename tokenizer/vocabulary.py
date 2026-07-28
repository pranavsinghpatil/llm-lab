class Vocabulary:
    def __init__(self, special_tokens: list[str] = None):
        """
        Initialize the Vocabulary.
        
        Should store:
        - token -> id mapping
        - id -> token mapping
        - special tokens (like <UNK>)
        """
        self.token_to_id = {}
        self.id_to_token = {}
        
        # Add special tokens first if provided
        if special_tokens:
            for token in special_tokens:
                self.add_token(token)

    def add_token(self, token: str) -> int:
        """
        Adds a token to the vocabulary if it doesn't already exist.
        Returns the integer ID assigned to the token.
        """
        if token in self.token_to_id:
            return self.token_to_id[token]

        token_id = len(self.token_to_id)
        self.token_to_id[token] = token_id
        self.id_to_token[token_id] = token
        return token_id

    def add_tokens(self, tokens: list[str]):
        """
        Adds a list of tokens to the vocabulary.
        """
        token_ids = []
        for token in tokens:
            token_id = self.add_token(token)
            token_ids.append(token_id)
        return token_ids

    def lookup_id(self, token: str, default_token: str = None) -> int:
        """
        Returns the ID for a given token. 
        If token isn't found, returns default_token's ID (e.g. <UNK>).
        """
        if token in self.token_to_id:
            return self.token_to_id[token]
        if default_token is not None:
            return self.token_to_id.get(default_token)
        raise KeyError(f"Token '{token}' not found and no default_token provided.")

    def lookup_token(self, token_id: int) -> str:
        """
        Returns the token string for a given token ID.
        """
        if token_id in self.id_to_token:
            return self.id_to_token[token_id]
        raise KeyError(f"Token ID '{token_id}' not found.") 

    def __contains__(self, token: str) -> bool:
        """
        Checks if a token exists in the vocabulary.
        Allows: 'a' in vocab
        """
        return token in self.token_to_id

    def __len__(self) -> int:
        """
        Returns the size of the vocabulary.
        Allows: len(vocab)
        """
        return len(self.token_to_id)
        
