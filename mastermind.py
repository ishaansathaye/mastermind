import random

allCharacters = '1234567890'
listOfAllCharacters = list(allCharacters)

computer1 = random.choice(listOfAllCharacters)
computer2 = random.choice(listOfAllCharacters)
computer3 = random.choice(listOfAllCharacters)
computer4 = random.choice(listOfAllCharacters)

CR1 = 0
CR2 = 0
CR3 = 0
CR4 = 0

CR1 = int(computer1)
CR2 = int(computer2)
CR3 = int(computer3)
CR4 = int(computer4)

UR1 = 0
UR2 = 0
UR3 = 0
UR4 = 0

win = False
guess = ""

winArray = [" - ", " - ", " - ", " - "]
for x in range(4):
    print(winArray[x], end=" "),


noUR1zero = False
noUR1one = False
noUR1two = False
noUR1three = False
noUR1four = False
noUR1five = False
noUR1six = False
noUR1seven = False
noUR1eight = False
noUR1nine = False

noUR2zero = False
noUR2one = False
noUR2two = False
noUR2three = False
noUR2four = False
noUR2five = False
noUR2six = False
noUR2seven = False
noUR2eight = False
noUR2nine = False

noUR3zero = False
noUR3one = False
noUR3two = False
noUR3three = False
noUR3four = False
noUR3five = False
noUR3six = False
noUR3seven = False
noUR3eight = False
noUR3nine = False

noUR4zero =False
noUR4one = False
noUR4two = False
noUR4three = False
noUR4four = False
noUR4five = False
noUR4six = False
noUR4seven = False
noUR4eight = False
noUR4nine = False

while win == False:

    numof0 = 0
    numof1 = 0
    numof2 = 0
    numof3 = 0
    numof4 = 0
    numof5 = 0
    numof6 = 0
    numof7 = 0
    numof8 = 0
    numof9 = 0

    if CR1 == '0':
        numof0 = numof0 + 1
    if CR1 == '1':
        numof1 = numof1 + 1
    if CR1 == '2':
        numof2 = numof2 + 1
    if CR1 == '3':
        numof3 = numof3 + 1
    if CR1 == '4':
        numof4 = numof4 + 1
    if CR1 == '5':
        numof5 = numof5 + 1
    if CR1 == '6':
        numof6 = numof6 + 1
    if CR1 == '7':
        numof7 = numof7 + 1
    if CR1 == '8':
        numof8 = numof8 + 1
    if CR1 == '9':
        numof9 = numof9 + 1

    if CR2 == '0':
        numof0 = numof0 + 1
    if CR2 == '1':
        numof1 = numof1 + 1
    if CR2 == '2':
        numof2 = numof2 + 1
    if CR2 == '3':
        numof3 = numof3 + 1
    if CR2 == '4':
        numof4 = numof4 + 1
    if CR2 == '5':
        numof5 = numof5 + 1
    if CR2 == '6':
        numof6 = numof6 + 1
    if CR2 == '7':
        numof7 = numof7 + 1
    if CR2 == '8':
        numof8 = numof8 + 1
    if CR2 == '9':
        numof9 = numof9 + 1

    if CR3 == '0':
        numof0 = numof0 + 1
    if CR3 == '1':
        numof1 = numof1 + 1
    if CR3 == '2':
        numof2 = numof2 + 1
    if CR3 == '3':
        numof3 = numof3 + 1
    if CR3 == '4':
        numof4 = numof4 + 1
    if CR3 == '5':
        numof5 = numof5 + 1
    if CR3 == '6':
        numof6 = numof6 + 1
    if CR3 == '7':
        numof7 = numof7 + 1
    if CR3 == '8':
        numof8 = numof8 + 1
    if CR3 == '9':
        numof9 = numof9 + 1

    if CR4 == '0':
        numof0 = numof0 + 1
    if CR4 == '1':
        numof1 = numof1 + 1
    if CR4 == '2':
        numof2 = numof2 + 1
    if CR4 == '3':
        numof3 = numof3 + 1
    if CR4 == '4':
        numof4 = numof4 + 1
    if CR4 == '5':
        numof5 = numof5 + 1
    if CR4 == '6':
        numof6 = numof6 + 1
    if CR4 == '7':
        numof7 = numof7 + 1
    if CR4 == '8':
        numof8 = numof8 + 1
    if CR4 == '9':
        numof9 = numof9 + 1

    print()
    print()
    guess = input("Enter the code: ")

    userInput1 = guess[0]
    userInput2 = guess[1]
    userInput3 = guess[2]
    userInput4 = guess[3]

    UR1 = int(userInput1)
    UR2 = int(userInput2)
    UR3 = int(userInput3)
    UR4 = int(userInput4)

    #print("User entered: " + UR1, UR2, UR3, UR4)

## FOR UR1
    #FOR UR1 -- 0
    if noUR1zero == False:
        if UR1 == 0:
            if (UR1 == CR1) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[0] = " = "
                noUR1one = True
                noUR1two = True
                noUR1three = True
                noUR1four = True
                noUR1five = True
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 1
    if noUR1one == False:
        if UR1 == 1:
            if (UR1 == CR1) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[0] = " = "
                noUR1two = True
                noUR1three = True
                noUR1four = True
                noUR1five = True
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 2
    if noUR1two == False:
        if UR1 == 2:
            if (UR1 == CR1) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[0] = " = "
                noUR1three = True
                noUR1four = True
                noUR1five = True
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 3
    if noUR1three == False:
        if UR1 == 3:
            if (UR1 == CR1) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[0] = " = "
                noUR1four = True
                noUR1five = True
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 4
    if noUR1four == False:
        if UR1 == 4:
            if (UR1 == CR1) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[0] = " = "
                noUR1five = True
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 5
    if noUR1five == False:
        if UR1 == 5:
            if (UR1 == CR1) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[0] = " = "
                noUR1six = True
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 6
    if noUR1six == False:
        if UR1 == 6:
            if (UR1 == CR1) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[0] = " = "
                noUR1seven = True
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 7
    if noUR1seven == False:
        if UR1 == 7:
            if (UR1 == CR1) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[0] = " = "
                noUR1eight = True
                noUR1nine = True
            elif (UR1 == CR2) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 8
    if noUR1eight == False:
        if UR1 == 8:
            if (UR1 == CR1) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[0] = " = "
                noUR1nine = True
            elif (UR1 == CR2) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

    # FOR UR1 -- 9
    if noUR1nine == False:
        if UR1 == 9:
            if (UR1 == CR1) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[0] = " = "
            elif (UR1 == CR2) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[0] = " | "
            elif (UR1 == CR3) and (numof9 >= 0):
                numof9 = numof1 - 1
                winArray[0] = " | "
            elif (UR1 == CR4) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[0] = " | "
            else:
                winArray[0] = " * "

## FOR UR2
    # FOR UR2 -- 0
    if noUR2zero == False:
        if UR2 == 0:
            if (UR2 == CR2) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[1] = " = "
                noUR2one = True
                noUR2two = True
                noUR2three = True
                noUR2four = True
                noUR2five = True
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 1
    if noUR2one == False:
        if UR2 == 1:
            if (UR2 == CR2) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[1] = " = "
                noUR2two = True
                noUR2three = True
                noUR2four = True
                noUR2five = True
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 2
    if noUR2two == False:
        if UR2 == 2:
            if (UR2 == CR2) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[1] = " = "
                noUR2three = True
                noUR2four = True
                noUR2five = True
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 3
    if noUR2three == False:
        if UR2 == 3:
            if (UR2 == CR2) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[1] = " = "
                noUR2four = True
                noUR2five = True
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 4
    if noUR2four == False:
        if UR2 == 4:
            if (UR2 == CR2) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[1] = " = "
                noUR2five = True
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 5
    if noUR2five == False:
        if UR2 == 5:
            if (UR2 == CR2) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[1] = " = "
                noUR2six = True
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 6
    if noUR2six == False:
        if UR2 == 6:
            if (UR2 == CR2) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[1] = " = "
                noUR2seven = True
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 7
    if noUR2seven == False:
        if UR2 == 7:
            if (UR2 == CR2) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[1] = " = "
                noUR2eight = True
                noUR2nine = True
            elif (UR2 == CR1) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 8
    if noUR2eight == False:
        if UR2 == 8:
            if (UR2 == CR2) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[1] = " = "
                noUR2nine = True
            elif (UR2 == CR1) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

    # FOR UR2 -- 9
    if noUR2nine == False:
        if UR2 == 9:
            if (UR2 == CR2) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[1] = " = "
            elif (UR2 == CR1) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[1] = " | "
            elif (UR2 == CR3) and (numof9 >= 0):
                numof9 = numof1 - 1
                winArray[1] = " | "
            elif (UR2 == CR4) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[1] = " | "
            else:
                winArray[1] = " * "

## FOR UR3
    # FOR UR3 -- 0
    if noUR3zero == False:
        if UR3 == 0:
            if (UR3 == CR3) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[2] = " = "
                noUR3one = True
                noUR3two = True
                noUR3three = True
                noUR3four = True
                noUR3five = True
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 1
    if noUR3one == False:
        if UR3 == 1:
            if (UR3 == CR3) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[2] = " = "
                noUR3two = True
                noUR3three = True
                noUR3four = True
                noUR3five = True
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 2
    if noUR3two == False:
        if UR3 == 2:
            if (UR3 == CR3) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[2] = " = "
                noUR3three = True
                noUR3four = True
                noUR3five = True
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 3
    if noUR3three == False:
        if UR3 == 3:
            if (UR3 == CR3) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[2] = " = "
                noUR3four = True
                noUR3five = True
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 4
    if noUR3four == False:
        if UR3 == 4:
            if (UR3 == CR3) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[2] = " = "
                noUR3five = True
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 5
    if noUR3five == False:
        if UR3 == 5:
            if (UR3 == CR3) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[2] = " = "
                noUR3six = True
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 6
    if noUR3six == False:
        if UR3 == 6:
            if (UR3 == CR3) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[2] = " = "
                noUR3seven = True
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 7
    if noUR3seven == False:
        if UR3 == 7:
            if (UR3 == CR3) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[2] = " = "
                noUR3eight = True
                noUR3nine = True
            elif (UR3 == CR1) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 8
    if noUR3eight == False:
        if UR3 == 8:
            if (UR3 == CR3) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[2] = " = "
                noUR3nine = True
            elif (UR3 == CR1) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

    # FOR UR3 -- 9
    if noUR3nine == False:
        if UR3 == 9:
            if (UR3 == CR3) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[2] = " = "
            elif (UR3 == CR1) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[2] = " | "
            elif (UR3 == CR2) and (numof9 >= 0):
                numof9 = numof1 - 1
                winArray[2] = " | "
            elif (UR3 == CR4) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[2] = " | "
            else:
                winArray[2] = " * "

## FOR UR4
    # FOR UR4 -- 0
    if noUR4zero == False:
        if UR4 == 0:
            if (UR4 == CR4) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[3] = " = "
                noUR4one = True
                noUR4two = True
                noUR4three = True
                noUR4four = True
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof0 >= 0):
                numof0 = numof0 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 1
    if noUR4one == False:
        if UR4 == 1:
            if (UR4 == CR4) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[3] = " = "
                noUR4two = True
                noUR4three = True
                noUR4four = True
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof1 >= 0):
                numof1 = numof1 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 2
    if noUR4two == False:
        if UR4 == 2:
            if (UR4 == CR4) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[3] = " = "
                noUR4three = True
                noUR4four = True
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof2 >= 0):
                numof2 = numof2 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 3
    if noUR4three == False:
        if UR4 == 3:
            if (UR4 == CR4) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[3] = " = "
                noUR4four = True
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof3 >= 0):
                numof3 = numof3 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 4
    if noUR4four == False:
        if UR4 == 4:
            if (UR4 == CR4) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[3] = " = "
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof4 >= 0):
                numof4 = numof4 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 5
    if noUR4five == False:
        if UR4 == 5:
            if (UR4 == CR4) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[3] = " = "
                noUR4five = True
                noUR4six = True
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof5 >= 0):
                numof5 = numof5 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 6
    if noUR4six == False:
        if UR4 == 6:
            if (UR4 == CR4) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[3] = " = "
                noUR4seven = True
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof6 >= 0):
                numof6 = numof6 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 7
    if noUR4seven == False:
        if UR4 == 7:
            if (UR4 == CR4) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[3] = " = "
                noUR4eight = True
                noUR4nine = True
            elif (UR4 == CR1) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof7 >= 0):
                numof7 = numof7 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 8
    if noUR4eight == False:
        if UR4 == 8:
            if (UR4 == CR4) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[3] = " = "
                noUR4nine = True
            elif (UR4 == CR1) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof8 >= 0):
                numof8 = numof8 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    # FOR UR4 -- 9
    if noUR4nine == False:
        if UR4 == 9:
            if (UR4 == CR4) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[3] = " = "
                break
            elif (UR4 == CR1) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[3] = " | "
            elif (UR4 == CR2) and (numof9 >= 0):
                numof9 = numof1 - 1
                winArray[3] = " | "
            elif (UR4 == CR3) and (numof9 >= 0):
                numof9 = numof9 - 1
                winArray[3] = " | "
            else:
                winArray[3] = " * "

    noUR1zero = False
    noUR1one = False
    noUR1two = False
    noUR1three = False
    noUR1four = False
    noUR1five = False
    noUR1six = False
    noUR1seven = False
    noUR1eight = False
    noUR1nine = False

    noUR2zero = False
    noUR2one = False
    noUR2two = False
    noUR2three = False
    noUR2four = False
    noUR2five = False
    noUR2six = False
    noUR2seven = False
    noUR2eight = False
    noUR2nine = False

    noUR3zero = False
    noUR3one = False
    noUR3two = False
    noUR3three = False
    noUR3four = False
    noUR3five = False
    noUR3six = False
    noUR3seven = False
    noUR3eight = False
    noUR3nine = False

    noUR4zero = False
    noUR4one = False
    noUR4two = False
    noUR4three = False
    noUR4four = False
    noUR4five = False
    noUR4six = False
    noUR4seven = False
    noUR4eight = False
    noUR4nine = False

    # Winning the Game
    for x in range(4):
        print(winArray[x], end=" "),

    if (winArray[0] == " = ") and (winArray[0] == winArray[1]) and (winArray[1] == winArray[2]) and (winArray[2] == winArray[3]):
        win = True
        print("You guessed the code!")