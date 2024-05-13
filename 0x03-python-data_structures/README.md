# 0x03-Python - Data Structures: Lists, Tuples


1. **Why Python programming is awesome:**
   Python's versatility, readability, extensive libraries, and strong community make it a popular choice for various applications such as web development, data analysis, machine learning, scripting, and more.

2. **What are lists and how to use them:**
   Lists in Python are ordered collections of items, which can be of different data types. They are mutable, meaning you can modify their elements after creation. Lists are created using square brackets `[]` and support indexing and slicing operations.

3. **Differences and similarities between strings and lists:**
   Strings and lists are both sequences in Python. The main difference is that strings are immutable (cannot be changed after creation), while lists are mutable. Both support indexing, slicing, and iteration.

4. **Most common methods of lists and how to use them:**
   Common list methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, `reverse()`, and more. These methods allow you to add, remove, search, and manipulate elements in lists.

5. **How to use lists as stacks and queues:**
   Lists can be used as stacks (Last In, First Out - LIFO) using `append()` and `pop()` methods or as queues (First In, First Out - FIFO) using `append()` and `pop(0)` methods.

6. **What are list comprehensions and how to use them:**
   List comprehensions provide a concise way to create lists based on existing lists or other iterables. They follow the syntax `[expression for item in iterable if condition]` and are efficient for filtering and transforming data.

7. **What are tuples and how to use them:**
   Tuples are ordered collections of items, similar to lists, but they are immutable (cannot be changed after creation). Tuples are created using parentheses `()` and support indexing, slicing, and iteration.

8. **When to use tuples versus lists:**
   Tuples are suitable for storing fixed collections of data that should not change, such as coordinates, constant configurations, or returning multiple values from functions. Lists are used when you need a mutable collection of items.

9. **What is a sequence:**
   A sequence in Python refers to an ordered collection of items where each item has a unique index. Lists, tuples, strings, and ranges are examples of sequences.

10. **What is tuple packing:**
    Tuple packing is the process of creating a tuple by grouping multiple values together inside parentheses. For example, `my_tuple = (1, 'hello', True)` packs three values into a tuple.

11. **What is sequence unpacking:**
    Sequence unpacking is the reverse of packing, where a tuple or another sequence is unpacked into individual variables. For example, `(x, y, z) = my_tuple` unpacks the values of `my_tuple` into `x`, `y`, and `z`.

12. **What is the del statement and how to use it:**
    The `del` statement in Python is used to delete variables, items in lists, or slices of lists. It can also be used to delete entire lists or tuples from memory.
---

| File      | Description |
| ----------- | ----------- |
| [0-print_list_integer.py](./0-print_list_integer.py) | Prints all integers of a list. |
| [1-element_at.py](./1-element_at.py) | Retrieves an element from a list like in C. |
| [2-replace_in_list.py](./2-replace_in_list.py) | Replaces an element of a list at a specific position (like in C). |
| [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py) | Prints all integers of a list, in reverse order. |
| [4-new_in_list.py](./4-new_in_list.py) | Replaces an element in a list at a specific position without modifying the original list (like in C). |
| [5-no_c.py](./5-no_c.py) | Removes all characters c and C from a string. |
| [6-print_matrix_integer.py](./6-print_matrix_integer.py) |  Prints a matrix of integers. |
| [7-add_tuple.py](./7-add_tuple.py) | Adds 2 tuples. |
| [8-multiple_returns.py](./8-multiple_returns.py) | Returns a tuple with the length of a string and its first character. |
| [9-max_integer.py](./9-max_integer.py) | Finds the biggest integer of a list. |
| [10-divisible_by_2.py](./10-divisible_by_2.py) | Finds all multiples of 2 in a list. |
| [11-delete_at.py](./11-delete_at.py) |  Deletes the item at a specific position in a list. |
| [12-switch.py](./12-switch.py) |  Switches value of ``a`` and ``b`` |
| [13-is_palindrome.c](./13-is_palindrome.c) | Checks if a singly linked list is a palindrome. |
| [lists.h](./lists.h) | Header file |
| [100-print_python_list_info.c](./100-print_python_list_info.c) | Prints some basic info about Python lists. |
