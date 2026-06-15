#1  Prime Numbers
l = [2, 3, 4, 5, 6, 7]
for n in l:
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n)


#2 Multiplication Table Matrix  
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()


#3 Even Count and Odd Sum     
def fun(l):
    even = 0
    oddsum = 0
    for i in l:
        if i % 2 == 0:
            even += 1
        else:
            oddsum += i
    print("Even =", even)
    print("Odd Sum =", oddsum)+
fun([1,2,3,4,5])


#4  Simple Interest
def si(p, r=5, t=2):
    print((p*r*t)/100)
si(1000)
si(p=1000, r=10, t=3)


#5 Create a Student class with attributes
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

name = input("Enter student name: ")
marks = int(input("Enter marks: "))
student = Student(name, marks)
print("Name:", student.name)
print("Marks:", student.marks)
print("Grade:", student.calculate_grade())


#6 Create at least two objects and display their grades. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"
student1 = Student("Rahul", 85)
student2 = Student("Priya", 45)
print(student1.name, "Grade:", student1.calculate_grade())
print(student2.name, "Grade:", student2.calculate_grade())


#7  Bank Account
class Bank:
    def __init__(self):
        self.__balance = 1000
    def deposit(self, a):
        self.__balance += a
    def withdraw(self, a):
        self.__balance -= a
    def show(self):
        print(self.__balance)
b = Bank()
b.deposit(500)
b.withdraw(200)
b.show()

#8 Exception Handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")


#9 File Handling
f = open("student.txt", "w")
f.write("Aman 80")
f.close()
f = open("student.txt", "r")
print(f.read())
f.close()


#10 Total and Average from File
try:
    f = open("num.txt", "r")
    total = 0
    count = 0
    for i in f:
        total += int(i)
        count += 1
    print("Total =", total)
    print("Average =", total/count)
except FileNotFoundError:
    print("File not found")
