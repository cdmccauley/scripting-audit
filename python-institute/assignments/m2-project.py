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

# set each octet of an ipv4 address
int_first = 192
int_second = 168
int_third = 1
int_fourth = 2

# set cidr notation
int_cidr = 24

# convert each octet to binary
# bin_first = bin(int_first)
# bin_second = bin(int_second)
# bin_third = bin(int_third)
# bin_fourth = bin(int_fourth)

# test the result, print will convert each octet to a string representation
# print(bin_first, bin_second, bin_third, bin_fourth, sep=".") # 0b11000000.0b10101000.0b1.0b10
# the result is correct but does not look as expected

# NOTE: requires explanation of format
# since the binary is correct but not immediately readable, we can instead turn it into a string
octetFormat = "08b"
str_first = format(int_first, octetFormat)
str_second = format(int_second, octetFormat)
str_third = format(int_third, octetFormat)
str_fourth = format(int_fourth, octetFormat)

# test the result
# print(str_first, str_second, str_third, str_fourth, sep=".") # 11000000.10101000.00000001.00000010
# the result is correct and looks as expected

# now that each octect is more readable, we can combine them into a single string for display using the concatenation operator
# instead of repeatedly typing the same string, we can define it once and use it multiple times, this allows us to quickly change the value
str_separator = "."
str_binary_ipv4 = str_first + str_separator + str_second + str_separator + str_third + str_separator + str_fourth

# test the result
print(str_binary_ipv4) # 11000000.10101000.00000001.00000010
# the result is correct and looks as expected

# we can now move on to converting the cidr notation to binary
# since cidr is just telling how many bits are "on" for the network portion of the address we can use some math to start
int_qty_full_on = int(int_cidr // 8)
int_qty_host = int(32 - int_cidr)
int_qty_full_off = int(int_qty_host // 8)

print(int_qty_full_on, int_qty_full_off, int_qty_host)

# build a full octect of on bits
str_on = "1"
str_full_on = str_on * 8 + str_separator

# build a full octet of off bits
str_off = "0"
str_full_off = str_off * 8 + str_separator

# build a mixed octect
# str_mix_on = (8 - (int_qty_host - (int_qty_full_off * 8))) * str_on
# str_mix_off = (int_qty_host - (int_qty_full_off * 8)) * str_off
# str_mix = str_mix_on + str_mix_off
# thoughts: instead of building the middle and end separately, build at the same time

# print("begin", str_full_on * int_qty_full_on)
# print("mid", str_full_off * int_qty_full_off)
# print("end", str_mix)

# full_cidr = (str_full_on * int_qty_full_on) + (str_full_off * int_qty_full_off) + str_mix

# print(full_cidr)