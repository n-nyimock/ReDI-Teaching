#funtion with one parameter
def our_function(lname):
    print("my last name is",lname)
our_function("Justice")

#function with two parameters
def my_details(fname,lname):
    print("This is my official name: ",lname.capitalize(),fname.capitalize())
my_details("bitanyanmi","justice")

def factorial(n):
    if n == 0:
        return 1 # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1) # Recursive case: call factorial with n - 1

# Example usage:
result = factorial(5)
print(result)#5x4x3x2x1
