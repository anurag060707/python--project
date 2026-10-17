import random
computer_number=random.randint(1,101)
user_number=int(input("enter your number:"))
if user_number>computer_number:
                     print("computer number",computer_number)
                     print("your guess number is too high:")
elif user_number<computer_number:
    print("computer number",computer_number)
    print("your number is too low:")
else:
    print("computer number",computer_number)
    print("your guess number is equal")
