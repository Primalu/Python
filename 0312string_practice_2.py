

def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char, end=" ")

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    minimum = min(example_string)
    print("\'" + minimum + " \'")

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string))

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    x = example_string.index("o")
    print(x)

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    my_list = list(example_string)
    print(my_list)

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    x = example_string.count("o")
    print(x)


main()
