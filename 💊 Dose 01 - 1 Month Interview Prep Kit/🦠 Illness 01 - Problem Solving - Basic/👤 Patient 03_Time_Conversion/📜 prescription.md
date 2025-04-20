# 📜 Prescription

# 💊 Patient 03 – Time Conversion

### 📌 Problem Link  
🔗 [Time Conversion – HackerRank](https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one)

---

### 🧠 Problem Summary

🧮 **Problem Statement**  
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.  
- `12:00:00AM` is `00:00:00` in 24-hour format.  
- `12:00:00PM` is `12:00:00` in 24-hour format.

📥 **Input**  
- A single string `s` representing a time in 12-hour format (e.g., `07:05:45PM`).

📤 **Output**  
- A string representing the input time in 24-hour format.

📌 **Constraints**  
- All input times are valid.

---

### 🚀 Approach

📌 **Approach:**  
Use Python’s built-in `datetime` module to parse the 12-hour formatted time and reformat it to 24-hour format.

**Why this approach?**  
- Built-in libraries reduce the need for manual string operations.
- Python's `strptime` and `strftime` handle format conversions efficiently and accurately.
- Code becomes concise, readable, and avoids logical bugs.

**Steps:**  
1. Parse input time string using `datetime.strptime()` with format `"%I:%M:%S%p"`.
2. Convert the datetime object to 24-hour time using `strftime("%H:%M:%S")`.
3. Return the resulting string.

---

### 🧮 Time & Space Complexity

| Metric        | Value     |
|---------------|-----------|
| 🕒 Time        | `O(1)`    |
| 🧠 Space       | `O(1)`    |

---

### 📘 Concepts Learnt

- ✅ **Datetime Module in Python**  
  Leveraging the `datetime` module simplifies complex time format transformations.  
  📌 **Usage**: `datetime.strptime()` parses string to datetime object; `strftime()` formats it back.

- ✅ **12-hour to 24-hour Format Conversion**  
  Python’s `strptime` with format `"%I:%M:%S%p"` interprets 12-hour time with AM/PM.  
  📌 **Usage**: `%I` = hour (12-hour), `%p` = AM/PM, `%H` = hour (24-hour).

- ✅ **Code Simplicity via Built-in Functions**  
  Instead of manually splitting strings and applying conditions for AM/PM, built-ins handle edge cases like `12AM` → `00`.

- ✅ **Return vs Print in Function Design**  
  Returning a string from the function (`return datetime...`) keeps logic separate from I/O, enabling better testability and reuse.  
  📌 **Good Practice**: Always separate computation from I/O.

- ✅ **Handling Edge Cases**  
  For example:  
  - `12:00:00AM` → `00:00:00`  
  - `12:00:00PM` → `12:00:00`  
  Built-in parsing ensures such cases are correctly handled without manual logic.

---

### 🧪 Sample Input/Output

```
Input:
07:05:45PM

Output:
19:05:45

```

---

### 💻 Language Used  
💬 Python  

---

### 📅 Solved on  
📆 Date: 08th April, 2025
