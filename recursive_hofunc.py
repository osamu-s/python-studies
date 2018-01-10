
def base(num, func):
    return (1 if num == 1
            else func(num-1)+1 )

print (base(3, lambda x: x*2))

f = lambda x: base(x, lambda y: y*2)
print (f(3))

def wrap(num):
    return base(num, wrap)

print (wrap(3))

g = lambda x: base(x, g)
print (g(3))


