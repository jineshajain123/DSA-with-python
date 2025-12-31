'''
OOPS: Object-Oriented Programming in Python

class: A blueprint for creating objects (a particular data structure), defining initial state (attributes) and behaviors (methods).
object: An instance of a class, containing data and methods that operate on that data.  
method: A function defined inside a class that operates on instances of that class.


class myclass:
    def __init__(self): # Initailization method to initialize attributes
        pass
    id = 10
    name = "Python"

object1 = myclass()   # object creation
print("ID:", object1.id)
print("Name:", object1.name)


inheritance: A mechanism where a new class can inherit attributes and methods from an existing class.
'''
#multilevel inheritance

class GrandChild:
    name = "GrandChild Class"

class teacher(GrandChild):
    name = "teacher Class"

class stud(teacher): 
    name = "stud Class"
    print("stud Class inherits from teacher Class")

object= Child()
print("Name:", object.name) 
