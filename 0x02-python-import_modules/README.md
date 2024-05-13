# 0x02-Python - Import & Modules

1. **Why Python programming is awesome:**
   Python's strength lies in its simplicity, readability, extensive standard library, and vibrant community. It excels in various domains such as web development, data analysis, machine learning, automation, and more.

2. **How to import functions from another file:**
   To import functions from another Python file/module, you can use the `import` statement followed by the module name or specific function names using the `from` keyword.

3. **How to use imported functions:**
   After importing functions, you can use them directly by calling their names prefixed with the module name (if imported using `import module`) or without the module name (if imported using `from module import function`).

4. **How to create a module:**
   A module in Python is a file containing Python definitions and statements. To create a module, you simply write your code in a `.py` file and save it with a meaningful name.

5. **How to use the built-in function dir():**
   The `dir()` function in Python is used to list the names of variables, functions, classes, and modules in the current scope or a specified object. It's useful for exploring available attributes and methods.

6. **How to prevent code in your script from being executed when imported:**
   To prevent specific code from running when a script is imported, you can use the `if __name__ == "__main__":` block. Code within this block only executes when the script is run directly, not when imported as a module.

7. **How to use command-line arguments with your Python programs:**
   Python programs can accept command-line arguments using the `sys.argv` list (from the `sys` module) or using the more powerful `argparse` module. Command-line arguments allow users to pass inputs to scripts during execution.

---

| File      | Description |
| ----------- | ----------- |
| [0-add.py](./0-add.py) | A program that imports the function ``def add(a, b):`` from the file ``add_0.py`` and prints the result of the addition ``1 + 2 = 3`` |
| [1-calculation.py](./1-calculation.py) |  A program that imports functions from the file ``calculator_1.py``, does some Maths, and prints the result. |
| [2-args.py](./2-args.py) | A program that prints the number of and the list of its arguments. |
| [3-infinite_add.py](./3-infinite_add.py) |  A program that prints the result of the addition of all arguments |
| [4-hidden_discovery.py](./4-hidden_discovery.py) | A program that prints all the names defined by the compiled module ``hidden_4.pyc`` |
| [5-variable_load.py](./5-variable_load.py) | A program that imports the variable ``a`` from the file ``variable_load_5.py`` and prints its value. |
| [100-my_calculator.py](./100-my_calculator.py) | Imports all functions from the file `calculator_1.py` and handles basic operations. |
| [101-easy_print.py](./101-easy_print.py) | Prints ``#pythoniscool``, followed by a new line, in the standard output. |
| [102-magic_calculation.py](./102-magic_calculation.py) | 102-magic_calculation.py |
| [103-fast_alphabet.py](./103-fast_alphabet.py) | Prints the alphabet in uppercase, followed by a new line. |
