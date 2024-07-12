def abc(fun):
    def wrapper(*args, **kwargs):
        print('i am wrapper')
        return fun(*args, **kwargs)
    return wrapper
@abc
def sum(a):
    print(f'Here is sum function with argument: {a}')
a=1
sum(a)