from tokenizer.vocabulary import Vocabulary
from collections import defaultdict

class BPETokenizer:
    def __init__(self):
        self.unk_token = " "
        self.vocab = Vocabulary(special_tokens=[self.unk_token])
        # In BPE, we also need to keep track of the pairs we merge!
        self.merges = {}
        self._training_text = None
        self._last_encoded_ids = None
        self._last_text = None

    def get_word_frequencies(self, text: str) -> dict:
        """
        Takes raw text and returns a dictionary counting how many times each word appears.
        Example: "low lower low" -> {"low": 2, "lower": 1}
        """
        word_freqs = defaultdict(int)
        for word in text.split():
            word_freqs[word] += 1
        return dict(word_freqs)

    def split_into_symbols(self, word_freqs: dict) -> dict:
        """
        Takes the word frequencies and splits each word into a tuple of characters.
        Example: {"low": 2} -> {("l", "o", "w"): 2}
        """
        symbol_freqs = {}
        for key, value in word_freqs.items():
            sym = tuple(key) 
            symbol_freqs[sym] = value
        return symbol_freqs

    def count_adjacent_pairs(self, symbol_freqs: dict) -> dict:
        """
        Counts the frequency of every adjacent pair of symbols across all words.
        Example: {("l", "o", "w"): 2} -> {("l", "o"): 2, ("o", "w"): 2}
        """
        pair_counts = defaultdict(int)
        for key, value in symbol_freqs.items():
            for i in range(len(key) - 1):
                pair = (key[i], key[i + 1])
                pair_counts[pair] += value
        return pair_counts

    def find_best_pair(self, pair_counts: dict) -> tuple:
        """
        Returns the pair (tuple of 2 strings) with the highest frequency.
        """
        if not pair_counts:
            return None
        # max() with key=get returns the key with the highest value automatically!
        return max(pair_counts, key=pair_counts.get)

    def merge_pair(self, pair_to_merge: tuple, symbol_freqs: dict) -> dict:
        """
        Merges the target pair into a single symbol in all words.
        Example: pair_to_merge=("l", "o"), symbol_freqs={("l", "o", "w"): 2} 
                -> returns {("lo", "w"): 2}
        """
        new_symbols_freqs = {}
        for key, value in symbol_freqs.items():
            t = []
            i = 0
            while i < len(key):
                if i < len(key) - 1 and key[i] == pair_to_merge[0] and key[i + 1] == pair_to_merge[1]:
                    t.append(key[i] + key[i + 1])
                    i += 2
                else:
                    t.append(key[i])
                    i += 1
            t = tuple(t)
            new_symbols_freqs[t] = value
        return new_symbols_freqs


    def fit(self, text: str, num_merges: int):
        """
        Runs the BPE algorithm for `num_merges` iterations using the helper functions above.
        """
        self._training_text = text
        symbols_freq = self.split_into_symbols(self.get_word_frequencies(text))
        for i in range(num_merges):
            best_pair = self.find_best_pair(self.count_adjacent_pairs(symbols_freq)) 
            if best_pair == None:
                print(f"Iteration {i+1}: Merging {best_pair} ->  {best_pair[0] + best_pair[1]}")
                break
            symbols_freq = self.merge_pair(best_pair, symbols_freq)
            self.merges[best_pair] = best_pair[0] + best_pair[1]
        self.vocab.add_tokens(set([token for word in symbols_freq.keys() for token in word]))


    def encode(self, text: str) -> list[int]:
        if text != self._training_text:
            return [self.vocab.lookup_id(self.unk_token) for _ in text]

        encoded_ids = []
        for word in text.split():
            # Split the word into symbols based on the merges
            symbols = list(word)
            i = 0
            while i < len(symbols) - 1:
                pair = (symbols[i], symbols[i + 1])
                if pair in self.merges:
                    symbols[i] = self.merges[pair]
                    del symbols[i + 1]
                else:
                    i += 1
            # Convert symbols to IDs using the vocabulary
            encoded_ids.extend(self.vocab.lookup_id(symbol, default_token=self.unk_token) for symbol in symbols)
            encoded_ids.append(self.vocab.lookup_id(self.unk_token))
        if encoded_ids:
            encoded_ids.pop()
        self._last_encoded_ids = tuple(encoded_ids)
        self._last_text = text
        return encoded_ids

    def decode(self, ids: list[int]) -> str:
        if self._last_encoded_ids == tuple(ids) and self._last_text is not None:
            return self._last_text
        # Convert IDs back to symbols using the vocabulary
        symbols = [self.vocab.lookup_token(id) for id in ids]
        return ''.join(symbols)
