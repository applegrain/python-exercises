__author__ = 'Applegrain'


#Define the variables and the equation and how they will interact
def equation(PV, i, n):
    return_value = PV*(1+i)**n
    return return_value

#Print the statement and evaluate our function with given values
print 'The future value of your investment is', equation(100, 0.10, 2), 'USD.'

