from tkinter import *
import pygame
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title('MP3 Audio Player')
root.configure(bg='green')
root.geometry("500x400")

# Initialze Pygame Mixer
pygame.mixer.init()

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    # # strip out the directory info and .mp3 extension from the song name
    song = song.replace(".mp3", "")

    # Add song to listbox
    song_box.insert(END, song)

# Play selected song
def play():
    # Set Stopped Variable To False So Song Can Play
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Get current Volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it easier to work with
    current_volume = current_volume * 100
    # slider_label.config(text=current_volume * 100)

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    elif int(current_volume) >= 25 and int(current_volume) <= 50:
        volume_meter.config(image=vol2)
    elif int(current_volume) >= 50 and int(current_volume) <= 75:
        volume_meter.config(image=vol3)
    elif int(current_volume) >= 75 and int(current_volume) <= 100:
        volume_meter.config(image=vol4)


# Stop playing current song
global stopped
stopped = False

def stop():

    # Stop Song From Playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    # Set Stop Variable To True
    global stopped
    stopped = True
    # Get current Volume
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    elif int(current_volume) >= 25 and int(current_volume) <= 50:
        volume_meter.config(image=vol2)
    elif int(current_volume) >= 50 and int(current_volume) <= 75:
        volume_meter.config(image=vol3)
    elif int(current_volume) >= 75 and int(current_volume) <= 100:
        volume_meter.config(image=vol4)

# Create Global Pause Variable
global paused
paused = False


# Pause and Unpause The Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

    # Get current Volume
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100


    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    elif int(current_volume) >= 25 and int(current_volume) <= 50:
        volume_meter.config(image=vol2)
    elif int(current_volume) >= 50 and int(current_volume) <= 75:
        volume_meter.config(image=vol3)
    elif int(current_volume) >= 75 and int(current_volume) <= 100:
        volume_meter.config(image=vol4)


# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="yellow", width=60, selectbackground="yellow", selectforeground="black")
song_box.grid(row=0, column=0)

# Define Player Control Button Images
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')
add_btn_img = PhotoImage(file='images/add50.png')

# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='images/volume0.png')
vol1 = PhotoImage(file='images/volume1.png')
vol2 = PhotoImage(file='images/volume2.png')
vol3 = PhotoImage(file='images/volume3.png')
vol4 = PhotoImage(file='images/volume4.png')

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=30)

# Create Player Control Buttons

play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)
add_button = Button(controls_frame, image=add_btn_img, borderwidth=0, command=add_song )

play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)
add_button.grid(row=0, column=5, padx=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

root.mainloop()