import math

def h(a, b):
    return math.sqrt(a*a + b*b)

h1 = h(3, 4)
h2 = h(6, 8)

print(h1)
print(h2)

if h1 > h2:
    print("first big")
else:
    print("second big")
