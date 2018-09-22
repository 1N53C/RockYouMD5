import hashlib as hash

user_input = input("Please enter the MD5 Hash to decrypt: ")

with open('rockyou.txt', 'r') as file:
    for line in file:
        word = hash.md5(line.strip().encode()).hexdigest()
        if word == user_input:
            print("[+] Password found: " + line)
            break
