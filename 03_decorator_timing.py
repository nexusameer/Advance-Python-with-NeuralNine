import time

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after= time.time()
        print(f'it takes {after-before} time to execute')

        return value
    return wrapper
@timed
def abc(x):
    for i in range(x):
        a = i*x  
    print(a)

abc(211410)