def isToeplitzMatrix(matrix):
    res = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            i1 = i;
            i2 = j;
            flag = 0
            while (i1 < len(matrix)-1 and i2 < len(matrix[i])-1):
                if (matrix[i1][i2] == matrix[i1 + 1][i2 + 1] and matrix[i1 + 1][i2 + 1] is not None and matrix[i1][
                    i2] is not None):
                    matrix[i1][i2]=None
                    i1 += 1
                    i2 += 1
                else:
                    if(matrix[i1 + 1][i2 + 1] is not None and matrix[i1][i2] is not None):
                        flag = 1
                        break
                    else:
                        flag=3
                        break
            if (flag == 1):
                res.append(0)
            elif(flag==0):
                matrix[i1][i2]=None
                res.append(1)
            else:
                break

    if(all(res)==1):
        return True
    else:
        return False

mat = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
isToeplitzMatrix(mat)