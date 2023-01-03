# guessing number game using random 

import random
cnumber= random.randrange(1,300)
userinput= int(input("Enter the number:---"))
if userinput>cnumber:
    print("Computer Number",cnumber)
    print("your guess number is too high")
elif cnumber>userinput:
    print("Computer Number",cnumber)
    print("Your guess number is too low")
else:
    print("Computer Number",cnumber)
    print("Your guess number is equal")
