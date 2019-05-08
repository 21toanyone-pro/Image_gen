# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:11:29 2019

@author: Lim
"""
from PIL import Image, ImageFilter
from PIL import ImageFont 
from PIL import ImageDraw 
import numpy as np
import os
import glob


file_path = './make_eval/'
bground_list = os.listdir(file_path)
File_List = glob.glob('./make_eval/*.jpg')
save2 = open('word2.txt', 'w', encoding='utf-8')

count = len(bground_list)
L =[]
for i in range(count):
    bground = Image.open(file_path+str(bground_list[i]))
    re = bground.resize((200, 50))
    re.save('gentest/' + str(i) + '.jpg')\
    
    s = os.path.splitext(File_List[i])
    s = os.path.split(s[0])
    f = str(s[1])
    L.append(f)
    save = open('gentest/'+str(i)+'.txt', 'w', encoding='utf')
    save.write(f)
    save2.write(f)
    save2.write('\n')