import random
secret = random.randint(1, 10)
num = 0
guess = 5

print("I am thinking of a number between 1 and 10")

while num != secret and guess != 0:
    print("You have %d guesses left." % guess)
    num = int(input("What's the number? "))
    if num < secret:
        print("%d is too low." % num)
    if num > secret:
        print("%d is too high." % num)
    guess -= 1

if num == secret:
    print("Yes! You win!")
else:
    print("You ran out of guesses!")