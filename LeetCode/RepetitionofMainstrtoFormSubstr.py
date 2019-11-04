def FindRepetition(mainstr,substr,count):
    tempstr = mainstr*count
    if(tempstr==substr):
        return 1
    elif(set(tempstr)!=set(substr)):
        return -1
    elif(substr in tempstr):
        return count
    else:
        return FindRepetition(mainstr,substr,count+1)

mainstr="abcd"
substr="cdabcdab"
count = 1
print(FindRepetition(mainstr,substr,count))