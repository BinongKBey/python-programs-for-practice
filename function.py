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

def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
