#!/bin/bash
<<com
Assignment 9
Author: Allyson Garcia
Date: 4/18/2022
com

#Problem 1: This script creates an array with 20 random elements. Then, the array is
#sorted from lowest number to highest number using a for loop.

#Create an array of size 20 using random elements
RANDOM=$$
for i in $(seq 0 19)
do
	randomArray[i]=$(($RANDOM%100))
done

#Print the original array
echo "Original Array:" ${randomArray[@]}

#Use two for loops to sort the array
for i in $(seq 0 19)
do
for ((j=((i+1)); j<=19; j++))
do
	#Determine if two elements should be swapped
	if [ ${randomArray[i]} -gt ${randomArray[j]} ]
	then
		temp=${randomArray[i]}
		randomArray[i]=${randomArray[j]}
		randomArray[j]=$temp
	fi
done
done

#Print the sorted array
echo "Sorted Array(low to high):" ${randomArray[@]}
echo " "


#Problem 2: This script creates an array with 20 random elements. Then, the
#array is sorted from highest number to lowest number.

#Create an array of size 20 using random elements
RANDOM=$$
for i in $(seq 0 19)
do
        randomArray2[i]=$(($RANDOM%100))
done

#Print the original array
echo "Original Array:" ${randomArray2[@]}

#Use two for loops to sort the array
for i in $(seq 0 19)
do
for ((j=((i+1)); j<=19; j++))
do
        #Determine if two elements should be swapped
        if [ ${randomArray2[i]} -lt ${randomArray2[j]} ]
        then
                temp=${randomArray2[i]}
                randomArray2[i]=${randomArray2[j]}
                randomArray2[j]=$temp
        fi
done
done

#Print the sorted array
echo "Sorted Array(high to low):" ${randomArray2[@]}
echo " "


#Problem 3: This script creates an array with numbers 1 to 50.

#Create the array using a for loop
for i in $(seq 50)
do
	array3[i]=$i
done

#Print the array
echo "Array with numbers 1 to 50:"
echo ${array3[@]}
echo " "


#Problem 4: This script uses two functions to find all the prime numbers
#from 1 to 50 and the summation of these numbers. The array from Problem
#3 is used to store all numbers from 1 to 50.

#function to find all prime numbers from 1 to 50
primeNumbersFunction()
{
arr=("$@")

for k in ${arr[@]}
do
    if [ $k -gt 1 ]
    then
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
    fi
done
}

#function to find the summation of the prime numbers
summationFunction()
{
arr=("$@")
sum=0

for k in ${arr[@]}
do
    if [ $k -gt 1 ]
    then
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
        let sum+=k
    fi
    let k++
    fi
done

#Print the summation
echo $sum
}

#Find the prime numbers
echo "Prime Numbers from 1 to 50:"
primeNumbersFunction "${array3[@]}"
echo " "

#Find the summation of the prime numbers
echo "Summation of Prime Numbers:"
summationFunction "${array3[@]}"
echo " "


#Problem 5: This script creates two arrays, with one holding odd numbers
#from 1 to 50 and the other holding even numbers from 1 to 50. Then, the
#summation of each array is found.

#Create an array holding odd numbers from 1 to 50
i=0
for j in $(seq 1 2 50)
do
	let oddArr[i]=j
	let i++
done

#Print the odd array
echo "Odd numbers:" ${oddArr[@]}

#Find the summation of all odd numbers from 1 to 50
sumOdd=0
for i in ${oddArr[@]}
do
	let sumOdd+=i
done

#Print the summation of odd numbers
echo "Summation of odd numbers:" $sumOdd

#Create an array holding even numbers from 1 to 50
i=0
for j in $(seq 2 2 50)
do
	let evenArr[i]=j
	let i++
done

#Print the even array
echo "Even numbers:" ${evenArr[@]}

#Find the summation of all even numbers from 1 to 50
sumEven=0
for i in ${evenArr[@]}
do
	let sumEven+=i
done

#Print the summation of even numbers
echo "Summation of even numbers:" $sumEven
echo " "
