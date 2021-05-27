import random
guess=0
answer=random.randint(1,10)
print(answer)
print("Enter any random number between 1 and 10")

while guess != answer:
    guess=int(input())
    if guess==answer:
        print("You got that in the first time")
        break
    else:
        if guess==answer:
            print("You got it this time")
        else:
                if guess > answer:
                    print("Guess some lower value")
                else:
                        print("Guess some higher value")