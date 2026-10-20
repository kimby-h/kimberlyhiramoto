# 3.1
foods = ["kalua pig", "fried chicken", "persimmon", "mango", "boba"]
print(foods[1])
print(foods[-1])
foods.append("momos")
print(foods)
foods.insert(0, "apple")
print(foods)
foods.remove("persimmon")
print(foods)
print(len(foods))

uppercase = []
for food in foods:
    uppercase.append(food.upper())
print(uppercase)

print(foods[0::5])

for food in foods:
    if food == "potato":
        print("A potato!")
    else:
        print("No potato!")
    break


'''
I encountered this error: 
"TypeError: 'builtin_function_or_method' object is not subscriptable"
I originally wrote: print[1]
I forgot that you have to say print(foods[1]) if you want to print something from the list. I fixed it by changing it to print(foods[1]).

I encountered this error:
"TypeError: 'builtin_function_or_method' object is not subscriptable"
I originally wrote foods.append["momos"]
I forgot to use parentheses. I fixed it by replacing the square brackets with parentheses.

I encountered this error:
"TypeError: 'list' object cannot be interpreted as an integer"
I originally wrote foods.insert([0], "apple")
I used square brackets. I fixed it by taking the square brackets out.
'''

# 3.2

numbers = list(range(0, 21))

def get_first_15(numbers):
    return numbers[:16]
print(get_first_15(numbers))
step1 = get_first_15(numbers)

def get_every_5th(step1):
    return step1[::5]
print(get_every_5th(step1))
step2 = get_every_5th(step1)

def reverse_and_stride(step2):
    return step2[::-1], step2[1::3]
print(reverse_and_stride(step2))

# 3.3.1

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(numbers):
    sum = 0
    for row in numbers:
        for num in row:
            sum += num
    return numbers, sum
print(sum_nested(numbers))

# 3.4

def fivebyfive():
    list = []
    input = 1
    for row in range(5):
        new_row = []
        for column in range(5):
            new_row.append(input)
            input += 1
        list.append(new_row)
    return(list)
print(fivebyfive()) # makes a list from 1-25

list_5x5 = fivebyfive() # storing it as list_5x5

def mult_3(list_5x5):
    for row in list_5x5:
        for i in range(len(row)):
            if row[i] % 3 == 0:
                row[i] = "?"
    return list_5x5
print(mult_3(list_5x5)) # will print the list with every multiple of 3 as a ?

three_is = list_5x5 # stores it as three_is

def not_three(three_is):
    sum = 0
    for row in three_is:
        for i in range(len(row)):
            if row[i] != "?":
                sum += row[i]
    return sum
print(not_three(three_is))

# 4.1: Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages.update({"Mira": 100})
ages["Milana"] = 52
del ages["Mariam"]

for name, age in ages.items():
    print(f"{name} is {age} years old")

# 5.2

print(not_three(three_is))