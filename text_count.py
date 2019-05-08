# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:10:20 2019

@author: Lim
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
dic = 'kor_data.txt'

with open(dic) as file_object:
    contents = file_object.read() #단어 저장
    

document_text = open('word.txt', 'r', encoding='UTF8' )
text_string = document_text.read()

save = open('text_count.txt', 'w', encoding='utf-8')
num = 0
lengths = 0
for i in range(len(contents)):
    counting = str(text_string.count(contents[i]))
    lengths = lengths + text_string.count(contents[i])
    if text_string.count(contents[i]) != 0:
        save.write(contents[i]+':')
        save.write(counting)
        save.write('\t')   
        num = num +1
        if num % 10 == 0:
            save.write('\n')

save.write('\n'+'총:'+str(lengths)+'\n')
save.write('평균:'+str(lengths / len(contents)))