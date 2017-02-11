# state--> string
def heuristic(state,turn):
    userscore=0
    compscore=0
    for i in state:
        if i=="P":
            compscore=compscore+1
        if i=="B":
            compscore=compscore+3
        if i=="N":
            compscore=compscore+3
        if i=="R":
            compscore=compscore+5
        if i=="Q":
            compscore=compscore+9
        if i=="p":
            userscore=userscore+1
        if i=="b":
            userscore=userscore+3
        if i=="n":
            userscore=userscore+3
        if i=="r":
            userscore=userscore+5
        if i=="q":
            userscore=userscore+9
        if i=="e":
            continue
    if turn=="user":
        return userscore-compscore
    else:
        return compscore-userscore

def move(origin,dist,state_list,piece):
    i=origin[0]
    j=origin[1]
    moves_list=[]
    if piece=="P":
        if state_list[i+1][j]=="e":
            moves_list.append((i+1,j))
        if "a"<state_list[i+1][j+1]<"z" and state_list!="e":
            moves_list.append((i+1,j+1))
        if "a"<state_list[i+1][j-1]<"z" and state_list!="e":
            moves_list.append((i+1,j-1))

    if piece == "N":
       if "a"<state_list[i-1][j-2]<"z":
           moves_list.append((i-1,j-2))
       if "a"<state_list[i+1][j-2]<"z":
           moves_list.append((i+1,j-2))
       if "a"<state_list[i-1][j+2]<"z":
           moves_list.append((i-1,j+2))
       if "a"<state_list[i+1][j+2]<"z":
           moves_list.append((i+1,j+2))
       if "a"<state_list[i-2][j-1]<"z":
           moves_list.append((i-2,j-1))
       if "a"<state_list[i-2][j+1]<"z":
           moves_list.append((i-2,j+1))
       if "a" < state_list[i -2][j -1] < "z":
           moves_list.append((i -2, j -1))
       if "a" < state_list[i -2][j +1] < "z":
           moves_list.append((i -2, j + 1))
            
            
    if piece=="B":
        k=i
        r=j
        while state_list[i-1][j+1] == "e": #/
            moves_list.append((i,j))
            i=i-1
            j=j+1
        i=k
        j=r
        
        while state_list[i+1][j-1]=="e": #/
            moves_list.append((i,j))
            i=i+1
            j=j-1
        i=k
        j=r
            
        while state_list[i-1][j-1]=="e":#\
            moves_list.append((i,j))
            i=i-1
            j=j-1
        i=k
        j=r
        
        while state_list[i+1][j+1]=="e":#\
            moves_list.append((i,j))
            i=i+1
            j=j+1
    
    if piece=="R":
        k = i
        r=j
        while state_list[i - 1][j] == "e":  # |
            moves_list.append((i, j))
            i = i - 1
        i = k
    
        while state_list[i + 1][j] == "e":  # |
            moves_list.append((i, j))
            i = i + 1
        i = k
    
        while state_list[i][j+1] == "e":  # -
            moves_list.append((i, j))
            j=j+1
        i = k
        j=r
        while state_list[i][j - 1] == "e":  # -
            moves_list.append((i, j))
            j = j - 1

    if piece == "p":
        if state_list[i - 1][j] == "e":
            moves_list.append((i - 1, j))
        if "a" < state_list[i - 1][j + 1] < "z" and state_list != "e":
            moves_list.append((i - 1, j + 1))
        if "a" < state_list[i - 1][j - 1] < "z" and state_list != "e":
            moves_list.append((i - 1, j - 1))

    if piece == "n":
        if "a" < state_list[i - 1][j - 2] < "z":
            moves_list.append((i - 1, j - 2))
        if "a" < state_list[i + 1][j - 2] < "z":
            moves_list.append((i + 1, j - 2))
        if "a" < state_list[i - 1][j + 2] < "z":
            moves_list.append((i - 1, j + 2))
        if "a" < state_list[i + 1][j + 2] < "z":
            moves_list.append((i + 1, j + 2))
        if "a" < state_list[i - 2][j - 1] < "z":
            moves_list.append((i - 2, j - 1))
        if "a" < state_list[i - 2][j + 1] < "z":
            moves_list.append((i - 2, j + 1))
        if "a" < state_list[i - 2][j - 1] < "z":
            moves_list.append((i - 2, j - 1))
        if "a" < state_list[i - 2][j + 1] < "z":
            moves_list.append((i - 2, j + 1))

    if piece == "b":
        k = i
        r = j
        while state_list[i - 1][j + 1] == "e":  # /
            moves_list.append((i, j))
            i = i - 1
            j = j + 1
        i = k
        j = r
    
        while state_list[i + 1][j - 1] == "e":  # /
            moves_list.append((i, j))
            i = i + 1
            j = j - 1
        i = k
        j = r
    
        while state_list[i - 1][j - 1] == "e":  # \
            moves_list.append((i, j))
            i = i - 1
            j = j - 1
        i = k
        j = r
    
        while state_list[i + 1][j + 1] == "e":  # \
            moves_list.append((i, j))
            i = i + 1
            j = j + 1

    if piece == "r":
        k = i
        r = j
        while state_list[i - 1][j] == "e":  # |
            moves_list.append((i, j))
            i = i - 1
        i = k
    
        while state_list[i + 1][j] == "e":  # |
            moves_list.append((i, j))
            i = i + 1
        i = k
    
        while state_list[i][j + 1] == "e":  # -
            moves_list.append((i, j))
            j = j + 1
        i = k
        j = r
        while state_list[i][j - 1] == "e":  # -
            moves_list.append((i, j))
            j = j - 1





def possible_moves(state_list,dist,turn):
    turn=0 #AI
    if turn==0:
        for i in (0,8):
            for j in range(0,8):
                if state_list[i][j] == "P":
                    piece="P"
                    move([i,j],dist,state_list,piece)
                if state_list[i][j]=="N":
                    piece="N"
                    move([i,j],dist,state_list,piece)
                if state_list[i][j]=="R":
                    piece="R"
                    move([i,j],dist,state_list,piece)
                if state_list[i][j]=="B":
                    piece="B"
                    move([i,j],dist,state_list,piece)
                if state_list[i][j]=="Q":
                    piece="Q"
                    move([i,j],dist,state_list,piece)










def minimax(depth):
    if depth==0:
        return
    for i in depth:
        if depth%2==0: #comp's turn





























































