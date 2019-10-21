import random
number= random.randint(1,11)
print('Enter a number between 1 and 10')
guess=input()
guess=int(float(guess))
print(guess==number)
