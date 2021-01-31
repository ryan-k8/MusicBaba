

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from pygame import mixer  #pygame module ver1.9.6

root = Tk()           #root= main UI of the music player
frame=Frame(root)
frame.pack()

mixer.init()           #initialize Mixer from pygame Module (allows Audio Functions# )

menubar= Menu(root)                #menubar (at top)
root.config(menu=menubar)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()


submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=submenu )        #submenu attributes
submenu.add_command(label="Open",command=browse_file)                            #drop down menus(below as well)
submenu.add_command(label="Exit",command=root.destroy)

def show_info(): #info when clicked on about us
    messagebox.showinfo("About MusicBaba","MusicBaba is a Music Player Coded From Tkinter Python by Ryan Khursheed ( ͡° ͜ʖ ͡°)")

submenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=submenu) #submenu attributes
submenu.add_command(label="About Us",command= show_info)       #drop down menu

root.geometry("640x250")
root.title("MusicBaBa")
root.iconbitmap(r"MusicBaba.ico")

welcome=PhotoImage(file="welcome32.png")
greetphoto=ttk.Label(frame,image=welcome)
greetphoto.grid(row=0,column=2,)

def play_music():       #play music by play_btn also solves file not found/opened error by excpt handling
    try:
        pause              #checks if pause button is initialized/activated or not
    except NameError:      #initialized when pause button is set to false or not activated
       try:
         mixer.music.load(filename)
         mixer.music.play()
         statusbar['text']="Playing Music" + '-' + os.path.basename(filename)
       except:
         messagebox.showerror("File Not Found!","MusicBaBa couldn't find or open the file. please check your file")
    else:
        mixer.music.unpause()       #initialized if pause button is activated


playphoto = PhotoImage(file="play.png")
play_btn= Button(frame,image=playphoto,relief=RAISED,borderwidth=8,command=play_music)
play_btn.grid(row=1,column=1)

def stop_music():                   #stop music by stop_btn
    mixer.music.stop()
    statusbar['text']= "Stopped The Music"
stophoto= PhotoImage(file="stop.png")
stop_btn= Button(frame,image=stophoto,relief=RAISED,borderwidth=8,command=stop_music)
stop_btn.grid(row=1,column=3)

def set_vol(val):
    volume = float(val)/100
    mixer.music.set_volume(volume)  #mixer uses vol range 0 to 1 so converting vol to 0 and 1 by division

def pause_music():
    global pause
    pause = TRUE
    mixer.music.pause()
    statusbar['text'] = "Paused The Music"


pausephoto=PhotoImage(file="pause.png")
pause_btn= Button(frame,image=pausephoto,relief=RAISED,borderwidth=8,command=pause_music)
pause_btn.grid(row=1,column=2,)

def rewind_music():
    mixer.music.rewind()

rewindphoto=PhotoImage(file="rewind.png")
rewind_btn= Button(frame,image=rewindphoto,relief=RAISED,borderwidth=5,command=rewind_music)
rewind_btn.grid(row=2,column=1,pady=10)

scale = ttk.Scale(frame,from_=0,to=100, orient=HORIZONTAL,command=set_vol )  #controls volume of the music
scale.set(50)     #Set vol to 50 when music starts playing otherwise its 0 volume
scale.grid(row=2,column=3,pady=10)

statusbar=ttk.Label(root,text="MusicBaBa Ver0.0.1 by Ryan Khursheed",relief=SUNKEN,anchor=W,font="Arial" )
statusbar.pack(side=BOTTOM,fill=X)
muted=FALSE

def mute_music():
   global muted
   if muted:
       scale.set(50)
       mixer.music.set_volume(0.5)
       mute_btn.config(image=mutephoto)
       muted=FALSE
   else:
       mixer.music.set_volume(0)
       scale.set(0)
       mute_btn.configure(image=unmutephoto)
       muted = TRUE

mutephoto=PhotoImage(file="muted.png")
unmutephoto=PhotoImage(file="unmute.png")

mute_btn= Button(frame,image=mutephoto,borderwidth=5,command=mute_music)
mute_btn.grid(row=2,column=2,pady=10)






root.mainloop()
