# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:38:32 2023

@author: Oluwajuwon
"""
word = input('enter a password: ')

def check(word):
    char = ['!','@','#','$','%','^','&','*','(',')']
    count_up = 0
    count_low = 0
    count_special = 0
    count_int = 0

    for i,j,k,l in zip(word,word,word,word):
        if i.islower():
            count_low += 1
            # if count_low
        if j.isupper():
            count_up += 1
        if k in char:
            count_special += 1
        if l.isdigit():
            count_int += 1
                
            
    print(word)
    print(count_low,count_up,count_special,count_int)
    if count_special < 2 or count_up < 2 or count_low < 1 or count_int < 1 or len(word) < 8:
        print(word + " is not a strong password")
    else:
        print(word + " is a strong password")
   
        if 8 <= len(word) <= 12:
            print('strong')
        elif 13 <= len(word) <= 15:
            print('very strong')
        elif len(word) > 15:
            print('excellent')
        
    q = input('would you like to enter another password [y / n]: ')
    while q == 'y':
        if q != 'y':
            break
        else:
            new_word = input('enter a new password: ')
            check(new_word)
            break
        

        
            
check(word)
        