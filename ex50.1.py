# Write a Python program to replace a string
# "Python" with "Java" and "Java"
# with "Python" in a given string.
import re

text = '''English letters (including single byte alphanumeric characters, blanks, symbols)
are given on one line. The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python'''

replaceRegex = re.compile(r'Java|Python')
list_words = replaceRegex.findall(text)

J_count = 0
P_count = 0

for word in list_words:
    if word == 'Java':
        J_count += 1
    elif word == 'Python':
        P_count += 1

print(text.replace('Java','Python',J_count).replace('Python', 'Java', P_count))
