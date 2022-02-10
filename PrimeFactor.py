import math
def is_prime(factor):
    prime = True
    half = (round(factor / 2) + 1)
    for x in range(2,int(half)):
        if factor % x == 0:
            prime = False
            return(False)
    return(True)

n = 1
total = 0
factor = []
max = 600851475143
for n in range(1,round(math.sqrt(max))+ 1):
    if max%n == 0:
        factor.append(max/n)
        factor.append(n)
        total = total + 2

for x in range(total):
    if is_prime(factor[x]) == True:
        print(factor[x])