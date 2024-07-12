def myFunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

    print(kwargs['key'])

myFunction(1,True, 14,'wow', key = 7)

def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, a=4, b=5)