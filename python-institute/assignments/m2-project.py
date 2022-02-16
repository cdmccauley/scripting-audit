# print(0b11000000)
# print(0xFE80)

# print(bin(192))
# print(hex(65152))

# we learned about binary representation in python
# one place we work with binary number is in networking
# ipv4 addresses are commonly displayed as integer representations of binary numbers
# you may have already learned about the concept of CIDR notation
# manually converting a CIDR notated IP address is a great exercise but we can save that for our certification study
# let's take a break from manually converting and make Python do it for us

# get each octet of an ipv4 address
int_first = 192
int_second = 168
int_third = 1
int_fourth = 2

# convert each octet to binary
bin_first = bin(int_first)
bin_second = bin(int_second)
bin_third = bin(int_third)
bin_fourth = bin(int_fourth)

# test the result, print will convert each octet to a string representation
print(bin_first, bin_second, bin_third, bin_fourth, sep=".") # 0b11000000.0b10101000.0b1.0b10
# the result is correct but does not look as expected

# since the binary is correct but not immediately readable, we can instead turn it into a string
octetFormat = "08b"
str_first = format(int_first, octetFormat)
str_second = format(int_second, octetFormat)
str_third = format(int_third, octetFormat)
str_fourth = format(int_fourth, octetFormat)

print(str_first, str_second, str_third, str_fourth, sep=".")

str_binary_ipv4 = str_first + "." + str_second + "." + str_third + "." + str_fourth

print(str_binary_ipv4)