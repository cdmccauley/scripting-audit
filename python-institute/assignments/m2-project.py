# we learned about binary representation in python
# one place we work with binary numbers is in networking
# ipv4 addresses are commonly displayed as integer representations of binary numbers
# you may have already learned about the concept of CIDR notation
# manually converting a CIDR notated IP address is a great exercise but we can save that for our certification study
# let's take a break from manually converting and make Python do it for us

# NOTE: this could be done via input and might be a good conversion candidate for the practice
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
# format will also help us remove the 0b prefix used by Python
octetFormat = "08b"
str_first = format(int_first, octetFormat)
str_second = format(int_second, octetFormat)
str_third = format(int_third, octetFormat)
str_fourth = format(int_fourth, octetFormat)

# test the result
# print(str_first, str_second, str_third, str_fourth, sep=".") # 11000000.10101000.00000001.00000010
# the result is correct and looks as expected

# now that each octect is more readable, we can combine them into a single string for display using the concatenation operator
# instead of repeatedly typing the same string to use as a separator, we can define it once and use it multiple times
# doing this allows us to quickly change the value if we want to at a later time
str_separator = "."
str_binary_ipv4 = str_first + str_separator + str_second + str_separator + str_third + str_separator + str_fourth

# test the result
print(str_binary_ipv4) # 11000000.10101000.00000001.00000010
# the result is correct and looks as expected

# we can now move on to converting the cidr notation to binary
# since we know mathematical operators we will creatively use them to form our output
# the logic used behind this process will become easier as we learn more features of Python

# find how many bits are "on" for the network portion of the address
int_qty_network = int(int_cidr)

# find how many bits are "off" for the host portion of the address
int_qty_host = int(32 - int_qty_network)

# find how many network octets are completely network octets
int_full_network = int(int_qty_network // 8)

# find how many host octets are completely host octets
int_full_host = int(int_qty_host // 8)

# find how many mixed octets are required
int_mix = int(4 - (int_full_network + int_full_host))

# build a full octect of on bits for easy output
str_on = "1"
str_full_on = (str_on * 8) + str_separator

# build a full octet of off bits for easy output
str_off = "0"
str_full_off = str_separator + (str_off * 8)

# build the mixed octet that will connect the host and network portions of the address
str_mix_on = (8 - (int_qty_host - (int_full_host * 8))) * str_on
str_mix_off = (int_qty_host - (int_full_host * 8)) * str_off
str_mix = str_mix_on + str_mix_off

# check if there will be an extra network octect
int_extra_network = int((int_mix - 1) * (int_mix - 1))

# multiply our results by the proper string representations to create a full mask
# start by assigning the start of the mask
str_full_cidr = str_full_on * (int_full_network - int_extra_network)
# use compound assignment to add the connecting octet
str_full_cidr += str_mix
# use compound assignment to add the end of the mask
str_full_cidr += str_full_off * int_full_host

# check the results
print(str_full_cidr)

# NOTE: this portion is repeat code and should be part of the practice
# get octets for a comparison via input
int_first_compare = int(input("Enter the first octet: "))
int_second_compare = int(input("Enter the second octet: "))
int_third_compare = int(input("Enter the third octet: "))
int_fourth_compare = int(input("Enter the fourth octet: "))

# convert input to octets
str_first_compare = format(int_first_compare, octetFormat)
str_second_compare = format(int_second_compare, octetFormat)
str_third_compare = format(int_third_compare, octetFormat)
str_fourth_compare = format(int_fourth_compare, octetFormat)

# concatenate the octets into a single string
str_binary_compare = str_first_compare + str_separator + str_second_compare + str_separator + str_third_compare + str_separator + str_fourth_compare

# print for comparison
print(str_binary_compare)