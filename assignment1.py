#1 string operations
name = "Sunil is fine"
print("First character:", name[0])
print("Last character:", name[-1])
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Reverse:", name[::-1])


#2 string slicing
s = "datasciencecourse"
print("First four characters:", s[:4])
print("Characters from index 2 to 5:", s[2:6])
print("Reverse string:", s[::-1])


#3 list operations
numbers = [10, 20, 30, 40]
print(numbers.append(50), numbers)
print(numbers.insert(2, 25), numbers)
print(numbers.remove(30), numbers)
print(numbers.pop())
print(numbers.reverse(), numbers)
print(numbers.sort())
print("Length:", len(numbers), numbers)
print("Count of 20:", numbers.count(20))


#4 Tuple Operations
subjects = ("Maths", "Physics", "Chemistry", "English", "Computer")
print(subjects[0])
print(subjects[-1])
print(len(subjects))
print(subjects[1:4])
nums = (10, 20, 30, 40, 50)
print(max(nums))
print(min(nums))
print(sum(nums))


#5 Tuple Packing and Unpacking
student = ("Void", 20, "CSE", "Jaipur")
name, age, course, city = student
print(name)
print(age)
print(course)
print(city)


#6 Dictionary Operations
student_1 = {
    "Name": "Void",
    "Age": 20,
    "Course": "CSE",
    "Address": "Jaipur"
}
print(student_1.keys())
print(student_1.values())
print(student_1.items())
student_1["Address"] = "Rajasthan"
student_1["Branch"] = "AI & ML"


#7 Access Nested List Element
lst = [1, 2, 3, 4, [2, 5], 7]
print(lst[4][1])


#8 += Operator
num = int(input("Enter a number: "))
num += 10
print("Updated value:", num)


#9 Type Casting
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Multiplication:", a * b)

 
#10 Dictionary Methods
data = {
    "Name": "Void",
    "Age": 20,
    "City": "Jaipur"
}
print(data.get("Name"))
print(data.keys())
print(data.values())
print(data.items())


#11 Copy a List
original = [10, 20, 30, 40]
copied = original.copy()
print("Original:", original)
print("Copied:", copied)
