import time
import platform
import os

SYSTEM=platform.system()

def clearScreen():
	if SYSTEM == "Linux":
    		os.system("clear")
	elif SYSTEM == "Windows":
    		os.system("cls")
	elif SYSTEM == "Darwin":
    		os.system("clear")

defaultTable=[["00","01","02"],
                ["10","11","12"],
                ["20","21","22"],]

tabla=[[' ',' ',' '],
       [' ',' ',' '],
       [' ' ,' ',' '],]

playerX = "X"
playerO = "O"
moves = 0
def printareTabla():
    ans = int(input("Insert the num for option:\n1.Play\n2.How to play\n\n\n"))
    if ans == 1:
        try:
            start()
        except KeyboardInterrupt:
            print("\nbye bye!\n")
            time.sleep(1)
	    clearScreen()
            exit(0)
       # start()
    elif ans == 2:
        printDefault()
        print("\n1.Return\n2.Exit\n")
        ret = int(input())
        if ret == 1:
            print("ok lets start")
            start()
        elif ret == 2:
            print("See you soon!")
            exit(0)

def printStart():
    for j in tabla:
        print(j)
def printDefault():
    for i in defaultTable:
        print(i)

#def checkValue(row,column,player):
#    rowType = type(row)
#    columnType = type(column)
#    print(rowType,columnType) * 3
#    try:
#        convertRow = int(row)
#        convertColumn = int(column)
#    except ValueError:
#        print("wrong dataType")
#        if player == "X":
#            xTurn()
#        elif player == "O":
#            oTurn()

def checkAvailability(linie,coloana,player):
    if not tabla[linie][coloana] == " ":
        print("\nPosition already busy, select other position\n")
        if player == "X":
            xTurn()
        else:
            oTurn()
    else:
        if player == "X":
            miscareX(linie,coloana)
        elif player == "O":
            miscareO(linie,coloana)

def miscareX(linie, coloana):
    tabla[linie][coloana] = "X"

def miscareO(linie, coloana):
    tabla[linie][coloana] = "O"

def xTurn():
    global moves
    print("X insert row ")
    row = input()
    print("X insert column")
    column = input()
#    checkValue(row,column,playerX)
    checkAvailability(row, column,playerX)
    moves +=1
    checkTablaX()

def oTurn():
    global moves
    print("O insert row ")
    row = input()
    print("O insert column")
    column = input()
#    checkValue(row,column,playerO)
    checkAvailability(row, column,playerO)
    moves += 1
    checkTablaO()

def start():
    printStart()
    for i in range(0,9):
        xTurn()
        printStart()
        oTurn()
        printStart()

def checkTablaX():
    global moves
    if tabla[0][0] == tabla[0][1] == tabla[0][2] == "X" or tabla[1][0] == tabla[1][1] == tabla[1][2] == "X" or tabla[2][0] == tabla[2][1] == tabla[2][2] == "X" or tabla[0][0] == tabla[1][0] == tabla[2][0] == "X" or tabla[0][1] == tabla[1][1] == tabla[2][1] == "X" or tabla[0][2] == tabla[1][2] == tabla[2][2] == "X" or tabla[0][0] == tabla[1][1] == tabla[2][2] == "X" or tabla[0][2] == tabla[1][1] == tabla[2][0] == "X":
        printStart()
        print("\033[1;32;40m X wins")
	exit(0)
    elif moves == 9:
        printStart()
        print("\033[1;32;40m TIE")
        exit(0)

def checkTablaO():
    global moves
    if tabla[0][0] == tabla[0][1] == tabla[0][2] == "O" or tabla[1][0] == tabla[1][1] == tabla[1][2] == "O" or tabla[2][0] == tabla[2][1] == tabla[2][2] == "O" or tabla[0][0] == tabla[1][0] == tabla[2][0] == "O" or tabla[0][1] == tabla[1][1] == tabla[2][1] == "O" or tabla[0][2] == tabla[1][2] == tabla[2][2] == "O" or tabla[0][0] == tabla[1][1] == tabla[2][2] == "O" or tabla[0][2] == tabla[1][1] == tabla[2][0] == "O":
        printStart()
        print("\033[1;32;40m O wins")
        exit(0)
    elif moves == 9:
        printStart()
        print("\033[1;32;40m TIE")
        exit(0)
if __name__ == "__main__":
    clearScreen()
    printareTabla()
