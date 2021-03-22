import nacl.pwhash
from nacl import pwhash, encoding

p = open("passwords.txt", "r")  # open the file with the users and the hashed passwords, for read


count1 = 0
salt = bytes(32)  # setting salt for hash function
size = pwhash.scrypt.BYTES_MIN  #setting size for hash function
us = ''
for line1 in p:  # reading line per line the file with the usernames and their hashed passwords
    count1 += 1  # this variable is used to check if the line is odd or even
                 # (we have usernames in the odds and hashed passwords in the evens

    if count1 % 2 != 0:  # if line is odd
        us = line1.strip()  # keep the username that reads

    if count1 % 2 == 0:  # if line is even
        count = 0
        pp = open("popularPasswords.txt", "r")  # open the file which has all the popular passwords
        password = line1.strip()  # read the hashed password from the file with the usernames
        for line in pp:  # read the popular passwords file line per line
            count += 1
            popularPassword = line.strip()  # getting line per line each popular password
            hashed = nacl.pwhash.scrypt.kdf(size, bytes(popularPassword, encoding='utf8'), salt,
                                            encoder=nacl.encoding.RawEncoder)  # hashing the popular password with specific salt and size

            if str(hashed) == line1.strip():  # checking if the hashed password is the same with the hashed popular password
                print('We have a match!')
                f = open("resultFile.txt", "a")  # opens the file in which the matches will be saved
                f.write(us + ":" + line1.strip() + "\n")  # writing the password and his matched username
                f.close()  # close the file

                break
            else:
                print('wait please! scanning...')  # while there is no match show message to user
                continue
