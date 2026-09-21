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
3. print(bool("skibidi toilet")) will return as True because a string of text within the boolean expression will evaluate to true.
4. print(bool(None)) will return as False because the value inside the boolean expression has no value, which evaluates to false.
'''
print(bool("skibidi toilet"))
print(bool(None))

# 3.3.1

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(5 % 2) # 1, % calculates remainder of a division problem
print(6 / 3) # 2, / performs division
print(3 ** 2) # 9, ** turns the latter number into an exponent
print(15 // 2) # 7, // divides the former by the latter and rounds to the nearest whole number

# 3.3.2

print(5 == 2) # False, == means equal to, the numbers aren't equal, thus false.
print(10 != 10) # False, != means not equal to, the numbers are equal, thus false.
print(2 < 5) # True, 5 is greater than 2.
print(12 > 5) # True, 12 is greater than 5.
print(5 <= 6) # True, 6 is greater than or equal 5.
print(1 >= 10) # False, 1 is not greater than or equal to 10.

# 3.3.3

x = 5

x += 5
print(x)

x -= 4
print(x)

x *= 3
print(x)

# 3.3.4

'''
1. The and operator will return True only if both operands are True.
    bool(True and True) will return True since both operands are true.
    bool(True and False) will return false as one of the operands are false

2. The or operator returns true if at least one of the operands is true.
    bool(True or False) will return True since one of the operands is true.
    bool(False or False) will return false since both operands are false.

3. The operator not negates the boolean value of the operands.
    bool(not True) will return False, since negating True means False.
    bool(not False) will return True, since negating False means True.

More Questions:
1. / means simple division, // means division and rounding the quotient to the nearest whole number.
2. // means what I said above, and % performs division and the result is the remainder.
3. I would use %, 
    example: print(7 % 3) = 1
4. Assignment operators change the value of a variable.
'''

# 3.4

my_string = "hello" 
print(my_string) # prints: hello
print(my_string[0]) # prints: 0th letter, h
print(my_string[1]) # prints: 1st letter, e
print(my_string[2]) # prints: 2nd letter, l
print(my_string[3]) # prints: 3rd letter, l
print(my_string[4]) # prints: 4th letter, o
print(my_string[-1]) # prints: last letter, o
print(my_string[1:3]) # prints: index 1 and index 2, el
print(my_string[0:5:2]) # prints: increments from 0-4 with a step of 2, hlo
print(len(my_string)) # prints: the length of the string, 5
print(my_string + "goodbye") # prints: hellogoodbye
print(7 * my_string) #prints: hellohellohellohellohellohellohello (hello 7x)

# 3.4.1

'''
1. slicing is when you extract a portion of a string by specifying start and end index and an optional step. For 8 and 9 we did this.
'''

name = "Oski"
print("Hello, my name is", name) # it says Hello, my name is Oski.
print(f"Hello, my name is {name}") # it says Hello, my name is Oski.
# The difference between the first and second print statments is that one concatenates the string with the variable name, while 
# the second one uses an f-string, where you prefix the string with f, and place the variable name in curled brackets.

# 3.5

'''
cd
changes directories. use it to move from one folder to another
example: cd Desktop

ls
list. use it to return the list files and directories.
example: ls Desktop

ls -a
this will list all files and folders in the current directory, including hidden files.
example: ls -a Desktop

mkdir
make directory. this will make a new empty folder or directory within a command-line.
example: mkdir Skibidi

cat
concatenate. used to read and display file contents.
example: cat skibidi

pwd
print working directory. displays the exact folder path you are currently in inside the terminal
example: pwd skibidi

cd ..
change directory to the parent directory. moves you up one directory level into the parent folder of your current location
example: if in skibidi/toilet, cd.. will take me back to skibidi

cd . 
change to current directory. keeps you in your current working directory.
example: if in skibidi/toilet, cd . will keep me there

cd ~
change directory to home folder. changes your current working directory to your user's home directory.
example: if in kimberlyhiramoto/skibidi, cd~ takes me to kimberlyhiramoto

cp
copy. used to duplicate files and directories from one location to another
example: cp skibidi tungtung

mv
move. moves or renames files and directories.
example: mv skibidi tungtung

rm
remove. permanently deletes files and directories from your stystem.
example: rm tungtung

clear
erases the visible text on your terminal screen and clears its scrollback history buffer.
example: clear (and it will clear stuff)

grep
global regular expression print. searches for specific words, phrases, or text patterns within files or from the output of other commands.
grep "tungtungtung sahur" skibidi toilet

Three other commands:

1. head: a command used to preview the first few rows of a data set. to see the first 5 rows, just say print(<file>.head())
2. tail: the opposite of head, it's used to preview the last few rows of a dataset. to see the last 5 rows, which is the default, just 
    say print(<file>.tail())
3. whoami: a command that prints the username associated witht he current effective user ID. to use, just type whoami into the terminal 
    and it will say back who you are, kimbe.

2. ls will list all files and directories, while ls -a will do the same but also listing the hidden files.
3. a hidden file is a file or folder that does not appear when you run a standard listing command, usually because its name starts with 
    a dot (.).
4.  1) -l is a flag for ls, it will show the long format of a file's contents, such as permissions, size, owner, and modified date. you 
    do ls -l in command line.
    2) -h is a flag for ls and -l, it'll show file sizes in an easy to read format. to use, type ls -l -h into the command line.
    3) -i is a flag for rm, and it will prompt you to confirm before deleting each file. to use, type rm -i <file>
'''

# 4





