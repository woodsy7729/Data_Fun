
import os
def add_category(category, cat_type="main"):
    if cat_type == "main":
        file_path = "/mnt/c/Users/woods/Google Drive/dreamteam/jamies_stuff/Prayer/" + category
        try:
            os.mkdir(file_path)
        except:
            print("Exists")

    else:
        file_path_1 = "/mnt/c/Users/woods/Google Drive/dreamteam/jamies_stuff/Prayer/" + cat_type
        file_path_2 = file_path_1 +"/"+category
        try:
            os.mkdir(file_path_1)
        except:
            print("Exists")
        try:
            os.mkdir(file_path_2)
        except:
            print("Exists")
        #navigate to Prayer folder and make new folder
        #what if multi-level files like People->Christian->Gibbs
print("0 to terminate")
print("main category, sub if needed")
while True:
    words = raw_input()
    if words == "0":
        break
    words= words.split(" ")
    if len(words) ==1:
        add_category(words[0])
    if len(words) ==2:
        add_category(words[1], words[0])
