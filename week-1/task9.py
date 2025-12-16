ticket = input()

s1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
s2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if s1 == s2:
    print("YES")
else:
    print("NO")