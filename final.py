import tkinter as tkp
import pygame
import os
from tkinter.filedialog import askdirectory,askopenfilenames
from PIL import ImageTk, Image
from stagger import read_tag

#window
player = tkp.Tk()
player.title("music player")
player.geometry("600x395")
player.configure(bg='DarkOrchid4')

# pygame init
pygame.init()
pygame.mixer.init()
admin_playlist = tkp.Listbox(width = 35)
playlists = {}
playlist_list = tkp.Listbox()



#########################  functions  #########################
def Play():
    music = admin_playlist.get(tkp.ACTIVE)
    pygame.mixer.music.load(music)
    var.set(music)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume.get())
    # tags = read_tag(admin_playlist.selection_get())
    # print(tags.)
    # cover = ImageTk.PhotoImage(tags.picture)
    # cover_photo.config(image = tags.picture)

def pl_play():
    admin_playlist.delete(0, "end")
    for item in playlists[playlist_list.selection_get()]:
        admin_playlist.insert("end", item)

def Stop():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()
    btnpause.configure(text='unpause', command = Unpause)

def Unpause():
    pygame.mixer.music.unpause()
    btnpause.configure(text = 'pause' , command = Pause)

def ChangeVolume(a):
    a = volume.get()
    pygame.mixer.music.set_volume(a)

def Loadfolder():
    directory = askdirectory()
    admin_playlist.delete(0,"end")
    os.chdir(directory)
    musiclist = os.listdir(directory)
    for item in musiclist:
        if item.endswith(".mp3") or item.endswith(".wav"):
            i = 0
            admin_playlist.insert(i,item)
            i = i+1
def Loadfiles():
    files = askopenfilenames()
    admin_playlist.delete(0,"end")
    for item in files:
        if item.endswith(".mp3") or item.endswith(".wav"):
            i = 0
            admin_playlist.insert(i,os.path.split(item)[1])
            i = i+1
def playlist_creator():
    pl_creator = tkp.Tk()
    pl_creator.title("playlist creator")
    pl_creator.resizable(width=False , height=False)
    plNameLabel = tkp.Label(pl_creator , text = 'playlist name : ')
    plNameLabel.place(x=50 ,y=50)
    plNameGetter = tkp.Entry(pl_creator)
    plNameGetter.place(x=50 , y=75)
    def pl_adder(name):
        playlists[name] = []
        openFile = askopenfilenames()
        playlist_list.delete(0,"end")
        for item in openFile:
            if item.endswith(".mp3") or item.endswith(".wav"):
                playlists[name].append(item)
        for items in playlists:
            playlist_list.insert("end", items)
        # playlist_list.insert("end", name)
        pl_creator.destroy()
    plNameOk = tkp.Button(pl_creator,text = 'select file and create',command=lambda :pl_adder(plNameGetter.get()))

    plNameOk.place(x=50,y=100)


menubar = tkp.Menu(player)
filemenubar = tkp.Menu(menubar, tearoff=0)
filemenubar.add_command(label = 'Open File',command = Loadfiles)
filemenubar.add_command(label = 'Open Folder',command = Loadfolder)
filemenubar.add_command(label = 'Create Playlist' , command = playlist_creator)
filemenubar.add_separator()
filemenubar.add_command(label = 'Exit' , command = player.quit)
menubar.add_cascade(label = 'File' , menu = filemenubar)
player.config(menu = menubar)


#########################  btn  ##############################
# btnplay = tkp.Button(player , width=5 , height=3 , text="play" ,bg= 'tomato', command = Play)

btnstop = tkp.Button(player , width=7 , height=5 , text="stop" ,bg= 'tomato', command = Stop)

btnpause = tkp.Button(player , width=7 , height=5 , text="pause" ,bg= 'tomato', command = Pause)

# btnunpause = tkp.Button(player , width=5 , height=3 , text="unpause" ,bg= 'tomato', command = Unpause)

# btnfolderload = tkp.Button(player , width=32 , height=3 , text="select folder" ,bg='cyan', fg = 'red' , command = Loadfolder)

# btntrackload = tkp.Button(player , width=32 , height=3, text="select track" , bg='cyan' , fg= 'red' , command=Loadfiles)

# make_playlist_btn = tkp.Button(player , width = 32, height=3, text = 'create playlist',bg= 'cyan', fg= 'red' , command=playlist_creator)

#####################  volume  ##########################
volume = tkp.Scale(player , from_=0,to_=100 , resolution=1 , orient = tkp.HORIZONTAL , command = ChangeVolume)


#####################  music name  ######################

var = tkp.StringVar()
musictitle = tkp.Label(player ,bg = 'LightBlue3', textvariable = var)

#####################  bind  ############################

playlist_list.bind("<Double-Button-1>",lambda x:pl_play())
admin_playlist.bind("<Double-Button-1>",lambda x:Play())

#####################  place  ############################

# btnload.pack(side='top',ipadx=0)
# btnfolderload.place(x=0,y=0)
# btntrackload.place(x=370,y=0)
# make_playlist_btn.place(x=0 , y=55)
playlist_list.place(x=475, y=0)
admin_playlist.place(x=0 , y=0)
volume.pack(fill = "x" , pady = 165)
musictitle.place(y = 207)
# btnplay.pack(fill = "x")
btnpause.place(x=277 , y=230)
# btnunpause.pack(fill = "x")
btnstop.place(x=277 , y=315)


player.mainloop()
