from copy import deepcopy

class Chess:
    state_list = []
    
    def __init__(self, state_str):
        self.state_list = self.make_matrix(state_str.split("/"))
        
    def heuristic(self, state):
        values={"p":-1,"r":-2, "b":-3, "k":-0, "n":-2 ,"q":-9,
                "P":1,"R":2,"B":3,"K":0,"N":2,"Q":9, "e":0}
        score=0
        for i in state:
            for j in i:
                score=score+values[j]
        return score
    
    def make_matrix(self, state_list):
        list1=[]
        final_state_list=[]
        for i in range(0,8):
            for j in range(0,8):
                list1.append(state_list[i][j])
            final_state_list.append(list1)
            list1=[]
        return final_state_list

    def make_str(self,state_list):
        return [ '/'.join (l) for l in state_list ]
    
    def move(self,origin,state_list,piece):
        i=origin[0]
        j=origin[1]
        moves_list=[]
        
        if piece=="P":
            if state_list[i+1][j]=="e" and 0<= i+1<8:
                moves_list.append((i+1,j))
            if  0<=i+1<8 and 0<=j+1<8 and "a"<state_list[i+1][j+1]<"z" and state_list[i+1][j+1]!="e" :
                moves_list.append((i+1,j+1))
            if 0<=i+1<8 and 0<=j-1<8 and "a"<state_list[i+1][j-1]<"z" and state_list[i+1][j-1]!="e" :
                moves_list.append((i+1,j-1))
        
        if piece == "N":
           if  0<=i-1<8 and 0<=j-2<8 and "a"<state_list[i-1][j-2]<"z" :
               moves_list.append((i-1,j-2))
           if  0<= i+1<8 and 0<=j-2<8 and "a"<state_list[i+1][j-2]<"z" :
               moves_list.append((i+1,j-2))
           if  0<= i-1<8 and 0<=j+2<8 and "a"<state_list[i-1][j+2]<"z":
               moves_list.append((i-1,j+2))
           if  0<=i+1<8 and 0<=j+2<8 and "a"<state_list[i+1][j+2]<"z":
               moves_list.append((i+1,j+2))
           if  0<=i+2<8 and 0<=j-1<8 and "a"<state_list[i+2][j-1]<"z":
               moves_list.append((i+2,j-1))
           if  0<=i+2<8 and 0<=j+1<8 and "a"<state_list[i+2][j+1]<"z" :
               moves_list.append((i+2,j+1))
           if  0<=i-2<8 and 0<=j-1<8 and "a" < state_list[i -2][j -1] < "z" :
               moves_list.append((i -2, j -1))
           if  0<=i-2<8 and 0<=j+1<8 and "a" < state_list[i -2][j +1] < "z" :
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
                if 0 <= i - 1 < 8 and 0 <= j + 1 < 8 and "a" < state_list[i - 1][j + 1] < "z" and state_list[i - 1][j + 1] != "e":
                    moves_list.append((i - 1, j + 1))
                    break
            i = k
            j = r
        
            while  0 <= i + 1 < 8 and 0 <= j - 1 < 8 and (state_list[i + 1][j - 1] == "e" or "a" < state_list[i + 1][j - 1] < "z"):  # /
                moves_list.append((i + 1, j - 1))
                if state_list[i + 1][j - 1] != "e":
                    break
                i = i + 1
                j = j - 1
                if 0 <= i + 1 < 8 and 0 <= j - 1 < 8 and "a" < state_list[i + 1][j - 1] < "z" and state_list[i + 1][j - 1] != "e":
                    moves_list.append((i + 1, j - 1))
                    break
            i = k
            j = r
        
            while  0 <= i - 1 < 8 and 0 <= j - 1 < 8 and (state_list[i - 1][j - 1] == "e" or "a" < state_list[i - 1][j - 1] < "z"):  # \
                moves_list.append((i - 1, j - 1))
                if state_list[i - 1][j - 1] != "e":
                    break
                i = i - 1
                j = j - 1
                if  0 <= i - 1 < 8 and 0 <= j - 1 < 8 and "a" < state_list[i - 1][j - 1] < "z" and state_list[i - 1][j - 1] != "e" :
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
                if 0 <= i + 1 < 8 and 0 <= j + 1 < 8 and "a" < state_list[i + 1][j + 1] < "z" and state_list[i + 1][j + 1] != "e" :
                    moves_list.append((i + 1, j + 1))
                    break
                    
        if piece=="R":
            k = i
            r = j
            while  0 <= i - 1 < 8 and (state_list[i - 1][j] == "e" or "a" < state_list[i - 1][j] < "z"):  # |
                moves_list.append((i - 1, j))
                if state_list[i - 1][j] != "e":
                    break
                i = i - 1
                if  0 <= i - 1 < 8 and "a" < state_list[i - 1][j] < "z" and state_list[i - 1][j] != "e":
                    moves_list.append((i - 1, j))
                    break
            i = k
            while  0 <= i + 1 < 8 and (state_list[i + 1][j] == "e" or "a" < state_list[i + 1][j] < "z") :  # |
                moves_list.append((i + 1, j))
                if state_list[i + 1][j] != "e":
                    break
                i = i + 1
                if 0 <= i + 1 < 8 and "a" < state_list[i + 1][j] < "z" and state_list[i + 1][j] != "e" :
                    moves_list.append((i + 1, j))
                    break
            i = k
        
            while 0 <= j + 1 < 8 and (state_list[i][j + 1] == "e" or "a" < state_list[i][j + 1] < "z"):  # -
                moves_list.append((i, j + 1))
                if state_list[i][j + 1] != "e":
                    break
                j = j + 1
                if  0 <= j + 1 < 8 and "a" < state_list[i][j + 1] < "z" and state_list[i][j + 1] != "e" :
                    moves_list.append((i, j + 1))
                    break
            i = k
            j = r
            while  0 <= j - 1 < 8 and (state_list[i][j - 1] == "e" or "a" < state_list[i][j - 1] < "z"):  # -
                moves_list.append((i, j - 1))
                if state_list[i][j - 1] != "e":
                    break
                j = j - 1
                if  0 <= j - 1 < 8 and "a" < state_list[i][j - 1] < "z" and state_list[i][j - 1] != "e" :
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
                if   0 <= j + 1 < 8 and "a" < state_list[i][j + 1] < "z" and state_list[i][j+1]!="e" :
                    moves_list.append((i, j + 1))
                    break
            i = k
            j = r
            while 0 <= j - 1 < 8 and (state_list[i][j - 1] == "e" or "a" < state_list[i][j - 1] < "z") :  # -
                moves_list.append((i, j - 1))
                if state_list[i][j-1]!="e":
                    break
                j = j - 1
                if  0 <= j - 1 < 8 and "a" < state_list[i][j - 1] < "z" and state_list[i][j-1]!="e" :
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
                if  0 <= i + 1 < 8 and 0 <= j + 1 < 8 and "a" < state_list[i + 1][j + 1] < "z" and state_list[i+1][j+1]!="e":
                    moves_list.append((i + 1, j + 1))
                    break
                        
                        
        if piece == "k":
            if ("A"<state_list[i - 1][j]<"Z" or state_list[i-1][j]=="e") and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
            if  0 <= i + 1 < 8 and ("A"<state_list[i + 1][j]<"Z" or state_list[i+1][j]=="e"):
                moves_list.append((i + 1, j))
            if  0 <= j + 1 < 8 and ("A"<state_list[i][j + 1] <"Z" or state_list[i][j+1]=="e"):
                moves_list.append((i, j + 1))
            if ("A"<state_list[i][j - 1] <"Z" or state_list[i][j-1]=="e") and 0 <= j - 1 < 8:
                moves_list.append((i, j - 1))
            if 0 <= i - 1 < 8 and 0 <= j + 1 < 8 and ("A"<state_list[i - 1][j + 1] <"Z" or state_list[i-1][j+1]=="e") :
                moves_list.append((i - 1, j + 1))
            if ("A"<state_list[i - 1][j - 1] <"Z" or state_list[i-1][j-1]=="e") and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i - 1, j - 1))
            if 0 <= i + 1 < 8 and 0 <= j - 1 < 8 and ("A"<state_list[i + 1][j - 1] <"Z" or state_list[i+1][j-1]=="e" ):
                moves_list.append((i + 1, j - 1))
            if 0 <= i + 1 < 8 and 0 <= j + 1 < 8 and ("A"<state_list[i + 1][j + 1]<"Z" or state_list[i+1][j+1]=="e") :
                moves_list.append((i + 1, j + 1))
    
        if piece == "p":
            if state_list[i - 1][j] == "e" and 0 <= i - 1 < 8:
                moves_list.append((i - 1, j))
            if "A" < state_list[i - 1][j - 1] < "Z" and state_list[i - 1][j - 1] != "e" and 0 <= i - 1 < 8 and 0 <= j - 1 < 8:
                moves_list.append((i + 1, j + 1))
            if 0 <= i - 1 < 8 and 0 <= j + 1 < 8 and "A" < state_list[i - 1][j + 1] < "Z" and state_list[i - 1][j + 1] != "e" :
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
            while 0 <= i + 1 < 8 and (state_list[i + 1][j] == "e" or "A" < state_list[i + 1][j] < "Z"):  # |
                moves_list.append((i + 1, j))
                if state_list[i+1][j]!="e":
                    break
                i = i + 1
                if  0<= i + 1 < 8 and "A" < state_list[i + 1][j] < "Z" and state_list[i+1][j]!="e":
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
            if  0 <= i + 1 < 8 and 0 <= j - 2 < 8 and "A" < state_list[i + 1][j - 2] < "Z" :
                moves_list.append((i + 1, j - 2))
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8 and "A" < state_list[i - 1][j + 2] < "Z":
                moves_list.append((i - 1, j + 2))
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8 and "A" < state_list[i + 1][j + 2] < "Z":
                moves_list.append((i + 1, j + 2))
            if  0 <= i + 2 < 8 and 0 <= j - 1 < 8 and "A" < state_list[i + 2][j - 1] < "Z":
                moves_list.append((i + 2, j - 1))
            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8 and "A" < state_list[i + 2][j + 1] < "Z":
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
            while  0 <= i + 1 < 8 and (state_list[i + 1][j] == "e" or "A" < state_list[i + 1][j] < "Z"):  # |
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
        
            while  0 <= i + 1 < 8 and 0 <= j - 1 < 8 and (state_list[i + 1][j - 1] == "e" or "A" < state_list[i + 1][
                    j - 1] < "Z"):  # /
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
                if  0 <= i + 1 < 8 and 0 <= j + 1 < 8 and "A" < state_list[i + 1][j + 1] < "Z" and state_list[i + 1][
                            j + 1] != "e":
                    moves_list.append((i + 1, j + 1))
                    break
            
        return moves_list
    
    def update_state_list(self,origin,state_list_copy,piece,moves):
        k1=origin[0]
        j1=origin[1]
        updated_state_list=[]
        for i in range (0,len(moves)):
            state_list = deepcopy(state_list_copy)
            k=moves[i][0]
            j=moves[i][1]
            state_list[k1][j1]="e"
            state_list[k][j]=piece
            updated_state_list.append(state_list)
        return updated_state_list
    
    def update_state_with_move(self,origin,state_list,move):
        k1 = origin[0]
        j1 = origin[1]
        k=move[0]
        j=move[1]
        if "a"<state_list[k1][j1]<"z" and ("A"<state_list[k][j]<"Z" or state_list[k][j]=="e") :
            piece=state_list[k1][j1]
            state_list[k1][j1]="e"
            state_list[k][j]=piece
        elif "A"<state_list[k1][j1]<"Z" and "a"<state_list[k][j]<"z":
            piece=state_list[k1][j1]
            state_list[k1][j1]="e"
            state_list[k][j]=piece
        return state_list
            
    def is_valid(self,origin,state_list,move):
        i= origin[0]
        j= origin[1]
        if state_list[i][j]=="e":
            return False
        else:
            piece=state_list[i][j]
            valid_moves=self.move(origin,state_list,piece)
            if move in valid_moves:
                return True
            else:
                return False
            
    def possible_moves(self,state_list,turn):
        updated_state_list=[]
        for i in range(0,8):
            for j in range(0,8):
                if turn=="AI" and state_list:
                    
                    if state_list[i][j] == "P":
                        piece="P"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="N":
                        piece="N"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="R":
                        piece="R"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="B":
                        piece="B"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="Q":
                        piece="Q"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="K":
                        piece="K"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                elif(turn == "user" and state_list):
                    
                    if state_list[i][j] == "p":
                        piece="p"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece,moves))
                        
                    if state_list[i][j]=="n":
                        piece="n"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="r":
                        piece="r"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="b":
                        piece="b"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
                    if state_list[i][j]=="q":
                        piece="q"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                    if state_list[i][j]=="k":
                        piece="k"
                        moves=self.move([i,j],state_list[:],piece)
                        updated_state_list.extend(self.update_state_list([i,j],state_list[:],piece, moves))
                        
        return updated_state_list
    
    def minimax(self,node, depth, turn):
        final_state=[]
        if depth == 0 or len(node) == 0:
            return (self.heuristic(node), None)
        if turn == "AI":
            best_value = -1000000
            for child in self.possible_moves(node, "user"):
                if(child):
                    v = self.minimax(child[:], depth - 1, "AI")[0]
                    if v>best_value:
                        best_value=v
                        final_state=child
            final_state = self.make_str(final_state)
            return (best_value,final_state)
        if turn == "user":
            best_value = 1000000
            for child in self.possible_moves(node,"AI"):
                if(child):
                    v = self.minimax(child[:], depth - 1, "user")[0]
                    if v<best_value:
                        best_value=v
                        final_state=child
            final_state= self.make_str(final_state)
            return (best_value,final_state)