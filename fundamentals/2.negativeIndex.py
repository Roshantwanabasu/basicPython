

student_name = "Joana"

# get last letter
end_letter = student_name[-1]
print(student_name,"ends with", "'" + end_letter + "'")

# [ ] review and run example
# get second to last letter
second_last_letter = student_name[-2]
print(student_name,"has 2nd to last letter of", "'" + second_last_letter + "'")
# [ ] review and run example
# you can get to the same letter with index counting + or -
print("for", student_name)
print("index 3 =", "'" + student_name[3] + "'")
print("index -2 =","'" + student_name[-2] + "'")

#Task 2
# [ ] assign a string 5 or more letters long to the variable: street_name
street_name = input("enter your street name:")
# [ ] print the last 3 characters of street_name
print("the last three letters are:")
for x in range(-3,0):
    print(street_name[x])

# [ ] create and assign string variable: first_name
first_name = input("Enter your name:")
print("the first letter of your name is:'"+first_name[0]+"' & the last letter is:'"+first_name[-1]+"'")
# [ ] print the first and last letters of name

#Task 3
#Fix the Errors
# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])
