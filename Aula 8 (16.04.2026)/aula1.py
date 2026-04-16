# Geradores

def meuGerador():
    yield 1
    yield 2
    yield 3

gen = meuGerador()

print (next(gen))
print (next(gen))
print (next(gen))