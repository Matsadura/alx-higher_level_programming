# 0x0B-Python - Input/Output (I/O)

1. **How to open a file:**
   Use the `open()` function with the appropriate mode ('r' for read, 'w' for write, 'a' for append, 'r+' for read/write) to open a file. For example:
   ```python
   file = open('filename.txt', 'r')
   ```

2. **How to write text in a file:**
   Use the file object's `write()` method to write text to a file. For example:
   ```python
   file.write('Hello, World!')
   ```

3. **How to read the full content of a file:**
   Use the file object's `read()` method to read the full content of a file. For example:
   ```python
   content = file.read()
   ```

4. **How to read a file line by line:**
   Use a for loop to iterate over each line in the file. For example:
   ```python
   for line in file:
       print(line)
   ```

5. **How to move the cursor in a file:**
   Use the file object's `seek()` method to move the cursor to a specific position in the file. For example:
   ```python
   file.seek(0)  # Move cursor to the beginning of the file
   ```

6. **How to make sure a file is closed after using it:**
   Use the `close()` method on the file object to ensure the file is properly closed after use. For example:
   ```python
   file.close()
   ```

7. **What is and how to use the with statement:**
   The `with` statement is used for resource management and ensures that resources are properly released after use, even if an exception occurs. It automatically closes files when the block is exited. For example:
   ```python
   with open('filename.txt', 'r') as file:
       content = file.read()
   ```

8. **What is JSON:**
   JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

9. **What is serialization:**
   Serialization is the process of converting a Python data structure (object, list, dictionary, etc.) into a JSON string representation.

10. **What is deserialization:**
    Deserialization is the process of converting a JSON string back into a Python data structure.

11. **How to convert a Python data structure to a JSON string:**
    Use the `json.dumps()` function to serialize a Python data structure to a JSON string. For example:
    ```python
    import json

    data = {'name': 'John', 'age': 30}
    json_string = json.dumps(data)
    ```

12. **How to convert a JSON string to a Python data structure:**
    Use the `json.loads()` function to deserialize a JSON string into a Python data structure. For example:
    ```python
    import json

    json_string = '{"name": "John", "age": 30}'
    data = json.loads(json_string)
    ```

---

| File      | Description |
| ----------- | ----------- |
| [0-read_file.py](./0-read_file.py) | Reads a text file (``UTF8``) and prints it to stdout |
| [1-write_file.py](./1-write_file.py) | Writes a string to a text file (``UTF8``) and returns the number of characters written |
| [2-append_write.py](./2-append_write.py) | Appends a string at the end of a text file (``UTF8``) and returns the number of characters added |
| [3-to_json_string.py](./3-to_json_string.py) | Returns the JSON representation of an object (string) |
| [4-from_json_string.py](./4-from_json_string.py) | Returns an object (Python data structure) represented by a JSON string |
| [5-save_to_json_file.py](./5-save_to_json_file.py) | Writes an Object to a text file, using a JSON representation |
| [6-load_from_json_file.py](./6-load_from_json_file.py) | Creates an Object from a “JSON file” |
| [7-add_item.py](./7-add_item.py) |  Adds all arguments to a Python list, and then save them to a file |
| [8-class_to_json.py](./8-class_to_json.py) | Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object |
| [9-student.py](./9-student.py) | A class ``Student`` that defines a student |
| [10-student.py](./10-student.py) |  A class ``Student`` that defines a student by: (based on ``9-student.py``) |
| [11-student.py](./11-student.py) |  A class ``Student`` that defines a student by: (based on ``10-student.py``) |
| [12-pascal_triangle.py](./12-pascal_triangle.py) | Returns a list of lists of integers representing the Pascal’s triangle of ``n`` |
| [100-append_after.py](./100-append_after.py) | Inserts a line of text to a file, after each line containing a specific string |
| [101-stats.py](./101-stats.py) | Reads ``stdin`` line by line and computes metrics |
