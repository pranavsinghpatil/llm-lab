# Module 01: Tokenization

## Problem Statement: Why Tokenization?
Computers cannot directly understand raw human text like `"hello"`. They only operate on numbers (tensors). 
Tokenization is the process of breaking text down into smaller discrete units (tokens) and mapping each token to a unique numerical identifier (integer ID).

---

## 1. Character-Level Tokenization

In a **Character Tokenizer**, the smallest unit of text is an individual character (letters, punctuation, whitespace).

Each unique character in the dataset is assigned a unique integer ID.

```
"cat" ---> ['c', 'a', 't'] ---> [3, 1, 5]
```

### A. Advantages
- **Tiny Vocabulary Size**: The total number of unique characters in a language (e.g. ASCII or basic English) is very small (often 50–256 tokens).
- **No Out-Of-Vocabulary (OOV) for Known Characters**: As long as a character exists in the alphabet, any new word made of known characters can be tokenized without needing new tokens.
- **Simple Implementation**: Easy to build and reason about without complex merging statistics.

### B. Disadvantages
- **Long Sequence Lengths**: Words become long lists of numbers (`"understanding"` becomes 13 tokens), making transformer context windows fill up quickly and increasing computational cost ($O(N^2)$ in self-attention).
- **Lack of Semantic Meaning**: Individual characters (like `'c'` or `'t'`) carry no individual meaning. The model has to spend capacity learning how characters combine to form concepts.

### C. Example Walkthrough
Given text: `"banana"`

1. **Vocabulary Building (`fit`)**:
   - Unique characters: `['a', 'b', 'n']`
   - Special tokens: `<UNK>` (ID 0)
   - Mapping:
     - `<UNK>` $\rightarrow$ 0
     - `'a'` $\rightarrow$ 1
     - `'b'` $\rightarrow$ 2
     - `'n'` $\rightarrow$ 3

2. **Encoding (`encode("banana")`)**:
   - `'b'` $\rightarrow$ 2
   - `'a'` $\rightarrow$ 1
   - `'n'` $\rightarrow$ 3
   - `'a'` $\rightarrow$ 1
   - `'n'` $\rightarrow$ 3
   - `'a'` $\rightarrow$ 1
   - Result: `[2, 1, 3, 1, 3, 1]`

3. **Decoding (`decode([2, 1, 3, 1, 3, 1])`)**:
   - `2` $\rightarrow$ `'b'`, `1` $\rightarrow$ `'a'`, `3` $\rightarrow$ `'n'`, etc.
   - Result: `"banana"`

### D. Complexity Analysis
- **`fit(text)`**: 
  - Time Complexity: $O(N \log N)$ where $N$ is the number of characters in the text (due to sorting unique characters).
  - Space Complexity: $O(V)$ where $V$ is the vocabulary size (number of unique characters).
- **`encode(text)`**: 
  - Time Complexity: $O(L)$ where $L$ is the length of input text (dictionary lookup per character).
  - Space Complexity: $O(L)$ to store token IDs.
- **`decode(tokens)`**: 
  - Time Complexity: $O(L)$ where $L$ is the number of tokens.
  - Space Complexity: $O(L)$ to construct string.

---

## E. References
- *Build a Large Language Model (From Scratch)* by Sebastian Raschka (Chapter 2: Working with Text Data)
- Karpathy's *nanoGPT* repository (`mini-shakespeare` character-level tokenizer)
