# 0x05-Python - Exceptions

1. **Difference between errors and exceptions:**
   Errors are generally compile-time issues or critical system failures that halt the program's execution, whereas exceptions are runtime errors that can be handled during program execution.

2. **What are exceptions and how to use them:**
   Exceptions in Python are unexpected events that disrupt the normal flow of the program. They are raised using the `raise` statement or triggered by built-in operations (e.g., division by zero). Exceptions can be caught and handled using try-except blocks.

3. **When to use exceptions:**
   Exceptions are used to handle exceptional conditions or unexpected errors that may occur during program execution, such as file not found, division by zero, or invalid input.

4. **How to correctly handle an exception:**
   Exceptions are handled using the try-except block. The code that might raise an exception is placed within the try block, and the except block catches and handles the exception if it occurs. Optionally, you can use `else` and `finally` blocks for additional handling.

5. **Purpose of catching exceptions:**
   Catching exceptions allows you to gracefully handle errors, prevent program crashes, provide meaningful error messages to users, and take appropriate actions based on the type of exception.

6. **How to raise a built-in exception:**
   You can raise built-in exceptions using the `raise` statement followed by the exception class or instance. For example, `raise ValueError("Invalid input")` raises a `ValueError` with a custom error message.

7. **When to implement a clean-up action after an exception:**
   Clean-up actions, such as closing files or releasing resources, are typically implemented in the `finally` block. This block is executed regardless of whether an exception occurs or not, ensuring that clean-up tasks are performed.

---

| File      | Description |
| ----------- | ----------- |
| [0-safe_print_list.py](./0-safe_print_list.py) |  Prints ``x`` elements of a list. |
| [1-safe_print_integer.py](./1-safe_print_integer.py) | Prints an integer with ``"{:d}".format()``. |
| [2-safe_print_list_integers.py](./2-safe_print_list_integers.py) | Prints the first ``x`` elements of a list and only integers. |
| [3-safe_print_division.py](./3-safe_print_division.py) | Divides 2 integers and prints the result |
| [4-list_division.py](./4-list_division.py) | Divides element by element 2 lists. |
| [5-raise_exception.py](./5-raise_exception.py) | Raises a type exception. |
| [6-raise_exception_msg.py](./6-raise_exception_msg.py) | Raises a name exception with a message. |
| [100-safe_print_integer_err.py](./100-safe_print_integer_err.py) | Prints an integer. |
| [101-safe_function.py](./101-safe_function.py) | Executes a function safely. |
| [102-magic_calculation.py](./102-magic_calculation.py) | 102-magic_calculation.py |
| [103-python.c](./103-python.c) | Three C functions that print some basic info about Python lists, Python bytes an Python float objects. |
