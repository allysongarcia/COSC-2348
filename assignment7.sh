#Assignment 7
#Author: Allyson Garcia
#Date: 04/06/2022

<<com
Problem 1: This problem contains two shell scripts which run on bash and sh,
respectively. (Each script would have to be in its own file).
com

#shell script that runs on bash 
#!/bin/bash
echo "This is assignment 7"

#shell script that runs on sh
#!/bin/sh
echo "This is assignment 7"


<<com
Problem 2: This script creates a variable for my name and each of the classes I am taking.
Then, all of these variables are printed.
com
#!/bin/bash
NAME="Allyson"                                                                                           
class_1="Intro to Scripting"
class_2="Data Structures"
class_3="Technical and Professional Writing"
class_4="Computer Architecture"
class_5="US Gov and Politics"
echo "My name is $NAME."
echo "I am taking $class_1, $class_2, $class_3, $class_4, and $class_5."
echo " "


<<com
Problem 3: This program uses special variables to print my name and the courses I am taking.
com
#!/bin/bash
echo "My name is $1"
echo "I am taking $2, $3, $4, $5, and $6"
echo " "


<<com
Problem 4: This shell script prints the process number and all arguments passed.
com
#!/bin/bash
#Print the process number
echo "Current process number is: $$"
#Print all arguments passed
echo $@
echo " "  


<<com
Problem 5:
com
#!/bin/bash
RANDOM=$$
num=$((1+$RANDOM%100))
echo "Number grade is: $num"
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


<<com
Problem 6:
com
#!/bin/bash
var_1=28
var_2=209                                                                                                                                                                                                          
var_3=7                                                                                                                                                                                  
var_4=23                                                                                                                                                                                                           
echo "Addition of $var_1 + $var_2: $((var_1+var_2))"                                                                                                                                                               
echo "Subtraction of $var_1 - $var_4: $((var_1-var_4))"                                                                                                                                                            
echo "Multiplication of $var_1 * $var_3: $((var_1*var_3))"                                                                                                                                                         
echo "Division of $var_1 / $var_3: $((var_1/var_3))"                                                                                                                                                               
echo "Incrementing $var_2: $((++var_2))"    
echo "Decrementing $var_3: $((--var_3))"
echo " "


<<com
Problem 7:
com
