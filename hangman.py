import random
import json
# Write your code here
s="HANGMAN"
print(" ".join(s))
data = json.load(open("dictionary.json"))
l=list(data.keys())
play=input(r'Type "play" to play the game, "exit" to quit: ')
#l=['python', 'java', 'kotlin', 'javascript']
x=random.randint(0,len(l)-1)

flag=0

ans=list(str(l[x]))
for i in range(0,len(l[x])):
    if l[x][i]==" ":
        l[x][i]='-'
    ans[i]='-'
cnt=0
inp=set()
temp1=0
if play=="play":
    while cnt<8:
        print()
        print("".join(ans))
        c=input('Input a letter: ')
        temp1=0
        if c.islower()==False :
            print("It is not an ASCII lowercase letter")
            temp1=1
        if(len(c)>1):
            print("You should input a single letter")
            temp1=1
        if(c in inp):
            print("You already typed this letter")
            temp1=1
        if c in l[x] and temp1==0:
            for j in range(0,len(l[x])):
                    if l[x][j]==c:
                        if ans[j]!='-':
                            print("You already typed this letter")
                            break 
                        else:
                            ans[j]=c               
        elif(temp1!=1):
            cnt+=1
            print("No such letter in the word. Chances left "+str((8-cnt)))
        inp.add(c)
        if "".join(ans)==l[x]:
            flag=1
            print("You guessed the word!")
            print("You survived!")
            break
else:
    quit()


if "".join(ans)==l[x] and flag==0:
    print("You guessed the word! The word was "+str(l[x]))
    print("You survived!")
elif(flag!=1):
    print("You are hanged!")
    print("The actual word was "+ str(l[x]))
