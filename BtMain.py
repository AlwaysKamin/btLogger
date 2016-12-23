import BtFinder
import tableModification
import time


def main():

    addrNew = []
    nameNew = []

    # Checks for table / creates if it doesnt exist
    tableModification.create()

    # Asks the user to decide to add or display
    print("Enter 1 if you would like to scan for devices, ")
    print("or Enter 2 if you would like to display the database: ")

    # Takes first input
    menuNum = input()

    while menuNum != int(0):
            # 1 = Scan for bluetooth devices
            if menuNum == 1:
                print("Scanning")

                # Gets time and sets timer
                # TODO FIX TIME TO REPRESENT CURRENT TIME // MIGHT BE ON THE PI NOT CODE
                endTime = int(raw_input('Enter the amount of seconds you would like to run this: '))
                startTime = time.time()

                # This loop deals with time, and how long the program will run
                while (time.time() - startTime) < endTime:
                    addrNew, nameNew = BtFinder.finder()

                    for i, item in enumerate(addrNew):
                        tableModification.add(newAddr=addrNew[i], newName=nameNew[i])
                        # print("addrNew: %s nameNew: %s" % (addrNew[i], nameNew[i]))

                # Query User to keep going
                print("Input another number or hit 0 to quit.")
                menuNum = input()

            elif menuNum == 2:

                # output the database
                print("Outputting Database: ")
                tableModification.display()

                # Query User to Keep Going
                print("Input another number or hit 0 to quit.")
                menuNum = input()

            else:
                # Error Checks
                print("Something went wrong, please try again!")
                print("Input another number or hit 0 to quit.")

    print("Thank you for using the program.")

main()
