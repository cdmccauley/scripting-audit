secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Your number: "))

while secret_number != user_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Your number: "))

print("Well done, muggle! You are free now.")