# Problem
Valid Anagram

## Problem Summary
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram is a rearrangement of characters such that both strings contain the same characters with the same frequencies.

## Pattern
Hashing / Frequency Counting

## Initial Approach
Iterate through both strings and check if each character exists in the other string using membership checks (`in`). This leads to repeated lookups inside loops.

This approach results in nested behavior because each membership check in a string is O(n).

### Complexity
Time: O(n²)  
Space: O(1)

The inefficiency comes from performing repeated membership checks inside loops.

## Optimized Approach
Use a dictionary (`hash map`) to count character frequencies.

1. If lengths differ → immediately return False.
2. Traverse string `s` and build a frequency dictionary.
3. Traverse string `t` and decrement the frequency.
4. If a character does not exist or count drops below zero → return False.
5. At the end, verify that all frequencies are balanced.

### Complexity
Time: O(n + m)  
Space: O(k), where k is the number of unique characters.

The improvement comes from:
- Traversing each string only once.
- Using O(1) average dictionary lookup instead of repeated linear membership checks.

### Key Insights and Performance Reflections
- Membership checks in strings are O(n). Doing them inside a loop causes O(n²).
- Dictionary lookups are O(1) average due to hash table implementation.
- The optimized approach avoids nested behavior by separating counting and validation.
- Important guardrail: always validate key existence before decrementing to avoid `KeyError`.
- Tactical takeaway: when a problem involves comparing character frequencies, immediately think **frequency counting with a hash map**.
- Mental trigger: anagram / permutation / same letters → frequency dictionary.