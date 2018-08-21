#Question 1

A=int(input("Enter a year to check if its leap year"))
if(A%4==0):
    if(year%100==0):
        if(A%400==0):
            print("LEAP YEAR!!!")
        else:
            print("NOT LEAP YEAR")
    else:
        print("LEAP YEAR!!!")
else:
    print("NOT LEAP YEAR")


#Question 2

Length=int(input("Enter length"))
Breadth=int(input("Enter breadth"))
if(Length==Breadth):
    print("IT'S A SQUARE")
else:
    print("IT'S A RECTANGLE")



#Question 3

a=int(input("Enter age of first person"))
b=int(input("Enter age of second person"))
c=int(input("Enter age of third person"))
if(a>=b and a>=c):
    print("First person is the oldest")
elif(b>=a and b>=c):
    print("Second person is the oldest")
else:
    print("Third person is the oldest")

if(a<=b and a<=c):
    print("First person is the youngest")
elif(b<=a and b<=c):
    print("Second person is the youngest")
else:
    print("Third person is the youngest")


#Question 4

Age=int(input("Enter age"))
Sex=input("Enter sex")
x=input("Enter marital status")
if(Sex=='F'):
    print("Work in Urban Areas")
else:
    if(Age>=20 and Age<=40):
        print("Can work anywhere")
    elif(Age>=40 and Age<=60):
        print("Work in urban areas")
    else:
        print("Error")


#Question 5

a=int(input("Enter quantity"))
b=100*a
if(b>1000):
    b=b-(b*0.1)
    print("Total cost is =",b)
else:
    print("Total cost is =",b)



#LOOPS

#Question 1
li=[]
for i in range(10):
    a=int(input("Enter a number"))
    li.append(a)
print(li)

#Question 2

while True:
    print("*")

    
#Question 3
    
a=[]
b=[]
num=int(input("enter number of elements"))
for i in range(num):
    c=int(input("enter number"))
    a.append(c)
for j in a:
    v=j*j
    b.append(v)
print(b)

#Question 4

li1=[]
li2=[]
li3=[]
li4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    li1.append(b)
for i in li1:
    if(i.isdigit()):
        li2.append(i)
    elif(i.isalpha()):
        li3.append(i)
    else:
        li4.append(i)
print(li2)
print(li3)
print(li4)

#Question 5

p=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            p.append(i)
print(p)

#Question 6

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Question 7


li8=[]
n=int(input("Enter number of elements of list"))
for i in range(n):
    a=int(input("Enter element"))
    li8.append(a)
num=int(input("Enter the number you want to delete from list"))
x=li8.count(num)
for i in range(x):
    y=li8.index(num)
    del(li8[y])
print(li8)







