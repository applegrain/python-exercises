__author__ = 'Applegrain'

tot_seconds = input('Please state total number of seconds.')

tot_hours = int(tot_seconds/3600)
tot_minutes = int((tot_seconds % 3600)/60)
tot_seconds = int((tot_seconds % 3600)%60)

print 'The time is', int(tot_hours), 'hours,', int(tot_minutes), 'minutes and', int(tot_seconds), 'seconds.'

