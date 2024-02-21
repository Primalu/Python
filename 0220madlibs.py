# Develop a Python-based Madlib based on a song of your choice.
# The program should collect at least 8 different pieces of information 
# from the user and incorporate them into the song using named arguments. 
# The goal is to practice using functions, user input, and string manipulation in Python.

# Trigging of triggers
def custom_song(animal, weather, luck_1, luck_2, time, person, verb, mystery):
    animal, weather, luck_1, luck_2, time, person, verb, mystery = get_words()
    madlibs(animal, weather, luck_1, luck_2, time, person, verb, mystery)

# Getting user imput
def get_words():
    animal = input("Please enter a kind of animal:  ")
    weather = input("Please enter a kind of weather:  ")
    luck_1 = input("Please enter a type of luck:  ")
    luck_2 = input("Please enter a diffrent type of luck:  ")
    time = input("Please enter a time of day:  ")
    person = input("Please enter a name:  ")
    verb = input("Please enter a kind of verb:  ")
    mystery = input("Please enter a kind of mystery:  ")

    return animal, weather, luck_1, luck_2, time, person, verb, mystery

# The madlib using user names
def madlibs(animal, weather, luck_1, luck_2, time, person, verb, mystery):
    print(f"Life is like a {weather} here in {animal} - burg")
    print(f"Race cars, lasers, aeroplanes it's a, {animal} - blur!")
    print(f"Might solve a {mystery}, or rewrite hist'ry!")
    print(f"{animal} Tales! oo woo oo")
    print(f"Every {time} they're out there making")
    print(f"{animal} Tales! oo woo oo")
    print(f"Tales of daring do {luck_1} and {luck_2} luck tales! whooh ooh")
    print(f"When it seems they're heading for the final curtain")
    print(f"Cool deduction never fails that's for certain")
    print(f"The worst of messes become successes\n\n")
    print(f"{animal} Tales! whooh ooh")
    print(f"Every {time} they're out there making")
    print(f"{animal} Tales! whooh ooh")
    print(f"Tales of daring do {luck_1} and {luck_2} luck tales! whooh ooh")
    print(f"D - D - D - Danger! Watch behind you!")
    print(f"There's a {person}, out to {verb} you!")
    print(f"What to do? Just grab on to some {animal} Tales")
    print(f"{animal} Tales! whooh ooh")
    print(f"Every {time} they're out there making")
    print(f"{animal} Tales! whooh ooh")
    print(f"Tales of daring do {luck_1} and {luck_2} luck tales! whooh ooh")
    print(f"D - D - D - Danger! Watch behind you!")
    print(f"There's a {person}, out to {verb} you!")
    print(f"What to do? Just grab on to some {animal} Tales")
    print(f"{animal} Tales! whooh ooh")
    print(f"Every {time} they're out there making")
    print(f"D - D - D - Danger! Watch behind you!")
    print(f"There's a {person}, out to {verb} you!")
    print(f"What to do? Just grab on to some")
    print(f"{animal} Tales! oo woo oo")
    print(f"Every {time} they're out there making")
    print(f"{animal} Tales! oo woo oo")
    print(f"Tales of daring do {luck_1} and {luck_2} luck tales! whooh ooh")
    print(f"Not pony tales or cotton tales, no")
    print(f"{animal} Tales! oo woo oo")

# Calling Song
custom_song()
