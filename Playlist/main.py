from pygame import mixer
import os
import tkinter as tk
from tkinter import font 
import numpy as np

myList=os.listdir("/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios")
myList2=os.listdir("/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios")
mixer.init()
# next=0

def play_click():   
    # text_label.config(text=current_playing+"is playing..")
    mixer.music.unpause()

def pause_click():
    # text_label.config(text=current_playing+"is paused..")
    mixer.music.pause()	

def stop_click():
    # mixer.music.pause()	
    global current_index
    mixer.music.stop()
    current_index=np.random.randint(len(myList))
    current_playing=myList[current_index]
    mixer.music.load("/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios/"+current_playing)
    print(current_playing) 
    if(len(myList)>1):
        myList.remove(current_playing)
    else:
        print("PLaylist completed once.")
        myList.remove(current_playing)
        myList.extend(myList2)
    mixer.music.set_volume(10)
    mixer.music.play()
    text_label.config(text=current_playing+"is the current song.")

window = tk.Tk()
window.title("Random Player")
window.geometry("600x400")
text_label = tk.Label(window, text="Press Play.",font=font.Font(size=30))
text_label.pack(padx=10, pady=10)


play = tk.Button(window, text="Play",font=font.Font(size=20), command=play_click)
play.pack(pady=10)

pause = tk.Button(window, text="Pause",font=font.Font(size=20), command=pause_click)
pause.pack(pady=10)

stop = tk.Button(window, text="Next",font=font.Font(size=20), command=stop_click)
stop.pack(pady=10)


current_index=np.random.randint(len(myList))
current_playing=myList[current_index]
mixer.music.load('/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios/'+current_playing)
text_label.config(text=current_playing+"is the current song.")

print("Player Started....")
print(current_playing)
myList.remove(current_playing)

mixer.music.set_volume(10)

mixer.music.play()
mixer.music.pause()

window.mainloop()




