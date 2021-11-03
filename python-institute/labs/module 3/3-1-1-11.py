income = float(input("Enter the annual income: "))

if income < 3089: # (3089 * .18) - 556.02 = 0
    tax = 0.0
elif income < 85528:
    tax = (income * .18) - 556.02
else:
    tax = 14839.02 + ((income - 85528) * .32)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")