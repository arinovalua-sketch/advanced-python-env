t = input()
w = t.split()

for i in range(len(w)):
    w[i] = ''.join(sorted(w[i]))

print(' '.join(w))
