# Byte Pair Encoding (BPE)

## Sprint 1 - History & Theory

**The Unknown Word Problem:**
A strict word tokenizer treats every slight variation of a word (typos, punctuation, tense) as a completely new, unknown token, causing the vocabulary size to explode.

**Why is learning "play" better than learning every variation (playing, played, player, players)?**
Because "play" is the root word. It has different forms in time or place, but it has a near-uniform meaning overall. By learning the root word, the core semantic meaning is captured efficiently without needing to memorize every possible suffix as a separate token.

## Sprint 2 - Manual Merge Example

Given the words: `low`, `lowest`, `lower`, `newer`, `new`

Show how BPE would merge these manually, step-by-step:

**Initial State (Characters):**
`l o w`, `l o w e s t`, `l o w e r`, `n e w e r`, `n e w`

**Iteration 1:**
Most frequent pair: `l` and `o` (3 times)
Merge into: `lo`
Result: `lo w`, `lo w e s t`, `lo w e r`, `n e w e r`, `n e w`

**Iteration 2:**
Most frequent pair: `lo` and `w` (3 times) — *Note: `w` and `e` also tied with 3!*
Merge into: `low`
Result: `low`, `low e s t`, `low e r`, `n e w e r`, `n e w`
