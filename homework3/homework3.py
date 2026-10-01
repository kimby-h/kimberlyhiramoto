# 3.1

def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye(name = "Kimberly")

# 3.2

def area_de_la_circle(radius):
    area_de_la_circle = 3.14 * radius**2
    print("The area of la circle is", area_de_la_circle)
area_de_la_circle(radius = 6)

# 4.1

def subtract(a, b):
    return a - b
print(subtract(6, 7))

def multiply(a, b):
    return a * b
print(multiply(2, 3))

def divide(a, b):
    return a / b
print(divide(48, 12))

# 5.1

temp = [57, 59, 63, 66, 70, 72, 73, 74, 68]
def what_are_the_highs_and_lows(temp):
    return max(temp), min (temp)

print(what_are_the_highs_and_lows(temp))

# 5.2

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

def day_of_the_week(int):
    if int == 6 or int == 7:
        return True
    else:
        return False

print(day_of_the_week(Saturday))

# 5.3

def fuel_efficiency(miles, gallons):
    return(miles / gallons)

print("The fuel efficiency is", fuel_efficiency(67, 400), "miles per gallon")

# 5.4

def encrypt(integer):
    return (integer % 10) * 10000 + (integer // 10)

print(encrypt(12345))

# 6.1

def stop_oski(x, y):
    result = 1

    for i in range(y):
        result *= x
        i += 1
    return result

print(stop_oski(2, 3))

# 6.2.1

los_numeros = [17, 38, 3, 2, 7]
small_numb = los_numeros[0]
big_numb = los_numeros[0]
for numb in los_numeros:
    if numb < small_numb:
        small_numb = numb
    if numb > big_numb:
        big_numb = numb
print(small_numb)
print(big_numb)

# 6.2.2

numbers = [18, 25, 38, 91, 4, 10]
def number_time(numbers):
    tiny_num = numbers[0]
    big_num = numbers[0]
    while True:
        for num in numbers:
            if tiny_num > num:
                tiny_num = num
            if big_num < num:
                big_num = num
        break
    return tiny_num, big_num
print(number_time(numbers))

# 6.3

def add_all(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)

add_all(2468)

# 7.1

add_all(1738)
# result will be 1 + 7 + 3 + 8
print(f"The result of Calculate the Sum (6.3) with num = 1738 will have a sum of 19.")

