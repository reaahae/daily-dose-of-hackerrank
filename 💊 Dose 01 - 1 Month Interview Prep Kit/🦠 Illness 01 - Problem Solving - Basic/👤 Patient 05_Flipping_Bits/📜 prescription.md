
# 📜 Prescription

# 💊 Patient 05 – Flipping Bits

### 📌 Problem Link  
🔗 [Flipping Bits – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
You will be given a list of 32-bit unsigned integers. Flip all the bits (i.e., convert 1 to 0 and 0 to 1) and return the result as an unsigned integer.

📥 **Input**  
- A single unsigned integer `n`.

📤 **Output**  
- Return an unsigned integer result after flipping all 32 bits of `n`.

📌 **Constraints**  
- `0 <= n <= 2^32 - 1`

---

### 🚀 Approach

📌 **Approach:**  
Hardcoded bit manipulation using:
- Manual binary conversion
- Padding to 32-bit
- Bit flipping logic using strings
- Binary to decimal conversion (manually via loop)

**Why this approach?**  
- Reinforces understanding of binary arithmetic and bit manipulation.

**Steps:**  
1. Convert number to binary using modulus/division.
2. Pad the result manually to 32 bits.
3. Flip each bit using conditional logic.
4. Convert the new binary string back to decimal using positional power multiplication.

---

### 🧮 Time & Space Complexity

| Metric        | Value      |
|---------------|------------|
| 🕒 Time        | `O(32)`    |  
| 🧠 Space       | `O(32)`    |

---

### 🧪 Sample Input/Output

```
Input:
3 
2147483647 
1 
0

Output:
2147483648 
4294967294 
4294967295

```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 11th April, 2025
