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

def printareTabla():
    ans = int(input("Insert the num for option:\n1.Play\n2.How to play\n\n\n"))
    if ans == 1:
        try:
            start()
        except KeyboardInterrupt:
            print("\nbye bye!\n")
            time.sleep(2)
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
    print("X insert row ")
    row = int(input())
    print("X insert column")
    column = int(input())
    checkAvailability(row, column,playerX)
    checkTablaX()

def oTurn():
    print("O insert row ")
    row = int(input())
    print("O insert column")
    column = int(input())
    checkAvailability(row, column,playerO)
    checkTablaO()

def start():
    printStart()
    for i in range(0,9):
        xTurn()
        printStart()
        oTurn()
        printStart()

def checkTablaX():
    if tabla[0][0] == tabla[0][1] == tabla[0][2] == "X" or tabla[1][0] == tabla[1][1] == tabla[1][2] == "X" or tabla[2][0] == tabla[2][1] == tabla[2][2] == "X" or tabla[0][0] == tabla[1][0] == tabla[2][0] == "X" or tabla[0][1] == tabla[1][1] == tabla[2][1] == "X" or tabla[0][2] == tabla[1][2] == tabla[2][2] == "X" or tabla[0][0] == tabla[1][1] == tabla[2][2] == "X" or tabla[0][2] == tabla[1][1] == tabla[2][0] == "X":
        print("\033[1;32;40m X wins")
        printStart()
        exit(0)

def checkTablaO():
    if tabla[0][0] == tabla[0][1] == tabla[0][2] == "O" or tabla[1][0] == tabla[1][1] == tabla[1][2] == "O" or tabla[2][0] == tabla[2][1] == tabla[2][2] == "O" or tabla[0][0] == tabla[1][0] == tabla[2][0] == "O" or tabla[0][1] == tabla[1][1] == tabla[2][1] == "O" or tabla[0][2] == tabla[1][2] == tabla[2][2] == "O" or tabla[0][0] == tabla[1][1] == tabla[2][2] == "O" or tabla[0][2] == tabla[1][1] == tabla[2][0] == "O":
        printStart()
        print("\033[1;32;40m O wins")
        exit(0)

if __name__ == "__main__":
    clearScreen()
    printareTabla()
