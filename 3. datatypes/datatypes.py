
def NumericTypes():
    print("------------------- NumericTypes")
    # Integer (int)
    # Represents whole numbers, both positive and negative.
    x = 10
    y = -5
    z = 0
    print(type(x)) #Output: <class 'int'>

    # Float (float)
    # Represents real numbers (i.e., numbers with a decimal point).
    x = 10.5
    y = -5.75
    print(type(x)) #Output: <class 'float'>

    # Complex (complex)
    # Represents complex numbers with real and imaginary parts.

    x = 3 + 4j
    print(type(x)) #Output: <class 'complex'>

def SequenceTypes():
    print("------------------- SequenceTypes")
    # String (str)
    # Represents text, enclosed in single or double quotes.
    x = "Hello, World!"
    print(type(x)) # Output: <class 'str'>

    # List (list)
    # Represents an ordered, mutable collection of items.
    x = [1, 2, 3, "hello", 3.14]
    print(type(x)) # Output: <class 'list'>

    # Tuple (tuple)
    # Represents an ordered, immutable collection of items.
    x = (1, 2, 3, "hello", 3.14)
    print(type(x)) # Output: <class 'tuple'>

    # Range (range)
    # Represents a sequence of numbers, used primarily in loops.
    x = range(1, 10, 2)
    print(type(x)) # Output: <class 'range'>

def MappingType():
    print("------------------- MappingType")
    # Dictionary (dict)
    # Represents an unordered collection of key-value pairs.
    x = {"name": "Alice", "age": 25}
    print(type(x)) # Output: <class 'dict'>

def SetTypes():
    print("------------------- SetTypes")
    # Set (set)
    # Represents an unordered collection of unique items.
    x = {1, 2, 3, 4, 5}
    print(type(x)) # Output: <class 'set'>

    # Frozenset (frozenset)
    # Represents an immutable set.
    x = frozenset([1, 2, 3, 4])
    print(type(x))  # Output: <class 'frozenset'>

def BooleanType():
    print("------------------- BooleanType")
    # Boolean (bool)
    # Represents a value of either True or False.
    x = True
    print(type(x))  # Output: <class 'bool'>

def BinaryTypes():
    print("------------------- BinaryTypes")
    # Bytes (bytes)
    # Represents a sequence of immutable byte values.
    x = b"Hello"
    print(type(x))  # Output: <class 'bytes'>

    # Bytearray (bytearray)
    # Represents a mutable sequence of byte values.
    x = bytearray([65, 66, 67])
    print(type(x))  # Output: <class 'bytearray'>

    # Memoryview (memoryview)
    # Represents a view object that exposes an array’s buffer interface.
    x = memoryview(b"Hello")
    print(type(x))  # Output: <class 'memoryview'>

# Entry Point
if __name__ == "__main__":
    NumericTypes()
    SequenceTypes()
    MappingType()
    SetTypes()
    BooleanType()
    BinaryTypes()