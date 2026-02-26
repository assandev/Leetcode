# Problem
Encode and Decode Strings

## Problem Summary
Design an algorithm to encode a list of strings into a single string and then decode it back to the original list of strings.

The encoding must be reversible and must work for any possible string content (including special characters, digits, or empty strings).

## Pattern
String Manipulation + Canonical Length Prefix Encoding

## Initial Approach
A naive idea would be to concatenate strings using a delimiter (e.g., "#") and then split during decoding.

However, this approach fails if any original string contains the delimiter itself. That would create ambiguity and break decoding.

Example failure case:
["ab#c", "x"] → "ab#c#x"  
Impossible to decode safely.

### Complexity
Not applicable, since this approach is logically flawed.

## Optimized Approach
Use length-prefix encoding to eliminate ambiguity.

For each string `s`:
1. Store its length.
2. Append a fixed separator (e.g., "#").
3. Append the string itself.

Encoded format:
<length>#<string>

Example:
["ab#c", "", "xyz"]
→ "4#ab#c0#3#xyz"

During decoding:
1. Read characters until "#" to extract the length.
2. Convert the substring to integer.
3. Read exactly `length` characters after "#".
4. Repeat until the end of the string.

---

### Key Insights and Performance Reflections

- Using only a delimiter is unsafe because the delimiter may appear in the original strings.

- Length-prefix encoding guarantees unambiguous decoding.

- The decoder never depends on the content of the string, only on the stored length.

- Python slicing makes substring extraction clean and efficient.

- Important design principle: when serializing data, always include metadata to remove ambiguity.