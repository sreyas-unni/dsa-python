---

# Check if Array is Sorted

## Problem
Given an array of integers, check if the array is sorted 
in non-decreasing order. Return True or False.

## Approaches

### Approach 1 — Sorting (Brute Force) ❌

    def check_sorted(arr):
        sorted_arr = sorted(arr)
        return arr == sorted_arr

- Time: O(n log n)
- Space: O(n)
- Why avoid: Creating a new sorted array just to compare is wasteful

---

### Approach 2 — Single Pass (Optimal) ✅

    def check_sorted(arr):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

- Time: O(n)
- Space: O(1)
- Why best: Compare adjacent elements, stop immediately when unsorted found

## Dry Run
arr = [1, 3, 2, 4, 5]

i=0 → arr[0]=1, arr[1]=3 → 1 > 3? No → continue
i=1 → arr[1]=3, arr[2]=2 → 3 > 2? Yes → return False ✅

## Key Takeaway
Compare adjacent elements in a single pass.
Early return as soon as unsorted pair is found — no need to check rest of array.
