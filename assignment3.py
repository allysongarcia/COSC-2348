'''
Assignment 3
Name: Allyson Garcia
Date: 02/15/2022
'''

'''
Problem 1: First, a class named "Car" is created with three private data
attributes and three methods. The accleration() and brake() methods are used to
increase and decrease the car's speed, respectively. The get_speed() method
returns the car's current speed. Then, the program creates a Car object and
calls the acceleration() and brake() methods five times each in order to change
the car's speed accordingly. After each call, the car's current speed is
displayed.
'''
#Car class
class Car():
    #Initialize data attributes
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    #Increase the car speed by 5
    def acceleration(self):
        self.__speed += 5
    #Decrease the car speed by 5
    def brake(self):
        self.__speed -= 5
    #Return car speed
    def get_speed(self):
        return self.__speed

#Main Function
def main():
    #Create car object
    my_car = Car("2013 Durango", "Dodge")

    #Increase the car speed five times
    print("Accelerating:")
    for temp in range (0,5):
        my_car.acceleration()
        print(my_car.get_speed())

    #Decrease the car speed 5 times
    print("\nBraking:")
    for temp in range(0,5):
        my_car.brake()
        print(my_car.get_speed())

    print()

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 2: First, a class called Employee is created to store 4 types of
information: name, id number, department, and job title. The class also has a
method that is used to display the information. Next, the program creates three
Employee objects to store information for three different employees. Then,
the aforementioned method is used to display the information for each employee.
'''
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
    #Create three Employee objects
    employee_1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    #Display information for each employee
    employee_1.display()
    employee_2.display()
    employee_3.display()

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 3: The Employee class is used to store the full name and email of an
employee. The full name is formed by joining the first and last names with a
space in between. The email is formed by joining the first and last names
without a space, adding "@company.com" to the end, and ensuring that the
entire email is lowercase. In the program, two employee objects are created in
order to demonstrate how the class creates the full_name and email data
attributes. This information is then displayed using the display_info() method.
'''
#Employee class
class Employee():
    #Initialize data attributes
    def __init__(self, first_name, last_name):
        #Create full_name by adding together first and last name
        self.__full_name = first_name + " " + last_name
        #Create email by combining first/last name and another string
        self.__email = first_name + last_name + "@company.com"
        #Make email address fully lowercase
        self.__email = self.__email.lower()
    #Create method to display the information
    def display_info(self):
        print("Full Name:", self.__full_name)
        print("Email:", self.__email, "\n")

#Main Function
def main():
    #Create two Employee objects to demonstrate the class
    employee_one = Employee("Allyson", "Garcia")
    employee_two = Employee("Joy","Rogers")
    #Print the full name and email for each of the Employee objects
    employee_one.display_info()
    employee_two.display_info()

#Execute main function
if __name__ == '__main__':
    main()


'''
Problem 4: This program creates 25 Student objects in order to store the
student's name and their grades for 6 courses. The program creates a list with
these objects and then determines the average of each student. The program also
sorts the students based on their average and displays this list. Additionally,
the average grade of each course is displayed.
'''
#Student class
class Student():
    #Initialize data attributes for each student
    def __init__(self, name, course_1, course_2, course_3, course_4, course_5, course_6):
        self.__name = name
        self.__course_1 = course_1
        self.__course_2 = course_2
        self.__course_3 = course_3
        self.__course_4 = course_4
        self.__course_5 = course_5
        self.__course_6 = course_6
    #Used to calculate average of each student
    def student_average(self):
        self.average = (self.__course_1 + self.__course_2 + self.__course_3 +
        self.__course_4 + self.__course_5 + self.__course_6)/600
    #Print each student's name and average
    def print_average(self):
        print(self.__name, ":", self.average)
    #Return average of course 1
    def course_average_1(self, ave_1):
        ave_1 += self.__course_1
        return ave_1
    #Return average of course 2
    def course_average_2(self, ave_2):
        ave_2 += self.__course_2
        return ave_2
    #Return average of course 3
    def course_average_3(self, ave_3):
        ave_3 += self.__course_3
        return ave_3
    #Return average of course 4
    def course_average_4(self, ave_4):
        ave_4 += self.__course_4
        return ave_4
    #Return average of course 5
    def course_average_5(self, ave_5):
        ave_5 += self.__course_5
        return ave_5
    #Return average of course 6
    def course_average_6(self,ave_6):
        ave_6 += self.__course_6
        return ave_6

#Main Function
def main():
    #Define variables to help calculate the average of each course
    ave_1, ave_2, ave_3, ave_4, ave_5, ave_6 = 0, 0, 0, 0, 0, 0

    #Create an array of 25 objects in order to store data for each student
    student_list = []
    student_list.append(Student("Ally", 95, 100, 91, 98, 89, 99))
    student_list.append(Student("Sam", 85, 89, 87, 84, 77, 87))
    student_list.append(Student("Ashley", 98, 89, 96, 95, 82, 85))
    student_list.append(Student("Brittney", 81, 78, 85, 83, 88, 84))
    student_list.append(Student("Carol", 44, 52, 56, 78, 75, 80))
    student_list.append(Student("Daria", 70, 74, 72, 80, 84, 79))
    student_list.append(Student("Erica", 20, 45, 63, 55, 49, 66))
    student_list.append(Student("Flynn", 87, 81, 82, 83, 84, 81))
    student_list.append(Student("Maya", 88, 87, 86, 89, 92, 93))
    student_list.append(Student("Kate", 78, 88, 69, 77, 77, 84))
    student_list.append(Student("Taylor", 66, 68, 72, 77, 71, 70))
    student_list.append(Student("Margaret", 94, 92, 93, 90, 88, 89))
    student_list.append(Student("Nathan", 92, 96, 98, 93, 95, 89))
    student_list.append(Student("Karen", 78, 80, 82, 84, 86, 88))
    student_list.append(Student("Pat", 55, 54, 57, 59, 58, 57))
    student_list.append(Student("Willow", 77, 65, 55, 81, 78, 67))
    student_list.append(Student("Matthew", 90, 92, 90, 90, 92, 98))
    student_list.append(Student("Jonathan", 77, 80, 81, 79, 78, 83))
    student_list.append(Student("Ethan", 90, 92, 89, 80, 89, 90))
    student_list.append(Student("Jennifer", 84, 87, 88, 81, 70, 84))
    student_list.append(Student("Patrick", 42, 50, 51, 49, 50, 51))
    student_list.append(Student("Sally", 20, 33, 43, 30, 53, 43))
    student_list.append(Student("John", 60, 61, 63, 64, 68, 70))
    student_list.append(Student("Jane", 84, 70, 65, 70, 78, 73))
    student_list.append(Student("Sarah", 66, 79, 60, 67, 72, 79))

    #Find the average for each student
    for temp in student_list:
        temp.student_average()

    #Sort the students by grade average
    print("\nStudents sorted by average (highest to lowest):")
    for temp in range(0,25):
        for temp2 in range(temp + 1, 25):
            if student_list[temp].average < student_list[temp2].average:
                student_list[temp], student_list[temp2] = student_list[temp2], student_list[temp]

    #Print sorted list of students
    for temp in student_list:
        temp.print_average()

    #Add up the grades for each class, will be used to calculate the average
    for temp in student_list:
        ave_1 = temp.course_average_1(ave_1)
        ave_2 = temp.course_average_2(ave_2)
        ave_3 = temp.course_average_3(ave_3)
        ave_4 = temp.course_average_4(ave_4)
        ave_5 = temp.course_average_5(ave_5)
        ave_6 = temp.course_average_6(ave_6)

    #Display the average grade of each course
    print("\nAverage of Course 1:",ave_1/2500)
    print("Average of Course 2:",ave_2/2500)
    print("Average of Course 3:",ave_3/2500)
    print("Average of Course 4:",ave_4/2500)
    print("Average of Course 5:",ave_5/2500)
    print("Average of Course 6:",ave_6/2500)

#Execute Main Function
if __name__ == "__main__":
    main()
