def add(a,b):
    result = a+b
    print("a=",a,"b=",b)
    return result


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

def print_kwargs(**args):
    print(args)


print_kwargs(name="kang",age=70,city="Daegu")

a = 1
def test_1():
    global a
    a = a+1
  
test_1()
print(a)