from os import system
from c_scan import c_scan
from fcfs import first_come_first_served
from scan import scan
from sstf import shortest_seek_time_first
from c_look import CLOOK

option = 0
trackNumbers = []
initialHeadPosition = 0

while option != 7:
    system('cls')
    print("""Menu
1. Enter track numbers.
2. FCFS.
3. SSTF.
4. SCAN.
5. C-SCAN.
6. Select example track numbers.
7. C-LOOK
8. Salir""")
    
    option = int(input('Ingrese una opcion: '))

    if len(trackNumbers) == 0 & option > 1 | option < 6:
        print('You have not entered any track numbers dummy~')
        system('pause')
        continue

    if option == 1:
        inputNumber = 0
        while inputNumber != -1:
            print('Enter track number and press Enter. Leave blank to finish.')
            inputString = input('Track number')

            if len(inputString) == 0:
                continue
            else:
                trackNumbers.append(int(inputNumber))

    elif option == 2:
        initialHeadPosition = int(input('Enter the initial head position: '))
        first_come_first_served(trackNumbers, initialHeadPosition)
        system('pause')
    elif option == 3:
        initialHeadPosition = int(input('Enter the initial head position: '))
        shortest_seek_time_first(trackNumbers, initialHeadPosition)
        system('pause')
    elif option == 4:
        initialHeadPosition = int(input('Enter the initial head position: '))
        direction = input('Enter the search direction [right, left]: ')
        scan(trackNumbers, initialHeadPosition, direction)
        system('pause')
    elif option == 5:
        initialHeadPosition = int(input('Enter the initial head position: '))
        c_scan(trackNumbers, initialHeadPosition)
        system('pause')
    elif option == 6:
        trackNumbers = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
    elif option == 7:
        size = int(input("Enter the size of the request array: "))
        arr = []
        for i in range(size):
            track = int(input(f"Enter track {i + 1}: "))
            arr.append(track)
        head = int(input("Enter the initial head position: "))

        print("Initial position of head:", head)

        CLOOK(arr, head)
    elif option == 8:
        print('Shutting down...')
    else:
        print('Enter a number in the menu dummy~')
        system('pause')