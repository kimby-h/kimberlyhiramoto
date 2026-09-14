# File: homework1.py

# --- Variables and Data Types ---

# 3.1
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a real number with a decimal or fractional part

c = 3j
print(c)
print(type(c)) # c is a complex number, a number that consists of a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a piece of text

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, stores a collection of items in a single variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, stores data as pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, stores ordered, immutable collection of items (you can't modify the contents)

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, stores a collection of items in a single variable

i = True
print(i)
print(type(i)) # i is a Boolean, represents either true or false

j = None
print(j)
print(type(j)) # j is a NoneType, represents the absence of a value or a null value

k = [True, "blue", 12]
print(k)
print(type(k)) # h is a list, stores a collection of items in a single variable

l = str(14)
print(l)
print(type(l)) # l is a string, a piece of text

m = 1e4
print(m)
print(type(m)) # b is a float, a real number with a decimal or fractional part

'''
1. I found 9 different data types.
2. Integer, Float, Complex Number, String, List, Dictionary, Tuple, Boolean, NoneType
3. b and m, e and h and k, d and l
4. The data type of l was a string becuase it was placed inside str(). Str() turns whatever is placed inside as text instead of an integer.
5. The data type I chose was Bytes.
'''

n = b"Malia"
print(n)
print(type(n)) # n is a bytes, an immutable sequence of integers ranging from 0 to 255.

# 3.2

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, string inside bool is considered true.
print(bool(123)) # True, any non-zero number in python is considered truthy.
print(bool(["apple", "cherry", "banana"])) # True, any non-empty list evaluates to True in Python.
print(bool(True)) # True, Python evaluates an expression from the innermost set of parentheses to the outermost, thus true.
print(bool(False)) # False, Python evaluates an expression from the innermost set of parentheses to the outermost, thus false.
print(bool(0)) # False, 0 inside the Boolean results as false.
print(bool("")) # False, an empty string "" is considered a falsy value.
print(bool(" ")) # True, a space is a content, and a string of something that is not nothing is considered true.
print(bool(())) # False, empty tuples are considered False.
print(bool([])) # False, empty dictionaries are considered False.
print(bool({})) # False, empty sets are considered False.
print(bool(True and False)) # False, boolean expression evaluates to false if false is with and.
print(bool(True and True)) # True, boolean expression evaluates to true.
print(bool(False and False)) # False, boolean expression evaluates to false.
print(bool(True or False)) # True, boolean expression evaluates to true when there's an or.
print(bool(True or True)) # True, boolean expression evaluates to true.
print(bool(False or False)) # False, boolean expression evaluates to false.
print(bool(not(False))) # True, not false means it's true.
print(bool(not(True))) # False, not true means it's false.

'''
1. Empty data types will return as false, but if there's a space in between, that is considered a something, so it will come back as true. If it's true and false, it'll be false, but if it's true or false, it'll return as true. 
2. I was surprised that expressions of True or False were true but expressions of True and False were false.
3

'''
print(bool("skibidi toilet"))
print(bool(None))

