# Practice Questions 9/30/26

list1 = list(range(0,11))
print(list1)
print(list1[0:5])
print(list1[::2])
print(list1[::-1])



nested_list = [[2, 4, 6], 
               [8, 10, 12], 
               [14, 16, 18]]

print(nested_list[2][1])

stars_data = {
    "name": ["Sirius", "Vega", "Altair"],
    "magnitude": [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation": ["Canis Major", "Lyra", "Aquila"]
}

for name in stars_data["name"]:
    print(name)

for stars in stars_data:
    if "distance_ly" < 20:

def count_close_stars(data):
    count = 0
    for distance in data ["distance_ly"]:
        if distance < 20:
            count += 1