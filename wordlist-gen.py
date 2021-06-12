# -*- coding: utf-8 -*-

import random
import os

pass_keys = "ABCDEFGHJKLMNPQRSTUVWYXZabcdefhjmnpqrstuvwxyz0123456789!@#$%^&*()";
pass_length = [10,18]; # password length [min, max] : in cpanel (min: 10, max: 18)
pass_store = [];


print('## FYI; Cracking cpanel password with this method is a bit imposible')
print('## Minimum password count : 13 x 10^26')
print('## Maximum password count : 42 x 10^40')
print('## Lottery chance         : 1  x 10^9\n\n')

pass_count = input('Password count: ').lower() # Get password count from user

def rand_digi(min_digi, max_digi):
    ''' Generate random digi between given digi '''
    return random.randrange(min_digi, max_digi);

def cpanel_char():
    ''' Random password generating for cpanel cracking '''
    passwd = ""
    limit = len(pass_keys);

    for char in range(0, rand_digi(pass_length[0], pass_length[1]) ):
        passwd += pass_keys[ rand_digi(1, limit) ]

    pass_store.append(passwd)

y = 0;
while (y < int(pass_count)):
    cpanel_char();
    y += 1;

# Write all generated password to file
filew = open("passwd.txt", "w+");
filew.write("\n".join(pass_store))