''' 
1.)Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!
2.)Write a program to input eight numbers from the user and display all the unique numbers (once).
3.)Can we have a set with 18(int) and “18”(str) as a value in it?
4.)What will be the length of the following set S:
S = Set()

S.add(20)

S.add(20.0)

S.add(“20”)
What will be the length of S after the above operations?

5.)S = {}, what is the type of S?
6.)Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
7.)If the names of 2 friends are the same; what will happen to the program in Program 6?
8.)If the languages of two friends are the same; what will happen to the program in Program 6?
9.)Can you change the values inside a list which is contained in set S
S = {8, 7, 12, “Harry”, [1, 2]}
'''

#q1
'''
dictionary = {
    "help" : "मदद",
    "change" : "परिवर्तन",
    "fix" : "हल करना"
}
print("which word's meaning you want to know\n",dictionary.keys())
a=input("enter your word\n")
print("the meaning of the word  \"" , a ,"\" is:",dictionary[a])
'''
#q2
'''
a = set()
i=1
while(i<9):
    a.add(input("enter the number \n"))
    i=i+1

print(a)
'''

#q3
'''
a=set()
a.add(18)
a.add("18")
print(a)
'''

#q4
'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
'''

#q5
'''
a={}
s = {1,2,3}
print(type(a))
print(type(s))
'''
#q6
'''
a={}
a.update({input("enter your name \n"):input("enter your fav lang\n")})
a.update({input("enter your name \n"):input("enter your fav lang\n")})
a.update({input("enter your name \n"):input("enter your fav lang\n")})
a.update({input("enter your name \n"):input("enter your fav lang\n")})
print(a)
'''

#q7
'''
a={}
a.update({input("enter your name \n"):input("enter your fav lang\n")})
a.update({input("enter your name \n"):input("enter your fav lang\n")})
print(a)
#second value will be printed for same keys 
'''

#q8
'''
a={}
a.update({input("enter your name \n"):input("enter your fav lang\n")})
a.update({input("enter your name \n"):input("enter your fav lang\n")})
print(a)
#both value will be printed
'''

#q9
'''
S = {8, 7, 12, "Harry", [1, 2]}
S[[1,2]]=[3,5]
print(S)
#we can not change list 
'''
