# Assignment Steps:
# Initialize the Seating List:
# Create a list in your program representing the 20 seats. 
# This list should initially include all seat numbers (1-20).
# Display Available Seats:

# Write code to display the list of available seats to the customer. 
# This list should update as seats are sold.
# Implement the Ticket Purchase Process:

# Prompt the customer to select a seat by entering its number.
# Include instructions in your prompt, indicating that the customer 
# should enter '0' to finish their purchase.
# Update Seat Availability:

# Once a seat is selected, remove it from the list of available seats.
# After each selection, display the updated list of available seats.
# Continue this process until the customer enters '0', 
# indicating they are done buying tickets.
# Ensure User-Friendly Interaction:

# Your program should handle inputs gracefully. If a customer selects 
# a seat that doesn't exist or is already sold, display a friendly message 
# and prompt them to choose again.
# Test Your Program:

# Run your program to ensure it works as expected. Try different scenarios, 
# such as selling all seats, selling a few seats, and entering invalid seat numbers.

seats = ["1A", "2A", "3A", "4A", "5A", "1B", "2B", "3B", "4B", "5B", "1C", "1D", "2D", "3D", "4D", "5D", "1E", "2E", "3E", "4E", "5E"]


seat = ""
while seat != "done":
    print ("\n\nYou can buy multipul tickes, when you're finshed purching please type '0'\nThe following seats are avaible:")
    for seat in seats:
        print (seat)


    seat = input("\nPlease enter the seats you want: ")
    if seat in seats:
        seats.remove(seat)
    else:
        print("Sorry thats not an avaible seat, please try again!")
    if len(seats) == 0:
        print("Thank you for shopping with us!")
        seat = "done"

