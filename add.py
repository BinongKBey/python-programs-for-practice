#Input a number, show multiplication table up to 10
x=int(input("Enter a number : "))
s=int(input("Print tables up to : "))
for i in range (1,s+1):
    print(x," x ",i," = ",x*i)
