__author__ = 'Applegrain'
import math

#prompt the user for number of folds
num_folds = int(input('Please state number of folds (no units please).'))

# original thickness is 0.005 and if the number of folds = 0, print original thickness
orig_thick = 0.005

#equation for new thickness and what the computers should perform at certain inputs

new_thick = (orig_thick*(2 ** num_folds))

#what the output should say in English
statement = 'The thickness of the paper is '

if num_folds == 0:
    print statement + str(orig_thick) + ' cm.'
if num_folds == 1:
    print statement + str(orig_thick * 2) + ' cm.'
elif num_folds > 1:
    print statement + str(new_thick) + ' cm.'




