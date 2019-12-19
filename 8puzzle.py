def matrix_ctor():

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

def print_matrix(list):
    curr = "---MATRIX---" + '\n'

    for i in range(3):
        for j in range(3):
            curr += "[" + str(list[i][j]) + "]"
        if(j%2 == 0 and i!=2):
            curr += '\n'

    print(curr)


def possible_ways(list):
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



def get_hierarchy(matrix):
    final_state = [[1,2,3],[4,5,6],[7,8,0]]
    x = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == final_state[i][j]:
                x += 1

    return x

"""def swap(matrix,i,j):
    possible_ways(matrix)
"""



def main():
    matrix = matrix_ctor()
    print_matrix(matrix)
    possible_ways(matrix)

main()









