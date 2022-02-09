current = 2
buffer = 0
second = 1
total = 2
while current < 35:
    buffer = current
    current = current + second
    second = buffer
    if (current % 2) == 0:
        total = total + current

print(total)