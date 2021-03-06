'''
Created on 22 Oct 2013

@author: Eyram
'''
import random


def printBoard(board):
    print "|"+board[1]+"|"+board[2]+"|"+board[3]+"|"
    print "--"*5
    print "|"+board[4]+"|"+board[5]+"|"+board[6]+"|"
    print "--"*5
    print "|"+board[7]+"|"+board[8]+"|"+board[9]+"|"

def starter():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "human"

def assignSymbol():
    humanSymbol = raw_input("What symbol would you like (X/O): ")
    if humanSymbol == "X":
        computerSymbol = "O"
    else:
        computerSymbol = "X"
        humanSymbol = "O"
    return humanSymbol, computerSymbol
           

def freeSlots(board):
    freeSlots = []
    for i in range(1,10):
        if board[i] == "  ":
            freeSlots.append(int(i))
        return freeSlots

def fullBoard(board):
    for i in range(1,10):
        if board[i] == "  ":
            return False
        return True
            
def winningSlots(b, s):
    return (b[1] == s and b[2] == s and b[3] == s)or(b[4] == s and b[5] == s and b[6] == s)or(b[7] == s and b[8] == s and b[9] == s)or(b[1] == s and b[5] == s and b[9] == s)or(b[3] == s and b[5] == s and b[7] == s)or(b[1] == s and b[4] == s and b[7] == s)or(b[2] == s and b[5] == s and b[8] == s)or(b[3] == s and b[6] == s and b[9] == s)



def nextTurn(turn):
    currentPlayer = starter()
    if currentPlayer == "computer":
        turn = "human"
        return turn
    else:
        turn = "computer"
        return turn

def humanPlay(board):
    move = int(raw_input("Select your move (1-9): "))
    if move in freeSlots(board):
        return move
    else:
        print "This is a list of available moves", freeSlots(board)
        move = int(raw_input("Select your move: "))
        return move

def computerPlay(board):
    move  =  random.randint(freeSlots(board))
    return move

def assignMoveToBoard(board,move,symbol):
    board[move] = symbol

def playAgain():
    answer = raw_input("Do you want to play again (Yes/No):")
    return answer.lower() == "yes"

while True:
    board = ["  "]*10
    
    printBoard(board)
    print "Welcome to a game of tic tac toe"
    
    turn = starter()
    
    humanSymbol, ComputerSymbol = assignSymbol()
    
    gamePlaying = True
    if turn == "human":
        humanPlay(board)
        move = humanPlay(board)
        assignMoveToBoard(board,move,humanSymbol)
        printBoard()
        if winningSlots(board,humanSymbol):
            printBoard()
            print"Hooray you beat the computer fella"
            gamePlaying = False
        else:
            if fullBoard(board):
                printBoard(board)
                print "This one is a tie"
            else:
                turn = "computer"
            
    else:
        print"Computer goes first"
        computerPlay(board)
        move = computerPlay(board)
        assignMoveToBoard(board,move,computerSymbol)
        printBoard(board)
        turn = nextTurn(turn)
        if winningSlots(board,computerSymbol):
            printBoard()
            print"Oopsy, the computer beat you to it"
            gamePlaying = False
        else:
            if fullBoard(board):
                printBoard(board)
                print "This one is a tie"
            else:
                turn = "human"
                
    turn = nextTurn(turn)
        
    if not playAgain():
        break
    
