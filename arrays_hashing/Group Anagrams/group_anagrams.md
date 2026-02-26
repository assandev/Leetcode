# Problem
Group Anagrams

## Problem Summary
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.

## Pattern
Hashing / Canonical Representation (Signature Key) / Frequency Counting

## Initial Approach
Tried grouping by direct comparison: for each word, compare it against the remaining words by building a frequency map for the base word and then decrementing while scanning candidate words.

This approach leads to nested loops, dictionary aliasing risks (if not copying), and unstable behavior when modifying the list while iterating.

### Complexity
Time: O(n² * k) where `n` is the number of words and `k` is average word length  
Space: O(k)

## Optimized Approach
Build a canonical signature for each word and use it as a dictionary key to group words with the same signature.

For lowercase English letters (a-z), the signature can be a fixed-size frequency vector of length 26, converted to an immutable tuple:
1. Create `count[26]` for each word
2. Increment counts based on letters
3. Convert to `tuple(count)` and use as the key
4. Append the word to `groups[key]`

### Complexity
Time: O(n * k)  
Space: O(n * k) for storing grouped strings (plus O(1) per word for the 26-length signature)

### Key Insights and Performance Reflections
- Direct comparison between words creates an unnecessary O(n²) structure.
- The key optimization is using a **canonical representation** (signature) so all anagrams map to the same key.
- Using a 26-length frequency vector avoids sorting (which would cost O(k log k)).
- `tuple(count)` is required because lists are mutable and cannot be dictionary keys.
- Mental trigger: “group by equivalence / anagrams / permutations” → build a canonical key and hash-group.