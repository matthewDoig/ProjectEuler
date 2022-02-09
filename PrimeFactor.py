def is_prime(factor):
    Prime = True
    current = 0
    for x in range(2,int(factor)):
        current = factor / x
        if current.is_integer() == True:
            prime = False
            return(False)
    return(True)


n = 1
total = 0
factor = []
max = 600851475143
for n in range(1,max):
    current = max/n
    if current.is_integer() == True:
        factor.append(current)
        total = total +1

for x in range(total):
    if is_prime(factor[x]) == True:
        print(factor[x])