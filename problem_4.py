a = []
b = []
for i in range(100,1000):
    for n in range(100,1000):
        a.append(i * n)

c = set(a)
for i in c:
    if str(i) == str(i)[::-1]:
        b.append(i)

print max(b)
