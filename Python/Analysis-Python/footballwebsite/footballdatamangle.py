f = open("FootballData/prem/rawdata", "r")
linenum =0
rand =0
'''
This function checks the first element in a given string, to see if it is an integer.
If the string consists of a non-integer item, False is returned.

'''
def isInt(string):
    try:
        int(string[0])
        return True
    except ValueError:
        return False
tosort = []
for line in f:
    linenum+=1
    newline = line.split()
    if "English Premier League" in line:
        year = newline[3]
    if len(newline) > 7:
        #print(year)
        positionunformat = list(newline[0])
        positionlist = positionunformat[:-1]
        position = ''
        for thing in positionlist:
            position+=thing
        # testing where the teamnam
        if newline[2] == '38' or newline[2] == '42':
            teamname = newline[1]
            #print("OneWords\n")
            #teamname is one word
        elif newline[3] == '38' or newline[3] == '42':
            teamname = newline[1] +  newline[2]
            #print("TwoWords\n")
            #teamname is 2 words
        elif newline[4] == '38' or newline[4] == '42':
            teamname = newline[1]  + newline[2] + newline[3]
            #print("ThreeWords\n")
            #teamname is 3 words
        else:
            teamname=""
        isint = isInt(newline[-1])
        if isint: #is true, therefore its an int
            points = newline[-1]
        else:
            points = newline[-2]
        if year == '2014/15':
            print(points)
        sqlline = year + ' '+position + ' ' +teamname + ' ' +points
        tosort.append(sqlline)
        #print(tosort)
        #print(sqlline) # sort based off sql line
#sort based off year
f.close()
ordereddata = tosort.sort(key=lambda x: x.split(" " )[0])
send = open("FootballData/prem/refineddata", "w")
for thing in tosort:
    send.write(thing)
    send.write('\n')
send.close()
