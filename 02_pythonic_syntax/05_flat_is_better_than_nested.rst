Flat is better than nested
---------------------------

**Too much nesting**

.. code:: python 

def print_matrices():
    for matrix in matrices:
        print('Matrix:')
        for row in matrix:
            for col in row:
                print(col, end='')
            print()
        print()

**Less nesting than last example**

.. code:: python 

    def print_row(row):
        for col in row:
            print(col, end='')

    def print_matrix(matrix):
        for row in matrix:
            print_row(row)
            print()

    def print_matrices(matrices):
        for matrix in matrices:
            print('Matrix:')
            print_matrix(matrix)
            print()
