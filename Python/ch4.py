'''
1.)Write a program to store seven fruits in a list entered by the user.
2.)Write a program to accept the marks of 6 students and display them in a sorted manner.
3.)Check that a tuple cannot be changed in Python.
4.)Write a program to sum a list with 4 numbers.
5.)Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
'''

#q1
'''a=input("enter the fruits")
b=input()
c= input()
d= input()
e= input()
f= input()
g= input()
list = [a,b,c,d,e,f,g]
print(list)
'''
#using loop
'''
li=[]
i=0
while(i<7):
    li.append(input("enter fruit name \n"))
    i=i+1

print(li)
'''
#q2
'''
li=[]
i=0
while(i<6):
    li.append(input("enter your marks \n"))
    i=i+1

li.sort()
print(li)
'''

#q3
'''
tuple1 =(1,2,3,4,5,6)
#there is no function in python to change tuple 
tuple1[1]=10 # it shows an error hence prove tuple cannot be changed
print(tuple1)
'''
#q4
'''
list = [10,55,88,97]
sum = list[0]+list[1]+list[2]+list[3]
print(sum)
print(sum(list)) #inbuild python fuction to find sum
'''
#q5
'''
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
'''