import zip_cracker
import hash_cracking

def input_validation(message, num1, num2):
    selection = input(message)

    while not selection.isnumeric() or int(selection) < num1 or int(selection) > num2:
        selection = input(f"Input must be a number between {num1}-{num2}: ")
    return int(selection)


selection = -1
while selection != 0:
    selection = input_validation("Select the type of password you'd like to crack:\n"
                                 "1) Zip files\n"
                                 "2) Hash cracking\n"
                                 "0) Exit\n", 0, 2)
    # zip file selection branch
    if selection == 1:
        selection = input_validation("Select the attack type you'd like to attempt:\n"
                                     "1) Dictionary attack\n"
                                     "2) Bruteforce attack\n"
                                     "0) Exit\n", 0, 2)
        if selection == 1:
            zip_cracker.dictionary()
        elif selection == 2:
            zip_cracker.bruteforce()
    # hash cracking selection branch
    elif selection == 2:
        selection = input_validation("Select the hash type you'd like to crack:\n"
                                     "1) NTLM\n"
                                     "0) Exit\n", 0, 1)
        if selection == 1:
            selection = input_validation("Select the attack type you'd like to attempt:\n"
                                         "1) Dictionary attack\n"
                                         "2) Bruteforce attack\n"
                                         "0) Exit\n", 0, 2)
            if selection == 1:
                hash_value = input("Enter the NTLM hash you want to crack: ")
                while len(hash_value) != 32:
                    hash_value = input("Invalid NTLM hash. Try again: ")
                hash_cracking.dictionary("ntlm", hash_value.lower())
            elif selection == 2:
                hash_value = input("Enter the NTLM hash you want to crack: ")
                while len(hash_value) != 32:
                    hash_value = input("Invalid NTLM hash. Try again: ")
                hash_cracking.bruteforce("ntlm", hash_value.lower())
