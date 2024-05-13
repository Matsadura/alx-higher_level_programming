# 0x06-Python - Classes and Objects

1. **What is OOP:**
   Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities. It focuses on encapsulation, inheritance, and polymorphism.

2. **“first-class everything”:**
   In Python, everything is treated as an object, including integers, functions, classes, etc. This means that objects can be assigned to variables, passed as arguments, and returned from functions.

3. **What is a class:**
   A class in Python is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that objects of that class will have.

4. **What is an object and an instance:**
   An object is an instance of a class. When a class is instantiated, it creates an object with its own unique identity, state, and behavior.

5. **Difference between a class and an object or instance:**
   A class is a template or blueprint, while an object is a specific instance of that class with its own unique attributes and behaviors.

6. **What is an attribute:**
   An attribute is a piece of data associated with an object or class. Attributes can be variables (instance variables or class variables) that hold data.

7. **How to use public, protected, and private attributes:**
   In Python, attributes are public by default. Protected attributes are prefixed with a single underscore (`_attribute`), indicating that they should not be accessed directly. Private attributes are prefixed with double underscore (`__attribute`), providing name mangling to prevent accidental modification.

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

15. **How to dynamically create arbitrary new attributes:**
    Python allows you to dynamically create new attributes for existing instances using dot notation or the `setattr()` function.

16. **How to bind attributes to objects and classes:**
    Attributes can be bound to objects by assigning values to instance variables. Class attributes are defined directly within the class and are shared among all instances of the class.

17. **What is the __dict__ of a class and/or instance:**
    `__dict__` is a dictionary that contains the namespace of a class or instance. It stores the attributes and methods associated with the object.

18. **How Python finds the attributes of an object or class:**
    Python uses attribute lookup to find attributes of an object or class. It searches in the object's namespace (`__dict__`), then in the class hierarchy (inheritance chain) if the attribute is not found.

19. **How to use the getattr function:**
    The `getattr()` function in Python is used to get the value of an attribute from an object. It takes the object and the attribute name as arguments and returns the attribute's value.

---

| File      | Description |
| ----------- | ----------- |
| [0-square.py](./0-square.py) | An empty class ``Square`` that defines a square: |
| [1-square.py](./1-square.py) | A class ``Square`` that defines a square by: (based on`` 0-square.py``) |
| [2-square.py](./2-square.py) | A class ``Square`` that defines a square by: (based on ``1-square.py``) |
| [3-square.py](./3-square.py) | A class ``Square`` that defines a square by: (based on ``2-square.py``) |
| [4-square.py](./4-square.py) | A class ``Square`` that defines a square by: (based on ``3-square.py``) |
| [5-square.py](./5-square.py) | A class ``Square`` that defines a square by: (based on ``4-square.py``) |
| [6-square.py](./6-square.py) | A class ``Square`` that defines a square by: (based on ``5-square.py``) |
| [100-singly_linked_list.py](./100-singly_linked_list.py) | A class ``Node`` that defines a node of a singly linked list |
| [101-square.py](./101-square.py) | A class ``Square`` that defines a square by: (based on ``6-square.py``) |
| [102-square.py](./102-square.py) | A class ``Square`` that defines a square by: (based on ``4-square.py``) |
| [103-magic_class.py](./103-magic_class.py) | A class ``MagicClass`` |
