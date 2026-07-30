# Engineering Comparison: Character vs. Word Tokenization

| Feature | Character Tokenizer | Word Tokenizer |
| :--- | :--- | :--- |
| **Vocabulary Size** | Very small (e.g., ~100-200 characters) | Massive (hundreds of thousands of words) |
| **Sequence Length** | Very long (one ID per letter) | Short (one ID per word) |
| **Unknown Problem** | Very rare (almost all characters are known) | Very common (typos, new slang, names) |
| **Memory** | Low memory for the embedding matrix | High memory for the embedding matrix |
| **Generalization** | Highly flexible to new words and typos | Poor flexibility (treats typos as completely new words) |

## Chris's Challenge
**Sentence:** `"Transformers changed AI forever."`

- **Character output:** `['T', 'r', 'a', 'n', 's', 'f', 'o', 'r', 'm', 'e', 'r', 's', ...]`
- **Word output:** `['Transformers', 'changed', 'AI', 'forever.']`

**Conclusion:**
The word output is much easier for a model to learn from. As you perfectly noted: *"It makes sense instead of individual chars which are raw. We see walls instead of specific bricks."* 

Because words carry intrinsic semantic meaning, the model can immediately start learning the relationships between concepts, rather than wasting its initial learning capacity just trying to figure out how to stitch 12 individual letters together to form the concept of a "Transformer".
