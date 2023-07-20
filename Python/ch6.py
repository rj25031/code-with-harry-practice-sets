'''
1.)Write a program to find the greatest of four numbers entered by the user.
2.)Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
3.)A spam comment is defined as a text containing the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

4.)Write a program to find whether a given username contains less than 10 characters or not.
5.)Write a program that finds out whether a given name is present in a list or not.
6.)Write a program to calculate the grade of a student from his marks from the following scheme:
90-100	Ex
80-90	A
70-80	B
60-70	C
50-60	D
<50	F
7.)Write a program to find out whether a given post is talking about “Harry” or not.
'''

#q1
'''
a=input("enter first number\n")
b= input("enter second number\n")
c=input("enter third number\n")
d=input("enter fourth number\n")

if(a>b):
    if(a>c):
        if(a>d):
            print(a," is greater")
        else :
                print(d," is greater")
    else:
        if(c>d):
            print(c," is greater")  
        else:
          print(d," is greater")
else:
    if(b>c):
        if(b>d):
            print(b," is greater")
        else:
            print(d," is greater")
    else:
        if(c>d):
            print(c," is greater")  
        else:
          print(d," is greater")

'''  
 #q2    
'''     
math = int(input("enter your marks in maths\n"))
sceince =int(input("enter your marks in sceince\n"))
marathi = int(input("enter your makrs in marathi\n"))

res=((math+sceince+marathi)/300)*100
if(math>=33 and sceince>=33 and marathi >=33 and res>=40):
    print("your pass")
else:
    print("your fail")
'''
#q3
'''
#“make a lot of money”, “buy now”, “subscribe this”, “click this”
comment = input("enter a comment\n")
if(comment=="make a lot of money" or comment == "buy now" or comment == "subscribe this" or comment=="click this") :
     print("comment not posted (spam comment)")
else:
    print("comment posted")

'''
#q4
'''
a=input("enter a username\n")
if(len(a)<10):
    print("accepted")
else:
    print("Less than 10 char please")
'''

#q5
'''
li = ['rupesh','rahul','dalvi','tanmay']
a=input("enter the name you want to find\n")   
if a in li:
    print("the element is available in list")
else:
    print("the element is not available in list")
    '''

#q6
'''
a=int(input("enter your marks\n"))
if(a<=100 and a>=90):
    print("grade : ex")
elif(a<90 and a>=80):
    print("grade : A")
elif(a<80 and a>=70):
    print("grade : B")
elif(a<70 and a>=60):
    print("grade : C")
elif(a<60 and a>=50):
    print("grade : D")
elif(a<50):
    print("your fail")
    '''
#q7

a="harry"
b="lorem ipilhgc hvghc  nhfnv hm hv hvm hvm hg harry"
if a in b:
    print("found")
else:
    print("not found")