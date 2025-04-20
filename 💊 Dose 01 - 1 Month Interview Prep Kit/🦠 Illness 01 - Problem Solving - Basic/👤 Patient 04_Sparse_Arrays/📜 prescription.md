# 📜 Prescription

# 💊 Patient 04 – Sparse Arrays

### 📌 Problem Link  
🔗 [Sparse Arrays – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
You are given `n` strings and `q` query strings. For each query string, determine how many times it occurs in the list of input strings.

📥 **Input**  
- The first line contains an integer `n`, the number of strings.  
- The next `n` lines each contain a string.  
- The next line contains an integer `q`, the number of queries.  
- The next `q` lines each contain a query string.

📤 **Output**  
- For each query, print the number of occurrences of the query string in the original list.

📌 **Constraints**  
- 1 <= n, q <= 1000  
- Each string consists of lowercase English letters only.

---

### 🚀 Approach

📌 **Approach:**  
Use Python’s `collections.Counter` to count frequencies of strings and quickly access counts for each query.

**Why this approach?**  
- Fast lookup: Dictionary access with `Counter` is O(1).  
- Clean and readable implementation.  
- Built-in functions reduce risk of logical errors.

**Steps:**  
1. Count the occurrences of each string in the input list using `Counter`.  
2. For each query string, fetch its count using dictionary access.  
3. Return the list of counts.

---

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n + q)`|  
| 🧠 Space       | `O(n)`    |

---

### 📘 Concepts Learnt

- ✅ **Using `collections.Counter` for Frequency Counting**  
  `Counter` provides an elegant way to count occurrences of items in a list.  
  📌 **Usage**: `Counter(strings)` builds a dictionary-like object where keys are strings and values are their frequencies.

- ✅ **Optimized Query Lookup**  
  Instead of looping through the list for every query (which would be `O(n*q)`), we use a precomputed frequency map for constant-time access.  
  📌 **Access**: `string_counter[x]` gives the count in `O(1)`.

- ✅ **List Comprehension for Efficient Iteration**  
  Used to build the result list concisely and efficiently.  
  📌 Example: `[string_counter[x] for x in queries]`

- ✅ **Default Value Handling with `Counter`**  
  If a queried string is not in the original list, `Counter` returns `0` automatically — no need for `if` conditions.

- ✅ **Clean Separation of Logic**  
  Logic is wrapped in a reusable function returning data (not printing), supporting testability and modularity.

---

### 🧪 Sample Input/Output

```
Input:
4
abc
def
abc
ghi
3
abc
ghi
xyz

Output:
2
1
0
```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 09th April, 2025
