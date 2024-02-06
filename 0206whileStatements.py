# 99 Bottles of beer assinment

# Setting bottle amount
bottles = 99

# setting While loop
while bottles > 1:
    print(bottles, "bottles of beer on the wall\n",bottles, "bottles of beer!\nTake one down pass it around")
    bottles -= 1  # Increment count
    if bottles > 1:
        print(bottles, "bottles of beer on the wall!\n\n")
    elif bottles == 1: # Dealing with 1's lack of plural 
        print(bottles, "bottle of beer on the wall!\n\n", bottles, "bottle of beer on the wall\n",bottles,"bottle of beer!\nTake one down pass it around")
        print ("No bottles of beer on the wall!")

