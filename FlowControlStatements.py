import random

secret_number = random.randint(1, 20)
print('I am thinking in between 1 and 20')

for guesses_taken in range(1, 5):
    print('Please take a guess!!!')
    guess = int(input())

    if guess < secret_number :
        print('The number is too low')
    elif guess > secret_number :
        print('The number is too high')
    else:
        break

if guess == secret_number:
    print('Amazing Job!!! you guessed my number in ' + str(guesses_taken) + 'guesses!')
else:
    print('DUH!!! The number i was thinking was' + str(secret_number))