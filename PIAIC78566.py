# Even and odd numbers by performing arthmatic oprations on two values

value1 = int(input("Enter Number value1 : "))

value2 = int(input("Enter Number Value2 : "))

oprator = input("Enter any of these char for specific operation +,-,*,//: ")

result = 0
if oprator == '+':
    result = value1 + value2
elif oprator == '-':
    result = value1 - value2
elif oprator == '*':
    result = value1 * value2
elif oprator == '//':
    result = value1 // value2
else:
    print("Input character is not recognized!")

print(value1, oprator , value2, "is Equal To", result)

if (result%2==0):
	print (result," is Even Number", "\n")
else:
	print (result," is odd number", "\n")

    
print("\n",  "1st Task Completed Sussfully")


# Here is the end of performing arthmatic oprations task

"""> > > > >"""

# Here is the piece of code in which we calculate factorial of positive number     

def factorial (number):
	fact = 1
	for i in range (number,0,-1):
		fact = fact*i
	return fact

fnumber = int(input("Enter Positive Number To Find Factorial:"))
fresult = factorial(fnumber)
print("Factorial of ",fnumber, "Is",fresult)

print("\n",  "2nd Task Completed Sussfully")


# Here is the end of calculating factorialof task 

"""> > > > >"""

# Here is the piece of code in which we find prime number 
    
prime = int(input("Enter Any Number To Check Number Is Prime Or Not "))
if prime>1:
	for i in range(2,prime):
		if (prime%i)==0:
			print(prime, "Not Prime Number")
			break
	else:
		print(prime, "Is a Prime Number")
else:
	print(prime, "Is Not Prime Number ", "\n")

print("\n",  "3rd Task Completed Sussfully")

 
# Here is the end of find prime number task 
    
"""> > > > >"""
