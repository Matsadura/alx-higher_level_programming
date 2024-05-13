# 0x07-Python - Test-driven Development (TDD)

1. **What’s an interactive test:**
   An interactive test in Python is a test that requires user interaction or input during execution. It can be used to test user interfaces, command-line interfaces, or interactive functionalities of a program.

2. **Why tests are important:**
   Tests are crucial in software development to ensure code correctness, maintainability, and reliability. They help identify bugs early, verify functionality, prevent regressions, and improve code quality.

3. **How to write Docstrings to create tests:**
   Docstrings in Python can be used to document functions, classes, and modules. By following a specific format (e.g., using `unittest` framework's `doctest` module), docstrings can also serve as tests by including executable code examples.

4. **How to write documentation for each module and function:**
   Writing documentation for modules and functions is important for code readability and maintainability. It typically involves using descriptive comments, docstrings, and following a consistent documentation style (e.g., reStructuredText or Markdown).

5. **What are the basic option flags to create tests:**
   In Python, you can create tests using various testing frameworks such as `unittest`, `pytest`, and `doctest`. Basic option flags for creating tests include:
   - `-v` or `--verbose`: Display detailed test output.
   - `-k EXPRESSION`: Run tests matching the given expression.
   - `-x` or `--exitfirst`: Stop testing after the first failure or error.
   - `-m MARKEXPR`: Run tests marked with the specified marker expression.

6. **How to find edge cases:**
   Edge cases are scenarios where the behavior of a program may differ from typical cases. To find edge cases, consider boundary conditions, extreme inputs, invalid inputs, empty inputs, and scenarios that might lead to unexpected behavior or errors.

---


| File      | Description |
| ----------- | ----------- |
| [0-add_integer.py](./0-add_integer.py) | A function that adds 2 integers. |
| [tests/0-add_integer.txt](./tests/0-add_integer.txt) | Doctests for the function ``def add_integer(a, b=98)``|
| [2-matrix_divided.py](./2-matrix_divided.py) |  A function that divides all elements of a matrix. |
| [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt) | Tests for the function ``def matrix_divided(matrix, div):`` |
| [3-say_my_name.py](./3-say_my_name.py) | Prints ``My name is <first name> <last name>`` |
| [tests/3-say_my_name.txt](./tests/3-say_my_name.txt) | Tests for the function ``def say_my_name(first_name, last_name=""):`` |
| [4-print_square.py](./4-print_square.py) | Prints a square with the character ``#``. |
| [tests/4-print_square.txt](./tests/4-print_square.txt) | Tests for the function ``def print_square(size):`` |
| [5-text_indentation.py](./5-text_indentation.py) | Prints a text with 2 new lines after each of these characters: ``.``, ``?`` and ``:`` |
| [tests/5-text_indentation.txt](./tests/5-text_indentation.txt) | Tests for the function ``def text_indentation(text):`` |
| [tests/6-max_integer_test.py](./tests/6-max_integer_test.py) | Unittests for the function ``def max_integer(list=[]):``. |
| [100-matrix_mul.py](./100-matrix_mul.py) | A function that multiplies 2 matrices |
| [tests/100-matrix_mul.txt](./tests/100-matrix_mul.txt) | Tests for the function ``def matrix_mul(m_a, m_b):`` |
| [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py) |  A function that multiplies 2 matrices by using the module ``NumPy`` |
| [tests/101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt) | Tests for the function ``def lazy_matrix_mul(m_a, m_b):`` |
| [102-python.c](./102-python.c) | A function that prints Python strings. |
