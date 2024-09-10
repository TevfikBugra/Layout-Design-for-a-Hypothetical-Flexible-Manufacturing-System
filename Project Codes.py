#1st state

#2nd state
#from_to_matrix=[[7, 0, 0, 0, 13, 0, 0, 0], [0, 0, 5, 3, 0, 5, 2, 0], [0, 0, 0, 2, 5, 0, 0, 0], [5, 5, 0, 1, 0, 2, 6, 0], [3, 2, 1, 0, 8, 4, 5, 0], [0, 0, 13, 8, 0, 0, 0, 5], [0, 0, 0, 4, 0, 0, 0, 9], [0, 0, 0, 5, 0, 2, 0, 6]]
#3rd state
#from_to_matrix=[[7, 0, 0, 0, 0, 0, 13, 0], [0, 0, 5, 3, 2, 5, 0, 0], [0, 0, 0, 2, 0, 0, 5, 0], [5, 5, 0, 1, 6, 2, 0, 0], [3, 2, 1, 0, 5, 4, 8, 0], [0, 0, 0, 5, 0, 2, 0, 6], [0, 0, 0, 4, 0, 0, 0, 9], [0, 0, 13, 8, 0, 0, 0, 5]]
#4th state
#from_to_matrix=[[0, 0, 7, 0, 0, 0, 13, 0], [0, 5, 5, 1, 6, 2, 0, 0], [0, 0, 0, 2, 0, 0, 5, 0], [5, 0, 0, 3, 2, 5, 0, 0], [1, 2, 3, 0, 5, 4, 8, 0], [0, 0, 0, 5, 0, 2, 0, 6], [0, 0, 0, 4, 0, 0, 0, 9], [13, 0, 0, 8, 0, 0, 0, 5]]
#5th state
#from_to_matrix=[[0, 0, 7, 13, 0, 0, 0, 0], [0, 5, 5, 0, 6, 2, 1, 0], [0, 0, 0, 5, 0, 0, 2, 0], [5, 0, 0, 0, 2, 5, 3, 0], [13, 0, 0, 0, 0, 0, 8, 5], [0, 0, 0, 0, 0, 2, 5, 6], [0, 0, 0, 0, 0, 0, 4, 9], [1, 2, 3, 8, 5, 4, 0, 0]]
#6th state
#from_to_matrix=[[0, 0, 7, 13, 0, 0, 0, 0], [0, 2, 3, 8, 5, 4, 1, 0], [2, 0, 0, 5, 0, 0, 0, 0], [3, 0, 0, 0, 2, 5, 5, 0], [8, 0, 0, 0, 0, 0, 13, 5], [5, 0, 0, 0, 0, 2, 0, 6], [4, 0, 0, 0, 0, 0, 0, 9], [1, 5, 5, 0, 6, 2, 0, 0]]
#from: [0]=Receiving, [1]=VTC1, [2]=UMC, [3]=SHP, [4]=HMC, [5]=VTC2, [6]=CB, [7]=VMC
#to: [0]=VTC1, [1]=UMC, [2]=SHP, [3]=HMC, [4]=VTC2, [5]=CB, [6]=VMC, [7]=Shipping

from_to_matrix=[[7,0,0,0,13,0,0,0],[0,0,5,5,0,3,2,0],[0,0,0,0,5,2,0,0],[5,5,0,2,0,1,6,0],
[0,0,0,0,0,4,0,9],[0,0,13,0,0,8,0,5],[3,2,1,4,8,0,5,0],[0,0,0,2,0,5,0,6]]
distance_matrix=[[6,18,6,12,24,18,24,30],[30,6,30,12,24,18,24,30],[54,66,54,0,48,66,12,30],[18,30,18,24,12,6,12,18],
[48,60,48,54,42,60,6,24],[30,42,30,36,0,42,48,6],[30,42,30,36,24,42,48,6],[36,48,36,42,30,48,54,12]]

def cost_finder(ftm,dm):
    cost = 0
    for i in range(0,8):
        for j in range(0,8):
            cost += ftm[i][j]*dm[i][j] 
    return cost

def row_column_changer(k,l,matrix):
    #since you cannot change receving, available numbers for k>=1, l>=1
    for i in range(0,8):
        a = int()
        a = matrix[i][k-1]
        matrix[i][k-1] = matrix[i][l-1]
        matrix[i][l-1] = a
    
    b = int()
    b = matrix[k]
    matrix[k] = matrix [l]
    matrix[l] = b

    return matrix
    
combinations_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,3),(2,4),(2,5),(2,6),(2,7),
(3,4),(3,5),(3,6),(3,7),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)]

print(cost_finder(from_to_matrix,distance_matrix),"no change")
for x,y in combinations_list:
    print(cost_finder(row_column_changer(x,y,from_to_matrix),distance_matrix),(x,y))
    from_to_matrix=[[7,0,0,0,13,0,0,0],[0,0,5,5,0,3,2,0],[0,0,0,0,5,2,0,0],
    [5,5,0,2,0,1,6,0],[0,0,0,0,0,4,0,9],[0,0,13,0,0,8,0,5],[3,2,1,4,8,0,5,0],[0,0,0,2,0,5,0,6]]
    #from_to_matrix=[[7, 0, 0, 0, 13, 0, 0, 0], [0, 0, 5, 3, 0, 5, 2, 0], [0, 0, 0, 2, 5, 0, 0, 0], [5, 5, 0, 1, 0, 2, 6, 0], [3, 2, 1, 0, 8, 4, 5, 0], [0, 0, 13, 8, 0, 0, 0, 5], [0, 0, 0, 4, 0, 0, 0, 9], [0, 0, 0, 5, 0, 2, 0, 6]]
    #from_to_matrix=[[7, 0, 0, 0, 0, 0, 13, 0], [0, 0, 5, 3, 2, 5, 0, 0], [0, 0, 0, 2, 0, 0, 5, 0], [5, 5, 0, 1, 6, 2, 0, 0], [3, 2, 1, 0, 5, 4, 8, 0], [0, 0, 0, 5, 0, 2, 0, 6], [0, 0, 0, 4, 0, 0, 0, 9], [0, 0, 13, 8, 0, 0, 0, 5]]
    #from_to_matrix=[[0, 0, 7, 0, 0, 0, 13, 0], [0, 5, 5, 1, 6, 2, 0, 0], [0, 0, 0, 2, 0, 0, 5, 0], [5, 0, 0, 3, 2, 5, 0, 0], [1, 2, 3, 0, 5, 4, 8, 0], [0, 0, 0, 5, 0, 2, 0, 6], [0, 0, 0, 4, 0, 0, 0, 9], [13, 0, 0, 8, 0, 0, 0, 5]]
    #from_to_matrix=[[0, 0, 7, 13, 0, 0, 0, 0], [0, 5, 5, 0, 6, 2, 1, 0], [0, 0, 0, 5, 0, 0, 2, 0], [5, 0, 0, 0, 2, 5, 3, 0], [13, 0, 0, 0, 0, 0, 8, 5], [0, 0, 0, 0, 0, 2, 5, 6], [0, 0, 0, 0, 0, 0, 4, 9], [1, 2, 3, 8, 5, 4, 0, 0]]
    #from_to_matrix=[[0, 0, 7, 13, 0, 0, 0, 0], [0, 2, 3, 8, 5, 4, 1, 0], [2, 0, 0, 5, 0, 0, 0, 0], [3, 0, 0, 0, 2, 5, 5, 0], [8, 0, 0, 0, 0, 0, 13, 5], [5, 0, 0, 0, 0, 2, 0, 6], [4, 0, 0, 0, 0, 0, 0, 9], [1, 5, 5, 0, 6, 2, 0, 0]]