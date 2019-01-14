#accessing sub-strings by step size
#Index Slicing [:], [::2]
#[:] returns the entire string
#[::2] returns the first char and then steps to every other char in the string
#[1::3] returns the second char and then steps to every third char in the string
#the number 2, in the print statement below, represents the step

long_word = "kathmanduNepal"
print(long_word[::2])

#Examples
# [ ] review and run example
student_name = "Colette"
# return all
print(student_name[:])
# [ ] review and run example
student_name = "Colette"
# return every other
print(student_name[::2])
# [ ] review and run example
student_name = "Colette"
# return every third, starting at 2nd character
print(student_name[1::2])
# [ ] review and run example
long_word = "Consequences"
# starting at 2nd char (index 1) to 9th character, return every other character
print(long_word[1:9:2])

#Task 4
# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"
print(long_word[::3])
# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::])