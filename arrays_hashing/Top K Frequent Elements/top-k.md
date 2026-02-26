# Top K Frequent Elements


## Problem Summary
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

The answer is guaranteed to be unique. The output can be returned in any order.

Constraints:
- 1 ≤ nums.length ≤ 10⁴
- 1 ≤ k ≤ number of distinct elements

## Pattern
Hashing + Sorting (Frequency Counting + Ordering by Value)

## Initial Approach
1. Traverse the array and build a frequency dictionary:
   - key → number
   - value → frequency count

2. Convert the dictionary into an iterable of `(number, frequency)` pairs using `freq.items()`.

3. Sort those pairs by frequency in descending order.

4. Take the first `k` elements using slicing.

5. Extract only the numbers from the `(number, frequency)` tuples.

### Optimized Approach

For the given constraints (n ≤ 10⁴), the sorting-based approach is acceptable and clean.
Further optimization (Heap or Bucket Sort) would reduce complexity to O(n), but is not strictly required unless explicitly stated.

### Key Insights and Performance Reflections

A dictionary cannot be directly sorted by values unless we expose its key-value pairs.

`freq.items()` returns a dictionary view of `(key, value)` pairs. While technically a view object, logically it behaves as a sequence of tuples that `sorted() `can process.

Without using `freq.items()`, calling `sorted(freq)` would only sort keys (numbers), not frequencies.

- Using `key=lambda p: p[1]` allows sorting by frequency (the second element of each tuple).
 
- `sorted()` in Python is stable, meaning elements with equal frequency preserve insertion order.

- The list comprehension [num for num, _ in ...] extracts only the numbers from the (number, frequency) tuples.

Important distinction: sorting is O(m log m), not O(n + m). This matters when reasoning about performance.