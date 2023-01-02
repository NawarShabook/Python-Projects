from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image,ImageTk
import os

img=""
file_path=""
def open_image():
  file_path = filedialog.askopenfilename( initialdir=os.getcwd(),title="Select image file", filetypes=(("JPG File","*.jpg"),("PNG File", "*.png")))
  return file_path

def show_image():
    global img
    global file_path
    file_path =open_image()
    img=Image.open(file_path)
    img_photo=ImageTk.PhotoImage(img)
    lbl.configure(image=img_photo)
    lbl.image=img_photo

def show_image_info():
    file_info = os.stat(file_path)
    file_name = os.path.basename(file_path)
    file_date = file_info.st_mtime
    file_size = file_info.st_size
    width, height = img.size
    format = img.format
    mode = img.mode
    messagebox.showinfo("Image Info", f"File name: {file_name}\nDimensions: {width}x{height}\n"
                                      f"Size: {file_size} bytes\nDate: {file_date}\n"
                                      f"Format: {format}\nMode: {mode}")

counter = 0
def resize():
    global counter
    counter += 1
    # Get the new size from the scale widget
    new_size = size.get()

    # Resize the image using PIL
    resized_image = img.resize((new_size, new_size), Image.ANTIALIAS)

    # Save the image in a folder
    folder = "resized_photos"
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_name = f"resized_image_{counter}.jpg"
    resized_image.save(os.path.join(folder, file_name))
    messagebox.showinfo("Success", "تم تغيير الأبعاد وحفظ الصورة الجديدة بنجاح")


root=Tk()
fram=Frame(root)
fram.pack(side=BOTTOM, padx=15,pady=15)

lbl=Label(root)
lbl.pack()

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Controll Menu", menu=file_menu)
file_menu.add_command(label="اختيار صورة", command=show_image)
file_menu.add_command(label="عرض تفاصيل الصورة", command=show_image_info)
file_menu.add_command(label="خروج", command=lambda:exit())

size = IntVar()
scale = tk.Scale(fram, from_=50, to=200, orient=tk.HORIZONTAL, variable=size)
btn3 = tk.Button(fram, text="تغيير أبعاد الصورة", command=resize)
btn3.pack()
scale.pack()


root.title("Image Viewer")
root.geometry("400x450")
root.mainloop()
