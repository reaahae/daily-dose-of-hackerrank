# 📜 Prescription

# 💊 Patient 08 – Pangrams

### 📌 Problem Link  
🔗 [Pangrams – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
A pangram is a sentence that contains every letter of the English alphabet at least once. Given a sentence, determine whether it is a pangram.

📥 **Input**  
- A single line containing a string `s`.

📤 **Output**  
- Return "pangram" if the sentence contains every letter, otherwise return "not pangram".

📌 **Constraints**  
- The string `s` consists of spaces and English alphabetic characters only.

---

### ✅ Solution 2: Set-Based Approach

#### 🚀 Approach
Use Python's `set` and `string.ascii_lowercase` to check if all 26 letters are present in the sentence.

#### ❓ Why this approach?
- Utilizes Python's built-in capabilities to perform set operations concisely.
- Simple and readable for beginners.

#### 🧩 Steps
1. Convert the input string to lowercase.
2. Create a set of the characters.
3. Check if all 26 lowercase letters (`string.ascii_lowercase`) are in the set.

#### 🧮 Time & Space Complexity

| Metric        | Value   |
|---------------|---------|
| 🕒 Time        | O(n)    |
| 🧠 Space       | O(1)    |

---

### ✅ Solution 2: Early Exit Approach

#### 🚀 Approach
Track seen letters as you iterate through the string. Exit early if all 26 letters are found.

#### ❓ Why this approach?
- Optimized for performance.
- Exits as soon as all letters are found, saving unnecessary checks.

#### 🧩 Steps
1. Initialize an empty `set()` to track letters.
2. Convert the input to lowercase and iterate through it.
3. Add letters to the set if they are alphabetic.
4. Return `"pangram"` if all 26 letters are found early.

#### 🧮 Time & Space Complexity

| Metric        | Value         |
|---------------|---------------|
| 🕒 Time        | O(n) worst case |
| 🕒 Time (Best) | O(k) where k < n |
| 🧠 Space       | O(1)          |

---

### 🧪 Sample Input/Output

```
Input:
We promptly judged antique ivory buckles for the next prize

Output:
pangram
```

```
Input:
We promptly judged antique ivory buckles for the prize

Output:
not pangram
```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 15th April, 2025
