import os
from shutil import copyfile
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("FootballData"):
    path = root.split(os.sep)
    #print(path)
    filepath = ''
    #filename = []
    for file in files:
        if "1-premierleague.conf.txt" == file:
            #mv file to another folder
            #copyfile(file, "FootballData/prem")

            if not (os.path.basename(root) == "2015-16" or os.path.basename(root) == "2016-17"):
                for thing in path:
                    #print(thing)
                    if filepath == '':
                        filepath = filepath + thing
                    else:
                        filepath = filepath + '/' + thing
                filepath = filepath + "/1-premierleague.conf.txt"
                #print(filepath)
                prem = open("FootballData/prem/data", "a")

                f = open(filepath, "r")
                for line in f:
                    print line
                    prem.write(line)
                f.close()
                prem.close()
                #print(file)

# up to 2014-15 (included), the premierleague tables are there.
#filename called 1-premierleague.conf.txt
