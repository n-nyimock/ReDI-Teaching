import math #to help use some advance functions

#getting inputs from the user
AB = int(input("Enter length AB:"))
BC = int(input("Enter length BC:"))

#manupulating the inputs to get the desired output
a = AB**2
b = BC**2
AC = a + b
c = int(math.sqrt(AC))

#printing the output to the user screen
print(f"The result of the pythagoras operation is, ",c)

#using lambda function to answer the same question
pythagoranean = lambda a, b: math.sqrt((a**2)+(b**2))
print(pythagoranean(3,4))
#converting the output to an integer value
print(int(pythagoranean(3,4)))