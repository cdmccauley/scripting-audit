# step 1, create an empty list
beatles = []
print("Step 1:", beatles)

# step 2, use append
# originals = ["John Lennon", "Paul McCartney", "George Harrison"]
# for original in originals:
#     beatles.append(original)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3, use for and append
# names = ["Stu Sutcliffe", "Pete Best"]
# for name in names:
#     beatles.append(input("Please enter \"" + name + "\": "))
for i in range(2):
    beatles.append(input("Please enter Stu Sutcliffe or Pete Best: "))
print("Step 3:", beatles)

# step 4, use del
# for i in range(2):
#     del beatles[3]
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

# step 5, insert a new element at the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))