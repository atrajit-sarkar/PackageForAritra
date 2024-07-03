import hashlib
import os
import os


#Making file hashesh.......
def file_hash(filename, method='md5'):
    """Generate a hash for a file."""
    hash_func = getattr(hashlib, method)()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

#Directory scanner.......
def scan_directory(directory):
    """Scan a directory for files with known malicious hashes."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_md5 = file_hash(file_path, 'md5')
            file_sha256 = file_hash(file_path, 'sha256')

            if file_md5 in KNOWN_HASHES['md5'] or file_sha256 in KNOWN_HASHES['sha256']:
                print(f"Malicious file detected: {file_path}")
                return 1
            else:
                print(f"{file_path} is clean.....")
    return 0
#File scanner..........
def scan_file(file_path):
    file_md5 = file_hash(file_path, 'md5')
    file_sha256 = file_hash(file_path, 'sha256')

    if file_md5 in KNOWN_HASHES['md5'] or file_sha256 in KNOWN_HASHES['sha256']:
        print(f"Malicious file detected: {file_path}")
        return 1
    else:
        print(f"{file_path} is clean.....")
        return 0


if __name__=='__main__':
    dir=os.getcwd()

    #Making Database of SHA256-Hashfiles....
    sha256=[]
    database=os.listdir(fr"{dir}\hard_signatures")
    for data in database:
        with open(fr"{dir}\hard_signatures\{data}") as f:
            lines = [line.rstrip() for line in f]
        for line in lines:
            sha256.append(line.split(";")[0])


    # Define the directory to scan and the known malicious hashes
    KNOWN_HASHES = {
        'md5': ['known_bad_md5_hash1', 'known_bad_md5_hash2'],
        'sha256': sha256
    }

    #Sarting Scanner Function......



    # Run the scan........
    consent=input("Want to scan whole directory or a single file(d/f): ")
    if consent=="d":
        DIRECTORY_TO_SCAN =input("Enter your directory: ")
        print("Scan started.Please Wait....")
        scan_directory(DIRECTORY_TO_SCAN)

        if scan_directory(DIRECTORY_TO_SCAN)==0:
            print("Your Directory is safe")
    elif consent=="f":
        file_path=input("Enter your file path: ")
        print("Scan started. Please Wait......")
        scan_file(file_path)

