a = 61
print(0 < a < 10)
print(0 < a and a < 62)
print((1, 2, 4) < (1, 3, 1))


a = 'asasas'
b = 20
c = a
d = 'asasas'
print(a == b)
print(a is b)
print(a == c)
print(a is c)

print(a == d)
print(a is d)

print([] or 'logo')


def f(msg =None):
    msg and print(msg)

f()
f('hihi')
