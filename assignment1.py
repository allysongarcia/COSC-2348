'''
Problem 1: This program uses the print() function to display my name, address,
telephone number, and college major.
Author: Allyson Garcia
Date: 01/30/2022
'''
print("Name: Allyson Garcia")
print("Address: 126 Lee Avenue, Gregory, TX 78359")
print("Telephone Number: 361-222-3334")
print("Major: Cyber Security\n")


'''
Problem 2: This program asks the user to enter the square feet of a tract
of land and then calculates the number of acres in the tract. The program
uses the print() and input() functions to ask for and receive information
from the user.
Author: Allyson Garcia
Date: 01/30/2022
'''
#ask user to enter square feet to be converted to acres
squareFeet = float(input("Enter the total square feet in the tract of land: "))

#calculate number of acres with this formula
acres = squareFeet / 43560

#print calculated number of acres
print("Acres:", acres, "\n")


'''
Problem 3: This program determines the distance traveled by a car over
certain amounts of time. The program uses the formula "distance = speed * time"
to find the distance traveled by a car going 70 mph.
Author: Allyson Garcia
Date: 01/30/2022
'''
#constant speed of the car, assuming no accidents/delays
speed = 70

#calculate the distance over certain periods of time
sixHourDistance = speed * 6
tenHourDistance = speed * 10
fifteenHourDistance = speed * 15

#print out the distances
print("Distance in 6 Hours:", sixHourDistance, "miles")
print("Distance in 10 Hours:", tenHourDistance, "miles")
print("Distance in 15 Hours:", fifteenHourDistance, "miles\n")


'''
Problem 4: This program uses the input() function to ask the user to enter
a person's age. The program then uses if/else statements to determine if the
person is an infant, a child, a teenager, or an adult.
Author: Allyson Garcia
Date: 01/30/2022
'''
#get an age from the user
userAge = int(input("Enter a person's age: "))

#determine if the person is an infant, child, teenager, or adult
if userAge <= 1:
    print("The person is an infant\n")
elif userAge > 1 and userAge < 13:
    print("The person is a child\n")
elif userAge >= 13 and userAge < 20:
    print("The person is a teenager\n")
elif userAge >= 20:
    print("The person is an adult\n")


'''
Problem 5: This program asks the user to enter the number of coins it takes to
make exactly one dollar. Then, the program calculates how many cents the input
adds up to. Finally, the program prints a message to the user depending on if
the input equals exactly one dollar, is less than a dollar, or is greater than
a dollar.
Author: Allyson Garcia
Date: 01/31/2022
'''
#tell the user the goal of the change-counting game
print("Enter the number of coins required to make exactly one dollar.")

#ask the user to enter the number of pennies, nickels, dimes, and quarters
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

#determine if the coins add up to 1 dollar (100 cents)
dollarAmount = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)

#print a message to the user depending on how many cents the input added up to
if dollarAmount == 100:
    print("Congratulations! You won the game!\n")
elif dollarAmount < 100:
    print("Amount entered was less than one dollar.\n")
else:
    print("Amount entered was more than one dollar.\n")


'''
Problem 6: This program asks the user to enter a year and then uses if/else
statements to determine if the input is a leap year. The resulting number of
days in February is then printed to the user.
Author: Allyson Garcia
Date: 01/31/2022
'''
#ask user to enter a year
userYear = int(input("Enter a year: "))

#determine if the entered year is a leap year or not
if userYear % 100 == 0 and userYear % 400 == 0:
    print("February will have 29 days this year.\n")
elif userYear % 100 != 0 and userYear % 4 == 0:
    print("February will have 29 days this year.\n")
else:
    print("February will have 28 days this year.\n")


'''
Problem 7: This program asks the user to enter their weight and height and then
determines the person's BMI. The program prints out the BMI and a message saying
if the person is underweight, optimal weight, or overweight.
Author: Allyson Garcia
Date: 01/31/2022
'''
#ask the user to enter their weight and height
userWeight = int(input("Enter your weight (in pounds): "))
userHeight = int(input("Enter you height (in inches): "))

#calculate and print BMI
userBMI = (userWeight * 703) / (userHeight ** 2)
print("Your BMI is:", userBMI)

#determine if the user is underweight, overweight, or optimal weight
if userBMI < 18.5:
    print("You are underweight.\n")
elif userBMI >= 18.5 and userBMI <= 25:
    print("Your weight is optimal.\n")
else:
    print("You are overweight.\n")


'''
Problem 8: This program calculates information regarding Joe's stock
transactions. First, the program stores the given information into variables
and then uses this information to perform several calculations. The calculations
are then printed to the user as well as a message stating whether Joe made a
profit or not.
Author: Allyson Garcia
Date: 01/31/2022
'''
#known information
sharesPurchased = 2000
purchasePrice = 40.00
sharesSold = 2000
soldPrice = 42.75
commissionPercent = 0.03

#calculations
amountPaid = sharesPurchased * purchasePrice
commissionWhenBought = amountPaid * commissionPercent
amountSold = sharesSold * soldPrice
commissionWhenSold = amountSold * commissionPercent
totalMoneyLeft = amountSold-amountPaid-commissionWhenBought-commissionWhenSold

#print information
print("Amount paid for the stock: $", amountPaid)
print("Amount paid to the broker after buying the stock: $", commissionWhenBought)
print("Amount for which the stock was sold: $", amountSold)
print("Amount paid to the broker after selling the stock: $", commissionWhenSold)
print("Remaining amount: $", totalMoneyLeft)

#determine if Joe made a profit or not
if totalMoneyLeft > 0:
    print("Joe made a profit.")
elif totalMoneyLeft < 0:
    print("Joe lost money.")
else:
    print("Joe broke even.")
