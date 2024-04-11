import zipfile
import pyzipper
import itertools
import os

def is_zip(file):
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            return True
    except zipfile.BadZipFile:
        return False

def zip_input_validation(zip_file):
    while not os.path.exists(zip_file) or not is_zip(zip_file):
        if not os.path.exists(zip_file):
            zip_file = input("File not found. Try again: ")
        else:
            zip_file = input("Invalid zip file. Try again: ")

    return zip_file

def dictionary():
    # ask user for zip file and wordlist
    zip_file = zip_input_validation(input("Enter the path to the zip file: "))
    word_list = input("Enter the path to the word list you are using: ")
    while not os.path.exists(word_list):
        word_list = input("File not found. Try again: ")

    # create directory to store extracted files
    if "\\" in zip_file:
        output_directory = f"{os.path.dirname(zip_file)}\\{os.path.splitext(os.path.basename(zip_file))[0]}_contents"
    else:
        output_directory = f"{os.path.splitext(os.path.basename(zip_file))[0]}_contents"

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # initialize success boolean
    success = False

    # open the dictionary list
    with open(word_list, "r", errors="ignore") as word_list:
        # loop through each word in the list
        for line in word_list:
            line = line.strip()
            # try each password, breaking loop if successful password is found
            try:
                with pyzipper.AESZipFile(zip_file) as zf:
                    zf.extractall(path=output_directory, pwd=line.encode())
                success = True
                print(f"\rAttempting: {line}                   ", end="")  # Output which word we are currently checking
                success = True
                break
            except:
                print(f"\rAttempting: {line}                   ", end="")  # Output which word we are currently checking

        if success:
            print("\nPassword successfully cracked.\n")
        else:
            print("\nPassword crack failed.\n")

def bruteforce():
    # ask user for zip file
    zip_file = zip_input_validation(input("Enter the path to the zip file: "))
    success = False

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?`~"
    for length in range(1, 10):
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            try:
                with pyzipper.AESZipFile(zip_file) as zf:
                    zf.extractall(path='testfolder', pwd=password.encode())
                print(f"\rPassword successfully cracked: {password}                   ")
                return password
            except:
                print(f"\rAttempting: {password}                   ", end="")
