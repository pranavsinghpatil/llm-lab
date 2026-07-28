# What I Learned: Character Tokenizer 

## 1. `fit()` vs `encode()`
* `fit()` is the training phase. It builds the knowledge and the vocabulary initially.
* `encode()` is the runtime phase. It encodes characters based on the vocabulary we already built at query time.

## 2. Why we need `<UNK>`
* `<UNK>` is for handling edge cases. Sometimes we get a new unknown character that doesn't exist in our vocabulary. Instead of the code crashing or throwing an error, we provide a general, safe fallback value (`0`) for these unknown characters.
