from random import randrange


def displayBoard(board):
    print("+","-"*24,"+",sep="")
    for row in board:
        print("|"," "*5,"|"," "*6,"|"," "*5,"|")
        print("|"," ",row[0]," ","|"," "*2,row[1]," ","|"," ",row[2]," ","|")
        print("|"," "*5,"|"," "*6,"|"," "*5,"|")
        print("+","-"*24,"+",sep="")
def victory(computerMoves,humanMoves):
    combinations = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,5,7),(4,5,6),(7,8,9),(3,6,9)]
    flag = 0
    for rows in combinations:
        if all(move in humanMoves for move in rows):
            flag = 1
    for rows in combinations:
        if all(move in computerMoves for move in rows):
            flag =2
    return flag
def takeUser(board,humanMoves,computerMoves):    
    userInput = int(input("Enter your move>>>"))
    if(userInput< 1 and userInput >10) or userInput in \
        humanMoves or userInput in computerMoves:
        print("Invalid input")
    elif(userInput<=3):
        board[0][userInput%3-1] ='O'
    elif(userInput>3 and userInput<=6):
        board[1][userInput%3-1]='O'
    else:
        board[2][userInput%3-1]='O'
    humanMoves.append(userInput)
    displayBoard(board)
def play():   
    computerMoves = [5]
    humanMoves=[]
    board = [[1,2,3],[4,'X',6],[7,8,9]]
    
    print("Initial board: ")   
    displayBoard(board)
    while True:
        takeUser(board,humanMoves,computerMoves)
        flag = victory(computerMoves,humanMoves)
        if flag == 1:
            print("You Won!")
            break
        elif len(humanMoves)+len(computerMoves)==9:
            print("Draw!")
            break;
        else:
            random = 5
            while random in humanMoves or random in computerMoves:
                random = randrange(1,9)
            if(random<=3):
                board[0][random%3-1] ='X'
            elif(random>3 and random<=6):
                board[1][random%3-1]='X'
            else:
                board[2][random%3-1]='X'

            computerMoves.append(random)
            print("Computer chooses: ",random)
            displayBoard(board)
            flag = victory(computerMoves,humanMoves)
            if flag==2:
                print("You Lost!")
                break
            elif len(humanMoves)+len(computerMoves)==9:
                print("Draw!")
                break
            else:
                continue
play()