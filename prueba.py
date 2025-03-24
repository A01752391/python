# To run: python3 prueba.py

import string
import math

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

test_directory = "tests/student_tests/"
filename = test_directory + 'hello_world.txt'
hello_world = load_file(filename)
print(hello_world)
