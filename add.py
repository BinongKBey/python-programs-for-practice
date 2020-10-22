#Input a number, show multiplication table up to 10
x=int(input("Enter a number : "))

s=int(input("Print tables up to : "))

for i in range (1,s+1):
    print(x," x ",i," = ",x*i)


a=int(input("Enter a new number : "))

# Python code to reverse a string 
# using loop 

def reverse(s): 
str = "" 
for i in s: 
	str = i + str
return str

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 
