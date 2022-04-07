#!/bin/bash
<<com
Assignment 7 (Problems 2-7)
Author: Allyson Garcia
com

#Problem 2: This script creates a variable for my name and each of the classes I am taking. Then, all of these variables are printed.
NAME="Allyson"
class_1="Intro to Scripting"
class_2="Data Structures"
class_3="Technical and Professional Writing"
class_4="Computer Architecture"
class_5="US Gov and Politics"
echo "My name is $NAME."
echo "I am taking $class_1, $class_2, $class_3, $class_4, and $class_5."
echo " "

#Problem 3: This script uses special variables to print my name and the courses I am taking.
#The special variables read my input. The first argument I enter is my name and the next five arguments are my classes.
echo "My name is $1"
echo "I am taking $2, $3, $4, $5, and $6"
echo " "

#Problem 4: This shell script prints the process number and all arguments passed.
#Print the process number
echo "Current process number is: $$"
#Print all arguments passed
echo "All arguments passed: $*"
echo " "

#Problem 5: This script generates a random number from 0 to 100. Then, if/else conditions are used to determine the letter grade. 
#Generate a random number
RANDOM=$$
num=$((1+$RANDOM%100))
#Print the number grade
echo "Number grade is: $num"
#If/else conditions used to find and print the letter grade
if [ "$num" -ge 90 ]
then
echo "Letter grade is: A"
elif [ "$num" -ge 80 ]
then
echo "Letter grade is: B"
elif [ "$num" -ge 70 ]
then
echo "Letter grade is: C"
elif [ "$num" -ge 60 ]
then
echo "Letter grade is: D"
else
echo "Letter grade is: F"
fi
echo " "

#Problem 6: This script creates several variables and uses them to perform a few calculations. 
#Variables
var_1=28
var_2=209
var_3=7
var_4=23
#Print out addition, subtraction, multiplication, and division of some of the variables
echo "Addition of $var_1 + $var_2: $((var_1+var_2))"
echo "Subtraction of $var_1 - $var_4: $((var_1-var_4))"
echo "Multiplication of $var_1 * $var_3: $((var_1*var_3))"
echo "Division of $var_1 / $var_3: $((var_1/var_3))"
#Increment and decrement two of the variables
echo "Incrementing $var_2: $((++var_2))"
echo "Decrementing $var_3: $((--var_3))"
echo " "

#Problem 7: This script reads an employee's basic salary and determines their gross salary.
#Let the user enter the employee's salary
read -p "Enter employee's basic salary: " basic_salary
#Print the basic salary
echo "Basic Salary: ""$""$basic_salary"
#Use if/else conditions to determine the hra and da of the employee
if [ "$basic_salary" -le 10000 ]
then
hra=$((basic_salary/5))
da=$(((basic_salary*4)/5))
elif [ "$basic_salary" -le 20000 ]
then
hra=$((basic_salary/4))
da=$(((basic_salary*9)/10))
else
hra=$(((basic_salary*3)/10))
da=$(((basic_salary*19)/20 | bc))
fi
#Calculate the gross salary using the basic salary, hra, and da
gross_salary=$((basic_salary+hra+da))
#Print the hra, da, and gross salary
echo "hra: ""$""$hra"
echo "da: ""$""$da"
echo "Gross Salary: ""$""$gross_salary"
