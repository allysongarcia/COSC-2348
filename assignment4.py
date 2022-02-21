'''
Assignment 4
Author: Allyson Garcia
Date: 02/20/2022
'''

'''
Problem 1: This program uses the Employee class and a dictionary to create an
employee management system. First, the program checks if a pickled dictionary is
avaiable in a file. If not, then a new empty dictionary is created. A menu is
displayed to the user with five different options. Each option allows the user
to view a certain employee's information or make changes to the dictionary. After
each selection, the user is asked to make another selection until the number 5
is entered. At the end of the program, the final dictionary is pickled and saved
to a file.
'''
import pickle
import os.path

#Employee class
class Employee():
    #Initialize data attributes
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    #Method used to print information for each employee
    def display(self):
        print("Name:",self.__name)
        print("ID Number:",self.__id_number)
        print("Department:",self.__department)
        print("Job Title:", self.__job_title, "\n")

#Main Function
def main():
    #Unpickle the dictionary if the file exists. Otherwise, create an empty dictionary
    exists = os.path.exists('employee_dict.dat')
    if exists:
        #Unpickle the file
        input_file = open('employee_dict.dat', 'rb')
        employee_dict = pickle.load(input_file)
    else:
        #Create an empty dictionary
        employee_dict = {}

    #Print the menu to the user
    print("Welcome to the Employee Management System!\nPlease make a selection from the following menu:\n")
    print("1. Look up an employee\n2. Add an employee")
    print("3. Change an existing employee's name, department, and job title")
    print("4. Delete an employee from the system\n5. Quit the program\n")

    #Get a menu selection from the user
    user_input = int(input("Enter the number associated with your menu selection: "))
    print()

    #Use a loop and if/elif/else statements to perform certain tasks based on
    #the user's selection. Also prompt the user to enter another input.
    while user_input != 5:
        #Look for employee in the dictionary
        if user_input == 1:
            emp_id = int(input("Enter the ID of the employee: "))
            if emp_id in employee_dict:
                #Display the employee's information
                employee_dict[emp_id].display()
            #Input validation
            else:
                print("The entered ID is not in the system.\n")
        #Add employee to the dictionary
        elif user_input == 2:
            emp_name = input("Enter the employee's name: ")
            emp_id = int(input("Enter the employee's ID: "))
            emp_depart = input("Enter the employee's department: ")
            emp_title = input("Enter the employee's job title: ")
            if emp_id in employee_dict:
                print("There is already an employee with the given ID.\n")
            else:
                employee_dict[emp_id] = Employee(emp_name, emp_id, emp_depart, emp_title)
                print("The employee has been added to the system.\n")
        #Change an employee's information
        elif user_input == 3:
            emp_id = int(input("Enter the ID of the employee: "))
            if emp_id in employee_dict:
                emp_name = input("Change the employee's name: ")
                emp_depart = input("Change the employee's department: ")
                emp_title = input("Change the employee's job title: ")
                employee_dict[emp_id] = Employee(emp_name, emp_id, emp_depart, emp_title)
                print("The employee's information has successfully been changed.\n")
            #Input validation
            else:
                print("The entered ID is not in the system.\n")
        #Delete employee from the dictionary
        elif user_input == 4:
            emp_id = int(input("Enter the ID of the employee: "))
            if emp_id in employee_dict:
                del employee_dict[emp_id]
                print("The employee has been deleted from the system.\n")
            #Input validation (ID is not in dictionary and therefore can't be deleted)
            else:
                print("The entered ID is not in the system.\n")
        #Input validation (user entered an invalid menu option)
        else:
            print("Invalid input. Please try again.\n")
        #Ask user to make another selection from the menu
        user_input = int(input("Select another option from the menu: "))
        print()

    #Pickle the dictionary
    output_file = open('employee_dict.dat', 'wb')
    pickle.dump(employee_dict, output_file)
    output_file.close()

    #User wants to exit the program
    if user_input == 5:
        print("Exiting the program.\n")

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 2: This program asks the user to enter twenty numbers and then stores
them into a list. Then, the program finds the largest/smallest number in the
list, the total of the numbers in the list, and the average of the list. This
information is then displayed to the user.
'''
def main():
    #List to store the user's numbers
    number_list = []

    #Append entered numbers into the list
    print("Enter a total of 20 numbers.\n")
    for num in range(0,20):
        number_list.append(float(input("Enter a number: ")))

    #Define variables
    list_sum = 0
    largest_num = number_list[0]
    smallest_num = number_list[0]

    #Use a loop to calculate the sum and determine the largest/smallest number
    for temp in number_list:
        list_sum += temp
        if temp > largest_num:
            largest_num = temp
        if temp < smallest_num:
            smallest_num = temp

    #Print information to the user
    print("\nLargest number in the list:", largest_num)
    print("Smallest number in the list:", smallest_num)
    print("Total of the numbers in the list:", list_sum)
    print("Average of the numbers in the list:", list_sum/20)


#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 3: This program first asks the user to enter a value to be used as the
range of the dictionary. Then, the program uses a for loop to generate the
dictionary, in which x is used as the key and x*x is the value. Then, the
dictionary is displayed.
'''
def main():
    #Ask the user to enter a value
    n = int(input("\nEnter a number: "))

    #Create an empty dictionary
    num_dict = {}

    #Use a for loop to generate the dictionary
    for x in range(1, n+1):
        num_dict[x] = x*x

    #Print the dictionary
    print(num_dict)
    print()

#Execute main function
if __name__ == '__main__':
    main()

'''
Problem 4: This program first generates a random list of 100 numbers, with each
number ranging from 0 to 20. Then, the find_second_largest() function is called
in order to find and return the second largest value in the list. Finally,
repeating elements are removed from the list. The original list, the second
largest number, and the new set of numbers are displayed to the user.
'''
import random

#Function to find the second largest number in the list
def find_second_largest(random_list):
    #Initialize variables with the first two numbers in the list
    largest, second_largest = random_list[0], random_list[1]
    #Swap the two variables if necessary
    if largest < second_largest:
        largest, second_largest = second_largest, largest
    #Use for loop to determine the largest and second largest number in the list
    for temp in range (2, 100):
        if random_list[temp] > largest:
            largest, second_largest = random_list[temp], largest
        elif random_list[temp] > second_largest and random_list[temp] != largest:
            second_largest = random_list[temp]
    #Return the second largest number
    return second_largest

#Main function
def main():
    #Generate a random list of size 100 with numbers from 0 to 20
    random_list = []
    for temp in range(0,100):
        number = random.randint(0,20)
        random_list.append(number)

    #Display the random list
    print("The randomly generated list is:", random_list, "\n")

    #Find and display the second largest number in the list
    print("The second largest number in the list is:", find_second_largest(random_list), "\n")

    #Remove duplicates from the list by using set(). Then display the new list
    random_list = set(random_list)
    print("The new list with no duplicates is:", random_list)

#Execute main function
if __name__ == '__main__':
    main()
