# 0x0F. Python - Object-Relational Mapping (ORM)

1. **How to connect to a MySQL database from a Python script:**
   Use the `mysql-connector-python` library to connect to a MySQL database from Python:
   ```python
   import mysql.connector

   # Establish connection
   connection = mysql.connector.connect(
       host='localhost',
       user='username',
       password='password',
       database='database_name'
   )
   ```

2. **How to SELECT rows in a MySQL table from a Python script:**
   Execute SELECT queries using the connection cursor:
   ```python
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM table_name')
   rows = cursor.fetchall()
   ```

3. **How to INSERT rows in a MySQL table from a Python script:**
   Execute INSERT queries using the connection cursor:
   ```python
   cursor = connection.cursor()
   cursor.execute('INSERT INTO table_name (column1, column2) VALUES (%s, %s)', (value1, value2))
   connection.commit()
   ```

4. **What ORM means:**
   ORM (Object-Relational Mapping) is a programming technique that converts data between incompatible type systems, such as a relational database and an object-oriented programming language.

5. **How to map a Python Class to a MySQL table:**
   Use ORM libraries like SQLAlchemy or Django ORM to map Python classes to MySQL tables. For example, using SQLAlchemy:
   ```python
   from sqlalchemy import Column, Integer, String, create_engine
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String(50))

   engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name')
   Base.metadata.create_all(engine)
   ```

6. **How to create a Python Virtual Environment:**
   Use the `venv` module to create a Python virtual environment:
   ```
   python -m venv myenv
   ```

7. **Activate the virtual environment:**
   On Windows:
   ```
   myenv\Scripts\activate
   ```
   On Unix/Linux:
   ```
   source myenv/bin/activate
   ```

---

| File      | Description |
| ----------- | ----------- |
| [0-select_states.py](./0-select_states.py) | Lists all ``states`` from the database ``hbtn_0e_0_usa`` |
| [1-filter_states.py](./1-filter_states.py) | Lists all ``states`` with a ``name`` starting with ``N`` (upper N) from the database ``hbtn_0e_0_usa`` |
| [2-my_filter_states.py](./2-my_filter_states.py) | Takes in an argument and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument. |
| [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | A script that takes in arguments and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where name matches the argument. But this time, It is safe from MySQL injections |
| [4-cities_by_state.py](./4-cities_by_state.py) | Lists all ``cities`` from the database ``hbtn_0e_4_usa`` |
| [5-filter_cities.py](./5-filter_cities.py) | A script that takes in the name of a state as an argument and lists all ``cities`` of that state, using the database ``hbtn_0e_4_usa`` |
| [model_state.py](./model_state.py) | A python file that contains the class definition of a ``State`` and an instance ``Base = declarative_base()`` |
| [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Lists all ``State`` objects from the database ``hbtn_0e_6_usa`` |
| [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Prints the first ``State`` object from the database ``hbtn_0e_6_usa`` |
| [9-model_state_filter_a.py](./9-model_state_filter_a.py) | Lists all ``State`` objects that contain the letter ``a`` from the database ``hbtn_0e_6_usa`` |
| [10-model_state_my_get.py](./10-model_state_my_get.py) | Prints the ``State`` object with the ``name`` passed as argument from the database ``hbtn_0e_6_usa`` |
| [11-model_state_insert.py](./11-model_state_insert.py) |  Adds the ``State`` object “Louisiana” to the database ``hbtn_0e_6_usa`` |
| [12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Changes the name of a ``State`` object from the database ``hbtn_0e_6_usa`` |
| [13-model_state_delete_a.py](./13-model_state_delete_a.py) | Deletes all ``State`` objects with a name containing the letter ``a`` from the database ``hbtn_0e_6_usa`` |
| [model_city.py](./model_city.py) | model_city.py |
| [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | 14-model_city_fetch_by_state.py |
