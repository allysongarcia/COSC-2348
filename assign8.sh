#!/bin/bash
<<com
Assignment 8
Author: Allyson Garcia
Date: 4/10/2022
com

#Question 1: This script prints numbers from 1 to 15 using
#while, until, and for loops.

#Using while loop
echo "Printing numbers 1 to 15 using while loop:"
i=1
while [ $i -le 15 ]
do
	echo $i
	let i++
done

echo " "

#Using until loop
echo "Printing numbers 1 to 15 using until loop:"
i=1
until [ $i -gt 15 ]
do
	echo $i
	let i++
done

echo " "

#Using for loop
echo "Printing numbers 1 to 15 using for loop:"
for i in $(seq 15)
do
	echo $i
done

echo " "


#Question 2: This script finds the summation of numbers
#20 to 40 using while, until, and for loops.

#Using while loop
j=20
sum=0
while [ $j -le 40 ]
do
	let sum+=j
	let j++
done
echo "Summation (found with while loop):" $sum

#Using until loop
j=20
sum=0
until [ $j -gt 40 ]
do
	let sum+=j
	let j++
done
echo "Summation (found with until loop):" $sum

#Using for loop
sum=0
for j in $(seq 20 40)
do
	let sum+=j
done
echo "Summation (found with for loop):" $sum
echo " "


#Question 3: This script finds all prime numbers less than 50
#using while, until, and for loops.

#Using while loop
echo "Finding prime numbers with while loop:"
k=2
while [ $k -le 50 ]
do
    divide=2
    while [ $divide -lt $k ]
    do
        remainder=$((k%divide))
        if [ $remainder -eq 0 ]
        then
            break
        fi
        let divide++
    done
    if [ $divide -eq $k ]
    then
        echo $k
    fi
    let k++
done
echo " "

#Using until loop
echo "Finding prime numbers with until loop:"
k=2
until [ $k -gt 50 ]
do
    divide=2
    until [ $divide -ge $k ]
    do
        remainder=$((k%divide))
        if [ $remainder -eq 0 ]
        then
            break
        fi
        let divide++
    done
    if [ $divide -eq $k ]
    then
        echo $k
    fi
    let k++
done
echo " "

#Using for loop
echo "Finding prime numbers with for loop:"
for k in $(seq 2 50)
do
    for divide in $(seq 2 $k)
    do
        if [ $((k%divide)) -eq 0 ]
        then
            break
        fi
        let divide++
    done
    if [ $divide -eq $k ]
    then
        echo $k
    fi
    let k++
done
echo " "


#Question 4: This script uses a switch condition to print the
#name of a certain college.
read -p "Enter the college name (with first letter capitalized): " COLLEGE

case $COLLEGE in
    Corpus)
        echo "Texas A&M University Corpus Christi" ;;
    Kingsville)
        echo "Texas A&M University Kingsville" ;;
    Commerce)
        echo "Texas A&M University Commerce" ;;
    *)
        echo "Texas A&M University" ;;
esac
echo " "

#Bonus Question: To fix the code, I changed the square brackets around the first
#two if statements and changed => and <= to -ge and -le, respectively.
var_test=20
#ranges 1 to 10, 11 to 20, more
if [ $var_test -ge 1 ] && [ $var_test -le 10 ]
then 
echo "Between 1 to 10"
elif [ $var_test -ge 11 ] && [ $var_test -le 20 ]
then 
echo "Between 11 to 20"
elif [ $var_test -gt 20 ]
then
echo "greater than 20"
else
echo "less than 1"
fi
