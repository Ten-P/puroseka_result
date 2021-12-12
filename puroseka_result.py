import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import os,sys
import tkinter.filedialog
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import pytesseract
import pyocr
import pyocr.builders
import re
import cv2


def click01():
    a_1 = int(entry01.get())
    a_4 = int(entry04.get())
    a_7 = int(entry07.get())
    a_10 = int(entry10.get())
    a_13 = int(entry13.get())
    s_1 = a_1 * 3
    s_4 = a_4 * 2
    s_7 = a_7 * 1
    s_10 = a_10 * 0
    s_13= a_13 * 0
    t_1 = s_1 + s_4 + s_7 + s_10 + s_13
    entry16.insert(END, t_1)

def click02():
    a_2 = int(entry02.get())
    a_5 = int(entry05.get())
    a_8 = int(entry08.get())
    a_11 = int(entry11.get())
    a_14 = int(entry14.get())
    s_2 = a_2 * 3
    s_5 = a_5 * 2
    s_8 = a_8 * 1
    s_11 = a_11 * 0
    s_14= a_14 * 0
    t_2 =s_2+s_5+s_8+s_11+s_14
    entry17.insert(END, t_2)

def click03():
    a_3 = int(entry03.get())
    a_6 = int(entry06.get())
    a_9 = int(entry09.get())
    a_12 = int(entry12.get())
    a_15 = int(entry15.get())
    s_3 = a_3 * 3
    s_6 = a_6 * 2
    s_9 = a_9 * 1
    s_12 = a_12 * 0
    s_15= a_15 * 0
    t_3 =s_3+s_6+s_9+s_12+s_15
    entry18.insert(END, t_3)

def click04():
    a_19 = int(entry19.get())
    a_22 = int(entry22.get())
    a_25 = int(entry25.get())
    a_28 = int(entry28.get())
    a_31 = int(entry31.get())
    s_19 = a_19 * 3
    s_22 = a_22 * 2
    s_25 = a_25 * 1
    s_28 = a_28 * 0
    s_31= a_31 * 0
    t_4 =s_19+s_22+s_25+s_28+s_31
    entry34.insert(END, t_4)

def click05():
    a_20 = int(entry20.get())
    a_23 = int(entry23.get())
    a_26 = int(entry26.get())
    a_29 = int(entry29.get())
    a_32 = int(entry32.get())
    s_20 = a_20 * 3
    s_23 = a_23 * 2
    s_26 = a_26 * 1
    s_29 = a_29 * 0
    s_32= a_32 * 0
    t_5 =s_20+s_23+s_26+s_29+s_32
    entry35.insert(END, t_5)

def click06():
    a_21 = int(entry21.get())
    a_24 = int(entry24.get())
    a_27 = int(entry27.get())
    a_30 = int(entry30.get())
    a_33 = int(entry33.get())
    s_21 = a_21 * 3
    s_24 = a_24 * 2
    s_27 = a_27 * 1
    s_30 = a_30 * 0
    s_33= a_33 * 0
    t_6 =s_21+s_24+s_27+s_30+s_33
    entry36.insert(END, t_6)

def small_sum01():
    c_1 = int(entry01.get())
    c_2 = int(entry02.get())
    c_3 = int(entry03.get())
    c_4 = int(entry04.get())
    c_5 = int(entry05.get())
    c_6 = int(entry06.get())
    c_7 = int(entry07.get())
    c_8 = int(entry08.get())
    c_9 = int(entry09.get())
    c_10 = int(entry10.get())
    c_11 = int(entry11.get())
    c_12 = int(entry12.get())
    c_13 = int(entry13.get())
    c_14 = int(entry14.get())
    c_15 = int(entry15.get())
    s_1 = c_1+c_2+c_3+c_4+c_5
    s_2 = c_6+c_7+c_8+c_9+c_10
    s_3 = c_11+c_12+c_13+c_14+c_15
    entry16.insert(END, s_1)
    entry17.insert(END, s_2)
    entry18.insert(END, s_3)

def small_sum02():
    c_1 = int(entry19.get())
    c_2 = int(entry20.get())
    c_3 = int(entry21.get())
    c_4 = int(entry22.get())
    c_5 = int(entry23.get())
    c_6 = int(entry24.get())
    c_7 = int(entry25.get())
    c_8 = int(entry26.get())
    c_9 = int(entry27.get())
    c_10 = int(entry28.get())
    c_11 = int(entry29.get())
    c_12 = int(entry30.get())
    c_13 = int(entry31.get())
    c_14 = int(entry32.get())
    c_15 = int(entry33.get())
    s_1 = c_1+c_2+c_3+c_4+c_5
    s_2 = c_6+c_7+c_8+c_9+c_10
    s_3 = c_11+c_12+c_13+c_14+c_15
    entry34.insert(END, s_1)
    entry35.insert(END, s_2)
    entry36.insert(END, s_3)

def musicsum_sub01():
    global o_1,o_2,o_3,o_4,o_5,o_6
    o_1 = int(entry16.get())
    o_2 = int(entry17.get())
    o_3 = int(entry18.get())
    o_4 = int(entry34.get())
    o_5 = int(entry35.get())
    o_6 = int(entry36.get())
    s_1 = o_1 + o_2 + o_3
    s_2 = o_4 + o_5 + o_6
    entry37.insert(END, s_1)
    entry38.insert(END, s_2)
    entry16.delete(0, tk.END)
    entry17.delete(0, tk.END)
    entry18.delete(0, tk.END)
    entry34.delete(0, tk.END)
    entry35.delete(0, tk.END)
    entry36.delete(0, tk.END)


def musicsum_sub02():
    global p_1,p_2,p_3,p_4,p_5,p_6
    p_1 = int(entry16.get())
    p_2 = int(entry17.get())
    p_3 = int(entry18.get())
    p_4 = int(entry34.get())
    p_5 = int(entry35.get())
    p_6 = int(entry36.get())
    s_1 = p_1 + p_2 + p_3
    s_2 = p_4 + p_5 + p_6
    entry39.insert(END, s_1)
    entry40.insert(END, s_2)
    entry16.delete(0, tk.END)
    entry17.delete(0, tk.END)
    entry18.delete(0, tk.END)
    entry34.delete(0, tk.END)
    entry35.delete(0, tk.END)
    entry36.delete(0, tk.END)

def musicsum_sub03():
    global q_1,q_2,q_3,q_4,q_5,q_6
    q_1 = int(entry16.get())
    q_2 = int(entry17.get())
    q_3 = int(entry18.get())
    q_4 = int(entry34.get())
    q_5 = int(entry35.get())
    q_6 = int(entry36.get())
    s_1 = q_1 + q_2 + q_3
    s_2 = q_4 + q_5 + q_6
    entry41.insert(END, s_1)
    entry42.insert(END, s_2)
    entry16.delete(0, tk.END)
    entry17.delete(0, tk.END)
    entry18.delete(0, tk.END)
    entry34.delete(0, tk.END)
    entry35.delete(0, tk.END)
    entry36.delete(0, tk.END)

def newwindow():

    a = str(entry_member01.get())
    b = str(entry_member02.get())
    c = str(entry_member03.get())
    d = str(entry_member04.get())
    e = str(entry_member05.get())
    f = str(entry_member06.get())



    new_window = tk.Toplevel()
    new_window.title('個別集計')
    new_window.geometry("680x250")

    tree = ttk.Treeview(new_window)

    tree["columns"] = (0,1,2,3,4,5,6)

    tree["show"] = "headings"
    tree.heading(0,text="    ")
    tree.heading(1,text=a)
    tree.heading(2,text=b)
    tree.heading(3,text=c)
    tree.heading(4,text=d)
    tree.heading(5,text=e)
    tree.heading(6,text=f)

    tree.column(0,width=60)
    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=100)

    list = [o_1,o_2,o_3,o_4,o_5,o_6,p_1,p_2,p_3,p_4,p_5,p_6,q_1,q_2,q_3,q_4,q_5,q_6]

    tree.insert("", "end", values=("1曲目",list[0],list[1],list[2],list[3],list[4],list[5]))


    tree.insert("", "end", values=("2曲目",list[6],list[7],list[8],list[9],list[10],list[11]))

    tree.insert("", "end", values=("3曲目",list[12],list[13],list[14],list[15],list[16],list[17]))

    tree.grid(column=0,row=0)



def delete():
    entry01.delete(0, tk.END)
    entry02.delete(0, tk.END)
    entry03.delete(0, tk.END)
    entry04.delete(0, tk.END)
    entry05.delete(0, tk.END)
    entry06.delete(0, tk.END)
    entry07.delete(0, tk.END)
    entry08.delete(0, tk.END)
    entry09.delete(0, tk.END)
    entry10.delete(0, tk.END)
    entry11.delete(0, tk.END)
    entry12.delete(0, tk.END)
    entry13.delete(0, tk.END)
    entry14.delete(0, tk.END)
    entry15.delete(0, tk.END)
    entry19.delete(0, tk.END)
    entry20.delete(0, tk.END)
    entry21.delete(0, tk.END)
    entry22.delete(0, tk.END)
    entry23.delete(0, tk.END)
    entry24.delete(0, tk.END)
    entry25.delete(0, tk.END)
    entry26.delete(0, tk.END)
    entry27.delete(0, tk.END)
    entry28.delete(0, tk.END)
    entry29.delete(0, tk.END)
    entry30.delete(0, tk.END)
    entry31.delete(0, tk.END)
    entry32.delete(0, tk.END)
    entry33.delete(0, tk.END)

def music_sum():
    d_1 = int(entry37.get())
    d_2 = int(entry38.get())
    d_3 = int(entry39.get())
    d_4 = int(entry40.get())
    d_5 = int(entry41.get())
    d_6 = int(entry42.get())
    s_1 = d_1 + d_3 + d_5
    s_2 = d_2 + d_4 + d_6
    entry43.insert(END, s_1)
    entry44.insert(END, s_2)

def result():
    a = str(entry_name01.get())
    b = str(entry_name02.get())
    c_1 = int(entry43.get())
    c_2 = int(entry44.get())
    if c_1 > c_2:
        entry45.insert(END, a)
    if c_2 > c_1:
        entry45.insert(END, b)
    if c_1 == c_2:
        entry45.insert(END, "-")

def get_Image():
    global get
    filetype = [("画像", "*.png")]
    file_path = tkinter.filedialog.askopenfilename(filetypes = filetype)
    get = entry_name01.insert(tkinter.END, file_path)


def Image_read_output():
    im = Image.read(get)
    im_crop = im.crop((695,450,759,482))
    im_crop.save('C:\\Users\\岸川　颯真\\Desktop\\python_file\\GUI_practice\\test01.png')
    read = cv2.imread(get)
    height = read.shape[0]
    width = read.shape[1]
    Im01 = cv2.resize(read, (int(width*5), int(height*5)))
    Im02 = cv2.imwrite('test000.png',Im01)
    number01 = int(pytesseract.image_to_string(Im02))
    entry01.insert(END, number01)



if __name__ =='__main__':
    root = tk.Tk()
    root.title("result")
    root.geometry("1500x1500")

    frame00= ttk.Frame(root)
    frame00.grid(column=0, row=0, sticky=tk.NSEW, padx=5,pady=15)
    frame01 = ttk.Frame(root)
    frame01.grid(column=0, row=1, sticky=tk.NSEW, padx=5,pady=15)
    frame02 = ttk.Frame(root)
    frame02.grid(column=0, row=2, sticky=tk.NSEW, padx=5,pady=15)
    frame03 = ttk.Frame(root)
    frame03.grid(column=0, row=3, sticky=tk.NSEW, padx=5,pady=15)
    frame04 = ttk.Frame(root)
    frame04.grid(column=0, row=4, sticky=tk.NSEW, padx=5,pady=15)
    frame05 = ttk.Frame(root)
    frame05.grid(column=0, row=5, sticky=tk.NSEW, padx=5,pady=15)
    frame06 = ttk.Frame(root)
    frame06.grid(column=0, row=6, sticky=tk.NSEW, padx=5,pady=15)
    frame07 = ttk.Frame(root)
    frame07.grid(column=0, row=7, sticky=tk.NSEW, padx=5,pady=15)
    frame08 = ttk.Frame(root)
    frame08.grid(column=0, row=9, sticky=tk.NSEW, padx=5,pady=15)
    frame09 = ttk.Frame(root)
    frame09.grid(column=1, row=7, sticky=tk.NSEW, padx=5,pady=15)


    #ここからentry
    entry_name01 = ttk.Entry(frame00,width=56)
    entry_name01.grid(column=1, row=0)
    entry_name02 = ttk.Entry(frame00,width=56)
    entry_name02.grid(column=3, row=0)
    entry_member01 = ttk.Entry(frame01,width=18)
    entry_member01.grid(column=1, row=0)
    entry_member02 = ttk.Entry(frame01,width=18)
    entry_member02.grid(column=2, row=0)
    entry_member03 = ttk.Entry(frame01,width=18)
    entry_member03.grid(column=3, row=0)
    entry_member04 = ttk.Entry(frame01,width=18)
    entry_member04.grid(column=5, row=0)
    entry_member05 = ttk.Entry(frame01,width=18)
    entry_member05.grid(column=6, row=0)
    entry_member06 = ttk.Entry(frame01,width=18)
    entry_member06.grid(column=7, row=0)

    entry01 = ttk.Entry(frame01, width=18)
    entry01.grid(column=1, row=1)
    entry02 = ttk.Entry(frame01, width=18)
    entry02.grid(column=2, row=1)
    entry03 = ttk.Entry(frame01, width=18)
    entry03.grid(column=3, row=1)
    entry04 = ttk.Entry(frame02, width=18)
    entry04.grid(column=1, row=0)
    entry05 = ttk.Entry(frame02, width=18)
    entry05.grid(column=2, row=0)
    entry06 = ttk.Entry(frame02, width=18)
    entry06.grid(column=3, row=0)
    entry07 = ttk.Entry(frame03, width=18)
    entry07.grid(column=1, row=0)
    entry08 = ttk.Entry(frame03, width=18)
    entry08.grid(column=2, row=0)
    entry09 = ttk.Entry(frame03, width=18)
    entry09.grid(column=3, row=0)
    entry10 = ttk.Entry(frame04, width=18)
    entry10.grid(column=1, row=0)
    entry11 = ttk.Entry(frame04, width=18)
    entry11.grid(column=2, row=0)
    entry12 = ttk.Entry(frame04, width=18)
    entry12.grid(column=3, row=0)
    entry13 = ttk.Entry(frame05, width=18)
    entry13.grid(column=1, row=0)
    entry14 = ttk.Entry(frame05, width=18)
    entry14.grid(column=2, row=0)
    entry15 = ttk.Entry(frame05, width=18)
    entry15.grid(column=3, row=0)
    entry16 = ttk.Entry(frame06, width=18)
    entry16.grid(column=1, row=0)
    entry17 = ttk.Entry(frame06, width=18)
    entry17.grid(column=2, row=0)
    entry18 = ttk.Entry(frame06, width=18)
    entry18.grid(column=3, row=0)
    entry19 = ttk.Entry(frame01, width=18)
    entry19.grid(column=5, row=1)
    entry20 = ttk.Entry(frame01, width=18)
    entry20.grid(column=6, row=1)
    entry21 = ttk.Entry(frame01, width=18)
    entry21.grid(column=7, row=1)
    entry22 = ttk.Entry(frame02, width=18)
    entry22.grid(column=5, row=0)
    entry23 = ttk.Entry(frame02, width=18)
    entry23.grid(column=6, row=0)
    entry24 = ttk.Entry(frame02, width=18)
    entry24.grid(column=7, row=0)
    entry25 = ttk.Entry(frame03, width=18)
    entry25.grid(column=5, row=0)
    entry26 = ttk.Entry(frame03, width=18)
    entry26.grid(column=6, row=0)
    entry27 = ttk.Entry(frame03, width=18)
    entry27.grid(column=7, row=0)
    entry28 = ttk.Entry(frame04, width=18)
    entry28.grid(column=5, row=0)
    entry29 = ttk.Entry(frame04, width=18)
    entry29.grid(column=6, row=0)
    entry30 = ttk.Entry(frame04, width=18)
    entry30.grid(column=7, row=0)
    entry31 = ttk.Entry(frame05, width=18)
    entry31.grid(column=5, row=0)
    entry32 = ttk.Entry(frame05, width=18)
    entry32.grid(column=6, row=0)
    entry33 = ttk.Entry(frame05, width=18)
    entry33.grid(column=7, row=0)
    entry34 = ttk.Entry(frame06, width=18)
    entry34.grid(column=5, row=0)
    entry35 = ttk.Entry(frame06, width=18)
    entry35.grid(column=6, row=0)
    entry36 = ttk.Entry(frame06, width=18)
    entry36.grid(column=7, row=0)
    entry37 = ttk.Entry(frame01, width=25) #ここからは一番右端（1曲目2曲目など）
    entry37.grid(column=9, row=1)
    entry38 = ttk.Entry(frame01, width=25)
    entry38.grid(column=10, row=1)
    entry39 = ttk.Entry(frame02, width=25)
    entry39.grid(column=9, row=0)
    entry40 = ttk.Entry(frame02, width=25)
    entry40.grid(column=10, row=0)
    entry41 = ttk.Entry(frame03, width=25)
    entry41.grid(column=9, row=0)
    entry42 = ttk.Entry(frame03, width=25)
    entry42.grid(column=10, row=0)
    entry43 = ttk.Entry(frame04, width=25)
    entry43.grid(column=9, row=0)
    entry44 = ttk.Entry(frame04, width=25)
    entry44.grid(column=10, row=0)
    entry45 = ttk.Entry(frame08, width=25)
    entry45.grid(column=1, row=0)



    #ここからLabel
    team_name01 = tkinter.Label(frame00,text="チーム名")
    team_name01.grid(column=0, row=0, padx=5, pady=5)
    team_name02 = tkinter.Label(frame00,text="   チーム名")
    team_name02.grid(column=2, row=0, padx=5, pady=5)
    member_name01 = tkinter.Label(frame01,text="メンバー")
    member_name01.grid(column=0,row=0, padx=5,pady=5)
    member_name02 = tkinter.Label(frame01,text="  メンバー")
    member_name02.grid(column=4,row=0, padx=5,pady=5)
    Perfect = tkinter.Label(frame01,text="Perfect")
    Perfect.grid(column=0, row=1, padx=5, pady=5)
    Great = tkinter.Label(frame02,text="Great   ")
    Great.grid(column=0, row=0, padx=5,pady=5)
    Good = tkinter.Label(frame03,text="Good   ")
    Good.grid(column=0, row=0, padx=5,pady=5)
    Bad = tkinter.Label(frame04,text="Bad      ")
    Bad.grid(column=0, row=0, padx=5,pady=5)
    Miss = tkinter.Label(frame05,text="Miss    ")
    Miss.grid(column=0, row=0, padx=5,pady=5)
    Perfect02 = tkinter.Label(frame01,text="    Perfect")
    Perfect02.grid(column=4, row=1, padx=5, pady=5)
    Great02 = tkinter.Label(frame02,text="    Great   ")
    Great02.grid(column=4, row=0, padx=5, pady=5)
    Good02 = tkinter.Label(frame03,text="    Good   ")
    Good02.grid(column=4, row=0, padx=5, pady=5)
    Bad02 = tkinter.Label(frame04,text="    Bad     ")
    Bad02.grid(column=4, row=0, padx=5, pady=5)
    Miss02 = tkinter.Label(frame05,text="    Miss    ")
    Miss02.grid(column=4, row=0, padx=5, pady=5)
    sentence = tkinter.Label(frame08,text="チームの勝利！！！")
    sentence.grid(column=2, row=0, padx=5, pady=5)

    #ここからget関数
    a_1 = entry01.get()
    a_2 = entry02.get()
    a_3 = entry03.get()
    a_4 = entry04.get()
    a_5 = entry05.get()
    a_6 = entry06.get()
    a_7 = entry07.get()
    a_8 = entry08.get()
    a_9 = entry09.get()
    a_10 = entry10.get()
    a_11 = entry11.get()
    a_12 = entry12.get()
    a_13 = entry13.get()
    a_14 = entry14.get()
    a_15 = entry15.get()
    a_16 = entry16.get()
    a_17 = entry17.get()
    a_18 = entry18.get()

    #ここから合計
    s_1 = a_1*3
    s_2 = a_2*3
    s_3 = a_3*3
    s_4 = a_4*2
    s_5 = a_5*2
    s_6 = a_6*2
    s_7 = a_7*1
    s_8 = a_8*1
    s_9 = a_9*1
    s_10 = a_10*0
    s_11 = a_11*0
    s_12 = a_12*0
    s_13 = a_13*0
    s_14 = a_14*0
    s_15 = a_15*0

    #ここからButton
    sum00 = tkinter.Button(frame06,text="合計", command=small_sum01)
    sum00.grid(column=0,row=0, padx=5, pady=5)
    sum01 = tkinter.Button(frame06,text="合計", command=small_sum02)
    sum01.grid(column=4,row=0, padx=5, pady=5)
    delete=ttk.Button(frame07, text="delete", command=delete)
    delete.grid(column=8,row=0)
    result=ttk.Button(frame08, text="結果", command=result)
    result.grid(column=0, row=0)
    music01 = tkinter.Button(frame01,text="1曲目" , command=musicsum_sub01)
    music01.grid(column=8, row=1, padx=5, pady=5)
    music02 = tkinter.Button(frame02,text="2曲目", command=musicsum_sub02)
    music02.grid(column=8, row=0, padx=5, pady=5)
    music03 = tkinter.Button(frame03,text="3曲目", command=musicsum_sub03)
    sum02 = tkinter.Button(frame04,text=" 合計  ", command=music_sum)
    sum02.grid(column=8, row=0, padx=5, pady=5)
    music03.grid(column=8, row=0, padx=5, pady=5)

    #ここからメニューバー
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    File_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=File_menu)

    Edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=Edit_menu)

    Contents_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Contents', menu=Contents_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='help', menu = help_menu)

    File_menu.add_command(label='ファイルを選択', command= get_Image)
    File_menu.add_command(label='ファイルを保存' )
    File_menu.add_command(label='実行', command=Image_read_output)
    File_menu.add_command(label='終了', command=quit)

    Edit_menu.add_command(label='個別集計ウィンドウの表示',command=newwindow)


    help_menu.add_command(label='help')


    root.mainloop()
