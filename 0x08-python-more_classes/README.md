# 0x08-Python - More Classes and Objects

1. **What is OOP:**
   Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities. It emphasizes concepts like encapsulation, inheritance, and polymorphism.

2. **“first-class everything”:**
   In Python, everything is treated as an object, including integers, functions, classes, etc. This means objects can be assigned to variables, passed as arguments, and returned from functions.

3. **What is a class:**
   A class in Python is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that objects of that class will have.

4. **What is an object and an instance:**
   An object is an instance of a class. When a class is instantiated, it creates an object with its own unique identity, state, and behavior.

5. **Difference between a class and an object or instance:**
   A class is a template or blueprint, while an object is a specific instance of that class with its own unique attributes and behaviors.

6. **What is an attribute:**
   An attribute is a piece of data associated with an object or class. Attributes can be variables (instance variables or class variables) that hold data.

7. **How to use public, protected, and private attributes:**
   In Python, attributes are public by default. Protected attributes are prefixed with a single underscore (`_attribute`), indicating that they should not be accessed directly. Private attributes are prefixed with double underscores (`__attribute`), providing name mangling to prevent accidental modification.

8. **What is self:**
   `self` is a reference to the current instance of a class. It is used within class methods to access instance variables and methods.

9. **What is a method:**
   A method is a function defined inside a class that operates on instances of that class. It can access and modify instance attributes.

10. **What is the special __init__ method and how to use it:**
    `__init__` is a special method (constructor) in Python classes that is automatically called when a new instance of the class is created. It initializes instance variables and sets up the object's initial state.

11. **Data Abstraction, Data Encapsulation, and Information Hiding:**
    - **Data Abstraction:** Hides complex implementation details and exposes only relevant features to the user.
    - **Data Encapsulation:** Bundles data (attributes) and methods (functions) that operate on the data within a class.
    - **Information Hiding:** Restricts direct access to certain attributes or methods to prevent unintended modifications.

12. **What is a property:**
    A property in Python allows you to define custom getter, setter, and deleter methods for accessing and modifying attributes. It provides control over attribute access and validation.

13. **Difference between an attribute and a property in Python:**
    An attribute is a data item associated with an object, while a property is a special attribute that provides getter, setter, and deleter methods for managing attribute access.

14. **Pythonic way to write getters and setters:**
    The Pythonic way to write getters and setters is to use properties. You can define a property with `@property` for the getter, `@attribute.setter` for the setter, and `@attribute.deleter` for the deleter method.

15. **What are the special __str__ and __repr__ methods and how to use them:**
    - `__str__`: Returns a human-readable string representation of an object. It is used by `print()` and `str()` functions.
    - `__repr__`: Returns an unambiguous string representation of an object. It is used by the `repr()` function and for debugging purposes.

16. **Difference between __str__ and __repr__:**
    `__str__` is meant for human consumption and readability, while `__repr__` is more for debugging and creating an unambiguous representation.

17. **What is a class attribute:**
    A class attribute is an attribute that is shared among all instances of a class. It is defined directly within the class but outside of any method.

18. **Difference between an object attribute and a class attribute:**
    An object attribute is specific to each instance of a class, while a class attribute is shared among all instances of the class.

19. **What is a class method:**
    A class method is a method that operates on the class itself rather than instances of the class. It is defined using the `@classmethod` decorator and takes the class (`cls`) as its first parameter.

20. **What is a static method:**
    A static method is a method that does not operate on instances or classes. It is defined using the `@staticmethod` decorator and does not take `self` or `cls` parameters.

21. **How to dynamically create arbitrary new attributes for existing instances of a class:**
    You can dynamically create new attributes for existing instances by simply assigning values to new attribute names.

22. **How to bind attributes to objects and classes:**
    Attributes can be bound to objects by assigning values to instance variables. Class attributes are defined directly within the class and are shared among all instances of the class.

23. **What is and what does contain __dict__ of a class and of an instance of a class:**
    `__dict__` is a dictionary that contains the namespace of a class or instance. It stores the attributes and methods associated with the object.

24. **How Python finds the attributes of an object or class:**
    Python uses attribute lookup to find attributes of an object or class. It searches in the object's namespace (`__dict__`), then in the class hierarchy (inheritance chain) if the attribute is not found.

25. **How to use the getattr function:**
    The `getattr()` function in Python is used to get the value of an attribute from an object. It takes the object and the attribute name as arguments and returns the attribute's value.
---

| File      | Description |
| ----------- | ----------- |
| [0-rectangle.py](./0-rectangle.py) | An empty class Rectangle that defines a rectangle |
| [1-rectangle.py](./1-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``0-rectangle.py``) |
| [2-rectangle.py](./2-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``1-rectangle.py``) |
| [3-rectangle.py](./3-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``2-rectangle.py``) |
| [4-rectangle.py](./4-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``3-rectangle.py``) |
| [5-rectangle.py](./5-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``4-rectangle.py``) |
| [6-rectangle.py](./6-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``5-rectangle.py``) |
| [7-rectangle.py](./7-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``6-rectangle.py``) |
| [8-rectangle.py](./8-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``7-rectangle.py``) |
| [9-rectangle.py](./9-rectangle.py) | A class ``Rectangle`` that defines a rectangle by: (based on ``8-rectangle.py``) |
| [101-nqueens.py](./101-nqueens.py) | Solves the N queens problem. |
