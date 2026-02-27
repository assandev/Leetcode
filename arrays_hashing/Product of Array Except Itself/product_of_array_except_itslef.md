# Problem
Product of Array Except Self

## Problem Summary
Given an integer array `nums`, return an array `output` such that:

    output[i] = product of all elements in nums except nums[i]

Constraints:
- Each product fits in a 32-bit integer.
- Must run in O(n) time.
- Follow-up: Solve without using division.

Example:
Input:  [1,2,4,6]
Output: [48,24,12,8]

Input:  [-1,0,1,2,3]
Output: [0,-6,0,0,0]

## Pattern
Prefix & Suffix Products (Two-Pass Accumulation)

## Initial Approach
A naive approach would be:

1. Compute total product of all elements.
2. For each index i, return total_product / nums[i].

This approach:
- Uses division.
- Fails when zeros are present.
- Violates the follow-up constraint.

### Complexity
Time: O(n)  
Space: O(1)

However, it is logically flawed due to division and zero handling.

## Optimized Approach
Use prefix and suffix products without division.

Core idea:
For each index i:

    output[i] = (product of elements to the left of i)
                ×
                (product of elements to the right of i)

Algorithm:

1. Initialize output array with 1s.
2. First pass (left → right):
   - Store prefix products in output.
3. Second pass (right → left):
   - Maintain a running suffix product.
   - Multiply each output[i] by suffix.
   - Update suffix.

### Complexity

Time: O(n)
Space: O(1) extra space
(The output array does not count as extra space in interview context.)

### Key Insights and Performance Reflections

- The key observation is that each position depends on left × right products.

- We avoid division entirely.

- The algorithm works correctly even with zeros.

- Output array to store prefix products

- A running variable to compute suffix products
