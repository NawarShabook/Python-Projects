from tkinter import *
from tkinter import filedialog, messagebox
import random
import pyautogui
from moviepy.editor import ImageSequenceClip
import os

def open_image():
  file_path = filedialog.askopenfilename( initialdir=os.getcwd(),title="Select image file", filetypes=(("PNG File", "*.png"),("all","*")))
  return file_path



root = Tk()
root.title('NSH motion graphic')
root.geometry("800x600")

w = 400
h = 400
x = w/2
y = h/2

# Open Add Image To Canvas
my_canvas = Canvas(root, width=w, heigh=h, bg="white")
my_canvas.pack(pady=20)
img = PhotoImage(file=open_image())

my_image = my_canvas.create_image(10,10, anchor=NW, image=img)

def left():
	x = -10
	y = 0
	my_canvas.move(my_image, x, y)

def right():
	x = 10
	y = 0
	my_canvas.move(my_image, x, y)


def up():
	x = 0
	y = -10
	my_canvas.move(my_image, x, y)

def down():
	x = 0
	y = 10
	my_canvas.move(my_image, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.after(1, left)
root.after(1, right)
root.after(1, up)
root.after(1, down)

def move_image(count=0, stop=0):
	global animation_id

	# generate random x and y coordinates
	x = random.randint(10, 350)
	y = random.randint(10, 350)
	if stop == 1:
		root.after_cancel(animation_id)
	else:
		if x > 400 or y > 400:
			my_canvas.move(my_image, -400, -400)
		else:
			my_canvas.move(my_image, x - my_canvas.coords(my_image)[0], y - my_canvas.coords(my_image)[1])
		screenshot = pyautogui.screenshot(region=(root.winfo_x()+210, root.winfo_y()+75, 400, 400))
		# save the screenshot as an image file
		# screenshot = my_canvas.grab()
		screenshot.save(os.path.join("screenshots", f"screenshot_{count}.png"))
		animation_id = root.after(500, move_image, count+1)

def stop_image():
	move_image(0 , 1)

def export_video():
	# create a video from a sequence of images in the "screenshots" directory
	clip = ImageSequenceClip("screenshots", fps=4)
	# save the video to a file
	clip.write_videofile("motions_videos/video.mp4")
	messagebox.showinfo("Video Exproted Successfully ", f"\nmotions_videos/video.mp4")

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Controll Menu", menu=file_menu)
file_menu.add_command(label="move", command=move_image)
file_menu.add_command(label="stop", command=stop_image)
file_menu.add_command(label="export as video", command=export_video)
file_menu.add_command(label="exit", command=lambda:exit())

root.mainloop()



