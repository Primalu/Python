'''
Create a Python program that uses a generator function to produce all possible two-letter 
combinations from a given list of characters. For example, if the list is ['a', 'b', 'c'], 
the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.
Instructions:
    Define a generator function two_letter_combinations that takes a list of characters as an argument.
    Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
    In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list.
    Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
'''

    # two_letter_combinations functions, responable for comboing the letters
def two_letter_combinations(characters):
    for character1 in characters:           # Getting character 1
        for character2 in characters:       # Getting character 2
            yield character1 + character2   # Pausing to print

    # Main functions, the backbone of any program
def main():
    characters = ['p', 'r', 'g', 'r', 'm']  # It's program without the voules, I thought I was funny
    # Calling the generator function while printing each combination at yield
    for combination in two_letter_combinations(characters):
        print(combination)

    # Calling main
main()
