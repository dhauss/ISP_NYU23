import hashlib
# import string
# import itertools

hashed_pw = hashlib.sha1(b'password').hexdigest()
print(len(hashed_pw))
hashed_pw = '00000' + hashed_pw[5:]
# print(hashed_pw)
# print('test: ' + hashlib.sha1(b'a1b2c3').hexdigest())
"""
# charList = list(string.ascii_letters + string.digits + string.punctuation)
# guesses = [''.join(i) for i in itertools.permutations(charList, 4)]
# print(guesses)
"""
with open('Assignment_1/A1_part2/linkedin/SHA1.txt', 'r') as pw_file:
    lines = pw_file.readlines()
    for line in lines:
        if line.strip() == hashed_pw:
            print('Found: ' + line.strip() + ' = ' + hashed_pw)
            break

"""
with open('Assignment_1/A1_part2/linkedin/out.txt', 'w') as out_file:
    for pw in yahoo_pws:
        out_file.write(f"{pw}\n")
"""
