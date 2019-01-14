#Task 1
# [ ] use len() to find the midpoint of the string
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
mid_pt = int(len(random_tip)/2)
print("the first half of random_tip:"+random_tip[:mid_pt])
print("the second half of random_tip:"+random_tip[mid_pt:])


#Task 2
#.count()
# for letters: "e" and "a" in random_tip
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
e = random_tip.count('e')
a = random_tip.count('a')
if e > a:
    print("letter e is more frequent")
elif a > e:
    print("letter a is more frequent")
else:
    print("they are both equally repeated")



#Task 3
#.find()
# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
indexT = long_word.find('t')
indexT2 = long_word.find('t',indexT+1)
print(long_word[indexT:indexT2+1])


#Task 4
#Program: print each word in a quote
start = 0
quote = "they stumble who run fast"
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ",space_index+1)

#code to print word (index slice start:space_index)
#Output should look like below:

  #they
  #stumble
  #who
  #run
  #fast
# [ ] Print each word in the quote on a new line
#quote = "they stumble who run fast"