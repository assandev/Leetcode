# Two Sum


## Problem Summary
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.  
Assumptions typically include: exactly one valid answer exists, and the same element cannot be used twice.

## Pattern
Hashing / One-pass Hash Map (complement lookup)

## Initial Approach
Maintain a dictionary `seen` that maps a number to its index while iterating through the array. For each element `x`, compute `complement = target - x` and check if `complement` is already in `seen`. If yes, return `[seen[complement], current_index]`. Otherwise, store `seen[x] = current_index` and continue.

### Complexity
Time: O(n) average  
Space: O(n)

## Optimized Approach
No change required — the initial approach is already optimal for the constraints and is the expected solution in high-performance interviews.

### Key Insights and Performance Reflections
- In Python, `dict` membership checks like `if key in seen:` operate on **keys** (not values) and are **O(1) average** due to hash table implementation.
- `seen[key] = value` inserts/updates without deleting other entries.
- I can improve code clarity and reduce indexing mistakes by using `enumerate(nums)` to access both index and value directly instead of manually indexing with `range(len(nums))`.
- The main improvement opportunity here is fluency: instantly recognizing when to use a hash map and remembering its complexity characteristics without hesitation.