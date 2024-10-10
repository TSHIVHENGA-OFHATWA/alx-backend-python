# 0x00. Python - Variable Annotations

## Description

This project focuses on Python variable annotations, covering the basics of type hints and annotations in Python.
You will learn how to write type-annotated functions that specify the types of input parameters
and return values, and understand how Python type hints work to ensure code clarity and reliability.

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes two floats `a` and `b` as arguments and returns their sum as a float.

**File:** `0-add.py`

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes two strings `str1` and `str2` as arguments and returns their concatenated string.

**File:** `1-concat.py`

### 2. Basic annotations - floor
Write a type-annotated function `floor` which takes a float `n` as an argument and returns the floor of the float.

**File:** `2-floor.py`

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` as an argument and returns the string representation of the float.

**File:** `3-to_str.py`

### 4. Define variables
Define and annotate the following variables:
- `a`, an integer with a value of `1`
- `pi`, a float with a value of `3.14`
- `i_understand_annotations`, a boolean with a value of `True`
- `school`, a string with a value of `"Holberton"`

**File:** `4-define_variables.py`

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` which takes a list `input_list` of floats as an argument and returns their sum as a float.

**File:** `5-sum_list.py`

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**File:** `6-sum_mixed_list.py`

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and an integer or float `v` as
arguments and returns a tuple. The first element is the string `k`, and the second element is the square of the integer/float `v`, annotated as a float.

**File:** `7-to_kv.py`

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by the `multiplier`.

**File:** `8-make_multiplier.py`

### 9. Let's duck type an iterable object
Annotate the function `element_length` with appropriate types:
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]

