c = [2]
a,b = 1,2
while(b < 4000000):
    a,b = b, a + b
    if b % 2 == 0:
        c.append(b)
    

d = sum(c) 
print d 
