a, b, c = map(int, input().split())

max_salary = max(a, b, c)
min_salary = min(a, b, c)

print(max_salary - min_salary)
