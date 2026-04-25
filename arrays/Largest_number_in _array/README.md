# Problem 1: Largest Element in Array

## Problem
Given an array of integers, find and return the largest element.

## Approaches

### Approach 1 — Sorting (Brute Force) 
```python
def largest(arr):
    arr.sort()
    return arr[-1]
```
- Time: O(n log n)
- Space: O(n)
- Why avoid: Sorting entire array just to find max is overkill
- The thing is interviewer looks for optimal solution

---

### Approach 2 — max() built-in ⚠️
```python
def largest(arr):
    return max(arr)
```
- Time: O(n)
- Space: O(1)
- Why avoid in interviews: Hides the logic, interviewer will ask you to implement it manually

---

### Approach 3 — Linear Scan (Optimal) ✅
```python
def largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
```
- Time: O(n)
- Space: O(1)
- Why best: Single pass, no extra space, shows clear thinking

## Key Takeaway
Never sort to find min or max. Always use linear scan.
