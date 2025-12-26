a = int(input())
b = int(input())
c = int(input())
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
if b < min:
    min = b
if c < min:
    min = c
print(max - min)

