# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

#Write a program to read contents of a file and perform following calculations:
#Average price per year. Average price per month. Highest and lowest prices per year.
#List of prices, lowest to highest. List of prices, highest to lowest.

import re

STARTING_DATE = 1993
ENDING_DATE = 2013

def main():

    gasFile = open('test.txt', 'r')

    gasList = gasFile.readlines()

    for i in range(STARTING_DATE, ENDING_DATE + 1):
        tempAverage = getYearlyAverage(gasList, i)
        print(f"The average gas price in {i} was {tempAverage}")

    for year in range(STARTING_DATE, ENDING_DATE + 1):
        for month in range(1, 13):
            tempAverage = getMonthlyAverage(gasList, year, month)
            print(f"The average gas price in {month}/{year} was {tempAverage}")

    
def getYearlyAverage(methodList, year):
    gasTotal = 0
    itemCount = 0
    yearlyAverage = 0

    for i in methodList:
        if getYear(i) == year:
            gasTotal += getPrice(i)
            itemCount += 1

    yearlyAverage = gasTotal / itemCount

    return yearlyAverage

def getMonthlyAverage(methodList, year, month):
    itemCount = 0
    monthlyAverage = 0

    for i in methodList:
        if getYear(i) == year:
            if getMonth(i) == month:
                monthlyAverage += getPrice(i)
                itemCount += 1
            
    if itemCount != 0: monthlyAverage /= itemCount
    else: monthlyAverage = "NAN"
    return monthlyAverage

def getYear(str):
    #Split the string at the colon.
    gasItems = str.split(':')
    #Split the date item at the hyphens.
    dateGasItems = gasItems[0].split('-')
    #Return the year, as an int.
    return int(dateGasItems[2])

def getDay(str):
    gasItems = str.split('-')
    return int(gasItems[1])

def getMonth(str):
    gasItems = str.split('-')
    return int(gasItems[0])

def getPrice(str):
    gasItems = str.split(':')
    return float(gasItems[1])

main()
