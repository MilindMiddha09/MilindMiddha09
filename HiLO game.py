low=1
high=1000
print("Please guess a number between {} and {}".format(low,high))
input("Press Enter to start ")
guesses=1
while True:
    guess=low + (high-low)//2
    result=input("My guess is {}. Type c if it is correct, h if less and l if greater".format(guess))

    if result=="c":
        print("Yipee I guessed it correctly in {} guesses".format(guesses))
        break

    elif result=="h":
        low=guess+1

    elif result=="l":
        high=guess-1

    guesses+=1
    
