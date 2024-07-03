import sqlite3
import os
from main import file_hash
dir=os.getcwd()

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_md5 = file_hash(file_path, 'md5')
            file_sha256 = file_hash(file_path, 'sha256')

            if check_exist(file_md5)==1:
                print(f"Malicious file detected: {file_path}")
                consent=input(f"Wanna delete {file_path}?(y/n)")
                if consent=="y":
                    os.remove(file_path)
                else:
                    continue
                return 1
            else:
                print(f"{file_path} is clean.....")
    return 0

db_file = fr"{dir}\HashDB"
hashes = sqlite3.connect(db_file)
db_cursor = hashes.cursor()

def check_exist(target_hash):
    exist = db_cursor.execute(fr"SELECT hash FROM HashDB where hash='{target_hash}'").fetchall()
    if exist != []:
        return 1
check=0
consent=input("Want to deepscan directory of file[d/f]: ")
if consent=="d":
    directory=input("Enter your directory path: ")
    scan_directory(directory)
    if scan_directory(directory)==0:
        print("Your Directory is clean............")
elif consent=="f":
    file_path=input("Enter your file path: ")
    f_hash=file_hash(file_path)
    if check_exist(f_hash)==1:
        virus=input("your file is malicious wanna delete? [y/n]")
        if virus=="y":
            os.remove(file_path)
        else:
            print("Thanks for scanning.....")
    else:
        print("Your file is clean....")

# check_exist("f4c3fa43b5bdfaa0205990d25ce51c5a")
