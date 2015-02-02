__author__ = 'Applegrain'

#I made the constants into variables, (N) is the only variable that will differ
current_pop = 330357870
seconds_in_year = 365*24*60*60

#the values used to calculate yearly population
yearly_births = seconds_in_year / 7.0
yearly_deaths = seconds_in_year/ 13.0
yearly_immigration = seconds_in_year/ 35.0

#the equation to calculate the annual population
year_end_population = current_pop + yearly_births + yearly_immigration - yearly_deaths

#Print the statement and call on the year_end_population
print ('The year end population is %d.' % int(year_end_population))

