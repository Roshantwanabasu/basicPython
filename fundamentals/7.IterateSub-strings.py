#Example
# [ ] review and run example
student_name = "Skye"

for letter in student_name[:3]:
    print(letter)
# Iterate BACKWARDS
# [ ] review and run example
student_name = "Cloud"

# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)

student_name = "iteration"
new_word = ""

for letter in student_name[:3]:
    new_word += letter
print(new_word)


student_name = "iteration"
count = 0
for letter in student_name:
    if letter.lower() == "e":
        print(count)
    count += 1


#Task 3
#String slicing and iteration
# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = ""
for letter in long_word[5::]:
    other_word +=letter
print(other_word)
# Mirror Color
# [ ] get user input, fav_color
fav_color = input("enter your favourite color")
other_word = ""
count = 0
for letter in fav_color[::-1]:
    count += 1
    other_word += letter
for letter in fav_color:
    other_word += letter
print(other_word)

# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"