import time

time_dict = {}

# Create add_timer decorator to add timing functionality to functions
def add_timer(func):

    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        global time_dict
        time_dict.setdefault(func.__name__, []).append(end-start)

    return inner


# Create a few no-op functions
def a():
    pass
def b():
    pass
def c():
    pass
def x():
    pass
def y():
    pass
def z():
    pass

# Create function call factory
func_dict = {
    'a': a,
    'b': b,
    'c': c,
    'x': x,
    'y': y,
    'z': z,
}

# Light wrapper function for calling into the factory.  Function exists solely for the decorator.
@add_timer
def dict_func(func_name):
    func_dict[func_name]()

# Create if elif chain function.
@add_timer
def switch_func(func_name):
    if func_name == 'x':
        x()
    elif func_name == 'y':
        y()
    elif func_name == 'z':
        z()
    elif func_name == 'a':
        a()
    elif func_name == 'b':
        b()
    elif func_name == 'c':
        c()


# Loop over all cases 1000 times to try and get a good average.
for loop in range(1000):
    for func in ['x','y','z','a','b','c']:
        switch_func(func)
        dict_func(func)

# Print out averages
for func_name, time_list in time_dict.items():
    print(f"{func_name} had an average run of {sum(time_list)/len(time_list):.08f}.")
