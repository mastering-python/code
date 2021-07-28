Simple is better than complex
------------------------------

**Complex**

.. code:: python 

    import sqlite3


    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE data (key text, value text)')
    cursor.execute('''INSERT INTO data VALUES ('key', 'value')''')
    connection.commit()
    connection.close()

**Simpler than the last example**

.. code:: python 

    import pickle # Or json/yaml


    with open('data.pickle', 'wb') as fh:
        pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
