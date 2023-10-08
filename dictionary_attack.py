import hashlib
import time
import os

def ShowStarting():
    print("""
        ░▒█▀▀▄░░▀░░█▀▄░▀█▀░█▀▀▄░▀█▀░▀█▀░█▀▀▄░█▀▄░█░▄
        ░▒█░▒█░░█▀░█░░░░█░▒█▄▄█░░█░░░█░░█▄▄█░█░░░█▀▄
        ░▒█▄▄█░▀▀▀░▀▀▀░░▀░▒█░▒█░░▀░░░▀░░▀░░▀░▀▀▀░▀░▀
        
    By Technobeast (@TechnobeastOP on Telegram)      2023\n""")
    
def Main():
    os.system("cls")
    ShowStarting()
    command = input("Do You Want to convert a text to hash form? then press E, If you wantt to convert a hash form to text or perform dictionary attack to a text? Then Press D\n> ")
    if command == "E":
        text = input("Which Text Do You Want To Encrypt?\n> ")
        hash_ty = input("Which Hash Type Do you Want to encrypt? Select Hash Type:\n1. md5\n2. sha1\n3. sha256 \n> ")
        ConvertToHash(text, hash_ty)
    elif command == "D":
        hashType = input("Select Hash Type:\n1. md5\n2. sha1\n3. sha256 \n> ")
        if hashType == "":
            print("No Hash Type Was Entered")
            Stop()
        passFile = input("Enter The Path of Password File: ")
        print(f"File Selected For Passwords {passFile}")
        hashPass = input(f"Password in {hashType} Hash Type \n> ")
        if hashPass == "":
            print("No Password Was Entered")
            Stop()
        FindPassword(hashPass, passFile, hashType=hashType)
    
def ConvertToHash(text, hashtype):
    input_string = str(text)
    if hashtype == "md5":
        hash_word = hashlib.md5()
    elif hashtype == "sha1":
        hash_word = hashlib.sha1()
    elif hashtype == "sha256":
        hash_word = hashlib.sha256()
    # Update the hash object with the input string
    hash_word.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the MD5 hash
    hash_hex = hash_word.hexdigest()
    # Print the MD5 hash
    print(f"{hashtype} Hash: {hash_hex}")
    Stop()
    
def Restart(restart):
    if "y" == restart:
        os.system("cls")
        Main()
    elif "n" == restart:
        print("Program Ended Sucsessfully")
        quit(1)
    else:
        Restart(input("Type y or n \n> "))
       
def FindPassword(hashedPassword, passwordFile, hashType):
    try:
        p_file = open(passwordFile, "r")
    except:
        print("File Not Found")
        Stop()
    pass_found = 0
    for word in p_file:
        enc_word = word.encode('utf-8')
        if hashType == "md5":
            hash_word = hashlib.md5(enc_word.strip())
        elif hashType == "sha1":
            hash_word = hashlib.sha1(enc_word.strip())
        elif hashType == "sha256":
            hash_word = hashlib.sha256(enc_word.strip())
        else:
            print("Hash Type Not Supported")
            Stop()
        digest = hash_word.hexdigest()
        
        if digest == hashedPassword:
            pass_found =+1
            print(f"{pass_found} Password Found, Password is")
            print(f"{word}")
            
            Stop()
            
    if not pass_found:
        print("Password not found")
        Stop()
        
def Stop():
    restart = input("Want To Continue? (y,n)\n> ")
    Restart(restart)
    
Main()