#Chapter 1

'''
1.)Write a Python program to add two numbers.
2.)Write a Python program to find the remainder when a number is divided by Z(Integer).
3.)Check the type of the variable assigned using the input() function.
4.)Use a comparison operator to find out whether a given variable a is greater than b or not. (Take a=34 and b=80)
5.)Write a Python program to find the average of two numbers entered by the user.
6.)Write a Python program to calculate the square of a number entered by the user.
'''

#q1
a=int(input("Enter First Number\n"))
b=int(input("Enter Second Number\n"))
print("Sum Is :\n",a+b)
#q2
print("remender is :\n",a%b)
#q3
var = input()
print(type(var))
#q4
if(a>b):
    print("A is greater than B\n")
else:
    print("B is greater than A \n")

#q5
print("Avarage is  :",(a+b)/2)

#q6

print("Square of A :",a**2)