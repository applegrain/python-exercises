__author__ = 'Applegrain'

#here I ask the user for data
pass_attempts = float(raw_input('How many total pass attempts?'))
pass_completions = float(raw_input('How many pass completions?'))

#repl pass attempts are less than pass completions

total_passing_yards = float(raw_input('How many total passing yards?'))
touchdowns = float(raw_input('How many total touchdowns?'))
interceptions = float(raw_input('How many total interceptions?'))

comp_per_att = pass_completions / pass_attempts
yards_per_att = total_passing_yards / pass_attempts
touchdowns_per_att = touchdowns / pass_attempts
interceptions_per_att = interceptions / pass_attempts

#here I define values that are used to caluclate the passer rating
C = comp_per_att - 0.30*5
Y = (yards_per_att-0.30)*0.25
T = touchdowns_per_att * 20
I = 2.375 - (interceptions_per_att*25)

#here I define the equation which uses above values to return a passer rating
passer_rating = (C+Y+T+I)/6*100

#print the final result
print ('The passer rating is %.2f.' % passer_rating)

#print statement indicating whether the rating is poor, mediocre, good or great
if passer_rating <= 85:
    print ('Better luck next time! This rating is poor.')
elif passer_rating < 90:
    print ('This is a bit better! But still mediocre.')
elif passer_rating < 95:
    print ('This is good!')
elif passer_rating >= 95:
    print ('Awesome! He is a keeper! This passer rating is great.')




