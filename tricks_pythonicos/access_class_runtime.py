# You can get the name of
# an object's class as a
# string:

class MyClass:
    pass

obj = MyClass()
obj.__class__.__name__
# output: 'MyClass'

# Functions have a
# similar feature:

def myfunc(): 
    pass

myfunc.__name__
# output: 'myfunc'
