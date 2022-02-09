total = 0
multiples = []
for n in range(334):
    if n*3 < 1000:
        if n*3 not in multiples:
            multiples.append(n*3)
            total = total + n*3
    if n*5 < 1000:
        if n * 5 not in multiples:
            multiples.append(n * 5)
            total = total + n*5

print(total)