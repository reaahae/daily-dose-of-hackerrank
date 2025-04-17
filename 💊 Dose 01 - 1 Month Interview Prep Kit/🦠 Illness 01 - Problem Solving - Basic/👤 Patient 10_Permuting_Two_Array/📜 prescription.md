
# 📜 Prescription

# 💊 Patient 10 – Permuting Two Arrays

### 📌 Problem Link  
🔗 [Permuting Two Arrays – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
Given two arrays A and B of the same length and an integer `k`, determine whether there is a permutation of the arrays such that the sum of corresponding elements in A and B is greater than or equal to `k` for every index.

📥 **Input**  
- Two integer arrays `A` and `B`, both of size `n`.
- An integer `k`.

📤 **Output**  
- Return "YES" if such a permutation exists, otherwise return "NO".

📌 **Constraints**  
- 1 ≤ n ≤ 1000  
- 0 ≤ A[i], B[i] ≤ 10⁹  
- 0 ≤ k ≤ 10⁹

---

### ✅ Solution 1: Brute Force

#### 🚀 Approach
Sort A in ascending order and B in descending order. Check if every pair `A[i] + B[i] ≥ k`.

#### ❓ Why this approach?
- Ensures maximum possible sum at each index.
- Greedy strategy guarantees an optimal match.

#### 🧩 Steps
1. Sort A in ascending order.
2. Sort B in descending order.
3. Check each pair's sum:
   - If any `A[i] + B[i] < k`, return `'NO'`.
4. If all pairs satisfy the condition, return `'YES'`.

#### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | O(n log n) |
| 🧠 Space       | O(1)       |

---

### ✅ Solution 2: Pythonic One-Liner with `all()` and `zip()`

#### 🚀 Approach
Use Python’s `zip()` and `all()` to make the logic cleaner and more readable.

#### ❓ Why this approach?
- Elegant and concise.
- Easy to debug and test.

#### 🧩 Steps
1. Sort A (asc), B (desc).
2. Use `zip()` to pair elements.
3. Use `all()` to validate every pair sum.

#### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | O(n log n) |
| 🧠 Space       | O(1)       |

---

### 📘 Concepts Learnt

- ✅ **Greedy Strategy**  
  Greedy algorithms make locally optimal choices at each step. Here, sorting one array ascending and the other descending ensures we maximize each pair's sum.

- ✅ **Sorting Before Comparison**  
  Sorting helps us align the weakest element of A with the strongest of B to get the highest possible sum at every index.

- ✅ **Early Exit in Loops**  
  As soon as a condition fails (`A[i] + B[i] < k`), we exit early, avoiding unnecessary iterations.

- ✅ **zip()**  
  `zip()` is a Python built-in function that aggregates elements from two or more iterables (like lists).  
  📌 **Usage**: Helps pair elements from `A` and `B` index-wise, making comparisons cleaner and more readable.  
  📘 **Example**: `zip([1, 2], [3, 4]) → (1, 3), (2, 4)`

- ✅ **all()**  
  `all()` returns `True` if all elements in the iterable are `True`.  
  📌 **Usage**: Used with list comprehensions or generators to check if all conditions are met (e.g., all sums `>= k`).  
  📘 **Example**: `all(x > 0 for x in [1, 2, 3]) → True`

- ✅ **List Comprehension + Generator Expression**  
  Using generator expressions within `all()` provides concise, memory-efficient logic for validating conditions.

- ✅ **Pythonic Syntax for Clean Code**  
  Python allows compact yet readable implementations using built-in functions and idiomatic expressions.

- ✅ Greedy strategy for maximizing pair sum.
- ✅ Using `zip()` and `all()` for cleaner iteration.
- ✅ Early return for optimization.
- ✅ Sorting as a preprocessing step in algorithm design.

---

### 🧪 Sample Input/Output

```
Input:
k = 10  
A = [2, 1, 3]  
B = [7, 8, 9]

Output:
YES
```

```
Input:
k = 5  
A = [1, 2, 2]  
B = [1, 3, 3]

Output:
NO
```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 17th April, 2025
