# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:20:40 2019

@author: Lim
"""

from PIL import Image, ImageFilter
from PIL import ImageFont 
from PIL import ImageDraw 
import numpy as np
import os
import glob
import random
import cv2
import textwrap

#단어 불러오기
L = []
word = open('word2.txt', 'r', encoding='UTF8')
while(1):
    #line = word.readline()
    line = word.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        L.append(line[0:escape])
    else:
        break
word.close()
num = 0
folderSave = 0


#이미지 사이즈 조정
def create_an_image(bground_path, width, height):
    bground_list = os.listdir(bground_path)
    bground_choice = random.choice(bground_list)
    bground = Image.open(bground_path+bground_choice)
    #x, y = random.randint(0,bground.size[0]-width), random.randint(0, bground.size[1]-height)
    re = bground.resize((width, 50))
    return re

#폰트 사이즈 조정 /
def  random_font_size():
    font_size = random.randint(20, 20)
    return font_size

#폰트 고르기
def random_font(font_path):
    font_list = os.listdir(font_path)
    random_font = random.choice(font_list)
    return font_path + random_font

#폰트 색
def random_word_color():
    font_color_choice = [[255,255,255]] #,[255,0,0],[0,255,0],[0,0,255],[0,255,255],[255,255,0],[255,0,255],[0,0,0]
    font_color = random.choice(font_color_choice)

    noise = np.array([random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    font_color = (np.array(font_color) + noise).tolist()
    return tuple(font_color)


for i in range(0, 20):   # 20회
    #randomWord = random.randint(0, 1000)

    #폰트 길이 알아냄
    lens = len(L[i])

    #폰트 사이즈 정하기
    font_size = random_font_size()
    
    #이미지 생성
    imageSize = lens*50
    target_image = create_an_image('./background/',imageSize, 50)

    #폰트 선택
    font_name = random_font('./font/')
    #폰트 색
    font_color = random_word_color()
    #폰트 지정
    font = ImageFont.truetype(font_name, 50) # 폰트 이름, 폰트 사이즈 (랜덤으로 할 거면 font_size 해주면댐)
    
    #10만장 마다 폴더 새로 만드는 거
    if i % 100000 ==0:
        folderSave = folderSave + 1
        dir_path = 'data/d' + str(folderSave)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path + '/')

    #텍스트 저장
    save = open(dir_path + '/'+str(num)+'.txt', 'w', encoding='utf')
    save.write(L[i])

    #이미지 그리기
    draw = ImageDraw.Draw(target_image)
    draw.text((0, 0), L[i] , fill = font_color, font = font)# 가로쓰기

    re = target_image.resize((150, 50)) # 이미지 크기를 W:150, H:50으로 리사이징 함. <- 필요하면 수정
    
    #이미지 저장
    re.save(dir_path +'/' + str(num) + '.jpg')#save image
    num = num + 1
    #print(str(num) +'/500000')
    
    #print(str(num) +'/1000')

