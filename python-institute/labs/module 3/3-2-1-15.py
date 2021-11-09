# c0 = 15
# c0 = 16
c0 = 1023
count = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    count += 1
    print(int(c0))
    
print("steps", int(count))