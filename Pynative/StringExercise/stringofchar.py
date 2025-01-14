# Create a string made of the first, middle and last character
from jinja2.utils import missing

str1 = "james"

l = len(str1)
middle = int(l / 2)

first_char = str1[0]
middle_char = str1[middle]
last_char = str1[l-1]

print(first_char+middle_char+last_char)
