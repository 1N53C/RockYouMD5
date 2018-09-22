user_input = input("Please enter the Hash to decrypt: ")
chosen_hash = input("Enter Type of Hash (md5 or sha256): ")

# in this case, the rockyou.txt is in the same folder as the script
with open('rockyou.txt', 'r') as file:
    for line in file:
        if chosen_hash == 'md5':
            word = hash.md5(line.strip().encode()).hexdigest()
        else:
            word = hash.sha256(line.strip().encode()).hexdigest()
           
        if word == user_input:
            print("[+] Password found: " + line)
            break
print("Finished")
