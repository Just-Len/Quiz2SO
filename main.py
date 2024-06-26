import os
from os import system
from c_scan import c_scan
from fcfs import first_come_first_served
from scan import scan
from sstf import shortest_seek_time_first
from look import look
from c_look import CLOOK
import time
import random

option = 0
trackNumbers = [20, 40, 51, 112, 34, 78, 99, 60]
initialHeadPosition = 0

while option != 11:
    system('cls')
    print(f"""Menu
Track numbers array: {trackNumbers}
1. Enter track numbers.
2. FCFS.
3. SSTF.
4. SCAN.
5. C-SCAN.
6. LOOK.
7. C-LOOK.
8. Select example track numbers.
9. Show algorithm table comparisons (massive)
10. Show algorithm table comparisons (digitized track numbers)
11. Exit""")
    
    option = int(input('Ingrese una opcion: '))

    if len(trackNumbers) == 0 & option > 1 | option < 10:
        print('You have not entered any track numbers dummy~')
        system('pause')
        continue

    if option == 1:
        inputNumber = 0
        trackNumbers = []
        while inputNumber != -1:
            print('Enter track numbers and press Enter. Leave blank to finish.')
            inputNumber = input('Track number: ')

            if len(inputNumber) == 0:
                break
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
        initialHeadPosition = int(input('Enter the initial head position: '))
        direction = input('Enter the search direction [right, left]: ')
        look(trackNumbers, initialHeadPosition, direction)
        system('pause')
    elif option == 7:
        initialHeadPosition = int(input("Enter the initial head position: "))
        CLOOK(trackNumbers, initialHeadPosition)
        system('pause')
    elif option == 8:
        trackNumbers = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
    elif option == 9:
        initialHeadPosition = int(input("Enter the initial head to all the algorithms: "))
        trackNumbersMassive = []
        for number in range(2000):
            trackNumbersMassive.append(random.randint(1, 199))

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'{"Algorithm used": <15} | {"Head movements": <15} | {"Execution time (seconds)": <20}')

        start_time = time.time()
        head_movements = first_come_first_served(trackNumbersMassive,initialHeadPosition,False)
        end_time = time.time()
        print(f'{"FCFS": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')

        start_time = time.time()
        head_movements = shortest_seek_time_first(trackNumbersMassive, initialHeadPosition, False)
        end_time = time.time()
        print(f'{"SSTF": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')

        start_time = time.time()
        head_movements = scan(trackNumbersMassive,initialHeadPosition,'right',False)
        end_time = time.time()
        print(f'{"SCAN": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')

        start_time = time.time()
        head_movements = c_scan(trackNumbersMassive,initialHeadPosition,False)
        end_time = time.time()
        print(f'{"C-SCAN": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')

        start_time = time.time()
        head_movements = look(trackNumbersMassive,initialHeadPosition,'right',False)
        end_time = time.time()
        print(f'{"LOOK": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')

        start_time = time.time()
        head_movements = CLOOK(trackNumbersMassive,initialHeadPosition, False)
        end_time = time.time()
        print(f'{"C-LOOK": <15} | {str(head_movements): <15} | {str(end_time - start_time): <20}')
        system('pause')
    elif option == 10:
        initialHeadPosition = int(input("Enter the initial head to all the algorithms: "))
        direction = input('Enter the search direction [right, left]: ')
        head_movements_FCFS = first_come_first_served(trackNumbers, initialHeadPosition, False)
        head_movements_SSTF = shortest_seek_time_first(trackNumbers, initialHeadPosition, False)
        head_movements_SCAN = scan(trackNumbers, initialHeadPosition, direction, False)
        head_movements_CSCAN = c_scan(trackNumbers, initialHeadPosition, False)
        head_movements_LOOK = look(trackNumbers, initialHeadPosition, direction, False)
        head_movements_CLOOK = CLOOK(trackNumbers, initialHeadPosition, False)

        print(f'{"Algorithm used": <15} | {"Head Movements": <15}')
        print(f'{"FCFS": <15} | {str(head_movements_FCFS): <15}')
        print(f'{"SSTF": <15} | {str(head_movements_SSTF): <15}')
        print(f'{"SCAN": <15} | {str(head_movements_SCAN): <15}')
        print(f'{"C-SCAN": <15} | {str(head_movements_CSCAN): <15}')
        print(f'{"LOOK": <15} | {str(head_movements_LOOK): <15}')
        print(f'{"C-LOOK": <15} | {str(head_movements_CLOOK): <15}')
        system('pause')
    elif option == 11:
        print('Shutting down...')
    else:
        print('Enter a number in the menu dummy~')
        system('pause')