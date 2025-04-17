# 📜 Prescription

# 💊 Patient 07 – Diagonal Difference

### 📌 Problem Link  
🔗 [Diagonal Difference – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

📥 **Input**  
- The first line contains a single integer `n`, the number of rows and columns in the square matrix.  
- Each of the next `n` lines describes a row, containing `n` space-separated integers.

📤 **Output**  
- Print the absolute difference between the sums of the matrix's two diagonals.

📌 **Constraints**  
- 1 <= n <= 100  
- -100 <= arr[i][j] <= 100

---

### 🚀 Solution 1 - Using Nested Loops and Manual Index Tracking

#### ✅ Approach
Use nested loops to iterate through the matrix. Add elements on the primary diagonal where `i == j` and use a manual index counter to track the secondary diagonal.

#### ❓ Why this approach?
It clearly separates how we access each diagonal and is easy to follow for beginners learning matrix traversal.

#### 🧩 Steps
1. Initialize `diag1` and `diag2` to 0.
2. Use a nested loop to find and sum the primary diagonal (`arr[i][i]`).
3. Use a manually managed index (`index = len(arr)`) to access the secondary diagonal (`arr[i][index - 1]`).
4. Return the absolute difference.

#### 🧮 Time & Space Complexity

| Metric        | Value   |
|---------------|---------|
| 🕒 Time        | O(n²)   |
| 🧠 Space       | O(1)    |

---

### 🚀 Solution 2 - Using Single Loop and Mathematical Indexing


#### ✅ Approach
Use a single loop to directly access both diagonals using mathematical indexing.

#### ❓ Why this approach?
- Reduces nested loop overhead.
- More readable and elegant.
- Minimizes computations.

#### 🧩 Steps
1. Initialize `diag1` and `diag2` to 0.
2. Use a single loop (`for i in range(n)`) to traverse rows.
3. Access the primary diagonal using `arr[i][i]`.
4. Access the secondary diagonal using `arr[i][n - 1 - i]`.
5. Return the absolute difference.

#### 🧮 Time & Space Complexity

| Metric        | Value   |
|---------------|---------|
| 🕒 Time        | O(n)    |
| 🧠 Space       | O(1)    |

---

### 📘 Concepts Learnt

- ✅ **Matrix Traversal in Python**  
  Iterating through a 2D list (matrix) using nested loops helps access elements row by row and column by column.  
  📌 **Usage**: Looping with `for i in range(len(arr))` helps target each row.

- ✅ **Primary Diagonal Identification**  
  In a square matrix, the primary diagonal elements have equal row and column indices: `arr[i][i]`.

- ✅ **Secondary Diagonal Identification**  
  For the secondary diagonal, the column index decreases as the row index increases: `arr[i][n - 1 - i]`.

- ✅ **Index Manipulation**  
  Managing indices effectively (like decrementing or calculating `n - 1 - i`) is key to accessing the correct elements diagonally.

- ✅ **Absolute Difference Calculation**  
  `abs(x - y)` is a built-in Python function used to calculate the non-negative difference between two values.  
  📌 **Usage**: Required to return the final answer per problem specification.

- ✅ **Code Optimization (Solution 2)**  
  Avoiding nested loops and using single-loop index math improves readability and performance.  
  📌 **Example**: `arr[i][n - 1 - i]` instead of maintaining a separate `index` variable.

- ✅ **Cleaner Variable Management**  
  Using meaningful variable names (`diag1`, `diag2`) and initializing once reduces overhead and enhances clarity.

---

### 🧪 Sample Input/Output

```
Input:
3
11 2 4
4 5 6
10 8 -12

Output:
15

```

---

### 💻 Language Used  
💬 Python

---

### 📅 Solved on  
📆 Date: 13th April, 2025

