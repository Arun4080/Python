def display_board(board):
	print("",board[0],"|",board[1],"|",board[2],"\n-----------\n",board[3],"|",board[4],"|",board[5],"\n-----------\n",board[6],"|",board[7],"|",board[8],"\n"*3)


def Assign(n,p):
        if board[n]==' ' and n < 9 and n>-1 :
                board[n]=p
                display_board(board)
        else:
                n1=int(input('Check your position and try again: '))
                Assign(n1,p)

def won_check(board,marker):
        if (board[0]==board[1]==board[2]==marker) or (board[3]==board[4]==board[5]==marker) or (board[6]==board[7]==board[8]==marker) or (board[0]==board[3]==board[6]==marker) or (board[1]==board[4]==board[7]==marker) or (board[2]==board[5]==board[8]==marker) or (board[0]==board[4]==board[8]==marker) or (board[2]==board[4]==board[6]==marker):
                return True
        else:return False

while 1:
        player1='a'
        while player1 not in ['X','O']:
                player1=input("you want to take X or O: ")
        player2=list(set(['X','O'])-set(player1))[0]
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

        for i in range(5):
                n1=int(input("which box you wana mark player1 (1-9): "))
                Assign(n1-1,player1)
                if won_check(board,player1)==True:
                        print("player1 Won !!")
                        break
                if i==4:
                        print("Its a Tie")
                        break
                n2=int(input("which box you wana mark player2 (1-9): "))
                Assign(n2-1,player2)
                if won_check(board,player2)==True:
                        print("player2 Won !!")
                        break
        if input('Wana Play Again (y/n)')!='y':
                break



