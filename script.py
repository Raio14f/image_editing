import tkinter as tk
from tkinter.constants import *
import tkinter.ttk as ttk
import tkinter
from tkinter import  StringVar,Tk, filedialog
from typing import Text
import cv2
import os,sys
from PIL import *
import numpy as np

def mosaic(imgCV, ratio=0.1):
    
    small = cv2.resize(imgCV, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, imgCV.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(imgCV, x, y, width, height, ratio=0.1):
    dst = imgCV.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst


def save():
    path_neme = IFileEntry.get()
    global fileneme
    fileneme = path_neme
    global imgCV
    imgCV = cv2.imread(fileneme)
    rdo_value = var.get()
    if rdo_value == 1:
        top_number = top.get()
        bottom_number = bottom.get()
        left_number = left.get()
        right_number = right.get()
        
        top_int = int(top_number)
        bottom_int = int(bottom_number)
        left_int = int(left_number)
        right_int = int(right_number)

        imgCV = imgCV[top_int:bottom_int,left_int:right_int]

    get_path = entry2.get()    
    if get_path == '':
        return
    
    rdo_value = var.get()

    if rdo_value == 0:

        HAAR_FILE = "C:\\Users\\raio\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
        cascade = cv2.CascadeClassifier(HAAR_FILE)

        face = cascade.detectMultiScale(imgCV)

        for x,y,w,h in face:
           
            imgCV = imgCV[y:y+h, x:x+w]

    if rdo_value == 1:
        top_number = top.get()
        bottom_number = bottom.get()
        left_number = left.get()
        right_number = right.get()
        
        top_int = int(top_number)
        bottom_int = int(bottom_number)
        left_int = int(left_number)
        right_int = int(right_number)

        imgCV = imgCV[top_int:bottom_int,left_int:right_int]

    #白黒化
    if bln1.get():

        imgCV = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)  # RGB2〜 でなく BGR2〜 を指定
    else:
        pass
   
    #疑似カラー化
    if bln2.get():

        imgCV = cv2.applyColorMap(imgCV, cv2.COLORMAP_JET)

    else:
        pass
    rdo_value2 = value_rotate.get()
    
    if rdo_value2 == 0:
        imgCV = cv2.rotate(imgCV, cv2.ROTATE_90_CLOCKWISE)

    elif rdo_value2 == 1:
           imgCV = cv2.rotate(imgCV, cv2.ROTATE_90_COUNTERCLOCKWISE)

    elif rdo_value2 == 2:
           imgCV = cv2.rotate(imgCV, cv2.ROTATE_180)

    elif rdo_value2 == 3:
        pass       

    else:
        pass           

    rdo_value3 = value_mosaic.get()

    face_cascade_path = "C:\\Users\\raio\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
    if rdo_value3 == 0:

        imgCV = mosaic(imgCV)

    elif rdo_value3 == 1:

        face_cascade = cv2.CascadeClassifier(face_cascade_path)


        faces = face_cascade.detectMultiScale(imgCV)

        for x, y, w, h in faces:

            imgCV = mosaic_area(imgCV, x, y, w, h)

    elif rdo_value3 == 2:
        top_number2 = top2.get()
        bottom_number2 = bottom2.get()
        left_number2 = left2.get()
        right_number2 = right2.get()

        top_int2 = int(top_number2)
        bottom_int2 = int(bottom_number2)
        left_int2 = int(left_number2)
        right_int2= int(right_number2)

        imgCV = mosaic_area(imgCV, bottom_int2, top_int2, left_int2, right_int2)
    
    Noise_get = noise_value.get()
    if Noise_get == 0:
        noise_Strength = noise_enter.get()
        noise_int = int(noise_Strength)
        imgCV = cv2.fastNlMeansDenoising(imgCV, h=noise_int)

    elif Noise_get == 1:
        pass

    get_filename = filename_entry.get()
    my_var = None
    extension_var = extension.get()
    if extension_var == 0:
        my_var = '.png'

    elif extension_var == 1:
        my_var = '.jpeg'

    elif extension_var == 2:
        my_var = '.jpg'

    
    extension2 = get_path + '/'  + get_filename + my_var
    cv2.imwrite(extension2,imgCV)

def filedialog_clicked():
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry1.set(iFilePath)


def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry2.set(iDirPath)

def editing_clicked():
    path_neme = IFileEntry.get()
    global fileneme
    fileneme = path_neme
    global imgCV
    imgCV = cv2.imread(fileneme)

    if path_neme == '':
        return
    rdo_value1 = var.get()
    
    #顔自動検出
    if rdo_value1 == 0:
        
        HAAR_FILE = "C:\\Users\\raio\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
        cascade = cv2.CascadeClassifier(HAAR_FILE)

        face = cascade.detectMultiScale(imgCV)
 
        for x,y,w,h in face:
           
            imgCV = imgCV[y:y+h, x:x+w]
    #範囲を指定
    elif rdo_value1 == 1:
        top_number = top.get()
        bottom_number = bottom.get()
        left_number = left.get()
        right_number = right.get()
        
        top_int = int(top_number)
        bottom_int = int(bottom_number)
        left_int = int(left_number)
        right_int = int(right_number)


        imgCV = imgCV[top_int:bottom_int,left_int:right_int]

    elif rdo_value1 == 2:
        pass

    #白黒化
    if bln1.get():

        imgCV = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)
    else:
        pass
    
    if bln2.get():
        JET = 'JET'
        HOT = 'HOT'
        HSV = 'HSV'        
        RAINBOW = 'RAINBOW'
        combobox_value = combobox.get()
        if JET == combobox_value:
            imgCV = cv2.applyColorMap(imgCV, cv2.COLORMAP_JET)

        elif HOT == combobox_value:
            imgCV = cv2.applyColorMap(imgCV, cv2.COLORMAP_HOT)

        elif HSV == combobox_value:
            imgCV = cv2.applyColorMap(imgCV, cv2.COLORMAP_HSV)

        elif RAINBOW == combobox_value:
            imgCV = cv2.applyColorMap(imgCV, cv2.COLORMAP_RAINBOW)

    else:
        pass

    rdo_value2 = value_rotate.get()
    
    if rdo_value2 == 0:
        imgCV = cv2.rotate(imgCV, cv2.ROTATE_90_CLOCKWISE)

    elif rdo_value2 == 1:
           imgCV = cv2.rotate(imgCV, cv2.ROTATE_90_COUNTERCLOCKWISE)

    elif rdo_value2 == 2:
           imgCV = cv2.rotate(imgCV, cv2.ROTATE_180)

    elif rdo_value2 == 3:
        pass       

    else:
        pass  

    rdo_value3 = value_mosaic.get()

    face_cascade_path = "C:\\Users\\raio\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
    if rdo_value3 == 0:

        imgCV = mosaic(imgCV)

    elif rdo_value3 == 1:

        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        faces = face_cascade.detectMultiScale(imgCV)

        for x, y, w, h in faces:

            imgCV = mosaic_area(imgCV, x, y, w, h)

    elif rdo_value3 == 2:
        top_number2 = top2.get()
        bottom_number2 = bottom2.get()
        left_number2 = left2.get()
        right_number2 = right2.get()

        top_int2 = int(top_number2)
        bottom_int2 = int(bottom_number2)
        left_int2 = int(left_number2)
        right_int2= int(right_number2)

        imgCV = mosaic_area(imgCV, bottom_int2, top_int2, left_int2, right_int2)
    
    Noise_get = noise_value.get()
    if Noise_get == 0:
        noise_Strength = noise_enter.get()
        noise_int = int(noise_Strength)
        imgCV = cv2.fastNlMeansDenoising(imgCV, h=noise_int)

    elif Noise_get == 1:
        pass

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", imgCV)


#--GUI--
window = tk.Tk()
window.resizable(0,0)
window.title('画像編集ソフト')
window.geometry('500x300')

notebook = ttk.Notebook(window)
tab_one = tk.Frame(notebook, bg='white')
tab_two = tk.Frame(notebook, bg='white')
tab_three = tk.Frame(notebook,bg='white')

notebook.add(tab_one, text='設定')
notebook.add(tab_two, text='基本編集')
notebook.add(tab_three,text='効果')

notebook.pack(expand=True, fill='both', padx=10, pady=10)


labelframe1 = tkinter.LabelFrame(tab_two, text='トリミング', width=500, height=60)
labelframe1.pack(padx=10, pady=8)

labelframe2 = tkinter.LabelFrame(tab_two, text='カラー', width=500, height=60)
labelframe2.pack(padx=10, pady=8)

labelframe3 = tkinter.LabelFrame(tab_two, text='回転', width=500, height=100)
labelframe3.pack(padx=10, pady=1, anchor=tkinter.SW)

labelframe4 = tkinter.LabelFrame(tab_three, text='モザイク', width=500, height=60)
labelframe4.pack(padx=10, pady=8)

labelframe5 = tkinter.LabelFrame(tab_three, text='ノイズ除去', width=500, height=60)
labelframe5.pack(padx=10, pady=8)


 # Frame2の作成
frame1 = ttk.Frame(tab_one, padding=10)
frame1.place(x=50,y=60)

 # 「ファイル参照」ラベルの作成
IFileLabel = ttk.Label(frame1, text="画像選択")
IFileLabel.pack(side=LEFT)

 # 「ファイル参照」エントリーの作成
entry1 = StringVar()
IFileEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
IFileEntry.pack(side=LEFT)

 # 「ファイル参照」ボタンの作成
IFileButton = ttk.Button(frame1, text="参照", command=filedialog_clicked)
IFileButton.pack(side=LEFT)

 # Frame1の作成
frame2 = ttk.Frame(tab_one, padding=10)
frame2.place(x=50, y=120)

 #「フォルダ参照」ラベルの作成
IDirLabel = ttk.Label(frame2, text="保存先指定")
IDirLabel.pack(side=LEFT)

entry2 = StringVar()
IDirEntry = ttk.Entry(frame2, textvariable=entry2,width=30)
IDirEntry.pack(side=LEFT)

IDirButton = ttk.Button(frame2, text="参照", command=dirdialog_clicked)
IDirButton.pack(side=LEFT)

filename_entry = ttk.Entry(tab_one,width=30)
filename_entry.place(x=7,y=220)
filename_entry.insert(0,'ファイル名')

#extension...「拡張子」
extension = tkinter.IntVar()
extension.set(0)

png = tkinter.Radiobutton(tab_one, value=0,variable=extension, text='png')
png.place(x=200,y=220)

jpeg = tkinter.Radiobutton(tab_one,value=1,variable=extension, text='jpeg')
jpeg.place(x=260,y=220)

jpg = tkinter.Radiobutton(tab_one,value=1,variable=extension, text='jpg')
jpg.place(x=320,y=220)

keep_btn = ttk.Button(tab_one, text="保存", command=save)
keep_btn.place(x=400,y=220)

while_editing = ttk.Button(window, text="編集中の画像を見る", command=editing_clicked)
while_editing.place(x=378,y=10)

var = tkinter.IntVar()
var.set(0)

rdo1 = tkinter.Radiobutton(labelframe1, value=0, variable=var, text='顔自動検出')
rdo1.place(x=1, y=10)

rdo2 = tkinter.Radiobutton(labelframe1, value=1, variable=var, text='指定')
rdo2.place(x=100, y=10)

top = ttk.Entry(labelframe1, width=3)
top.place(x=150, y=10)
top.insert(0, 'top')

bottom = ttk.Entry(labelframe1, width=3)
bottom.place(x=180, y=10)
bottom.insert(0, 'bottom')

left = ttk.Entry(labelframe1, width=3)
left.place(x=210, y=10)
left.insert(0, 'left')

right = ttk.Entry(labelframe1, width=5)
right.place(x=240, y=10)
right.insert(0, 'right')


rdo3 = tkinter.Radiobutton(labelframe1, value=3, variable=var, text='変更しない')
rdo3.place(x=300, y=10)

bln1 = tkinter.BooleanVar()
bln1.set(True)

bln2 = tkinter.BooleanVar()
bln2.set(True)

black_and_white = tkinter.Checkbutton(labelframe2, variable=bln1,text='白黒化')
black_and_white.place(x=10, y=6)

Colorization = tkinter.Checkbutton(labelframe2, variable=bln2, text='疑似カラー化')
Colorization.place(x=80, y=6)

model = ('JET', 'HOT', 'HSV', 'RAINBOW')
v = tk.StringVar()
combobox = ttk.Combobox(labelframe2, values=model, textvariable=v, width=9)
combobox.place(x=170, y=8)

value_rotate = tkinter.IntVar()
value_rotate.set(0)

clockwise = tkinter.Radiobutton(labelframe3, value=0, variable=value_rotate, text='時計周りに90度')
clockwise.place(x=1, y=21)

Counterclockwise = tkinter.Radiobutton(labelframe3,value=1,variable=value_rotate,text='反時計周りに90度')
Counterclockwise.place(x=120,y=21)

upside_down = tkinter.Radiobutton(labelframe3,value=2,variable=value_rotate,text='180度回転')
upside_down.place(x=250,y=21)

no_change = tkinter.Radiobutton(labelframe3,value=3,variable=value_rotate,text='変更無し')
no_change.place(x=360,y=21)

value_mosaic = tkinter.IntVar()
value_mosaic.set(0)

Overall = tkinter.Radiobutton(labelframe4,value=0,variable=value_mosaic,text='全体')
Overall.place(x=1,y=10)

face_mosaic = tkinter.Radiobutton(labelframe4,value=1,variable=value_mosaic,text='顔自動検出モザイク')
face_mosaic.place(x=60,y=10)

face_number = tkinter.Radiobutton(labelframe4,value=2,variable=value_mosaic,text='数値指定')
face_number.place(x=180,y=10)

face_number = tkinter.Radiobutton(labelframe4,value=3,variable=value_mosaic,text='使用しない')
face_number.place(x=370,y=10)


top2= ttk.Entry(labelframe4, width=3)
top2.place(x=250, y=10)
top2.insert(0, 'top')

bottom2 = ttk.Entry(labelframe4, width=3)
bottom2.place(x=280, y=10)
bottom2.insert(0, 'bottom')

left2 = ttk.Entry(labelframe4, width=3)
left2.place(x=310, y=10)
left2.insert(0, 'left')

right2 = ttk.Entry(labelframe4, width=4)
right2.place(x=340, y=10)
right2.insert(0, 'right')

mosaic_var = tkinter.IntVar()
mosaic_var.set(0)



noise_value = tkinter.IntVar()
noise_value.set(0)

noise_removal = tkinter.Radiobutton(labelframe5,value=0,variable=noise_value,text='ノイズ除去')
noise_removal.place(x=10,y=10)

noise_enter = ttk.Entry(labelframe5,width=5)
noise_enter.place(x=90,y=10)
noise_enter.insert(0,'強弱')
#do not use(ノイズ除去を使わないという意味)頭文字を取った変数名
dnu = tkinter.Radiobutton(labelframe5,value=1,variable=noise_value,text='使用しない')
dnu.place(x=170,y=10)

window.mainloop()