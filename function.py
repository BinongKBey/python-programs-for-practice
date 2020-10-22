print("BKB Quiz APP")
print("==============")

ans1="indra"
ans2="itachi uchiha"

total=0

#Function to check correct answer
def correct(inp,ans):
    global total
    if(inp.lower()==ans):
        print("Correct")
        total=total+1
    else:
        print("Wrong")

#Function to check total
def check():
    if(total==2):
        print("Congratulations all Correct")
    else:
        print(total," out of 2 is correct")

a=input("Who is the founder of Uchiha : ")
correct(a,ans1)

b=input("Who is Sasuke's Brother (Full name) : ")
correct(b,ans2)

check()

