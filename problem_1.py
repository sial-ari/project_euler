a = []
for i in range(1, 1000):
    if i % 3 == 0:
        a.append(i)
    elif i % 5 == 0:
        a.append(i)

print a
print sum(a)

