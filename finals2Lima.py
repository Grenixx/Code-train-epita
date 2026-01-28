def list_cumulated_sum(L,inf,sup):
    sum = 0
    i = 0
    l = len(L)
    temp = []
    while i < l:
        sum += L[i]
        if sum <= sup:
            temp.append(L[i])
            i+=1
        else:
            sum -= L[i]
            i = l
            
    if inf <= sum:
        return temp
    else:
        return []
    
#L = [30,50,20,10,40]
#print(list_cumulated_sum(L,35,70))


M = [[1,2,3],[1,2,3],[1,2,3]]
M2 = [[5,5,5],[5,5,5],[5,5,5]]
def printmat(M):
    for line in M:
        for elem in line:
            print(elem, end = " ")
        print()


def init(l,c,val):
    tempMat = []
    for i in range(l):
        tempMat.append([])
        for j in range(c):
            tempMat[i].append(val)
    return tempMat

#printmat(init(5,5,0))
            
def matmult(M1,M2):
    mat = init(len(M1), len(M2[0]),0)
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                mat[i][j] += M1[i][k] * M2[k][i] 
    return mat

M2 = [[5,5,5],[5,5,1],[5,0,5]]
def gap(M):
    maxGap = M[0][0] - M[0][1]
    min, maxx = M[0][0], M[0][0]
    for li in M:
        for elem in li:
            if elem < min:
                min = elem
            elif elem > maxx:
                maxx = elem
        tempGap = maxx - min
        if tempGap > maxGap:
            maxGap = tempGap
    return maxGap

M3 = [[4,5,5],[5,5,5],[5,5,5]]

def sym(M):
    for i in range(len(M)):
        for j in range(len(M)):  
            if i!=j and M[i][j] != M[j][i]:
                return False
    return True

print(sym(M3))