# Pattern Printing in Python

A comprehensive guide to understanding and creating different pattern-printing programs in Python. Perfect for beginners who want to strengthen their logic-building and looping concepts.

---

## 📌 Table of Contents

| S.No. | Pattern Name | Problem Link | Solution Link |
|-------|--------------|--------------|---------------|
| 1 | Square Star Pattern | [Problem](#1-square-star-pattern) | [Solution](#1-square-star-pattern) |
| 2 | Left Triangle Pattern | [Problem](#2-left-triangle-pattern) | [Solution](#2-left-triangle-pattern) |
| 3 | Right Triangle Pattern | [Problem](#3-right-triangle-pattern) | [Solution](#3-right-triangle-pattern) |
| 4 | Number Triangle Pattern | [Problem](#4-number-triangle-pattern) | [Solution](#4-number-triangle-pattern) |
| 5 | Same Number Triangle Pattern | [Problem](#5-same-number-triangle-pattern) | [Solution](#5-same-number-triangle-pattern) |
| 6 | Inverted Number Pattern | [Problem](#6-inverted-number-pattern) | [Solution](#6-inverted-number-pattern) |
| 7 | Number Sequence Pattern | [Problem](#7-number-sequence-pattern) | [Solution](#7-number-sequence-pattern) |
| 8 | Pyramid Pattern | [Problem](#8-pyramid-pattern) | [Solution](#8-pyramid-pattern) |
| 9 | Inverted Pyramid | [Problem](#9-inverted-pyramid) | [Solution](#9-inverted-pyramid) |
| 10 | Diamond Pattern | [Problem](#10-diamond-pattern) | [Solution](#10-diamond-pattern) |
| 11 | Number Pyramid with Dashes | [Problem](#11-number-pyramid-with-dashes) | [Solution](#11-number-pyramid-with-dashes) |
| 12 | Reverse Number Pyramid | [Problem](#12-reverse-number-pyramid) | [Solution](#12-reverse-number-pyramid) |
| 13 | Hollow Square Pattern | [Problem](#13-hollow-square-pattern) | [Solution](#13-hollow-square-pattern) |
| 14 | Hollow Rectangle Pattern | [Problem](#14-hollow-rectangle-pattern) | [Solution](#14-hollow-rectangle-pattern) |
| 15 | Hollow Diamond Pattern | [Problem](#15-hollow-diamond-pattern) | [Solution](#15-hollow-diamond-pattern) |
| 16 | Butterfly Pattern | [Problem](#16-butterfly-pattern) | [Solution](#16-butterfly-pattern) |
| 17 | Number Pattern with Dashes | [Problem](#17-number-pattern-with-dashes) | [Solution](#17-number-pattern-with-dashes) |
| 18 | Complex Number Pattern | [Problem](#18-complex-number-pattern) | [Solution](#18-complex-number-pattern) |
| 19 | Inverted Triangle Pattern | [Problem](#19-inverted-triangle-pattern) | [Solution](#19-inverted-triangle-pattern) |
| 20 | Combined Triangle Pattern | [Problem](#20-combined-triangle-pattern) | [Solution](#20-combined-triangle-pattern) |
---

## 📚 What You Will Learn

* Basics of loops for pattern printing
* Star (`*`) patterns
* Number patterns
* Alphabet patterns
* Pyramid patterns
* Hollow patterns
* Advanced patterns
* Common mistakes and how to fix them
* Practice exercises

---

## ⭐ Basic Patterns

### **1. Square Star Pattern**
```
*****
*****
*****
*****
*****
```
**Solution:**
```python
rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

### **2. Left Triangle Pattern**
```
*
**
***
****
*****
```
**Solution:**
```python
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()
```

### **3. Right Triangle Pattern**
```
    *
   **
  ***
 ****
*****
```
**Solution:**
```python
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (i + 1))
```

---

## 🔢 Number Patterns

### **4. Number Triangle Pattern**
```
1
12
123
1234
12345
```
**Solution:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### **5. Same Number Triangle Pattern**
```
1
22
333
4444
55555
```
**Solution:**
```python
for i in range(5):
    for j in range(i + 1):
        print(i + 1, end="")
    print()
```

### **6. Inverted Number Pattern**
```
12345
1234
123
12
1
```
**Solution:**
```python
for i in range(5):
    for j in range(1, 6 - i):
        print(j, end="")
    print()
```

### **7. Number Sequence Pattern**
```
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
```
**Solution:**
```python
num = 0
for i in range(1, 6):
    for j in range(i):
        num += 1
        print(f"{num} ", end="")
    print()
```

---

## 🔺 Pyramid Patterns

### **8. Pyramid Pattern**
```
    *
   ***
  *****
 *******
*********
```
**Solution:**
```python
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
```

### **9. Inverted Pyramid**
```
*********
 *******
  *****
   ***
    *
```
**Solution:**
```python
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```

### **10. Diamond Pattern**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```
**Solution:**
```python
# Upper part
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    for m in range(i):
        print("*", end="")
    print()

# Lower part
for i in range(4):
    for j in range(i + 2):
        print(" ", end="")
    for k in range(4 - i):
        print("*", end="")
    for m in range(3 - i):
        print("*", end="")
    print()
```

### **11. Number Pyramid with Dashes**
```
----1
---12
--123
-1234
12345
```
**Solution:**
```python
for k in range(1, 6):
    for m in range(5 - k):
        print("-", end="")
    for n in range(1, k + 1):
        print(n, end="")
    print()
```

### **12. Reverse Number Pyramid**
```
----1
---21
--321
-4321
54321
```
**Solution:**
```python
for k in range(1, 6):
    for m in range(5 - k):
        print("-", end="")
    for n in range(k, 0, -1):
        print(n, end="")
    print()
```

---

## 🕳️ Hollow Patterns

### **13. Hollow Square Pattern**
```
*****
*   *
*   *
*   *
*****
```
**Solution:**
```python
rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

### **14. Hollow Rectangle Pattern**
```
****
*  *
*  *
****
```
**Solution:**
```python
for i in range(1, 5):
    for j in range(1, 5):
        if 2 <= i <= 3 and 2 <= j <= 3:
            print(" ", end="")
        else:
            print("*", end="")
    print()
```

### **15. Hollow Diamond Pattern**
```
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
```
**Solution:**
```python
# Upper Part
for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    for k in range(i):
        print(" ", end="")
    for m in range(i):
        print(" ", end="")
    for n in range(5 - i):
        print("*", end="")
    print("")

# Lower Part
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    for k in range(5 - i):
        print(" ", end="")
    for m in range(5 - i):
        print(" ", end="")
    for n in range(i):
        print("*", end="")
    print("")
```

---

## 🔥 Advanced Patterns

### **16. Butterfly Pattern**
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```
**Solution:**
```python
# Upper Part
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    for k in range(5 - i):
        print(" ", end="")
    for m in range(5 - i):
        print(" ", end="")
    for n in range(i):
        print("*", end="")
    print()

# Lower Part
for i in range(4):
    for j in range(4 - i):
        print("*", end="")
    for k in range(i + 1):
        print(" ", end="")
    for m in range(i + 1):
        print(" ", end="")
    for n in range(4 - i):
        print("*", end="")
    print()
```

### **17. Number Pattern with Dashes**
```
1------1
12----21
123--321
12344321
```
**Solution:**
```python
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print("-" * (4 * 2 - i * 2), end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
```

### **18. Complex Number Pattern**
```
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
```
**Solution:**
```python
for i in range(1, 8):
    for j in range(1, 8):
        if (i == 2 and 2 <= j <= 6) or (i == 6 and 2 <= j <= 6) or (3 <= i <= 5 and j == 2) or (3 <= i <= 5 and j == 6):
            print("3 ", end="")
        elif (j == 3 and 3 <= i <= 5) or (j == 5 and 3 <= i <= 5) or (i == 3 and 3 <= j <= 5) or (i == 5 and 3 <= j <= 5):
            print("2 ", end="")
        elif i == 4 and j == 4:
            print("1 ", end="")
        else:
            print("4 ", end="")
    print()
```

### **19. Inverted Triangle Pattern**
```
*****
****
***
**
*
```
**Solution:**
```python
for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    print()
```

### **20. Combined Triangle Pattern**
```
*
**
***
****
*****
****
***
**
*
```
**Solution:**
```python
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
    
for i in range(5):
    for j in range(4 - i):
        print("*", end="")
    print()
```

---

## ❗ Common Mistakes Students Make

### **1. Forgetting `end=""`**
This prints each symbol on a new line.

### **2. Using wrong indentation**
Python is indentation-sensitive — wrong spaces break your program.

### **3. Misunderstanding ranges**
Examples:
* `range(5)` → 0 to 4
* `range(1,5)` → 1 to 4
* `range(5,0,-1)` → 5 to 1

### **4. Incorrect loop boundaries**
Always test edge cases for your loops.

---

## 📝 Practice Exercises

Try to code these yourself:

1. **Hollow pyramid**
2. **Pascal's triangle**
3. **Hourglass pattern**
4. **Floyd's triangle**
5. **Spiral pattern**
6. **Zigzag pattern**
7. **Heart pattern**
8. **Arrow patterns**

---

## 🎯 Tips for Success

1. **Start simple**: Begin with basic patterns before moving to complex ones
2. **Understand the logic**: Don't just copy code - understand the pattern structure
3. **Use variables**: Make your code flexible by using variables for rows/columns
4. **Debug step by step**: Print intermediate values to understand what's happening
5. **Practice regularly**: Pattern printing improves with consistent practice

---

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [GeeksforGeeks Pattern Programs](https://www.geeksforgeeks.org/python-pattern-printing/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

**Happy Coding! 🚀**
