import random
number= random.randint(1,11)
print('Enter a number between 1 and 10')
guess= input()
if guess==number:
    print('Guess is correct')
else:
    print('Sorry, your guess is incorrect')
    
