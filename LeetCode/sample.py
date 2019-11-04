#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    sumarr = []
    if(rows>=3 and cols>=3):
        for i in range(0,len(arr)-2):
            print(sumarr)
            tempi = i
            temp = []
            j = 0
            count = 1
            flag = 0
            tempj = j
            while(j <= len(arr[i])):
                if(count%4 != 0):
                    try:
                        temp.append(arr[i][j])
                    except:
                        break
                    count += 1
                elif(count%4==0):
                    if(flag==0):
                        temp.append(arr[i+1][j-2])
                        flag += 1
                        j = tempj-1
                        i = i+2
                    else:
                        j = tempj+1
                        tempj = j
                        sumarr.append(temp)
                        temp = []
                        count =1
                        flag =0
                        i = tempi
                        continue
                    count = 1

                j += 1

        resultarr = []
        for i in sumarr:
            resultarr.append(sum(i))

        return max(resultarr)
    else:
        return 0





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
