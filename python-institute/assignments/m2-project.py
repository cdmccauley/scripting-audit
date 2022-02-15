# print(0b11000000)
# print(0xFE80)

# print(bin(192))
# print(hex(65152))

# print(bin(0xFE80))

first = 192
second = 168
third = 1
fourth = 2

# first = bin(first)[2:]
# second = bin(second)[2:]
# third = bin(third)[2:]
# fourth = bin(fourth)[2:]

octetFormat = "08b"
first = format(first, octetFormat)
second = format(second, octetFormat)
third = format(third, octetFormat)
fourth = format(fourth, octetFormat)

print(first, second, third, fourth, sep=".")