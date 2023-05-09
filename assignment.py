fname = input("Enter your first name here: ")
lname = input("Enter your lasst name here: ")
age = input("How old are you: ")
hometown = input("Where do you come from? ")
location = input("where are you located now? ")
#country = input("Enter your country name here: ")
#education = input("Your educational level: ")
 
if hometown == location:
    print("Please your full name is,",fname,lname+",","you come from",hometown,"and currently live there.")
else:
    print("Please your full name is,",fname,lname+",","you come from",hometown,"and currently live at",location+".")

# def my_details(fname):
  #  print(fname)
#my_details(fname)