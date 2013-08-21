import math

a = 600851475143
counter = 2
while math.sqrt(counter) < a :
    while a % counter == 0:
        a = a / counter
        print counter
    counter += 1



   
