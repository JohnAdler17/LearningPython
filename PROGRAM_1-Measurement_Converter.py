'''
 * Program 1: Measurement Converter
 *
 * Programmer: John Adler
 *
 * Due Date: Thursday, September 7, 2017
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program.
 *
 * Description: This program will convert a measurement of miles/hour to
 *              barleycorns/day, furlongs/fortnight, mach number, and 
 *              percentage of the speed of light.
 *
 * Input: The user inputs a value for a measurement of miles/hour to be
 *        converted into other measurements.
 * Output: The inputted value of miles/hour is output as 4 different
 *         measurements: barleycorns/day, furlongs/fortnight, mach number,
 *         and the percentage of the speed of light.
 *
'''

#User inputs value for miles/hour (mi_hr) to be converted
mi_hr = float(input("Enter a speed in miles/hour: "))

#Equations that convert the miles/hour into other measurements

#To convert miles/hour into barleycorn/day, I multiplied the inputted mi_hr by
#the number of meters in a mile (1609.34), the number of barleycoins in a
#meter (117.647) and the number of hours in a day (24).
barley_day = 1609.34 * 117.647 * mi_hr * 24

#To convert miles/hour into furlong/fortnight, I multiplied mi_hr by the number
#of yards in a mile (1760) and the number of hours in a week (336). Then I
#divided the product by the number of yards in a furlong (220).
fur_fort = (1760 * 336 * mi_hr)/220

#To convert miles/hour into mach number, I multiplied mi_hr by the number of
#feet in a mile (5280) and divided that product by the product of the number
#of seconds in an hour (3600) and by mach 1 (1130).
num_mach = (5280 * mi_hr)/(3600 * 1130)

#I kept getting an error when trying to calculate the percentage of the speed
#of light so I converted the (1/299792458) I was multiplying into a variable
#named sl and substituted it in the formula for num_SOL. The 1609.34 is the
#number of meters in a mile, the 1/3600 is the number of hours in a second,
#and the variable sl represents the reciprocal of the speed of light.
sl = (1/299792458)
num_SOL = 1609.34 * mi_hr * (1/3600) * sl


#Printing the output and final measurements
print ("Original speed in miles/hour:", mi_hr)

print ("Converted to barleycorns per day:", barley_day)

print ("Converted to furlongs per fortnight:", fur_fort)

print ("Converted to mach number:", num_mach)

print ("Converted to a percentage of the speed of light:", num_SOL)
