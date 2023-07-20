'''
1.)Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.
2.)The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
3.)Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.
4.)A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.
5.)Repeat program 4 for a list of such words to be censored.
6.)Write a program to mine a log file and find out whether it contains ‘python’.
7.)Write a program to find out the line number where python is present from question 6.
8.)Write a program to make a copy of a text file “this.txt.”
9.)Write a program to find out whether a file is identical and matches the content of another file.
10.)Write a program to wipe out the contents of a file using python.
11.)Write a python program to rename a file to “renamed_by_python.txt.”
'''

#q1
'''
flag = False
f=open("poem.txt",'r')
s=f.read()
print(s,'\n')
g=s.split()
for i in g:
    if i=='twinkle':
       flag=True
if flag==True:
    print("the word contains in file")
else:
    print("not found")
f.close
'''
#q2
'''
def game():
    return 44
score = game()
f=open("highscore.txt",'r')
s=f.read()

if s=='':
    f=open("highscore.txt",'w')
    f.write(str(score))
    print('score updated\n')
elif int(s)<score:
    f=open("highscore.txt",'w')
    f.write(str(score))
    print('score updated\n')
else:
    print('play again it\'s not hiscore')
f.close
'''

#q3
'''
for k in range(2,21):   
    f=open(f"table/mul_of_{k}.txt",'w')  
    for i in range(1,11):
        s=f.write(f"{k}x{i}={i*k}")
        f.write('\n')
    
f.close
'''
#q4
'''
with open("cencore.txt") as f:
    s=f.read()

d=s.split()
for i in d:
    if i=='donkey':
        with open("cencore.txt",'w') as f:
            f.write(f"{s.replace('donkey','#####')}")
f.close
'''
#q5
'''
with open("cencore.txt") as f:
    s=f.read()

d=s.split()
for i in d:
    if i=='donkey':
        with open("cencore.txt",'w') as f:
            f.write(f"{}")
f.close
'''