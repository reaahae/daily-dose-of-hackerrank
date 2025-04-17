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

### 📘 Concepts Learnt

- ✅ **Set in Python**  
  A `set` is an unordered collection of unique elements. It is ideal for membership testing and eliminating duplicates.  
  📌 **Usage**: Used to track distinct letters in the sentence.

- ✅ **string.ascii_lowercase**  
  From the `string` module, this gives a string of all lowercase English letters (`'abcdefghijklmnopqrstuvwxyz'`).  
  📌 **Usage**: Helps compare whether the sentence covers the full alphabet.

- ✅ **Early Exit Strategy**  
  To enhance performance, especially for large inputs, the program stops checking once all 26 letters have been found.

- ✅ **Membership Check (`in`)**  
  Efficiently checks whether a letter is in a set. This operation runs in average O(1) time.

- ✅ **Lowercasing Strings**  
  Ensures case-insensitive comparisons since both uppercase and lowercase letters are treated the same in pangrams.

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
