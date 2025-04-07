# 📜 Prescription

# 💊 Patient 01 – Plus Minus

### 📌 Problem Link  
🔗 [Plus Minus – HackerRank]([https://](https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one))

---

### 🧠 Problem Summary
🧮 Problem Statement
Given an array of integers, the task is to calculate the ratios of its elements that are positive, negative, and zero. Each ratio should be printed on a new line with exactly 6 digits after the decimal point.

This challenge emphasizes precision handling, so results are validated up to six decimal places (a small margin of absolute error is acceptable).

📥 Input
- An integer n: the number of elements in the array.
- A line of n space-separated integers representing the array.

📤 Output
1. Print three lines, each showing:
2. The proportion of positive numbers
3. The proportion of negative numbers
4. The proportion of zeros
5. Each value must be displayed with 6 decimal places.

📌 Constraints
- 1 ≤ n ≤ 100
- Each element in the array is between -100 and 100.

---

### 🚀 Approach

📌 Approach:
The plusMinus function calculates the ratio of positive, negative, and zero elements in a given integer array.

Why this approach?
1. This method is simple, readable, and efficient.
2. It uses Python generator expressions inside sum() to count occurrences in a single line, making the code concise.
3. We avoid manual iteration or maintaining counters with loops, improving clarity and reducing potential for errors.
4. The logic is split into clean steps: counting → calculating ratios → formatting → printing, which is ideal for maintenance and debugging.

Steps:
1. Count positive numbers: Using a generator expression with sum() to count elements > 0.
2. Count negative numbers: Similarly count elements < 0.
3. Count zeroes: Count elements == 0.
4. Compute proportions: Divide each count by the total number of elements in the array.
5. Format and print: Each proportion is printed with 6 decimal places, one per line.

---

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(n)`    |
| 🧠 Space       | `O(1)`    |

---

### 🧪 Sample Input/Output

```
Input:
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Output:
0.500000
0.333333
0.166667

```

---

### 💻 Language Used
💬 Python 

---

### 📅 Solved on
📆 Date
