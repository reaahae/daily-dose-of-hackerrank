# 📜 Prescription

# 💊 Patient 05 – Lonely Integer

### 📌 Problem Link  
🔗 [Lonely Integer – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
Given an array of integers where all elements except one occur twice, find the element that occurs only once.

📥 **Input**  
- The first line contains a single integer, `n`, the number of integers in the array.  
- The second line contains `n` space-separated integers.

📤 **Output**  
- Print the integer that occurs only once.

📌 **Constraints**  
- 1 <= n < 100  
- It is guaranteed that exactly one integer occurs once and the rest occur in pairs.

---

### 🚀 Approach

📌 **Approach:**  
Use **bitwise XOR** to find the unique element.

**Why this approach?**  
- XOR of a number with itself is 0: `x ^ x = 0`  
- XOR of a number with 0 is the number itself: `x ^ 0 = x`  
- Therefore, all paired elements cancel each other out, leaving the unique one.

**Steps:**  
1. Initialize a variable `result = 0`.  
2. Iterate through the array and XOR each element with `result`.  
3. The final value of `result` is the lonely integer.

---

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n)`    |  
| 🧠 Space       | `O(1)`    |

---

### 🧪 Sample Input/Output

```
Input: 5 1 2 3 4 3 2 1
Output: 4

```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 10th April, 2025

