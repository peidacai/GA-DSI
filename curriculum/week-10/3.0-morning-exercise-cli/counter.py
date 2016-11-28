import sys
import string

# program to count the unique words in a file


file_txt = ''

for line in sys.stdin:

    file_txt += line

file_txt = file_txt.lower()

print file_txt


#file_txt=file_txt.translate(None, string.punctuation)


file_txt = file_txt.split()

words = set()

for word in file_txt:
    for char in word:
        if char not in string.ascii_lowercase:
            word = word.replace(char, '')
    words.add(word)

words = list(words)


word_count = []
for word in words:
    word_count.append(str(file_txt.count(word)))

for i in range(len(words)):
    print words[i]+'\t'+word_count[i]

