# Tricky Situations with Python Data Types

Python's data types are versatile and easy to use, but understanding their behavior—especially in tricky cases—can help avoid bugs and confusion. Always be cautious with floating-point precision, mutability in collections, and boolean context evaluations.

### Boolean Contexts

In Python, non-zero numbers and non-empty sequences are treated as True, while zero and empty sequences are treated as False.

```python
x = []
if x:
print("True")
else:
print("False") # Output: False
```

```python
x = 0
if x:
print("True")
else:
print("False") # Output: False
```

### Mutability in Lists and Tuples

Lists are mutable, but tuples are immutable. If you modify a list inside a tuple, the tuple will reflect the changes.

```python
x = ([1, 2, 3],)
x[0][0] = 100
print(x) # Output: ([100, 2, 3],)
```

### Nested Lists and Identity

When you assign a list to another variable, the identity of the list remains the same (they point to the same object in memory).

```python
x = [1, 2, 3]
y = x
y[0] = 100
print(x) # Output: [100, 2, 3]
```

### String Concatenation and Multiplication

Multiplying a string by an integer repeats it, and concatenating strings combines them.

```python
x = "hello" \* 3
print(x) # Output: hellohellohello

y = "hello" + " world"
print(y) # Output: hello world
```

### Floating Point Precision

Floating-point numbers have precision issues in Python (and most programming languages).

```python
x = 0.1 + 0.2
print(x) # Output: 0.30000000000000004
```

### Comparison of Floating Points

Due to floating-point precision issues, two floating-point numbers that appear equal might not be exactly the same.

```python
x = 0.1 + 0.2
y = 0.3
print(x == y) # Output: False
```
