def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

def lcmm(*args):
    return reduce(lcm, args)

if __name__ == '__main__':
    print lcmm(*range(1,21))
