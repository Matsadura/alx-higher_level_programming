# 0x04-Python - More Data Structures: Set, Dictionary

1. **What are sets and how to use them:**
   Sets in Python are unordered collections of unique elements. They are created using curly braces `{}` or the `set()` constructor. Sets do not allow duplicate elements and are useful for operations like membership testing, union, intersection, etc.

2. **Most common methods of set and how to use them:**
   Common set methods include `add()`, `remove()`, `discard()`, `pop()`, `clear()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`, and `update()`. These methods allow you to modify and perform set operations efficiently.

3. **When to use sets versus lists:**
   Sets are used when you need to work with unique elements and perform set operations like union, intersection, etc. Lists are used when you need ordered collections with possible duplicate elements.

4. **How to iterate into a set:**
   You can iterate through a set using a for loop or use set comprehensions to perform operations on each element of the set.

5. **What are dictionaries and how to use them:**
   Dictionaries in Python are unordered collections of key-value pairs. They are created using curly braces `{}` with key-value pairs separated by colons `:`. Dictionaries are mutable and allow efficient lookup and manipulation of data.

6. **When to use dictionaries versus lists or sets:**
   Dictionaries are used when you need to store data with unique keys and fast access to values based on keys. Lists are used for ordered collections, and sets are used for unique elements without specific key-value pairs.

7. **What is a key in a dictionary:**
   A key in a dictionary is a unique identifier used to access the associated value. Keys can be of any immutable data type such as strings, numbers, or tuples.

8. **How to iterate over a dictionary:**
   You can iterate over a dictionary using a for loop, which iterates over keys by default. To iterate over both keys and values, you can use the `items()` method.

9. **What is a lambda function:**
   A lambda function, also known as an anonymous function, is a small, inline function defined without a name using the `lambda` keyword. Lambda functions are often used for short, one-time operations.

10. **What are the map, reduce, and filter functions:**
    - `map()` function applies a function to each item in an iterable and returns an iterator of the results.
    - `reduce()` function is used to apply a function cumulatively to the items of an iterable, reducing it to a single value.
    - `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

---

| File      | Description |
| ----------- | ----------- |
| [0-square_matrix_simple.py](./0-square_matrix_simple.py) | A function that computes the square value of all integers of a matrix. |
| [1-search_replace.py](./1-search_replace.py) | Replaces all occurrences of an element by another in a new list. |
| [2-uniq_add.py](./2-uniq_add.py) |  Adds all unique integers in a list (only once for each integer). |
| [3-common_elements.py](./3-common_elements.py) | Returns a set of common elements in two sets. |
| [4-only_diff_elements.py](./4-only_diff_elements.py) | Returns a set of all elements present in only one set. |
| [5-number_keys.py](./5-number_keys.py) | Returns the number of keys in a dictionary. |
| [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py) | Prints a dictionary by ordered keys. |
| [7-update_dictionary.py](./7-update_dictionary.py) |  Replaces or adds key/value in a dictionary. |
| [8-simple_delete.py](./8-simple_delete.py) |  Deletes a key in a dictionary. |
| [9-multiply_by_2.py](./9-multiply_by_2.py) | Returns a new dictionary with all values multiplied by 2 |
| [10-best_score.py](./10-best_score.py) | Returns a key with the biggest integer value. |
| [11-multiply_list_map.py](./11-multiply_list_map.py) | Returns a list with all values multiplied by a number without using any loops. |
| [12-roman_to_int.py](./12-roman_to_int.py) | A function ``def roman_to_int(roman_string):`` that converts a Roman numeral to an integer. |
| [100-weight_average.py](./100-weight_average.py) | returns the weighted average of all integers tuple ``(<score>, <weight>)`` |
| [101-square_matrix_map.py](./101-square_matrix_map.py) |  Computes the square value of all integers of a matrix using ``map`` |
| [102-complex_delete.py](./102-complex_delete.py) | Deletes keys with a specific value in a dictionary. |
| [103-python.c](./103-python.c) |  C functions that print some basic info about Python lists and Python bytes objects. |
