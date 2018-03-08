import datetime
wholedate= datetime.datetime.now()
yr= wholedate.year
month = wholedate.month
day= wholedate.day
date= str(day) + "/" + str(month) + "/" + str(yr)
prayer_data = open("prayer_data.csv","a")
name = input("Prayed for: ").lower().title()

read = open("prayer_data.csv","r")
first =0
found =0
for line in read:
    if first ==0:
        first =1
    else:
        words= line.split(",")
        if words[0] == name:
            faith= words[1]
            found =1
if found ==0:
    print("\n\n\n")
    christian = input("Christian Y/N/Mistake:")
    if christian.upper() == "Y":
        faith = "Christian"
    elif christian.lower() == "mistake":
        name = input("Prayed for: ").lower().title()
        christian = input("Christian Y/N/Mistake:")
        if christian.upper() == "Y":
            faith = "Christian"
        else:
            faith = "Non-Christian"
    else:
        faith = "Non-Christian"
if name != "":
    prayer_data.write(name +"," +faith+","+ str(date) +'\n')
while name != "Exit":
    name = input("Prayed for: ").lower().title()
    if name != "Exit":
        read = open("prayer_data.csv","r")
        first =0
        found =0
        for line in read:
            if first ==0:
                first =1
            else:
                words= line.split(",")
                if words[0] == name:
                    faith= words[1]
                    found =1
        if found ==0:
            print("\n\n\n")
            christian = input("Christian Y/N/Mistake:")
            if christian.upper() == "Y":
                faith = "Christian"
            elif christian.lower() == "mistake":
                name = input("Prayed for: ").lower().title()
                christian = input("Christian Y/N/Mistake:")
                if christian.upper() == "Y":
                    faith = "Christian"
                else:
                    faith = "Non-Christian"
            else:
                faith = "Non-Christian"
        if name != "":
            prayer_data.write(name +"," +faith+","+ str(date) +'\n')
prayer_data.close()
