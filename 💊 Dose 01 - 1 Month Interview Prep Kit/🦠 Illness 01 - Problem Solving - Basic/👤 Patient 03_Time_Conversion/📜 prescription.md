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
