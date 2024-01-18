"""


Part 3: Student dataclass

Type in the dataclass code from the slides/video. You would have done this before class.

Add one more field: gpa, a float.

Write a main function to create some example Student objects with some example names, college_id and GPA values. 

Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, 
the GPA is included. 

Add some comments in your code to compare the dataclass version to the "traditional" version.
"""
from dataclasses import dataclass

@dataclass
class Student:  # A quick way to define a class. Uniquely, in this the datatype is defined for each portion of this. 
    # There is no __init__ or __str__ methods needed to be defined here.  I think dataclass would be most useful for 
    # data structures that are not really getting piped back to the user.  Just a quick way to keep tat together.
    name: str
    college_id: int
    gpa: float

def main():
    alice = Student('Alice', 12345, 3.5)
    bob = Student('Bob', 98765, 3.5)

    print(alice)
    print(bob)

main()



## PART II:
# Prevent there being two books with the same name