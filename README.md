# Pattern Printing in Python

This README provides a complete guide to understanding and creating different pattern-printing programs in Python. Perfect for beginners who want to strengthen their logic-building and looping concepts.

---

## 📌 What You Will Learn

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

## ⭐ 1. Square Star Pattern

### **Pattern:**

```
*****
*****
*****
*****
*****
```

### **Code:**

```python
rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

---

## ⭐ 2. Left Triangle Pattern

### **Pattern:**

```
*
**
***
****
*****
```

### **Code:**

```python
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()
```

---

## ⭐ 3. Right Triangle Pattern

### **Pattern:**

```
    *
   **
  ***
 ****
*****
```

### **Code:**

```python
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (i + 1))
```

---

## ⭐ 4. Pyramid Pattern

### **Pattern:**

```
    *
   ***
  *****
 *******
*********
```

### **Code:**

```python
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
```

---

## ⭐ 5. Inverted Pyramid

### **Pattern:**

```
*********
 *******
  *****
   ***
    *
```

### **Code:**

```python
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```

---

## ⭐ 6. Hollow Square Pattern

### **Pattern:**

```
*****
*   *
*   *
*   *
*****
```

### **Code:**

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

---

## 🔢 7. Number Triangle Pattern

### **Pattern:**

```
1
12
123
1234
12345
```

### **Code:**

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

---

## 🔠 8. Alphabet Triangle Pattern

### **Pattern:**

```
A
AB
ABC
ABCD
ABCDE
```

### **Code:**

```python
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()
```

---

## ❗ Common Errors Students Make

### **1. Forgetting `end=""`**

This prints each symbol on a new line.

### **2. Using wrong indentation**

Python is indentation-sensitive — wrong spaces break your program.

### **3. Misunderstanding ranges**

Examples:

* `range(5)` → 0 to 4
* `range(1,5)` → 1 to 4
* `range(5,0,-1)` → 5 to 1

---

## 📝 Practice Tasks

Try to code these yourself:

* Hollow pyramid
* Diamond pattern
* Number pyramid
* Pascal’s triangle
* Hourglass pattern

---

## 📚 More Coming Soon

* Advanced Python pattern questions
* ASCII art using loops
* Pattern printing interview problems
