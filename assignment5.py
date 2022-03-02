'''
Assignment 5
Author: Allyson Garcia
Date: 03/01/2022
'''

'''
Problem 1: This program uses a dictionary to store the Morse Code representations
of each letter, each number, and various punctuation characters. First, the
program asks the user to enter a string to be converted into Morse Code. The
program converts any lowercase letters in the string into uppercase. Then, the
program uses a loop to convert each character of the string into Morse Code using
the dictionary. The converted string is finally displayed to the user.
'''
#Main function
def main():
    #Create a dictionary storing the morse code conversions
    morse_code = {',':'--..--', '.':'.-.-.-', '?':'..--..', '0':'-----',
                  '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                  '6':'-....', '7':'--...', '8':'---..', '9':'----.', 'A':'.-',
                  'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
                  'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                  'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                  'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
                  'X':'-..-', 'Y':'-.-', 'Z':'--..', ' ':' '}

    #Ask the user to enter a string to be converted into Morse Code
    input_string = input("Enter a string: ")
    #Create a second string to hold the converted string
    converted_string = ""
    #Make any lowercase letters in the string uppercase
    input_string2 = input_string.upper()

    #Use a loop to convert each character of the string into its Morse Code equivalent
    for ch in input_string2:
        converted_string += morse_code[ch]

    #Display the Morse Code
    print(converted_string)

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 2: This program gets a string from the user and then uses two functions
to determine the number of vowels and consonants in the string. These numbers
are then displayed to the user.
'''
#Function to count the number of vowels in the string
def num_vowels(str_input):
    #convert entire string into lowercase
    str_input2 = str_input.lower()
    #initialize counter at 0
    counter = 0
    #use a loop to count the number of vowels
    for ch in str_input2:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            counter += 1
    #return final number of vowels to the main function
    return counter

#Function to count the number of consonants in the string
def num_consonants(str_input):
    #convert entire string into lowercase
    str_input2 = str_input.lower()
    #initialize counter at 0
    counter2 = 0
    #create a list to store all consonants
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
                      'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    #use a loop to count the consonants in the string
    for ch in str_input2:
        if ch in consonant_list:
            counter2 += 1
    #return final number of consonants to the main function
    return counter2

#Main function
def main():
    #Ask the user to enter a string
    str_input = input("\nEnter a string: ")

    #Call the two functions to find the number of vowels/consonants in the string
    vowels = num_vowels(str_input)
    consonants = num_consonants(str_input)

    #Dislay the number of vowels and consonants
    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 3: This program performs tasks on 4 different strings. For part 1, a loop
is used to determine if each character in the string is a letter, digit, or
symbol. In part 2, the special characters and punctuation are removed from the
string. For part 3, the dashes in the string are replaced with spaces. For part
4, the consonants are removed from the string.
'''
#Main function
def main():
    #**********Part 1**********
    #original string
    str1 = "P@#yn26at^&i5ve"
    #initialize variables to 0
    letters = 0
    digits = 0
    symbols = 0
    #use a loop to determine if each character is a letter, digit, or symbol
    for ch in str1:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    #print the number of letters, digits, and symbols
    print("\nNumber of letters:", letters)
    print("Number of digits:", digits)
    print("Number of symbols:", symbols)

    #**********Part 2**********
    #Original string
    str1 = "/*Jon is @developer & musician"
    #Create a new string
    new_str = ""
    #Use a loop to create the new string without special characters
    for ch in str1:
        if ch.isalpha() or ch.isspace():
            new_str += ch
    #Print the new string
    print(new_str)

    #**********Part 3**********
    #Original string
    str1 = "Emma-is-a-data-scientist"
    #Create new string
    new_str = ""
    #Use a loop to replace dashes with a space
    for ch in str1:
        if ch == "-":
            new_str += " "
        else:
            new_str += ch
    #Print the new string
    print(new_str)

    #**********Part 4**********
    #Original string
    str1 = "Hello, have a good day"
    #Create a new string
    new_str = ""
    #Use a loop to create the new string without consonants
    for ch in str1:
        if ch not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            new_str += ch
    #Print the new string
    print(new_str)

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 4: This program solves the two problems given in the assignment. For
part 1, a list of integers is created, and the average, median, and standard
deviation are calculated and displayed. For part 2, a new list is created to
store the division of elements. Exception handling is used in case the program
tries to divide by zero. The division of elements (with "N/A" being used for
instances in which the program tried dividing by zero) is then displayed.
'''
#Main function
def main():
    #**********Part 1**********
    #Ask the user to enter a value for n (size of the list)
    n = int(input("\nHow many integers would you like to enter? "))

    #Validate the input
    while n <= 10:
        n = int(input("Invalid input. Please enter a number greater than 10: "))

    #Create a list to store integers and a variable to store the sum of the list
    list_part_1 = []
    list_1_sum = 0

    #Get integers from the user and store them in the list. Also calculate the
    #sum of the list in the process for future use.
    for num in range(0,n):
        int_input = int(input("Enter an integer from 0 to 100: "))
        while int_input < 0 or int_input > 100:
            int_input = int(input("Invalid input. Please enter a integer from 0 to 100: "))
        list_part_1.append(int_input)
        list_1_sum += int_input

    #Calulate the average of the list
    list_avg = list_1_sum/n

    #Sort the list
    for temp in range(0, n):
        for temp2 in range(temp + 1, n):
            if list_part_1[temp] > list_part_1[temp2]:
                list_part_1[temp], list_part_1[temp2] = list_part_1[temp2], list_part_1[temp]

    #Determine the median
    if n % 2 == 0:
        median_left = list_part_1[n//2]
        median_right = list_part_1[n//2 - 1]
        median = (median_left + median_right)/2
    else:
        median = list_part_1[n//2]

    #Find the standard deviation
    temp2 = 0
    for temp in list_part_1:
        temp2 += (temp-list_avg)**2
    variance = temp2 / n
    standard_dev = variance**0.5

    #Print information to the user
    print("\nOrdered List:", list_part_1)
    print("List Average:", list_avg)
    print("Median:", median)
    print("Standard Deviation:", standard_dev)
    print()

    #**********Part 2**********
    #Define a new list to store the division of elements
    list_part_2 = []

    #Use a loop to create the list of division of elements. Use exceptions in
    #case the program tries to divide by zero.
    for num in range(0,n-1):
        try:
            list_part_2.append(list_part_1[num] / list_part_1[num+1])
        except:
            list_part_2.append("N/A")

    #Print the division of elements
    print("Division of elements:")
    print(list_part_2, "\n")

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 5: This program uses loops to change the given string in four
different ways. Each converted string is displayed to the user.
'''
#Main function
def main():
    #Given string
    class_string = "this is the string for the class"

    #**********Part 1**********
    class_str1 = ""
    #Use a loop to capitalize the first letter of each word in the string
    for ch in range(0,len(class_string)):
        if ch == 0:
            class_str1 += class_string[ch].upper()
        elif class_string[ch-1].isspace():
            class_str1 += class_string[ch].upper()
        else:
            class_str1 += class_string[ch]
    #Display the new string
    print(class_str1)

    #**********Part 2**********
    class_str2 = ""
    #This loop uses the string created in part 1
    for ch in class_str1:
        #Remove the spaces between words by not adding them to the new string
        if not ch.isspace():
            class_str2 += ch
    #Display the new string
    print(class_str2)

    #**********Part 3**********
    class_str3 = ""
    for ch in range(0,len(class_string)):
        #Change each s to $
        if class_string[ch] == 's':
            class_str3 += '$'
        #Capitalize the first letter of certain words
        elif ch == 0 or ch == 5 or ch == 27:
            class_str3 += class_string[ch].upper()
        #Remove the first "the" from the string
        elif ch < 7 or ch > 10:
            class_str3 += class_string[ch]
    #Display the new string
    print(class_str3)

    #**********Part 4**********
    class_str4 = ""
    #Use a loop to capitalize the first letter of certain words
    for ch in range(0,len(class_string)):
        if ch == 0 or ch == 12 or ch == 27:
            class_str4 += class_string[ch].upper()
        else:
            class_str4 += class_string[ch]
    #Display the new string
    print(class_str4)

#Execute main function
if __name__ == '__main__':
    main()
