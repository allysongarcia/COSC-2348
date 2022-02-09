'''
Assignment 2
Author: Allyson Garcia
Date: 02/08/2022
'''

'''
Problem 1: This program uses nested for loops in order to print two patterns.
For the first pattern, two for loops are used. For the second pattern, three
for loops are used.
'''
#i.)
#first loop for rows
for counter in range(0,5):
    #second loop for columns
    for counter2 in range(0,counter+1):
        #print asterisks
        print("* ", end = '')
    #go to next line
    print()

print()

#ii.)
#variable used for printing spaces
k = 8
#first loop for rows
for index in range(0,5):
    #second loop to place a certain amount of spaces in each row
    for index2 in range(0,k):
        print(end = ' ')
    #decrement after each loop
    k = k - 2
    #third loop for columns
    for index3 in range(0,index+1):
        #print asterisks
        print("* ", end = '')
    #go to next line
    print()

print()


'''
Problem 2: This program first gets two inputs from the user. Then, the program
uses while loops to find n!, r!, and (n-r)!. Then, nCr and nPr are calculated
using the given formulas and are printed to the user.
'''
#i.)
#get inputs from the user
n = int(input("Enter n: "))
r = int(input("Enter r: "))

#define loopCounters
loopCounter1 = 1
loopCounter2 = 1
loopCounter3 = 1

#define variables to store the calculated values
nFactorial = 1
rFactorial = 1
subtractFact = 1

#use while loops to calculate n!, r!, and (n-r)!
while loopCounter1 <= n:
    nFactorial = nFactorial * loopCounter1
    loopCounter1 += 1
while loopCounter2 <= r:
    rFactorial = rFactorial * loopCounter2
    loopCounter2 += 1
while loopCounter3 <= (n - r):
    subtractFact = subtractFact * loopCounter3
    loopCounter3 += 1

#ii.)
nCr = nFactorial / (rFactorial * subtractFact)
print("nCr", nCr)

#iii.)
nPr = nFactorial / subtractFact
print("nPr", nPr)

print()


'''
Problem 3: This program uses nested for loops and an if statement to sort a
list of integers in ascending order. The program then prints the new list.
'''
#list to be sorted
list = [20, 68, 41, 88, 16, 40, 65, 97, 85]

#use nested for loops to sort the list in ascending order
for temp in range(len(list)):
    for temp2 in range(temp + 1, len(list)):
        if list[temp] > list[temp2]:
            list[temp], list[temp2] = list[temp2], list[temp]

#print the new list
print("List sorted in ascending order:")
print(list)

print()


'''
Problem 4: This program first calculates and prints the sum of all the elements
in the list. Then, a for loop and if/else statements are used to create two new
lists, one containing even numbers and the other containing odd numbers. Next,
the sum of each new list is calculated. Finally, each new list and their sum are
printed to the user.
'''
#original list
list = [20, 68, 41, 88, 16, 40, 65, 97, 85]

#variables to hold the sum of each list
listSum = 0
oddSum = 0
evenSum = 0

#create two new lists to hold the even and odd numbers
oddList = []
evenList = []

#i.) Find the sum of all elements in the list
for temp in list:
    listSum = listSum + temp
print("Sum of all elements in list:", listSum)

#ii.) and iii.)
#Create even and odd number lists
for temp in list:
    if temp % 2 == 0:
        evenList.append(temp)
    else:
        oddList.append(temp)

#Find the sum of elements in each list
for temp in evenList:
    evenSum = evenSum + temp
for temp in oddList:
    oddSum = oddSum + temp

#Print each new list and the sum of elements in each list
print("List of even numbers:", evenList)
print("Sum of even numbers:", evenSum)
print("List of odd numbers:", oddList)
print("Sum of odd numbers:", oddSum)

print()


'''
Problem 5: This program uses nested for loops to print out prime numbers
between 2 and 50.
'''
print("Prime numbers between 2 and 50:")

#use nested for loops to print the prime numbers
for num in range(2,(50 + 1)):
    #test if num is divisible by anything other than 1 and itself
    for i in range(2, num):
        #if number is not prime, break out of the loop
        if (num % i) == 0:
            break
    #if number is prime, print the number
    else:
        print(num, " ")

print()


'''
Problem 6: This program uses individual methods for the first three problems in
the assignment. The main function calls each of these methods in order to print
the output for each problem.
'''
#-----Problem 1-----
#function to print the two patterns
def patterns():
    #first pattern
    for counter in range(0,5):
        for counter2 in range(0,counter+1):
            print("* ", end = '')
        print()
    print()
    #second pattern
    k = 8
    for index in range(0,5):
        for index2 in range(0,k):
            print(end = ' ')
        k = k - 2
        for index3 in range(0,index+1):
            print("* ", end = '')
        print()

#-----Problem 2-----
#function to perform calculations
def calculate(n,r):
    #define variables
    nFactorial = 1
    rFactorial = 1
    subtractFact = 1
    counter = 1
    #use while loops to calculate the factorial of n, r, and (n-r)
    while counter <= n:
        nFactorial = nFactorial * counter
        counter += 1
    counter = 1
    while counter <= r:
        rFactorial = rFactorial * counter
        counter += 1
    counter = 1
    while counter <= (n - r):
        subtractFact = subtractFact * counter
        counter += 1
    #calculate and print nCr and nPr
    nCr = nFactorial / (rFactorial * subtractFact)
    print("nCr", nCr)
    nPr = nFactorial / subtractFact
    print("nPr", nPr)

#-----Problem 3-----
#function to sort the array
def sorter(list):
    for temp in range(len(list)):
        for temp2 in range(temp + 1, len(list)):
            if list[temp] > list[temp2]:
                list[temp], list[temp2] = list[temp2], list[temp]
    print("List sorted in ascending order:")
    print(list)

#define main function for all three problems
def main():
    #problem 1
    patterns()
    print()
    #problem 2
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    calculate(n,r)
    print()
    #problem 3
    list = [20, 68, 41, 88, 16, 40, 65, 97, 85]
    sorter(list)
    print()

#call main function
main()


'''
Problem 7: This program takes an input from the user and determines if it is
an Armstrong number or not. The program uses a function to determine if the
input can be written as the sum of the exponential of its digits. If this sum
is equal to the input, then the input is an Armstrong number.
'''
#function to calculate if input is an Armstrong number
def armstrongNumber(num):
    #calculate total num of digits
    length = len(str(num))

    #initialize variables
    sum = 0
    tempNum = num

    #use while loop to calculate the sum of the exponential of the digits
    while tempNum > 0:
        singleDigit = tempNum % 10
        sum += singleDigit ** length
        tempNum = tempNum // 10

    #print the sum
    print("Sum of Exp. of Digits:", sum)

    #tell user if input is an Armstrong number or not
    if num == sum:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is not an Armstrong Number")

#main function
def main():
    num = int(input("Enter an integer: "))
    armstrongNumber(num)
    print()

#call main function
main()


'''
Problem 8: This program uses a function to determine the Fibonacci number at a
certain index. Within this function, if/else statements are first used in case
the user enters 0 or 1. Otherwise, a for loop is used to calculate the
Fibonacci number at the given index. This number is returned to the main
function, where it is printed to the user.
'''
#function to calculate fibonacci number at certain index
def fibonacci(userInput):
    #define variables
    firstNum = 0
    secondNum = 1
    #use if/else statements to return a certain value to the main function
    if userInput == 0:
        return firstNum
    elif userInput == 1:
        return secondNum
    else:
        #use for loop to calculate fibonacci number
        for index in range(1, userInput):
            temp = firstNum + secondNum
            firstNum = secondNum
            secondNum = temp
        return secondNum

#main function
def main():
    #ask user to enter an integer
    userInput = int(input("Enter an integer: "))
    #call the fibonacci function to find the corresponding number
    number = fibonacci(userInput)
    #print number to user
    print(number, "is the Fibonacci number at index", userInput)

#call main function
main()

print()


'''
Problem 9: In this problem, I revise the given code in order to print even
numbers. The only revision I needed to make was to delete the line of code in
the while loop that printed the loop_counter before determining if the number
is even or not. This line was the reason why odd numbers were printing once
and even numbers were printing twice. By deleting the line, the code will now
only print even numbers.
'''
loop_counter = 1
while loop_counter <= 10:
    #print(loop_counter)  (this line should be deleted)
    if loop_counter%2 == 0:
        print(loop_counter)
    loop_counter += 1 #Here we are increasing loop count by 1
