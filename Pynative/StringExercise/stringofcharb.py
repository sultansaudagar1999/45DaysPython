# Exercise 1B: Create a string made of the middle three characters


# Create a string made of the first, middle and last character
from jinja2.utils import missing

str1 = "JhonDipPeta"

l = len(str1)
middle = int(l/2)

middle1= str1[middle-1]
middle2 = str1[middle]
middle3 = str1[middle+1]

print(middle1+middle2+middle3)
