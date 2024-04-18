'''
    read in and total a list of numbers
    strip and save to list while in process
'''


def main():
    try:
        total = 0
        # count
        accounts = open("sales_totals.txt", 'r')
        line = accounts.readline()
        while line:
            line = accounts.readline()
            line = float(line.rstrip('\n'))
            print(f"\nvalue: {line}")
            total += line
            print(f"total: {total:,.2f}")
        accounts.close()
        print(line)

    except IOError:
        print("An IOError has occurred.")


main()
