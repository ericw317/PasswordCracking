from Crypto.Hash import MD4
import binascii
import os
import itertools

def ntlm_hash(plaintext):
    #  the current libraries have no NTLM hash function, so we are going to replicate the function on our own
    #  NTLM hashes are created by encoding the plaintext with utf-16LE, then hashing that with MD4
    hash_ntlm = MD4.new()  # creates MD4 hash object
    hash_ntlm.update(plaintext.encode('utf-16le'))  # encodes plaintext to utf-16le then hashes it using MD4
    return binascii.hexlify(hash_ntlm.digest()).decode()  # returns the hash


hash_functions = {
    "ntlm": ntlm_hash
}

def dictionary(hash_type, hash_to_crack):
    success = False  # flag to indicate whether crack was successful or not
    wordlist = input("Enter the path to the wordlist you are using: ")
    while not os.path.exists(wordlist):
        wordlist = input("File not found. Try again: ")

    # open wordlist and read line by line
    with open(wordlist, "r", errors="ignore") as dictionary_list:
        for line in dictionary_list:
            word = line.strip()  # strip whitespace from lines and store the word
            print(f"\rAttempting: {word}                   ", end="")  # Output which word we are currently checking
            if hash_functions[hash_type](word) == hash_to_crack:  # hash the word and check if the hashes match
                print(f"\nCrack successful: {word}\n")
                success = True
                break

    if not success:
        print("\nHash crack failed.\n")

def bruteforce(hash_type, hash_to_crack):
    max_length = input("Enter the max length you'd like to bruteforce up to: \n")
    while not max_length.isnumeric() or int(max_length) < 1:
        max_length = input("Input must be a number that is greater than 0: ")

    success = False

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?`~"
    for length in range(1, int(max_length) + 1):
        for attempt in itertools.product(characters, repeat=length):
            word = ''.join(attempt)
            print(f"\rAttempting: {word}                   ", end="")  # Output which word we are currently checking
            if hash_functions[hash_type](word) == hash_to_crack:  # hash the word and check if the hashes match
                print(f"\nCrack successful: {word}\n")
                success = True
                break
        if success:
            break
    if not success:
        print("\nHash crack failed.\n")
