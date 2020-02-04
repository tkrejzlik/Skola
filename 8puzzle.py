MAX_ITERATIONS = 1000
import copy
def matrix_ctor(): #vytvareni uvodni matice

    real=[]
    pom = 1
    for i in range(3):
        curr = []
        for j in range(3):
            cislo = int(input("zadej " + str(pom) + ". cislo do matice: "))
            curr.append(cislo)
            pom+=1
        real.append(curr)

    return real

def print_matrix(list): #tisk matice
    curr = "---MATRIX---" + '\n'

    for i in range(3):
        for j in range(3):
            curr += "[" + str(list[i][j]) + "]"
        if(j%2 == 0 and i!=2):
            curr += '\n'

    print(curr)

def possible_ways(list): #vrací seznam s možnými moves
    actual_i = 0
    actual_j = 0
    location = []
    moves = [[-1,0],[0,-1],[0,1],[1,0]]#top,left,right,bottom
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if list[i][j] == 0:
                actual_i = i
                actual_j = j

    location.append(actual_i)
    location.append(actual_j)


    for x in range(len(moves)):

        if location[0] + moves[x][0] <=2 and location[0] + moves[x][0]  >= 0 and location[1] + moves[x][1] >=0 and location[1] + moves[x][1] <=2:
            cur_i = location[0] + moves[x][0]
            cur_j = location[1] + moves[x][1]
            mini_move = []
            mini_move.append(cur_i)
            mini_move.append(cur_j)
            possible_moves.append(mini_move)
    return possible_moves



def get_hierarchy(list): #vrací hierarchii
    final_state = [[1,2,3],[4,5,6],[7,8,0]]
    x = 0
    for i in range(3):
        for j in range(3):
            if list[i][j] == final_state[i][j]:
                x += 1

    return x

def swap(ct_matrix,i,j): #swap 0 a cisla na miste, kam lze vlozit 0
    for x in range(3):
        for y in range(3):
            if ct_matrix[x][y] == 0:
                actual_i = x #lokace 0
                actual_j = y #lokace 0
    current = ct_matrix[i][j]
    ct_matrix[actual_i][actual_j] = current
    ct_matrix[i][j] = 0

def solve(matrix):
    iter_count = 0
    final_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    while matrix != final_state and iter_count < MAX_ITERATIONS:
        best_place = -1
        best_hierarchy = 0
        for i in range(len(possible_ways(matrix))):
            new_list = copy.deepcopy(matrix)
            loc_i = possible_ways(new_list)[i][0]
            loc_j = possible_ways(new_list)[i][1]
            swap(new_list,loc_i,loc_j)
            if get_hierarchy(new_list) > best_hierarchy:
                best_hierarchy = get_hierarchy(new_list)
                best_place = i
        swap(matrix,possible_ways(matrix)[best_place][0],possible_ways(matrix)[best_place][1])
        print_matrix(matrix)
        iter_count += 1

def main():
    matrix = matrix_ctor()
    print_matrix(matrix)
    solve(matrix)


main()
