'''
Assignment 6
Author: Allyson Garcia
Date: 03/08/2022
'''

'''
Problem 1:This program uses regular expressions to extract certain information
from a file and store the info in a class object for each student. Then, a list
of 25 other students is appended to the original file. Finally, all of the
students (35 total) are sorted by first name and saved in a new file.
'''
#Used for regular expressions
import re

#Student class
class Student():
    def __init__(self, firstname, lastname, email, courses):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__all_course = courses
    #Accessor Methods
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_email(self):
        return self.__email
    def get_all_course(self):
        return self.__all_course

#Main function
def main():
    #List to store Student objects
    student_list = []

    #Open the file and find the data to store in each class object
    infile = open('students.txt', 'r')
    #Skip the title line of the file
    infile.readline()
    for line in infile:
        info = line
        #Find the first name using regular expressions and convert it into a string
        f = re.findall('^[A-Z]+[a-z]+', info)
        firstname = ""
        for temp in f: firstname += temp
        #Find the last name using regular expressions and convert it into a string
        l = re.findall('\s[A-Z]+[a-z]+', info)
        lastname = ""
        for temp in l: lastname += temp
        lastname = lastname.lstrip() #Get rid of space at front of lastname
        #Find the email using regular expressions and convert it into a string
        e = re.findall('[a-z]+@islander.tamucc.edu', info)
        email = ""
        for temp in e: email += temp
        #Find the course scores using regular expressions and convert each value into an integer
        courses = re.findall('\d+', info)
        courses = [int(i) for i in courses]
        #Create a new class object with the info from the file
        student_list.append(Student(firstname, lastname, email, courses))
    #Close the file
    infile.close()

    #List of 25 students from previous assignment
    student_info = []
    student_info.append(Student("Ally", "Garcia", "agarcia@islander.tamucc.edu", [95, 100, 91, 98, 89, 99]))
    student_info.append(Student("Sam", "Miller", "smiller@islander.tamucc.edu", [85, 89, 87, 84, 77, 87]))
    student_info.append(Student("Ashley", "Garcia", "agarcia@islander.tamucc.edu", [98, 89, 96, 95, 82, 85]))
    student_info.append(Student("Brittney", "Harris", "bharris@islander.tamucc.edu", [81, 78, 85, 83, 88, 84]))
    student_info.append(Student("Carol", "Davis", "cdavis@islander.tamucc.edu", [44, 52, 56, 78, 75, 80]))
    student_info.append(Student("Daria", "Brown", "dbrown@islander.tamucc.edu", [70, 74, 72, 80, 84, 79]))
    student_info.append(Student("Erica", "Smith", "esmith@islander.tamucc.edu", [20, 45, 63, 55, 49, 66]))
    student_info.append(Student("Flynn", "Jones", "fjones@islander.tamucc.edu", [87, 81, 82, 83, 84, 81]))
    student_info.append(Student("Maya", "Williams", "mwilliams@islander.tamucc.edu", [88, 87, 86, 89, 92, 93]))
    student_info.append(Student("Kate", "Johnson", "kjohnson@islander.tamucc.edu", [78, 88, 69, 77, 77, 84]))
    student_info.append(Student("Taylor", "Martin", "tmartin@islander.tamucc.edu", [66, 68, 72, 77, 71, 70]))
    student_info.append(Student("Margaret", "Harris", "mharris@islander.tamucc.edu", [94, 92, 93, 90, 88, 89]))
    student_info.append(Student("Nathan", "Moore", "nmoore@islander.tamucc.edu", [92, 96, 98, 93, 95, 89]))
    student_info.append(Student("Karen", "Garcia", "kgarcia@islander.tamucc.edu", [78, 80, 82, 84, 86, 88]))
    student_info.append(Student("Pat", "Murphy", "pmurphy@islander.tamucc.edu", [55, 54, 57, 59, 58, 57]))
    student_info.append(Student("Willow", "Flores", "wflores@islander.tamucc.edu", [77, 65, 55, 81, 78, 67]))
    student_info.append(Student("Matthew", "Flores", "mflores@islander.tamucc.edu", [90, 92, 90, 90, 92, 98]))
    student_info.append(Student("Jonathan", "Wilson", "jwilson@islander.tamucc.edu", [77, 80, 81, 79, 78, 83]))
    student_info.append(Student("Ethan", "Taylor", "etaylor@islander.tamucc.edu", [90, 92, 89, 80, 89, 90]))
    student_info.append(Student("Jennifer", "Lee", "jlee@islander.tamucc.edu", [84, 87, 88, 81, 70, 84]))
    student_info.append(Student("Patrick", "White", "pwhite@islander.tamucc.edu", [42, 50, 51, 49, 50, 51]))
    student_info.append(Student("Sally", "Thompson", "sthompson@islander.tamucc.edu", [20, 33, 43, 30, 53, 43]))
    student_info.append(Student("John", "Taylor", "jtaylor@islander.tamucc.edu", [60, 61, 63, 64, 68, 70]))
    student_info.append(Student("Jane", "Lewis", "jlewis@islander.tamucc.edu", [84, 70, 65, 70, 78, 73]))
    student_info.append(Student("Sarah", "Allen", "sallen@islander.tamucc.edu", [66, 79, 60, 67, 72, 79]))

    #Append 25 students to the file
    outfile = open('students.txt', 'a')
    for i in range(0, len(student_info)):
        outfile.write(student_info[i].get_firstname()+" "+student_info[i].get_lastname()+" "+student_info[i].get_email()+" ")
        all_course = student_info[i].get_all_course()
        for t in range(0, 6):
            score = str(all_course[t])
            outfile.write(score)
            if t < 5: outfile.write(",")
        outfile.write("\n")
    outfile.close()

    #Concatenate the two lists and sort the students by first name
    students = student_list + student_info
    students.sort(key=lambda x: x.get_firstname())

    #Write all of the students to a new file
    new_file = open('sorted.txt', 'w')
    for i in range(0, len(students)):
        new_file.write(students[i].get_firstname()+" "+students[i].get_lastname()+" "+students[i].get_email()+" ")
        #Write each score to the file
        all_course = students[i].get_all_course()
        for t in range(0,6):
            num = str(all_course[t])
            new_file.write(num)
            if t < 5: new_file.write(",")
        #Move to the next line
        new_file.write("\n")
    #Close the new file
    new_file.close()

#Execute main function
if __name__ == "__main__":
    main()


'''
Problem 2: This program reads n files and writes their contents into a single
file. First, the program uses exceptions to catch the error in case one or more
of the files doesn't exist. For each file that does exist, two functions are
used to read the contents and write them to the new file. Then, the contents of
the resulting new file are printed to the user.
'''
#Method used to read the contents from a file
def read_file(file):
    infile = open(file, 'r')
    file_contents = infile.read()
    infile.close()
    return file_contents

#Method used to write file contents to the final file
def write_file(file_contents):
    outfile = open('final_file.txt', 'a')
    outfile.write(file_contents)
    outfile.close()

#Main Function
def main():
    #Ask the user how many files (use for variable n)
    n = int(input("How many files would you like to write into a single file? "))

    #Validate the user's input
    while n <= 0:
        n = int(input("Invalid input. How many files you would like to write into a single file? "))

    #Try to write the contents from the given number of files to a new file
    print("\nNow writing contents from", n, "files to final_file.txt")
    for i in range(1,n+1):
        #File name(follows the pattern f1.txt, f2.txt...fn.txt)
        file = 'f%d.txt' % i
        #If file exists, read the file and write its contents to the final file
        try:
            #Call a method to read the file
            file_contents = read_file(file)
            #Call another method to write the file contents to the final file
            write_file(file_contents)
            #Tell the user that the file's contents have been written to the new file
            print("Contents from", file, "have been written to final_file.txt")
        #If file does not exits, print an appropriate message
        except FileNotFoundError:
            print(file, "does not exist")

    #Read the contents from final_file.txt to make sure that the contents have
    #successfully been written to it
    print("\nHere are the contents from final_file.txt:\n")
    #Open the file
    inputfile = open('final_file.txt', 'r')
    #Read the file
    final_file_contents = inputfile.read()
    #Print the file contents
    print(final_file_contents)
    #Close the file
    inputfile.close()

#Execute main function
if __name__ == "__main__":
    main()
