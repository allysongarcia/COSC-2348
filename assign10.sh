#!/bin/bash
<<com
Assignment 10
Author: Allyson Garcia
Date: 4/26/2022
com

#Problem 1: This script finds the summation of the numbers in a file by using a
#recursive function. First, the numbers in the file are put in an array. Then, the
#recursive function is called to add up the numbers in the array and return the sum.
summationFunction()
{
    i=$1
    if [ $1 -lt 0 ]
    then
    	return
    else
    	let sum+=${numArr[i]}
    	let i--
    	summationFunction $i
    	return $sum
    fi
}

#Starting index for the array
i=0

#Array that will hold the numbers in the file
numArr=()

#Read the file and put the values into the array
file1="num.txt"
while read line
do
	let numArr[i]+=line
	let i++
done < $file1

#Pass the index of the last value in the array to the function
let i--
summationFunction $i

#Store the return value from the function and print it
summation=$?
echo "Summation:" $summation
echo " "


#Problem 2: This script uses a recursive function to find the fibonacci
#sequence up to the number entered by the user.
fibonacciFunction()
{
num=$1
#Base Case
if [ $num -le 2 ]
then
	echo 1
#General Case
else
	let temp1=num-1
	let temp2=num-2
	echo $(( $(fibonacciFunction $temp1) + $(fibonacciFunction $temp2) ))
fi
}

#Ask the user to enter a number
read -p "Enter a number: " num

#Create an array to store the fibonacci series
fibonacciSeq=()

#Variable to keep track of the array index
j=0

#Use a for loop to repeatedly call the recursive function and find the fibonacci sequence
for i in $(seq 1 $num)
do
	fibonacciSeq[j]+=$(fibonacciFunction $i)
	let j++
done

#Display the fibonacci sequence
echo "First" $num "numbers in the fibonacci series:" ${fibonacciSeq[@]}
echo " "


#Problem 3: This script appends the output from problems 1 and 2 to a file. The output from
#problem 1 is stored in the variable summation, and the output from problem 2 is stored in the
#array fibonacciSeq.
file="output.txt"
echo "Writing the output for problems 1 and 2 to" $file "..."

#Append the output from problem 1 to the file
echo $summation >> $file

#Append the output from problem 2 to the file
echo ${fibonacciSeq[@]} >> $file
echo " "


#Problem 4: This script uses a recursive function to sort an array
#of random values. Then, the sorted array is written to a file.
recursiveSort()
{
n=$1
#Base Case
if [ $n -le 1 ]
then
	return
#General Case
else
	let n--
	for i in $(seq 0 $n)
	do
		#Put the values in order
		if [ ${randomArray[i]} -gt ${randomArray[n]} ]
		then
			temp=${randomArray[n]}
			randomArray[n]=${randomArray[i]}
			randomArray[i]=$temp
		fi
	done
fi
#Call the function from itself
recursiveSort $n
}

#Create an array of 10 random values
RANDOM=$$
for i in $(seq 0 9)
do
	randomArray[i]=$(($RANDOM%50))
done

#Print the original array
echo "Original Array:"
echo ${randomArray[@]}

#Call the function to sort the array
recursiveSort "${#randomArray[@]}"

#Write the sorted array to a file
echo "Writing sorted array to a file..."
filename="numbers.txt"
echo ${randomArray[@]} > $filename
