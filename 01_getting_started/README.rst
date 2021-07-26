**Chapter 1, Getting started**
##############################################################################

One Environment per Project introduces virtual Python environments 
using virtualenv or venv to isolate the packages in your Python projects.

1. Using virtual environments with venv
---------------------------------------

Create the virtual env
.......................

python3 -m venv MY_ENV

Activate the virtual env
.........................

source my_test_MY_ENV/bin/activate

Install packages inside the virtual env
........................................

pip install MY_PACKAGE1
pip install MY_PACKAGE2

Deativate the virtual env
..........................

deactivate

2. Using C/C++ libraries
---------------------------------------

Option 1 - Install the development headers
.............................................

sudo apt-get install python3-dev

Option 2 - Install the development headers and a compiler
..........................................................

sudo apt-get build-dep python3