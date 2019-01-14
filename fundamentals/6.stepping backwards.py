#print(long_word[::-1])
#use [::-1] to reverse a string

#Example
# [ ] review and run example of stepping backwards using [::-1]
long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])
# [ ] review and run example of stepping backwards using [6::-1]
long_word = "characteristics"
# start at the 7th letter backwards to start
print(long_word[6::-1])
print(long_word[:6])

name = "Alton"
print(name[::2])

word = "cat"
print(word[::-1])
print(word[::1])
print(word[0:1:2])
#print(word[2:1:0])


#Task 5
#use slicing
# [ ] reverse long_word
long_word = "stressed"
print(long_word[::-1])
# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"
print(long_word[4::-1])

#Task 6
#use slicing

# [ ] print the first 4 letters of long_word
print(long_word[:4:])
# [ ] print the first 4 letters of long_word in reverse
print(long_word[3::-1])
# [ ] print the last 4 letters of long_word in reverse
print(long_word[-1:-5:-1])
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"
print(long_word[6:2:-1])
