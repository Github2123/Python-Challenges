def add(a,b):
    return a+b
print(add(10,20))
def add(*args):
    print(type(args))
    return sum(args)


print(add(1,2,3,4,5))



def add(*kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}::{v}")




