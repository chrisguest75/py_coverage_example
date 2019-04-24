# README.md
A simple binary search tree with a pytest class configured to run in VSCode.
Also a simple demonstration of using coverage module. 

# TODO:
* pydoc

# Running
Use 'pipenv install --dev' to install the required modules

NOTE: Before you do this you may wish to export 'export PIPENV_VENV_IN_PROJECT=1' to have the .venv in local folder.

Now load 'code .'

And run the tests through the test execution extension. 

# Assessing coverage
In the terminal run 'pytest --cov=.' this will tell you the coverage for the module

You also have the ability to write out reports 'pytest --cov=. --cov-report html:coverage'

You can now open the coverage file. 
```
open ./coverage/binary_search_tree_py.html
```