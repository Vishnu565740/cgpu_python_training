import string

with open("pride_and_prejudice.txt") as file:
    text = file.read()

text=text.lower()
for punctuation_mark in string.punctuation:
    text=text.replace(punctuation_mark,"")

words=text.split()

word_frequencies={}

for word in words:
    if word not in word_frequencies.keys():
        word_frequencies[word]=1
    else:
        word_frequencies[word]=word_frequencies[word]+1

print(word_frequencies)
print(len(word_frequencies))

file = open("words in Pride and Prejudice.csv","w")

file.write("Word, Frequency\n")

for word,frequency in word_frequencies.items():
    file.write(f"{word},{frequency}\n")
file.close()