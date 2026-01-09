def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

up = a * d
down = b * c

g = gcd(up, down)
print(up // g, "/", down // g)
def in_circle(x, y, a, b, r):
    return (x-a)**2 + (y-b)**2 < r*r

a = 0
b = 0
r = 5

dots = [(1,1), (6,6), (2,2)]
c = 0

for d in dots:
    if in_circle(d[0], d[1], a, b, r):
        c += 1

print(c)
