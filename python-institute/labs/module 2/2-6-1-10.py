x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + (1 / x))))

print("y =", y)

# sample input 1
# expected output 0.6000000000000001

# sample input 10
# expected output 0.09901951266867294

# sample input 100
# expected output 0.009999000199950014

# sample input -5
# expected output -0.19258202567760344