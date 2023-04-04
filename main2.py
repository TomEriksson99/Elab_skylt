
from os import remove
from tkinter import *  
from PIL import ImageTk,Image 
import math
import tkinter.font as tkFont
import time

import requests
from getapi2 import get_apidata2

def update_screen(canvas, data, img_buss, img_buss_red, img_tbana, fontExample):
    try:
        buss = data[1]
        tbana = data[0]

        blåbuss = ["4","6"]
        rödbuss = ["72","67","94"]
        #rödbuss = ["67","94"]

        size_vert = 128
        size_hori = 1024

        buss_nr_hori = 152
        buss_nr_vert = 62

        buss_namn_hori = 260
        buss_namn_vert = buss_nr_vert

        buss_times_hori = 680
        buss_times_period = 130
        buss_times_vert = buss_nr_vert

        t_bana_nr_hori = 100

        lineorder = []
        column = []
        row = 0
        for i in range(len(buss)):
            temp = buss[i]
            temp.append(temp[1]+temp[2])  
            print(temp)
            try:
                if temp[2] in blåbuss:
                    if temp[3] in lineorder:
                        index = lineorder.index(temp[3])
                        col = column[index] + 1
                        column[index] = col
                    else:
                        index = len(lineorder)
                        lineorder.append(temp[3])
                        column.append(0)
                        col = 0
                        if index < 9:
                            canvas.create_image(0, size_vert*index, anchor='nw', image=img_buss)
                    if col < 3 and index < 9:
                        canvas.create_text(buss_times_hori+buss_times_period*col, size_vert*index+buss_times_vert,text=temp[0] ,anchor='center',font=fontExample)
                        canvas.create_text(buss_namn_hori, size_vert*index+buss_namn_vert,text=temp[1] ,anchor='w',font=fontExample)
                        canvas.create_text(buss_nr_hori, size_vert*index+buss_nr_vert,text=temp[2] ,anchor='center',font=fontExample, fill='#fff')

                elif temp[2] in rödbuss:
                    if temp[3] in lineorder:
                        index = lineorder.index(temp[3])
                        col = column[index] + 1
                        column[index] = col
                    else:
                        index = len(lineorder)
                        lineorder.append(temp[3])
                        column.append(0)
                        col = 0
                        if index < 9:
                            canvas.create_image(0, size_vert*index, anchor='nw', image=img_buss_red)
                    if col < 3 and index < 9:
                        canvas.create_text(buss_times_hori+buss_times_period*col,  size_vert*index+buss_times_vert,text=temp[0] ,anchor='center',font=fontExample)
                        canvas.create_text(buss_namn_hori, size_vert*index+buss_namn_vert,text=temp[1] ,anchor='w',font=fontExample)
                        canvas.create_text(buss_nr_hori, size_vert*index+buss_nr_vert,text=temp[2] ,anchor='center',font=fontExample, fill='#fff')
            except:
                pass

        #print(lineorder)
        t_lineorder = []
        t_column = []
        row = 0
        for i in range(len(tbana)):
            #print(i)
            temp = tbana[i]
            if temp[1] in t_lineorder:
                    index = t_lineorder.index(temp[1])
                    col = t_column[index] + 1
                    t_column[index] = col
            else:
                index = len(t_lineorder)
                t_lineorder.append(temp[1])
                t_column.append(0)
                col = 0
                canvas.create_image(0, size_vert*(index+8), anchor='nw', image=img_tbana)
            if col < 3:
                canvas.create_text(buss_times_hori+buss_times_period*col, size_vert*(index+8)+buss_times_vert,text=temp[0] ,anchor='center',font=fontExample)
                canvas.create_text(buss_namn_hori, size_vert*(index+8)+buss_namn_vert,text=temp[1] ,anchor='w',font=fontExample)
                row = row + 1
        
        canvas.update()
    except:
        pass
    
def reduce_min(data):
    buss = data[1]
    tbana = data[0]

    newbuss = []
    for i in range(len(buss)):
        temp = buss[i]
        if temp[0]=='Nu':
            pass
        elif temp[0] == '1 min':
            temp[0] = 'Nu'
            newbuss.append(temp)
        elif ':' in temp[0]:
            newbuss.append(temp)
        else:
            time = temp[0].split()
            temp[0] = str(int(time[0])-1)+' min'
            newbuss.append(temp)

    new_tbana = []
    for i in range(len(tbana)):
        temp = tbana[i]
        if temp[0]=='Nu':
            pass
        elif temp[0] == '1 min':
            temp[0] = 'Nu'
            new_tbana.append(temp)
        elif ':' in temp[0]:
            new_tbana.append(temp)
        else:
            time = temp[0].split()
            temp[0] = str(int(time[0])-1)+' min'
            new_tbana.append(temp)

    new_data = [new_tbana, newbuss]
    return new_data

def main():
    root = Tk() 
    #root.attributes('-fullscreen', True)
    canvas = Canvas(root, width = 1024, height = 1280)  
    canvas.pack()  

    fontExample = tkFont.Font(family="Calibri", size=26, weight="bold")

    size_vert = 128# 98*(1024/768)
    size_hori = 1024 #768*(1024/768)

    img_n = Image.open("buss_3_red.png")
    img_r = img_n.resize((size_hori, size_vert))  
    img_tbana = ImageTk.PhotoImage(img_r)

    img_n1 = Image.open("Buss_2.png")
    img_r1 = img_n1.resize((size_hori, size_vert))   
    img_buss = ImageTk.PhotoImage(img_r1)

    img_n2 = Image.open("Buss_2_red.png")
    img_r2  = img_n2.resize((size_hori, size_vert))  
    img_buss_red = ImageTk.PhotoImage(img_r2)
    times = 30

    while True:
        plats_id = '9600'
        keys = ['4700b7208f1c4e2391705d8eb1500df7','cb8f98c017ce4a688acbb20c1f8b7cf8','dc89cad813a04116a28ddb7ecb8dcece','4cf2e9516701466a9fb73a370634b3ff','2fcafe82422c474fb73427ef2de46db1']
        for j in range(len(keys)):
            link_real = 'https://api.sl.se/api2/realtimedeparturesV4.json?key='+keys[j]+'&siteid='+plats_id+'&timewindow=30'
            data=get_apidata2(link_real)
            update_screen(canvas, data, img_buss, img_buss_red, img_tbana, fontExample)
            print("data update")
            #print(data)
            for i in range(1):
                time.sleep(2)
                update_screen(canvas, data, img_buss, img_buss_red, img_tbana, fontExample)
                #print("screen update")
        
main()

