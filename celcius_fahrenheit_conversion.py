__author__ = 'Applegrain'
#Lovisa Svallingson February 2015
#A program that takes an input in F or C and converts it to F or C respectively

degrees = raw_input("Press (F) for Fahrenheit and (C) for Celcius:")

if degrees == "C" or degrees == "c":
    celcius = float(raw_input("State Celcius degrees:"))
    celc_to_fahr = ((celcius*9) / 5) + 32
    print ("The temperature in Fahrenheit is %0.2f degrees." % celc_to_fahr)

if degrees == "F" or degrees == "f":
    fahrenheit = float(raw_input("State degrees Fahrenheit:"))
    fahr_to_celc = ((fahrenheit - 32) * 5)/9
    print ("The temperature in Celsius is %0.2f degrees." %fahr_to_celc)
else:
    print "Invalid input"







