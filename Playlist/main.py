from pygame import mixer
import os
import random
import tkinter as tk
from tkinter import font

myList=os.listdir("/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios")
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
    mixer.music.stop()
    current_playing=random.choice(myList)
    mixer.music.load("/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios/"+current_playing) 
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



current_playing=random.choice(myList)
mixer.music.load('/home/kartikeya/Desktop/Prob/PLAYLIST-project/audios/'+current_playing)

print("Player Started....")

mixer.music.set_volume(10)

mixer.music.play()
mixer.music.pause()

window.mainloop()




