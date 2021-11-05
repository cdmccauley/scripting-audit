blocks = int(input("Enter the number of blocks: "))

# base = 0
height = 0

# incrementing height by current height + 1 blocks
while blocks > height:
    height += 1
    blocks -= height

# incrementing height by current base length + 1 blocks
# while blocks > height:
#     base += 1
#     blocks -= base
#     height += 1
    
print("The height of the pyramid:", height)