__author__ = 'Applegrain'


#C is cost/mile and M is number of miles
def roundtrip(C, M):
    cost_1 = C*M
    return cost_1

#Same variables as previous + D=days a week
def month(C, M, D):
    cost_2 = C*M*D
    return cost_2

#Same variables + W=weeks a year you drive (15 weeks * 2 semester = 30)
def year(C, M, D, W):
    cost_3 = C*M*D*W
    return cost_3

#print statements and call on corresponding equation
print 'The cost of a roudntrip is', roundtrip(2, 70), 'US Dollars.'
print 'The monthly cost is', month(2, 70, 5), 'US Dollars.'
print 'The yearly cost (30 weeks of class) is', year(2, 70, 5, 30), 'US Dollars.'