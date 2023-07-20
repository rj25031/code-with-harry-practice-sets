'''
1.)Write a program to print the multiplication table of a given number using for loop.
2.)Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”]
3.)Attempt problem 1 using a while loop.
4.)Write a program to find whether a given number is prime or not.
5.)Write a program to find the sum of first n natural numbers using a while loop.
6.)Write a program to calculate the factorial of a given number using for loop.
7.)Write a program to print the following star pattern.
    *
  ***  
***** for n=3
8.)Write a program to print the following star pattern:
*
**
*** for n = 3
9.)Write a program to print the following star pattern:
* * *
*   *             #For n=3
* * * 
10. Write a program to print the multiplication table of n using for loop in reversed order.
11.)Write a program to print the following star pattern.
    *
   ***
  *****  for n=3
'''

n = int(input("enter a number : "))

#q1
'''
for i in range(1,11):
    print(n , "x",i,"=",n*i)
'''
#q2
'''
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for i in l1 :
    if(i.startswith('S')):
        print("hello",i)

'''

#q3
'''
i=0
while(i<=10):
     print(n , "x",i,"=",n*i)
     i+=1
'''

#q4
'''
a = False
for i in range(2,n):
    if n%i==0:
        a=True
        break
if a==True:
    print("it's not a prime number")
else:
    print("it's a prime number")

'''

#q5
'''
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)

'''

#Q6
'''
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
'''
#q7
'''
for i in range(n,-1,-1):
    for j in range(i):
        print("*", end='')
    print("\n",end='')
'''
#q8
'''
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print("\n",end='')
'''
#q9
'''
for i in range(n):
    for j in range(n):
        if j>0 and j<n-1 and i>0 and i<n-1:
           print(" ",end='')
        else:
            print("*", end='')
    print("\n",end='')
'''
#q10
'''
for i in range(10,-1,-1):
    print(n , "x",i,"=",n*i)
'''
#q11
'''
for i in range(n):
    print(" " * (n-i-1),end='')
    print("*" * (2*i+1),end='')
    print(" " *(n-i-1))
'''
'''
for i in range(1,n+1):
    for j in range(1,n):
        print(" ",end='')
    for k in range(2*i-1):
        print("*",end='')
    print("\n",end='')
    n-=1
'''