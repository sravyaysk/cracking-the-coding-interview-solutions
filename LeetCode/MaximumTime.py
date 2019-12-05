def generatehrsrange():
    result = []
    for i in range(0,24):
        if(len(str(i))==1):
            result.append('0'+str(i))
        else:
            result.append(str(i))
    return result

def generateminsrange():
    result = []
    for i in range(0,60):
        if(len(str(i))==1):
            result.append('0'+str(i))
        else:
            result.append(str(i))
    return result

def getReqElements(arr,ind,num):
    result = []
    for i in arr:
        if(i[ind]==num):
            result.append(i)
    return result

def MaximumTime(time):
    hrs = time.split(':')[0]
    mins = time.split(':')[1]
    hrsrange=generatehrsrange()
    minsrange = generateminsrange()
    result = ""
    if('?' in hrs):
        if(hrs.count('?')==2):
            result += "23"
        elif(hrs.count('?')==1):
            ques_ind = hrs.index('?')
            if(ques_ind==1):
                num_ind=0
            else:
                num_ind=1
            reqhrselem = getReqElements(hrsrange, num_ind, hrs[num_ind])
            result += max(reqhrselem)
    else:
        result += hrs

    result += ":"

    if('?' in mins):
        if(mins.count('?')==2):
            result += "59"
        elif(mins.count('?')==1):
            ques_ind = mins.index('?')
            if(ques_ind==1):
                num_ind=0
            else:
                num_ind=1
            reqminselem = getReqElements(minsrange, num_ind, mins[num_ind])
            result += max(reqminselem)
    else:
        result += mins

    print(result)

def method2(time):
    dumtime=""
    if(time[0] == '?'):
        if (int(time[1]) <= int('3') or time[1] == '?'):
            dumtime += '2'
        else:
            dumtime +='1'

    if(time[1] == '?'):
        if (time[0] == '2'):
            dumtime += '3'
        else:
            dumtime +='9'

    dumtime +=":"

    if (time[3] == '?'):
        dumtime += '5'
    else:
        dumtime +=time[3]

    if (time[4] == '?'):
        dumtime += '9'
    else:
        dumtime +=time[4]

    print(dumtime)

times = ["?4:5?","23:5?","2?:22","0?:??","??:??"]
for t in times:
    #MaximumTime(t)
    method2(t)