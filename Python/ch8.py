'''
1.)Write a program using the function to find the greatest of three numbers.
2.)Write a python program using the function to convert Celsius to Fahrenheit.
3.)How do you prevent a python print() function to print a new line at the end?//by using \end=''\ keyword
4.)Write a recursive function to calculate the sum of first n natural numbers.
5.)Write a python function to print the first n lines of the following pattern.
***

**       #For n = 3

*
6.)Write a python function that converts inches to cms.
7.)Write a python function to remove a given word from a list and strip it at the same time.
8.)Write a python function to print the multiplication table of a given number.
'''
a=int(input("enter the NUM : "))
#q1
'''
a=int(input("enter the fist number  : "))
b=int(input("enter the seconf number  : "))
c=int(input("enter the third number  : "))
d=int(input("enter the fourth number  : "))

def max(a,b):
    if a>b:
        return a
    else:
        return b

if(max(a,b)>max(c,d)):
    print(max(a,b)," is greater")
else:
    print(max(c,d), " is greater")
'''

#q2
'''
a=int(input("enter the temperature  : "))

def temp_to_fer(a):
    return (a*(9/5))+32

print(temp_to_fer(a))
'''
#Q4
'''
def sum(n):
    if n==1 :
        return 1
    elif n==0:
        return 0 
    return n+sum(n-1)
print(sum(a))
'''
#q5
'''
i=1
def p(n,i):
    if n==0:
        return
    print('*'*i)
    
    p(n-1,i+1)
p(a,i)
'''
#q6
'''
def in_to_cm(a):
    return a*2.54

print(in_to_cm(a))
'''
#Q7
'''
c="    my name is      rupesh    j"
def sar(b):
    c=b.replace("rupesh"," ")
    return c.strip()
     
print(sar(c))
'''
#q8
i=0
def mul(m,i,n):
    
    if n==0:
        return
    print(m ,"x",i,"=",m*i)
    mul(m,i+1,n-1)
mul(a,i,11)