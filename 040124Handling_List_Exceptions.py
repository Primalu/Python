
'''
        Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new 
            artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
        General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."

        Use input() to get user input for the index and new artist name.
        Convert the index input to an integer using int(). This might raise a ValueError if the input is not a valid integer.
        When replacing an artist in the list, accessing an invalid index will raise an IndexError.
        Use a try...except block to catch and handle these exceptions.
        Remember that you can catch multiple exceptions in a single block by using a tuple for general error handling.
'''



def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    try: # To catch errors
        
        # Starting list  
        for artist in top_artists:
            index = top_artists.index(artist) + 1
            print(f"{index}. {artist}")

        # Getting user input
        index = input("\nPlease enter the index of the artist you want to replace: ")
        new_artist = input("Please enter the new artists name: ")

        # Checking if user info correct
        index = int(index)
        if index < 0 or index >= len(top_artists):
            raise IndexError("Index is out of range.") # I don't know how to move this to the tuple without causing more issues
        
        # Replacing artists, man the music industry moves fast
        top_artists[index - 1] = new_artist
        print("Artist replaced successfully!")
    
    # Error handling, using ✨tuples✨
    except (ValueError, IndexError) as error:
        print(f"An error occurred: {error}")

    # Printing the updated list
    print("\nUpdated list of top artists:")
    for artist in top_artists:
        index = top_artists.index(artist) + 1
        print(f"{index}. {artist}")

main()