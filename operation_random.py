from random import randint
import math

#generating random number
rand_int = randint(0,90)
print(rand_int)
#ceil and floor buil-in functions
print(math.ceil(3.5)) #rounds the number up
print(math.floor(3.5)) #rounds the number down
print(int(math.sqrt(25)))
print(5**2)

#what if we coul take the random itegers from a user
start = 2
end = 5
random1 = randint(start,end) #start and end represent 2 and 5 respectively
print(f"This is the generated random integer: ",random1,"Thank You!")
print(pow(random1,2))