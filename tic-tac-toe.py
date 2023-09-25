l=[1,2,3,4,5,6,7,8,9]
turn=1
over=0
def board():
    print(f' {l[0]} | {l[1]} | {l[2]}')
    print(' --|---|--')
    print(f' {l[3]} | {l[4]} | {l[5]}')
    print(' --|---|--')
    print(f' {l[6]} | {l[7]} | {l[8]}')
while True:
    board()
    if turn==1:
        x=int(input("X's Turn: "))-1
        if l[x]!='X' and l[x]!='O':
            l[x]='X'
            turn=0
    else:
        x=int(input("O's Turn: "))-1
        if l[x]!='X' and l[x]!='O':
            l[x]='O'
            turn=1
    for i in range(3):
        if l[i*3+1]==l[i*3+2]==l[i*3+3]=='X':
            board()
            print("X's won the Game !...")
            over=1
        elif l[i*3+1]==l[i*3+2]==l[i*3+3]=='O':
            board()
            print("O's won the Game !...")
            over=1
        elif l[i+1]==l[i+4]==l[i+7]=='X':
            board()
            print("X's won the Game !...")
            over=1
        elif l[i+1]==l[i+4]==l[i+7]=='O':
            board()
            print("O's won the Game !...")
            over=1
        elif l[0]==l[4]==l[8]=='X':
            board()
            print("X's won the Game !...")
            over=1
        elif l[0]==l[4]==l[8]=='O':
            board()
            print("O's won the Game !...")
            over=1
        elif l[2]==l[4]==l[6]=='X':
            board()
            print("X's won the Game !...")
            over=1
        elif l[2]==l[4]==l[6]=='O':
            board()
            print("O's won the Game !...")
            over=1
    if over==1:
        break