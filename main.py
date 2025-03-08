"""
Reminders and resources for future me:

PEP8 naming conventions: https://peps.python.org/pep-0008/
snake_case for functions, PascalCase for methods.

Structure of project:
why add __init__.py to folders? with the init file, python recognizes the folder
    as a package from which I can import modules from cleanly and without issues.

Type hints:
Helps communicate expected types of values.
Typing library docs: https://docs.python.org/3/library/typing.html
Cheat sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

Python's enumerate function:
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

Testing:
Testing done via pytest. Pytest looks for files named test_*.py or *_test.py.
It looks for functions that start with test_.
It runs the test functions and checks if assertions (assert) pass or fail.
Helps run all tests at once.
Running tests in terminal via "pytest".
"""

if __name__ == '__main__':
    pass
