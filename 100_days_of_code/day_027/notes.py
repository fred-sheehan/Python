# python advanced arguments
# creating a function with 3 default parameters if none are passed
def my_function(a=1, b=2, c=3):
    print(a, b, c)
my_function() # prints 1 2 3 the defaults
my_function(10, 20, 30) # prints 10 20 30 the given values
my_function(10) # prints 10 2 3 the given values and default for b and c
my_function(b=15) # prints 1 15 3 the default for a and c

# unlimited functions
# *args and **kwargs
def add(*values): # often written as *args can be anything
    return sum(values)
print(add(1, 2, 3, 4, 5)) # prints 15
print(add(5, 6, 3, 93, 2)) # prints 109

# key word arguments (kwargs)
def calculate(**kwargs): # often written as **kwargs can be anything
    print(kwargs)
calculate(add=3, multiply=5, divide=10) # prints {'add': 3, 'multiply': 5, 'divide': 10}

# using kwargs in a class with the get method (to avoid errors if the key doesn't exist in the dictionary)
class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.year = kw.get('year')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

my_car = Car(make='Toyota', year=2019, color='red')
print(my_car.make) # prints Toyota
print(my_car.model) # prints None rather than an error
