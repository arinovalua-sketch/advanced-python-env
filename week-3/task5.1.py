def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

up = a*d - b*c
down = b*d

g = gcd(abs(up), down)
print(up//g, "/", down//g)
