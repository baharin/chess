# state--> string
#class chess():
#I,J=input().split
#i,j=int(I),int(J)
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

def move(origin,state_list,piece):
    i=origin[0]
    j=origin[1]
    moves_list=[]
    
    if piece=="P":
        if state_list[i+1][j]=="e" and 0<= i+1<8:
            moves_list.append((i+1,j))
        if "a"<state_list[i+1][j+1]<"z" and state_list[i+1][j+1]!="e" and 0<=i+1<8 and 0<=j+1<8:
            moves_list.append((i+1,j+1))
        if "a"<state_list[i+1][j-1]<"z" and state_list[i+1][j-1]!="e" and 0<=i+1<8 and 0<=j-1<8:
            moves_list.append((i+1,j-1))
    
    if piece == "N":
       if "a"<state_list[i-1][j-2]<"z" and 0<=i-1<8 and 0<=j-2<8:
           moves_list.append((i-1,j-2))
       if "a"<state_list[i+1][j-2]<"z" and 0<= i+1<8 and 0<=j-2<8:
           moves_list.append((i+1,j-2))
       if  0<= i-1<8 and 0<=j+2<8 and "a"<state_list[i-1][j+2]<"z":
           moves_list.append((i-1,j+2))
       if  0<=i+1<8 and 0<=j+2<8 and "a"<state_list[i+1][j+2]<"z":
           moves_list.append((i+1,j+2))
       if "a"<state_list[i+2][j-1]<"z" and 0<=i+2<8 and 0<=j-1<8:
           moves_list.append((i+2,j-1))
       if "a"<state_list[i+2][j+1]<"z" and 0<=i+2<8 and 0<=j+1<8:
           moves_list.append((i+2,j+1))
       if "a" < state_list[i -2][j -1] < "z" and 0<=i-2<8 and 0<=j-1<8:
           moves_list.append((i -2, j -1))
       if "a" < state_list[i -2][j +1] < "z" and 0<=i-2<8 and 0<=j+1<8:
           moves_list.append((i -2, j + 1))
            
    if piece=="B":
        k = i
        r= j
        while 0 <= i - 1 < 8 and 0 <= j + 1 < 8 and (state_list[i - 1][j + 1] == "e" or "a" < state_list[i - 1][j + 1] < "z"):  # /
            moves_list.append((i - 1, j + 1))
            if state_list[i - 1][j + 1] != "e":
                break
            i = i - 1
            j = j + 1
            if "a" < state_list[i - 1][j + 1] < "z" and state_list[i - 1][j + 1] != "e" and 0 <= i - 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i - 1, j + 1))
                break
        i = k
        j = r
    
        while (state_list[i + 1][j - 1] == "e" or "a" < state_list[i + 1][j - 1] < "z") and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:  # /
            moves_list.append((i + 1, j - 1))
            if state_list[i + 1][j - 1] != "e":
                break
            i = i + 1
            j = j - 1
            if "a" < state_list[i + 1][j - 1] < "z" and state_list[i + 1][j - 1] != "e" and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i + 1, j - 1))
                break
        i = k
        j = r
    
        while (state_list[i - 1][j - 1] == "e" or "a" < state_list[i - 1][j - 1] < "z") and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:  # \
            moves_list.append((i - 1, j - 1))
            if state_list[i - 1][j - 1] != "e":
                break
            i = i - 1
            j = j - 1
            if "a" < state_list[i - 1][j - 1] < "z" and state_list[i - 1][j - 1] != "e" and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i - 1, j - 1))
                break
        i = k
        j = r
    
        while 0 <= i + 1 < 8 and 0 <= j + 1 < 8 and (state_list[i + 1][j + 1] == "e" or "a" < state_list[i + 1][j + 1] < "z"):  # \
            moves_list.append((i + 1, j + 1))
            if state_list[i + 1][j + 1] != "e":
                break
            i = i + 1
            j = j + 1
            if "a" < state_list[i + 1][j + 1] < "z" and state_list[i + 1][j + 1] != "e" and 0 <= i + 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i + 1, j + 1))
                break
                
    if piece=="R":
        k = i
        r = j
        while (state_list[i - 1][j] == "e" or "a" < state_list[i - 1][j] < "z") and 0 <= i - 1 < 8:  # |
            moves_list.append((i - 1, j))
            if state_list[i - 1][j] != "e":
                break
            i = i - 1
            if "a" < state_list[i - 1][j] < "z" and state_list[i - 1][j] != "e" and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
                break
        i = k
        while (state_list[i + 1][j] == "e" or "a" < state_list[i + 1][j] < "z") and 0 <= i + 1 < 8:  # |
            moves_list.append((i + 1, j))
            if state_list[i + 1][j] != "e":
                break
            i = i + 1
            if "a" < state_list[i + 1][j] < "z" and state_list[i + 1][j] != "e" and 0 <= i + 1 < 8:
                moves_list.append((i + 1, j))
                break
        i = k
    
        while 0 <= j + 1 < 8 and (state_list[i][j + 1] == "e" or "a" < state_list[i][j + 1] < "z"):  # -
            moves_list.append((i, j + 1))
            if state_list[i][j + 1] != "e":
                break
            j = j + 1
            if "a" < state_list[i][j + 1] < "z" and state_list[i][j + 1] != "e" and 0 <= j + 1 < 8:
                moves_list.append((i, j + 1))
                break
        i = k
        j = r
        while (state_list[i][j - 1] == "e" or "a" < state_list[i][j - 1] < "z") and 0 <= j - 1 < 8:  # -
            moves_list.append((i, j - 1))
            if state_list[i][j - 1] != "e":
                break
            j = j - 1
            if "a" < state_list[i][j - 1] < "z" and state_list[i][j - 1] != "e" and 0 <= j - 1 < 8:
                moves_list.append((i, j - 1))
                break
                
    if piece=="K":
        if "a"<state_list[i-1][j]<"z" and 0<= i-1 <8:
            moves_list.append((i-1,j))
        if "a"<state_list[i+1][j]<"z" and 0<= i+1<8:
            moves_list.append((i+1, j))
        if "a"<state_list[i][j+1]<"z" and 0<= j+1<8:
            moves_list.append((i,j+1))
        if "a"<state_list[i][j-1]<"z" and 0<= j-1 <8:
            moves_list.append((i,j-1))
        if "a"<state_list[i-1][j+1]<"z" and 0<= i-1<8 and 0<= j+1<8:
            moves_list.append((i-1,j+1))
        if "a"<state_list[i-1][j-1]<"z" and 0<= i-1 <8 and 0<= j-1<8:
            moves_list.append((i-1,j-1))
        if "a"<state_list[i+1][j-1]<"z" and 0<= i+1<8 and 0<= j-1<8:
            moves_list.append((i+1,j-1))
        if "a"<state_list[i+1][j+1]<"z" and 0<=i+1<8 and 0<=j+1<8:
            moves_list.append((i+1,j+1))
    
    if piece == "Q":
        k = i
        r = j
        while (state_list[i - 1][j] == "e" or "a" < state_list[i - 1][j] < "z") and 0 <= i - 1 < 8:  # |
            moves_list.append((i - 1, j))
            if state_list[i-1][j]!="e":
                break
            i = i - 1
            if "a" < state_list[i - 1][j] < "z" and state_list[i-1][j]!="e" and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
                break
        i = k
        while (state_list[i + 1][j] == "e" or "a" < state_list[i + 1][j] < "z") and 0 <= i + 1 < 8:  # |
            moves_list.append((i + 1, j))
            if state_list[i+1][j]!="e":
                break
            i = i + 1
            if "a" < state_list[i + 1][j] < "z" and state_list[i+1][j]!="e" and 0<= i + 1 < 8:
                moves_list.append((i + 1, j))
                break
        i = k
    
        while 0 <= j + 1 < 8 and (state_list[i][j + 1] == "e" or "a" < state_list[i][j + 1] < "z") :  # -
            moves_list.append((i, j + 1))
            if state_list[i][j+1]!="e":
                break
            j = j + 1
            if "a" < state_list[i][j + 1] < "z" and state_list[i][j+1]!="e" and  0 <= j + 1 < 8:
                moves_list.append((i, j + 1))
                break
        i = k
        j = r
        while (state_list[i][j - 1] == "e" or "a" < state_list[i][j - 1] < "z") and 0 <= j - 1 < 8:  # -
            moves_list.append((i, j - 1))
            if state_list[i][j-1]!="e":
                break
            j = j - 1
            if "a" < state_list[i][j - 1] < "z" and state_list[i][j-1]!="e" and 0 <= j - 1 < 8:
                moves_list.append((i, j - 1))
                break
                    
            #----------
        i=k
        j=r
        while  0<= i - 1 < 8 and 0 <= j + 1 < 8 and (state_list[i - 1][j + 1] == "e" or "a" < state_list[i - 1][j + 1] < "z") and 0:  # /
            moves_list.append((i - 1, j + 1))
            if state_list[i-1][j+1]!="e":
                break
            i = i - 1
            j = j + 1
            if "a" < state_list[i - 1][j + 1] < "z"and state_list[i-1][j+1]!="e" and 0 <= i - 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i - 1, j + 1))
                break
        i = k
        j = r

        while (state_list[i + 1][j - 1] == "e" or "a" < state_list[i + 1][j - 1] < "z") and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:  # /
            moves_list.append((i + 1, j - 1))
            if state_list[i+1][j-1]!="e":
                break
            i = i + 1
            j = j - 1
            if "a" < state_list[i + 1][j - 1] < "z" and state_list[i+1][j-1]!="e" and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i + 1, j - 1))
                break
        i = k
        j = r

        while (state_list[i - 1][j - 1] == "e" or "a" < state_list[i - 1][j - 1] < "z") and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:  # \
            moves_list.append((i - 1, j - 1))
            if state_list[i-1][j-1]!="e":
                break
            i = i - 1
            j = j - 1
            if "a" < state_list[i - 1][j - 1] < "z" and state_list[i-1][j-1]!="e"  and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i - 1, j - 1))
                break
        i = k
        j = r

        while  0 <= i + 1 < 8 and 0 <= j + 1 < 8 and (state_list[i + 1][j + 1] == "e" or "a" < state_list[i + 1][j + 1] < "z"):  # \
            moves_list.append((i + 1, j + 1))
            if state_list[i+1][j+1]!="e":
                break
            i = i + 1
            j = j + 1
            if "a" < state_list[i + 1][j + 1] < "z" and state_list[i+1][j+1]!="e" and 0 <= i + 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i + 1, j + 1))
                break
                    
                    
    if piece == "k":
        if ("A"<state_list[i - 1][j]<"Z" or state_list[i-1][j]=="e") and 0 <= i - 1 < 8:
            moves_list.append((i - 1, j))
        if ("A"<state_list[i + 1][j]<"Z" or state_list[i+1][j]=="e")and 0 <= i + 1 < 8:
            moves_list.append((i + 1, j))
        if ("A"<state_list[i][j + 1] <"Z" or state_list[i][j+1]=="e")  and 0 <= j + 1 < 8:
            moves_list.append((i, j + 1))
        if ("A"<state_list[i][j - 1] <"Z" or state_list[i][j-1]=="e") and 0 <= j - 1 < 8:
            moves_list.append((i, j - 1))
        if ("A"<state_list[i - 1][j + 1] <"Z" or state_list[i-1][j+1]=="e") and 0 <= i - 1 < 8 and 0 <= j + 1 < 8:
            moves_list.append((i - 1, j + 1))
        if ("A"<state_list[i - 1][j - 1] <"Z" or state_list[i-1][j-1]=="e") and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
            moves_list.append((i - 1, j - 1))
        if ("A"<state_list[i + 1][j - 1] <"Z" or state_list[i+1][j-1]=="e" )and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:
            moves_list.append((i + 1, j - 1))
        if ("A"<state_list[i + 1][j + 1]<"Z" or state_list[i+1][j+1]=="e") and 0 <= i + 1 < 8 and 0 <= j + 1 < 8:
            moves_list.append((i + 1, j + 1))

    if piece == "p":
        if state_list[i - 1][j] == "e" and 0 <= i - 1 < 8:
            moves_list.append((i - 1, j))
        if "A" < state_list[i - 1][j - 1] < "Z" and state_list[i - 1][j - 1] != "e" and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
            moves_list.append((i + 1, j + 1))
        if "A" < state_list[i - 1][j + 1] < "Z" and state_list[i - 1][j + 1] != "e" and 0 <= i - 1 < 8 and 0 <= j + 1 < 8:
            moves_list.append((i - 1, j + 1))

    if piece == "r":
        k = i
        r = j
        while (state_list[i - 1][j] == "e" or "A" < state_list[i - 1][j] < "Z") and 0 <= i - 1 < 8:  # |
            moves_list.append((i - 1, j))
            if state_list[i-1][j]!="e":
                break
            i = i - 1
            if "A" < state_list[i - 1][j] < "Z" and state_list[i-1][j]!="e" and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
                break
        i = k
        while (state_list[i + 1][j] == "e" or "A" < state_list[i + 1][j] < "Z") and 0 <= i + 1 < 8:  # |
            moves_list.append((i + 1, j))
            if state_list[i+1][j]!="e":
                break
            i = i + 1
            if "A" < state_list[i + 1][j] < "Z" and state_list[i+1][j]!="e" and 0<= i + 1 < 8:
                moves_list.append((i + 1, j))
                break
        i = k
    
        while 0 <= j + 1 < 8 and (state_list[i][j + 1] == "e" or "A" < state_list[i][j + 1] < "Z") :  # -
            moves_list.append((i, j + 1))
            if state_list[i][j+1]!="e":
                break
            j = j + 1
            if "A" < state_list[i][j + 1] < "Z" and state_list[i][j+1]!="e" and  0 <= j + 1 < 8:
                moves_list.append((i, j + 1))
                break
        i = k
        j = r
        while (state_list[i][j - 1] == "e" or "A" < state_list[i][j - 1] < "Z") and 0 <= j - 1 < 8:  # -
            moves_list.append((i, j - 1))
            if state_list[i][j-1]!="e":
                break
            j = j - 1
            if "A" < state_list[i][j - 1] < "Z" and state_list[i][j-1]!="e" and 0 <= j - 1 < 8:
                moves_list.append((i, j - 1))
                break
                
                
    if piece == "n":
        if "A" < state_list[i - 1][j - 2] < "Z" and 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
            moves_list.append((i - 1, j - 2))
        if "A" < state_list[i + 1][j - 2] < "Z" and 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
            moves_list.append((i + 1, j - 2))
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8 and "A" < state_list[i - 1][j + 2] < "Z":
            moves_list.append((i - 1, j + 2))
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8 and "A" < state_list[i + 1][j + 2] < "Z":
            moves_list.append((i + 1, j + 2))
        if "A" < state_list[i + 2][j - 1] < "Z" and 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
            moves_list.append((i + 2, j - 1))
        if "A" < state_list[i + 2][j + 1] < "Z" and 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            moves_list.append((i + 2, j + 1))
        if "A" < state_list[i - 2][j - 1] < "Z" and 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
            moves_list.append((i - 2, j - 1))
        if "A" < state_list[i - 2][j + 1] < "Z" and 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            moves_list.append((i - 2, j + 1))
    
    if piece == "q":
        k = i
        r = j
        while (state_list[i - 1][j] == "e" or "A" < state_list[i - 1][j] < "Z") and 0 <= i - 1 < 8:  # |
            moves_list.append((i - 1, j))
            if state_list[i - 1][j] != "e":
                break
            i = i - 1
            if "A" < state_list[i - 1][j] < "Z" and state_list[i - 1][j] != "e" and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
                break
        i = k
        while (state_list[i + 1][j] == "e" or "A" < state_list[i + 1][j] < "Z") and 0 <= i + 1 < 8:  # |
            moves_list.append((i + 1, j))
            if state_list[i + 1][j] != "e":
                break
            i = i + 1
            if "A" < state_list[i + 1][j] < "Z" and state_list[i + 1][j] != "e" and 0 <= i + 1 < 8:
                moves_list.append((i + 1, j))
                break
        i = k
    
        while 0 <= j + 1 < 8 and (state_list[i][j + 1] == "e" or "A" < state_list[i][j + 1] < "Z"):  # -
            moves_list.append((i, j + 1))
            if state_list[i][j + 1] != "e":
                break
            j = j + 1
            if "A" < state_list[i][j + 1] < "Z" and state_list[i][j + 1] != "e" and 0 <= j + 1 < 8:
                moves_list.append((i, j + 1))
                break
        i = k
        j = r
        while (state_list[i][j - 1] == "e" or "A" < state_list[i][j - 1] < "Z") and 0 <= j - 1 < 8:  # -
            moves_list.append((i, j - 1))
            if state_list[i][j - 1] != "e":
                break
            j = j - 1
            if "A" < state_list[i][j - 1] < "Z" and state_list[i][j - 1] != "e" and 0 <= j - 1 < 8:
                moves_list.append((i, j - 1))
                break

                # ----------
        i = k
        j = r
        while 0 <= i - 1 < 8 and 0 <= j + 1 < 8 and (
                state_list[i - 1][j + 1] == "e" or "A" < state_list[i - 1][j + 1] < "Z") and 0:  # /
            moves_list.append((i - 1, j + 1))
            if state_list[i - 1][j + 1] != "e":
                break
            i = i - 1
            j = j + 1
            if "A" < state_list[i - 1][j + 1] < "Z" and state_list[i - 1][
                        j + 1] != "e" and 0 <= i - 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i - 1, j + 1))
                break
        i = k
        j = r
    
        while (state_list[i + 1][j - 1] == "e" or "A" < state_list[i + 1][
                j - 1] < "Z") and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:  # /
            moves_list.append((i + 1, j - 1))
            if state_list[i + 1][j - 1] != "e":
                break
            i = i + 1
            j = j - 1
            if "A" < state_list[i + 1][j - 1] < "Z" and state_list[i + 1][
                        j - 1] != "e" and 0 <= i + 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i + 1, j - 1))
                break
        i = k
        j = r
    
        while (state_list[i - 1][j - 1] == "e" or "A" < state_list[i - 1][
                j - 1] < "Z") and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:  # \
            moves_list.append((i - 1, j - 1))
            if state_list[i - 1][j - 1] != "e":
                break
            i = i - 1
            j = j - 1
            if "A" < state_list[i - 1][j - 1] < "Z" and state_list[i - 1][
                        j - 1] != "e" and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i - 1, j - 1))
                break
        i = k
        j = r
    
        while 0 <= i + 1 < 8 and 0 <= j + 1 < 8 and (
                state_list[i + 1][j + 1] == "e" or "A" < state_list[i + 1][j + 1] < "Z"):  # \
            moves_list.append((i + 1, j + 1))
            if state_list[i + 1][j + 1] != "e":
                break
            i = i + 1
            j = j + 1
            if "A" < state_list[i + 1][j + 1] < "Z" and state_list[i + 1][
                        j + 1] != "e" and 0 <= i + 1 < 8 and 0 <= j + 1 < 8:
                moves_list.append((i + 1, j + 1))
                break
        
    return moves_list




def possible_moves(state_list):
    for i in (0,8):
        for j in range(0,8):
            if state_list[i][j] == "P":
                piece="P"
                print (move([i,j],state_list,piece))
            if state_list[i][j]=="N":
                piece="N"
                print(move([i,j],state_list,piece))
            if state_list[i][j]=="R":
                piece="R"
                print(move([i,j],state_list,piece))
            if state_list[i][j]=="B":
                piece="B"
                print (move([i,j],state_list,piece))
            if state_list[i][j]=="Q":
                piece="Q"
                print(move([i,j],state_list,piece))
state_list=["PebeeeNe","eRePpeeQ","perepebe","npPePeeR","qeBKenpe","ePeerPep","kepPeeee","NeeeBPep"]

print (move([6,0],state_list,"k"))