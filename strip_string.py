#strip() operation is only used to remove spaces before the string and the leading spaces. It does not affect the inside spaces

project = "              My project at ReDI School                          :"
project_aim = "To create awareness of how AI will advance in future."

print(project.strip(),"The aim of the project",project_aim)

#strip() operation can also be used to get rid of characters that are not needed in a string.This does not include characters within strings.
name = "--???--,,,,,,,,-Alawanson ----Peter------,,,???,,,,,"
print(name.strip("-,"))

#to remove those spaces and characters within strings we have to use join()
modify = " ".join(project.split())
print(modify)
#sometimes, one has to use more than one string operation in order to get thier data cleaned.
cleaned_string = "".join(name.split("-")).replace(",", "").replace("?","").strip()
print(cleaned_string)