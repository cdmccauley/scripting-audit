# step 1
beatles = []
print("Step 1:", beatles)

# step 2
originals = ["John Lennon", "Paul McCartney", "George Harrison"]
for original in originals:
    beatles.append(original)
print("Step 2:", beatles)

# step 3
names = ["Stu Sutcliffe", "Pete Best"]
for name in names:
    beatles.append(input("Please enter \"" + name + "\": "))
print("Step 3:", beatles)

# step 4
for name in names:
    del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))