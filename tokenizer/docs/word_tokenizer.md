# Word Tokenizer Design

## What is a word tokenizer?
Unlike a character tokenizer that breaks text into individual letters, a word tokenizer splits text at the word level, allocating a unique integer ID to each specific word.

## Advantages
Words carry semantic meaning natively. "Cat" has meaning on its own, making it easier for the model to learn context without having to first learn how letters combine into words.

## Disadvantages
- **Spelling Mistakes:** A simple typo (e.g., "hello" vs "heloo") results in an entirely new, unrecognized token.
- **Punctuation Sensitivity:** Words attached to punctuation (e.g., "world!" vs "world") might be treated as different tokens if not handled properly.
- **Vocabulary Size:** The vocabulary size becomes massive because every unique word needs its own ID.

## Real-world analogy
It is like reading a sentence by recognizing whole words at a glance, rather than spelling it out letter by letter. (It is the foundational building block for attention mechanisms and next-word predictors!)

## Complexity
**Space Complexity is High:** The vocabulary size explodes because there are hundreds of thousands of words in a language. This requires massive memory for the embedding layer.

## Example
Input: `"hello world I am here"`
Tokenized output:
- `hello` = 1
- `world` = 2
- `I` = 3
- `am` = 4
- `here` = 5