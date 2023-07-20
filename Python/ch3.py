'''
1.)Write a Python program to display a user-entered name followed by Good Afternoon using input() function.
2.)Write a program to fill in a letter template given below with name and date.
letter = ‘’’ Dear <|NAME|>,

                        You are selected!

                        <|DATE|>
3.)Write a program to detect double spaces in a string.
4.)Replace the double spaces from problem 3 with single spaces.
5.)Write a program to format the following letter using escape sequence characters.
letter = “Dear Harry, This Python course in nice. Thanks!!”
'''
#q1
a=input("Enter your name\n")
print("Good Afternoon "+a)

#q2
b= input("enter date\n")
print("Dear "+a,"\nYou Are Selected\n"+b)

#q3
d="ru  pesh"
print(d.find("  "))

#q4
print(d.replace("  "," "))

#q5

print("\"Dear Harry, This Python course in nice. Thanks!!\"")