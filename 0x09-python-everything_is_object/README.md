# 0x09-Python - Everything is an Object

1. **What is an object:**
   In Python, everything is an object, including integers, strings, functions, classes, etc. An object is an instance of a class and has attributes and methods associated with it.

2. **Difference between a class and an object or instance:**
   A class is a blueprint for creating objects, while an object (or instance) is a specific instance of that class with its own unique identity, state, and behavior.

3. **Difference between immutable object and mutable object:**
   - **Immutable Object:** An immutable object cannot be modified after creation. Examples include integers, strings, tuples, and frozensets.
   - **Mutable Object:** A mutable object can be modified after creation. Examples include lists, dictionaries, sets, and user-defined classes.

4. **What is a reference:**
   A reference in Python is a pointer or address that points to the location of an object in memory.

5. **What is an assignment:**
   Assignment in Python involves binding a variable name to an object. It does not copy the object but creates a reference to it.

6. **What is an alias:**
   An alias is when multiple variable names refer to the same object in memory. Changes made through one alias affect the object and are reflected through other aliases.

7. **How to know if two variables are identical:**
   You can use the `is` keyword to check if two variables refer to the same object in memory. For example, `a is b` checks if `a` and `b` are identical.

8. **How to know if two variables are linked to the same object:**
   You can use the `id()` function to get the unique identifier (memory address) of an object. If the IDs of two variables are the same, they are linked to the same object.

9. **How to display the variable identifier (memory address):**
   You can display the memory address of an object using the `id()` function. For example, `print(id(variable_name))` displays the memory address of `variable_name`.

10. **What is mutable and immutable:**
    - **Mutable:** Objects that can be modified after creation are mutable.
    - **Immutable:** Objects that cannot be modified after creation are immutable.

11. **Built-in mutable types:**
    Python's built-in mutable types include lists, dictionaries, sets, and user-defined classes (if designed to be mutable).

12. **Built-in immutable types:**
    Python's built-in immutable types include integers, floats, strings, tuples, and frozensets.

13. **How does Python pass variables to functions:**
    Python passes variables to functions by reference. For mutable objects, changes made within a function affect the original object. For immutable objects, variables are passed by value (copy), and changes within the function do not affect the original object.
