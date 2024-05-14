# 0x0A. Python - Inheritance

1. **What is a superclass, base class, or parent class:**
   A superclass, base class, or parent class is a class from which other classes (subclasses) inherit attributes and methods. It serves as a template for creating subclasses.

2. **What is a subclass:**
   A subclass is a class that inherits attributes and methods from a superclass or base class. It can extend and modify the behavior of the superclass while inheriting its functionalities.

3. **How to list all attributes and methods of a class or instance:**
   You can use the `dir()` function to list all attributes and methods of a class or instance. For example, `dir(ClassName)` or `dir(instance_name)`.

4. **When can an instance have new attributes:**
   Instances can have new attributes added dynamically during runtime. This can be done by assigning values to new attribute names directly to the instance.

5. **How to inherit a class from another:**
   Inheritance in Python is achieved by specifying the superclass(es) in parentheses after the subclass name. For example:
   ```python
   class Subclass(Superclass):
       # Subclass definitions
   ```

6. **How to define a class with multiple base classes:**
   Multiple inheritance is achieved by specifying multiple superclasses separated by commas in the class definition. For example:
   ```python
   class Subclass(BaseClass1, BaseClass2):
       # Subclass definitions
   ```

7. **What is the default class every class inherits from:**
   The default class every class inherits from in Python is the `object` class. It serves as the root class for all other classes and provides default behaviors and methods.

8. **How to override a method or attribute inherited from the base class:**
   Method or attribute overriding is done in subclasses by defining a method or attribute with the same name as the one in the superclass. This allows the subclass to provide its own implementation.

9. **Which attributes or methods are available by heritage to subclasses:**
   Subclasses inherit all attributes and methods (including public and protected ones) from the superclass unless explicitly overridden. Private attributes are not inherited.

10. **What is the purpose of inheritance:**
    The purpose of inheritance is to promote code reusability, reduce redundancy, and create a hierarchical relationship between classes. It allows subclasses to inherit and extend functionalities from superclasses.

11. **What are, when and how to use isinstance, issubclass, type, and super built-in functions:**
    - **isinstance(object, class):** Checks if an object is an instance of a specified class or its subclasses.
    - **issubclass(subclass, superclass):** Checks if a class is a subclass of another class.
    - **type(object):** Returns the type of an object (class).
    - **super():** Returns a proxy object that represents the superclass, allowing access to superclass methods and attributes.

---

| File      | Description |
| ----------- | ----------- |
| [0-lookup.py](./0-lookup.py) |  Returns the list of available attributes and methods of an object |
| [1-my_list.py](./1-my_list.py) | A class ``MyList`` that inherits from ``list`` |
| [tests/1-my_list.txt](./tests/1-my_list.txt) | Tests for the method ``def print_sorted(self):`` |
| [2-is_same_class.py](./2-is_same_class.py) | Returns ``True`` if the object is exactly an instance of the specified class ; otherwise ``False``. |
| [3-is_kind_of_class.py](./3-is_kind_of_class.py) | Returns ``True`` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise ``False``. |
| [4-inherits_from.py](./4-inherits_from.py) | Returns ``True`` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ``False``. |
| [5-base_geometry.py](./5-base_geometry.py) | An empty class ``BaseGeometry``. |
| [6-base_geometry.py](./6-base_geometry.py) | A class BaseGeometry (based on ``5-base_geometry.py``) |
| [7-base_geometry.py](./7-base_geometry.py) |  A class BaseGeometry (based on ``6-base_geometry.py``). |
| [tests/7-base_geometry.txt](./tests/7-base_geometry.txt) | Tests for the class |
| [8-rectangle.py](./8-rectangle.py) | A class ``Rectangle`` that inherits from ``BaseGeometry`` (``7-base_geometry.py``). |
| [9-rectangle.py](./9-rectangle.py) | A class ``Rectangle`` that inherits from BaseGeometry (``7-base_geometry.py``). |
| [10-square.py](./10-square.py) | A class ``Square`` that inherits from ``Rectangle`` (``9-rectangle.py``) |
| [11-square.py](./11-square.py) | A class ``Square`` that inherits from Rectangle (``9-rectangle.py``). (task based on ``10-square.py``). |
| [100-my_int.py](./100-my_int.py) | A class ``MyInt`` that inherits from ``int`` |
| [101-add_attribute.py](./101-add_attribute.py) | Adds a new attribute to an object if it’s possible |
