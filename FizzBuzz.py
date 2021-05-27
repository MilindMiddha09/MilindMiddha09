def fizzbuzz(num: int) -> str :
    """
    Plays the FizzBuzz game
    param: num
    return: 'Fizz' if the number is divisible by 3
            'Buzz' if the number is divisible by 5
            'Fizz Buzz' if the number is divisible by both '3' and '5'
            'number as a string' if the number is neither divisible by 3 nor divisible by 5
    """
    if num%15==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return str(num)


print("Playing FizzBuzz game ")
input("Press Enter to start ")
print()
next_number=0
while next_number <= 100:
    next_number +=1
    print(fizzbuzz(next_number))
    next_number += 1
    correct_guess=fizzbuzz(next_number).casefold()
    players_guess=input()
    if players_guess!=correct_guess:
        print("Sorry You failed, the correct answer was {}".format(fizzbuzz(next_number)))
        break
    elif next_number==100:
        print("Well done You completed the game")
        break
