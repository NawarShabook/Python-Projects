import time
from tkinter import *
from tkinter import filedialog,messagebox
from tkVideoPlayer import TkinterVideo
import os
import pygame
from pydub import AudioSegment
from videoprops import get_video_properties

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate

window = Tk()
window.title("Tkinter Play Videos in Video Player")
window.geometry("450x450")
window.configure(bg="orange red")

# Initialze Pygame Mixe
pygame.mixer.init()
file=""
videoplayer=""

def open_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",
            filetypes=(('Video Files', ["*.mp4"]),))
    # Load the video file
    video = AudioSegment.from_file(file, "mp4")
    # Save the audio file
    video.export("my_audio.mp3", format="mp3")
    # sound = AudioSegment.from_file("my_audio.mp3")
    # speed_sound = speed_swifter(sound, 1,4)
    # speed_sound.export("my_audio.mp3", format="mp3")
    pygame.mixer.music.load("my_audio.mp3")
    play()


def play():
    global videoplayer
    videoplayer = TkinterVideo(master=window, scaled=True)
    videoplayer.load(r"{}".format(file))
    videoplayer.pack(expand=True, fill="both")
    pygame.mixer.music.play(loops=0, start=0.0,fade_ms=4)
    videoplayer.play()


def video_info():

    global file
    print(file)
    props=get_video_properties(file)

    messagebox.showinfo("Video Info",f"Full Path: {file}\nCodec: {props['codec_name']}\nDimensions: {props['width']} x {props['height']}\n"
                                      f"Aspect Ratio: {props['display_aspect_ratio']} \n"
                                      f"Frame Rate: {props['avg_frame_rate']}")

def playAgain():
    print(file)
    videoplayer.play()
    pygame.mixer.music.unpause()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()


def StopVideo():
    print(file)
    videoplayer.stop()
    pygame.mixer.music.stop()

def PauseVideo():
    print(file)
    pygame.mixer.music.pause()
    videoplayer.pause()



# center this label
lbl1 = Label(window, text="Tkinter Video Player", bg="orange red",
             fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()


playbtn = Button(window, text='Play Video', command=lambda: playAgain())
playbtn.pack(side=TOP, pady=2)

stopbtn = Button(window, text='Stop Video', command=lambda: StopVideo())
stopbtn.pack(side=TOP, padx=3)

pausebtn = Button(window, text='Pause Video', command=lambda: PauseVideo())
pausebtn.pack(side=TOP, padx=4)

my_menu = Menu(window)
window.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Controll Menu", menu=file_menu)
file_menu.add_command(label="open video", command=open_file)
file_menu.add_command(label="display video info", command=video_info)
file_menu.add_command(label="exit", command=lambda:exit())
window.mainloop()