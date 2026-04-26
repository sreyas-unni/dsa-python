---

# Second Largest Element in Array

## Problem
Given an array of integers, find the second largest element without sorting.

## Approaches

### Approach 1 — Sorting (Brute Force) ❌
```python
def getSecondLargest(arr):
    arr.sort()
    return arr[-2]
```
- Time: O(n log n)
- Space: O(n)
- Why avoid: Sorting entire array is overkill

---

### Approach 2 — Two Pass (Better) ⚠️
```python
def getSecondLargest(arr):
    largest = max(arr)
    second_largest = -1
    for num in arr:
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest
```
- Time: O(n) — but two passes
- Space: O(1)
- Why avoid: Two passes when one is enough

---

### Approach 3 — Single Pass (Optimal) ✅
```python
def getSecondLargest(arr):
    largest = -1
    second_largest = -1
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest
```
- Time: O(n) — single pass
- Space: O(1)
- Why best: One loop, handles duplicates, no sorting

## Key Takeaway
Always try to solve in a single pass. Two O(n) passes is still O(n)
