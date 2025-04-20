# 📜 Prescription

# 💊 Patient 02 – Mini-Max Sum

### 📌 Problem Link  
🔗 [Mini-Max Sum – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary
🧮 Problem Statement
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.  
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

📥 Input
- A single line of **five space-separated positive integers**.

📤 Output
- Print **two space-separated long integers**:
  - The **minimum** sum of any four of the five integers.
  - The **maximum** sum of any four of the five integers.

📌 Constraints
- `1 ≤ arr[i] ≤ 10⁹`
- Exactly **5 integers** in the input.
- Each integer is **positive**.
- The output may exceed 32-bit range, so use **64-bit integers**.

---

## ✅ Solution 1: Sorting + Slicing

### 🚀 Approach

📌 **Approach:**
We sort the array to easily access the smallest and largest values, then sum the first 4 and last 4 elements to get the minimum and maximum sums respectively.

**Why this approach?**
- Easy to understand and implement.
- Sorting gives direct access to the smallest and largest values.
- Clean and Pythonic using slicing.

**Steps:**
1. Sort the array using `sorted(arr)`.
2. Sum the first 4 elements → `min_sum = sum(sorted_arr[:4])`.
3. Sum the last 4 elements → `max_sum = sum(sorted_arr[-4:])`.
4. Print both values.

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n log n)` |
| 🧠 Space       | `O(n)`    |

---

## ✅ Solution 2: Sum – Max/Min Optimization

### 🚀 Approach

📌 **Approach:**
We use the fact that to get the **minimum sum**, we can subtract the most significant element from the total sum, and for **maximum sum**, subtract the smallest element from the total.

**Why this approach?**
- No sorting needed.
- More efficient for fixed-sized arrays (like this one).
- Very concise and clean logic.

**Steps:**
1. Calculate total sum of the array → `total = sum(arr)`.
2. Compute `min_sum = total - max(arr)`.
3. Compute `max_sum = total - min(arr)`.
4. Print both values.

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n)`    |
| 🧠 Space       | `O(1)`    |

---

### 📘 Concepts Learnt

- ✅ **Array Sorting in Python**  
  The `sorted()` function returns a new sorted list, making it easy to access the smallest and largest values directly.  
  📌 **Usage**: `sorted(arr)` for arranging the array in ascending order.

- ✅ **List Slicing**  
  Python’s slicing syntax allows quick selection of sublists.  
  📌 **Usage**: `arr[:4]` gets the first 4 elements; `arr[-4:]` gets the last 4 elements after sorting.

- ✅ **Built-in Aggregation Functions**  
  Python’s `sum()`, `max()`, and `min()` provide fast and readable ways to compute totals and boundaries.  
  📌 **Usage**: `sum(arr)` for total, `max(arr)` to get the largest number, `min(arr)` to get the smallest.

- ✅ **Alternative Optimization Techniques**  
  Using `sum(arr) - max(arr)` and `sum(arr) - min(arr)` avoids the need to sort.  
  📌 **Usage**: Reduces time complexity from `O(n log n)` to `O(n)`.

- ✅ **Print Formatting**  
  Python’s `print(a, b)` prints space-separated values in a single line.  
  📌 **Usage**: Clean output without needing string concatenation.

- ✅ **Time & Space Complexity Optimization**  
  Knowing when to avoid sorting (if not required) helps achieve better performance in large-scale problems.  
  📌 **Usage**: `Solution 2` leverages this idea for optimal performance.

- ✅ **Working with Large Integers**  
  Recognizing that values can exceed 32-bit integer range, especially when using 10⁹, and relying on Python's native arbitrary-precision integers.  
  📌 **Usage**: No special data types needed in Python, but awareness is crucial for other languages.

---

### 🧪 Sample Input/Output

```
Input:
7 69 2 221 8974

Output:
299 9271

```

---

### 💻 Language Used
💬 Python 

---

### 📅 Solved on
📆 Date: 08th April, 2025

