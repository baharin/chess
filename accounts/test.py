state_str="RNBQKBNR/PPPPPPPP/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/pppppppp/rnbqkbnr"


def make_matrix(state_list):
    list1 = []
    final_state_list = []
    for i in range(0, 8):
        for j in range(0, 8):
            list1.append(state_list[i][j])
        final_state_list.append(list1)
        list1 = []
    return final_state_list


def update_state_with_move(origin, state_list, move):
    k1 = origin[0]
    j1 = origin[1]
    k = move[0]
    j = move[1]
    if "a" < state_list[k1][j1] < "z" and ("A" < state_list[k][j] < "Z" or state_list[k][j] == "e"):

        piece = state_list[k1][j1]

        state_list[k1][j1] = "e"

        state_list[k][j] = piece

    elif "A" < state_list[k1][j1] < "Z" and "a" < state_list[k][j] < "z":
        piece = state_list[k1][j1]
        state_list[k1][j1] = "e"
        state_list[k][j] = piece
    return state_list

state_list=make_matrix(state_str.split("/"))
print (update_state_with_move([6,3],state_list,[5,3]))