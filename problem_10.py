i = 2
a = []
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

while i <= 2000000:
        i += 1
        if isPrime(i):
            a.append(i)

print sum(a) + 2
