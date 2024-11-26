# Guessing number game
# store one number
# take the number input from user until it match with the number
# instruct the user if number is greate of lesser than the actual number
# limit the guesses and print the message

myNum = 18
i = 5

while (i > 0):
    print("You have ", i, " life left")
    print("Enter the number:")
    userNum = int(input())
    i -= 1

    if userNum > myNum:
        print("You entered bigger number")
    elif userNum < myNum:
        print("You entered smaller number")
    else:
        print("Hurry!You guess the number and you have ", i, " life")
        break
