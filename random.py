__author__ = 'Applegrain'

import random

#generate a number between 0 and 100

number = random.randint(0,100)

#make the first guess

guess = int(input('Guess a number between 0 and 100.'))

numFound = False
while numFound == False:
    if guess > number:
        print 'You guessed too high'
        guess = int(input('Guess again:'))
    elif guess < number:
        print 'You guessed too low.'
        guess = int(input('Guess again:'))
    else:
        print "That's it. The number was %d." % number
        numFound = True

