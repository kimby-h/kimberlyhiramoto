# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_name(targets):
    for name in targets:
        print(name)
print_name(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_and_type(targets):
      for (name, properties) in targets.items():
          print(name,properties["Spectral Type"])
name_and_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def big_stars(targets):
	for (name, properties) in targets.items():
		if properties["Magnitude"] > 0.1:
			print (name, properties["Magnitude"])
big_stars(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Deneb"] = {
	"RA": "20h 41m 25s",
	"Dec": "+45° 16' 49″",
	"Magnitude": 1.25,
	"Spectral Type": "A2la"
}
print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def declination(targets):
    the_star = None
    the_diff = 1000
    the_mag = 1000
    for (name, properties) in targets.items():
        dec_string = properties["Dec"].replace("−", "-")
        degree = int(dec_string.split("°")[0])
        diff = abs(degree - 20)
        magnitude = properties["Magnitude"]
    if diff < the_diff:
        the_star = name
        the_diff = diff
        the_mag = magnitude
    elif diff == the_diff and magnitude < the_mag:
        the_star = name
        the_mag = magnitude
    return (the_star)

print(declination(targets))

# 6) What is your favorite constellation?

# my fav is cygnus