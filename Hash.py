import nacl.pwhash
from nacl import pwhash, encoding

# Add a user
print('Please give username in the type USERXXX and password \n')
username = input()  # getting username from user
# checking if the username that the user gave, looks like USERXXX
while (username[0] != 'U' and username[1] != 'S' and username[2] != 'E' and username[3] != 'R') or (username[0] != 'u' and username[1] != 's' and username[2] != 'e' and username[3] != 'r'):
    print('Please enter the correct type of username')
    username = input()  # asking again for username until we get what we want
    if (username[0] == 'U' and username[1] == 'S' and username[2] == 'E' and username[3] == 'R') or (username[0] == 'u' and username[1] == 's' and username[2] == 'e' and username[3] == 'r'):
        break  # if the username is what we want then we continue

password = input()  # asking the password from user

salt = bytes(32)  # setting salt for hash function

size = pwhash.scrypt.BYTES_MIN  # setting size for hash function
hashed = pwhash.scrypt.kdf(size, bytes(password, encoding='utf8'), salt, encoder=nacl.encoding.RawEncoder)  # hashing the password with the specific salt

try:
    f = open("passwords.txt", "a")  # open the file in which we will save the username and the corresponding hashed password
    hashed1 = str(hashed)  # make the hashed password as string
    try:
        f.write(username + "\n" + hashed1 + "\n")  # writing the username and in the next line the hashed password
        print('user submitted')  # after the writing was successful we show a corresponding message to user
    except IOError as e:
        print('Error in writing to file')  # message to user if something goes wrong through the writing
    f.close()  # close the file after writing
except:
    print('False')
