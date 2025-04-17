# 📜 Prescription

# 💊 Patient 05 – Counting Sort 1

### 📌 Problem Link  
🔗 [Counting Sort 1 – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
You are given a list of integers where each value is in the range `0` to `99`. You need to return a frequency array of size 100, where each element at index `i` indicates the number of times `i` appeared in the input list.

📥 **Input**  
- An array of integers in the range `0` to `99`.

📤 **Output**  
- A list of 100 integers representing the frequency of each value.

📌 **Constraints**  
- 100 >= len(arr) >= 1  
- 0 <= arr[i] < 100

---

### 🚀 Approach

📌 **Approach:**  
Use a fixed-size list of 100 elements initialized to 0 and increment the count at each index corresponding to the value encountered.

**Why this approach?**  
- Constant time indexing.  
- Optimal for bounded ranges (0–99).  
- Simple and efficient.

**Steps:**  
1. Create a list of 100 zeros.  
2. Iterate over each number in the input array.  
3. Increment the count at the corresponding index.  
4. Return the frequency list.

---

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n)`    |  
| 🧠 Space       | `O(1)`    | (Since result size is fixed: 100)

---

### 📘 Concepts Learnt

- ✅ **Counting Sort Basics**  
  Counting sort is an integer sorting algorithm suitable when the range of input values is known and limited.  
  📌 **Usage**: Instead of sorting directly, it counts occurrences of each number and reconstructs the sorted result.

- ✅ **Frequency Array**  
  A fixed-size list is used to track how many times each value (0 to 99) appears.  
  📌 **Example**: `result[5] = 3` means the number `5` appears 3 times.

- ✅ **List Initialization in Python**  
  `result = [0] * 100` creates a list of 100 zeros efficiently.  
  📌 **Why**: Prevents manual or loop-based initialization.

- ✅ **In-Place Counting with Indexing**  
  Accessing list elements by index (e.g., `result[i] += 1`) is fast and constant time.  
  📌 **Advantage**: No need for nested loops or complex logic.

- ✅ **Space-Time Tradeoff**  
  Counting sort uses extra space (O(k) where k is the range of values) to achieve better time complexity (O(n)).

- ✅ **Zero-Based Indexing**  
  The input values are assumed to be in the range [0, 99], making it ideal to use them directly as indices in the frequency array.

---

### 🧪 Sample Input/Output

```
Input:
[1, 1, 3, 2, 1]

Output:
[0, 3, 1, 1, 0, 0, ..., 0]  # Total 100 elements
```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 14 April, 2025
