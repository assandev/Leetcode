# Contains Duplicate

## Problem Summary
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

---

## Pattern
Hashing / Set membership

This is a classic membership-check optimization problem.

---

## Initial Approach

Used a list (`seen = []`) to track visited elements:

- For each element, checked `if num in seen`
- Then appended it

### Complexity

- Time: O(n²)
  - Membership check in list is O(n)
  - Done inside a loop of size n
- Space: O(n)

---

## Optimized Approach

Use a `set` to track visited elements.

> [!INFO]
> Set membership is O(1) average due to hash table implementation.

### Complexity
- Time: O(n)
    - Each membership check and insertion in a set is O(1) on average
- Space: O(n)
    - In the worst case, all elements are distinct, so we store all n elements in the set.

### Key Insights and Performance Reflections

When checking for duplicates, using a list for membership checks leads to O(n) time per check, resulting in O(n²) overall. In contrast, using a set allows for O(1) average time complexity for membership checks and insertions, leading to an overall O(n) time complexity. This optimization is crucial for large input sizes, as it significantly reduces the time taken to determine if duplicates exist in the array.
