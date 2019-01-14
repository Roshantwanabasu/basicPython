student_name = "Roshan"
print(student_name[0], "<-- first character at index 0")
print(student_name[1], "<-- second character at index 1")
print(student_name[2], "<-- third character at index 2")
print(student_name[3], "<-- fourth character at index 3")
print(student_name[4], "<-- fifth character at index 4")
print(student_name[5], "<-- sixth character at index 5")

student_name = input("Enter your name:")
if student_name[0].upper() == "R":
    print('Winner! Name starts with R:', student_name)
elif student_name[0].upper() == "T":
    print('Winner! Name starts with T:', student_name)
else:
    print('Not a match, try again tomorrow:', student_name)

street_name = input("Enter your street name:")
print(street_name[0], "First character of the string")
print(street_name[2], "third character of the string")
print(street_name[4], "fifth character of the string")

team_name = input("Enter a team name with second character either 'i','o' or 'u':")
if team_name[1].upper() == 'I' or team_name[1].upper() == 'O' or team_name[1].upper() == 'U':
    print("You entered as instructed!!")
else:
    print("YOu entered wrong team name")
