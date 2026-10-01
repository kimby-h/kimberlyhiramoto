name = "Kimberly"

# print("Hello,", name)

# def say_hello(name):
#   print("hello,", name)

# say_hello(name="Kimberly")

# def add(a,b):
#   return a+b

# added_number = add(7,8)

# print (added_number)

# def check_num(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     elif num == 0:
#         return "Zero"

# print(check_num(0))

# print(41 < 0)

# print(False or False)

# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen:
#         print("You can vote!")
#     else:
#         print("You cannot vote")

# can_vote(18, True)

# def is_weekend(day):
#     if day == "Saturday" or day == "Sunday":
#         return "TGIS or S!"
#     else:
#         return "sadness"

# print(is_weekend("Monday"))

# fruit_basket = ["lychee", "mango", "persimmon"]

# for fruit in fruit_basket:
#     print(fruit)

# def countdown(start):
#     while start > 0:
#         print("T-", start)
#         start -= 1
#     print("Lift off")

# countdown(10)

# def temp_check(temp):
#     if temp > 80:
#         return "It's hot today! Yeowch!"
#     elif temp < 65:
#         return "Ooh it's cold out here, there must be some alpha's..."
#     else:
#         return "Heh"

# print(temp_check(67))



# number = [40, 80, 10, 30, 50, 20]
# def min_value(number):
#     return min(number)

# print(min(number))

# create a function to determine if a positive integer is a prime number

# def is_prime(num):
#     if num <= 0 or type(num) != int:
#         return "try again pal"
#     else:
#         if num == 1:
#             return "neither"
#         elif num == 2:
#             return "is a prime number"
#         else:
#             if num % 2 == 0:
#                 return "composite number"
#             else:
#                 for i in range(2, num):
#                     if num % i == 0:
#                         return "composite number"
#                     else:
#                         return "prime number"

# print(is_prime(7))



text = "apple and carrot"

def counting_vowels_and_consonents(text):
    vowels = 0
    consonants = 0
    for characters in text:
        if characters.isalpha():
            if characters in "aAeEiIoOuU":
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)

print(counting_vowels_and_consonents(text))

# paragraph = "hey it's me it's verity"
def average_vowels_and_consonants(paragraph):
    sentence = paragraph.split(".") # will separate the lines
    sent_length = len(sentence)
    sentence_vowels = 0
    sentence_consonants = 0
    for sentence in paragraph:
        vowels, consonants = counting_vowels_and_consonents(sentence) # connects to previous function
        sentence_vowels += vowels # adds the vowels to the output
        sentence_consonants += consonants # adds the consonants to the output
    average_vowels = sentence_vowels / sent_length
    average_consonants = sentence_consonants / sent_length
    return (f"The number of sentences in this paragraph is {sent_length}. The average vowels per sentence is {average_vowels}. The average consonants per sentence is {average_consonants}.")
    # return (sent_length, average_vowels, average_consonants)
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)
print(average_vowels_and_consonants(paragraph))