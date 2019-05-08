# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:27:26 2019

@author: Lim
"""
import random


filename = 'kor_data.txt' #kor_data.txt
with open(filename) as file_object:
    contents = file_object.read()
    
save = open('word.txt', 'w', encoding='utf-8')


for j in range (0, 800000):
    char_size = random.randrange(2, 7)
    for i in range(0, char_size):
        rand_char = random.randrange(0, len(contents))
        save.write(contents[rand_char])  
    save.write('\n')