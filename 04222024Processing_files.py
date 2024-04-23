'''
    Open the file sales_totals in read mode ✔️
    Read in all the lines using a loop ✔️
    Strip the newline symbol and convert each line to a float ✔️
    Add each number to the running total ✔️
    Count the number of lines ✔️
    Format and display each number ✔️
    Outside of the loop, format and display the total, the count, and the average ✔️
    Do this using a main function ✔️
    Use try and except statements to handle file errors ✔️
'''

    # Defining Main
def main(): # Do this using a main function
    running_total = 0
    line_count = 0
    try:    # Use TRY and except statements to handle file errors
        with open('sales_totals.txt', 'r') as directory:    # Open the file sales_totals in read mode
            for line in directory:                          # Read in all the lines using a loop
                line_float = float(line.strip())            # Strip the newline symbol and convert to float
                running_total += line_float                 # Add each number to the running total 
                line_count += 1                             # Count the number of lines
                print (line_float)                          # Format and display each number
            print (f"\n\nThe Total is: {running_total}")    # Outside of the loop, format and display the total
            print (f"The Line Count is: {line_count}")      # Outside of the loop, format and display the count
            print (f"The Avarage is: {running_total / line_count:.2f}\n") # Outside of the loop, format and display the average
    except FileNotFoundError: # Use try and EXCEPT statements to handle file errors / File Error
        print("Error: File not found.")
    except Exception as e: # Use try and EXCEPT statements to handle errors / Genric Error
        print("An unexpected error occurred:", e)

    #Calling Main
main()
