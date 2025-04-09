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
