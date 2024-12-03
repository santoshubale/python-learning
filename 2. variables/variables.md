# Python Variables

Variables in Python are used to store data values. They are created when you assign a value to them.

## Declaring Variables

In Python, you can assign a value to a variable directly without declaring its type explicitly.

```python
# Example of variable assignment
x = 5           # Integer
name = "Mahesh" # String
pi = 3.14       # Float
is_happy = True # Boolean
```

# Variable Naming Rules in Python

- Must start with a letter or an underscore (`_`).
- Cannot start with a number.
- Can only contain letters, numbers, and underscores.
- Case-sensitive (`Name` and `name` are different).
- Cannot be a Python keyword.

## Best Practices for Naming Variables

```python
# Use snake_case for variable names
age = 25
first_name = "Mahesh"
total_price = 100.50

user_age = 30
is_valid = True

# By convention, constants are written in UPPERCASE:
MAX_USERS = 100

# Underscore (_) is used for special purposes, like ignoring values
for _ in range(5):
    print("Hello")
```

## Dynamic Typing

Python variables are dynamically typed, meaning you can change their type during runtime.

```python
x = 10        # Integer
x = "Hello"   # Now a String
```
