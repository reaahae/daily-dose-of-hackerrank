
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

## ✅ Solution 1: Manual (Hardcoded) Bit Manipulation

### 🚀 Approach
- Manually convert the number to binary using division and modulus.
- Pad the binary number to 32 bits by adding leading zeros.
- Flip each bit one-by-one using conditional checks.
- Convert the flipped binary back to a decimal integer manually using power of 2 logic.

### 🤔 Why this approach?
- Good for learning the basics of bit manipulation.
- No use of built-in functions — reinforces understanding of binary arithmetic.
- Useful for educational or interview contexts where understanding matters more than speed.

### 🧩 Steps
1. Convert the number to binary using `%` and `//`.
2. Add leading zeros until length becomes 32.
3. Flip each bit (`'0' -> '1'` and `'1' -> '0'`).
4. Convert the new binary string to decimal using loop and powers of 2.

### ⏱️ Time & Space Complexity
| Metric        | Value      |
|---------------|------------|
| 🕒 Time        | O(32)      |
| 🧠 Space       | O(32)      |

---

## ✅ Solution 2: Using Python Built-ins (Semi-Manual)

### 🚀 Approach
- Use `bin()` to convert the number to binary.
- Pad the binary string to 32 bits using `zfill()`.
- Flip the bits using a one-liner comprehension.
- Convert the binary string back to an integer using `int(..., 2)`.

### 🤔 Why this approach?
- Uses minimal built-in functions for cleaner, more readable code.
- Good trade-off between control and performance.
- Easier to implement and debug.

### 🧩 Steps
1. Convert `n` to binary string: `bin(n)[2:]`.
2. Use `.zfill(32)` to ensure 32-bit representation.
3. Flip all bits using a generator expression.
4. Convert flipped binary back to decimal.

### ⏱️ Time & Space Complexity
| Metric        | Value      |
|---------------|------------|
| 🕒 Time        | O(32)      |
| 🧠 Space       | O(32)      |

---

## ✅ Solution 3: Bitwise XOR (Most Efficient)

### 🚀 Approach
- Use the XOR operator `^` with `0xFFFFFFFF` to flip all 32 bits of the number.

### 🤔 Why this approach?
- Fastest and most efficient method for this specific problem.
- Minimal memory usage, ideal for large input sizes.
- One-liner — perfect for production-grade code or competitive programming.

### 🧩 Steps
1. XOR the number with `0xFFFFFFFF` (i.e., 4294967295 in decimal).
2. The result will be the flipped 32-bit version of `n`.

### ⏱️ Time & Space Complexity
| Metric        | Value      |
|---------------|------------|
| 🕒 Time        | O(1)       |
| 🧠 Space       | O(1)       |

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
