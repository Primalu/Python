
# Setting up the nato alphabet conversion
nato_alphabet = {
    "A" : "Alpha",
    "B" : "Bravo",
    "C" : "Charlie",
    'D' : "Delta",
    "E" : "Echo",
    "F" : "Foxtrot",
    "G" : "Golf",
    "H" : "Hotel",
    "I" : "India",
    "J" : "Juliette",
    "K" : "Kilo",
    "L" : "Lima",
    "M" : "Mike",
    "N" : "November",
    "O" : "Oscar",
    "P" : "Papa",
    "Q" : "Quebec",
    "R" : "Romeo",
    "S" : "Sierra",
    "T" : "Tango",
    "U" : "Uniform",
    "V" : "Victor",
    "W" : "Whiskey",
    "X" : "X-Ray",
    "Y" : "Yankee",
    "Z" : "Zulu"
}

def spell_word(): 
    nato_word = "" # Resetting and defining the nato version of the word
    user_word = input("\n\nPlease enter a word you want conveted into NATO: ") # Getting user input
    capitalized_input = user_word.upper() # Captlizing the user input, perping it for interaction with nato_alphabet
    for letter in capitalized_input: # Letter each letter change
        nato_word = nato_word + " " + nato_alphabet[letter] # Changing the letter
    print(f"The word {user_word} in nato would be {nato_word}.")


spell_word()
