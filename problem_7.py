num = 1
i = 2
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

while num < 10001:
        i += 1
        if isPrime(i):
            num += 1
print i 
