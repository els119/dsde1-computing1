import random
number= random.randint(1,11)
print('Enter a number between 1 and 10')
guess= input()
if guess==number:
    print('Guess is correct')
else:
    print('please enter another number')
    guess2=input()
    if guess2==number:
        print('well done your guess is correct')
    else: 
        print('incorrect, last try')
        guess3=input()
        if guess3==number:
            print('Congrats, you got it right!')
        else:
            print('Incorrect, you have no more guesses left, the answer was ' + str(number))
    
