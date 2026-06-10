#1 Largest, Smallest and Second Largest

nums=[int(input("Enter number: ")) for _ in range(10)]
nums.sort()
print("Largest:", nums[-1])
print("Smallest:", nums[0])
print("Second Largest:", nums[-2])


#2 Count vowels, consonants, digits, special characters
s=input("Enter string: ")
v=c=d=sp=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v+=1
        else:
            c+=1
    elif ch.isdigit():
        d+=1
    else:
        sp+=1
print(v,c,d,sp)


#3 Armstrong Number
n=int(input("Enter number: "))
p=len(str(n))
temp=n
s=0
while temp>0:
    digit=temp%10
    s+=digit**p
    temp//=10
print("Armstrong" if s==n else "Not Armstrong")


#4 Duplicate elements and frequency in tuple
t=(1,2,2,3,3,3,3,4,4,4,5)
for i in set(t):
    if t.count(i)>1:
        print(i, t.count(i))


#5 Topper from tuple
students=(("Aman",85),("Riya",92),("Karan",88))
topper=max(students,key=lambda x:x[1])
print("Topper:", topper[0], topper[1])


#6  Word frequency using dictionary
s=input("Enter sentence: ")
freq={}
for w in s.split():
    freq[w]=freq.get(w,0)+1
print(freq)


#7 Students above average marks
marks={"Aman":80,"Riya":95,"Karan":70,"Neha":85}
avg=sum(marks.values())/len(marks)
for name,m in marks.items():
    if m>avg:
        print(name,m)



#8  Menu-driven Product Management
products={}
while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    ch=int(input())
    if ch==1:
        products[input("Product: ")]=float(input("Price: "))
    elif ch==2:
        print(products)
    elif ch==3:
        products.pop(input("Product to delete: "),None)
    else:
        break        

        

#9  Triangle Type
a,b,c=map(int,input("Enter sides: ").split())
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")



#10 Student Management System
students={}
while True:
    print("1.Add 2.View 3.Search 4.Exit")
    ch=int(input())
    if ch==1:
        roll=input("Roll No: ")
        students[roll]=(input("Name: "),float(input("Marks: ")))
    elif ch==2:
        for r,d in students.items():
            print(r,d)
    elif ch==3:
        r=input("Roll No: ")
        print(students.get(r,"Not Found"))
    else:
        break