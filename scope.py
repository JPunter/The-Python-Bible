a = 250
def f1():
    global a
    a = 90 # global
    b = a + 15
    print(b)

def f2():
    a = 50 # local
    print(a)

f1()
f2()
print(a)
