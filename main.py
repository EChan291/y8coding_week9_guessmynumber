from random import randint

correct = randint(16, 64)
number = None

while number != correct:
    print("Guess my number!")
    number = int(input())

    if number > correct:
        print("Lower!")

    if number < correct:
        print("Higher!")

    if number >= five_less and number <= five_more:
        print("Almost - Within 5 away!")

    if number == correct:
        print("You wonnn!")

    five_less = number - 5
    five_more = number + 5 

