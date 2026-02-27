# Longest Consecutive Sequence

## Problem Summary
Given an unsorted array of integers `nums`, return the length of the longest consecutive sequence of elements.

A consecutive sequence means each element is exactly 1 greater than the previous.

Constraints:
- Must run in O(n) time.
- Elements do not need to be consecutive in the original array.

Example:
Input:  [2,20,4,10,3,4,5]
Output: 4  (sequence: [2,3,4,5])

Input:  [0,3,2,5,4,6,1,1]
Output: 7  (sequence: [0,1,2,3,4,5,6])

## Pattern
Hash Set + Sequence Start Detection

## Initial Approach
A naive approach would be:

1. Sort the array.
2. Traverse and count consecutive runs.

However:
- Sorting costs O(n log n).
- The problem explicitly requires O(n) time.

### Complexity
Time: O(n log n)  
Space: O(1)

This violates the required time complexity.

## Optimized Approach
Use a hash set for O(1) membership checks.

Key Insight:
A number `x` is the start of a sequence only if `(x - 1)` is NOT in the set.

Algorithm:

1. Convert nums into a set to:
   - Remove duplicates
   - Enable O(1) lookup

2. For each number x in the set:
   - If (x - 1) is not in the set:
     - Start counting consecutive numbers from x upward
     - Continue while (x + 1) exists in the set

3. Track the maximum sequence length.

### Key Insights and Performance Reflections

- Sorting is unnecessary and violates O(n).

- A set does NOT maintain order; it enables constant-time lookup.

- The critical optimization is only expanding from true sequence starts.

- If (x - 1) exists, we skip because that sequence has already been counted.

- Duplicates are automatically handled by converting to a set.

- This is a classic example of using hashing to simulate ordering logic without sorting.