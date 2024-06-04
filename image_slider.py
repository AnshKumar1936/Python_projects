from itertools import cycle
from PIL import Image ,ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image SlideShow Viewer")

#List of Image Path
image_paths = [
    r"C:\Users\kingr\Downloads\download.jpeg"
    r"C:\Users\kingr\Downloads\wp9342857-gta-5-pc-4k-wallpapers.jpg"
    r"C:\Users\kingr\Downloads\wp9365311-gta-5-pc-4k-wallpapers.jpg"
    r"C:\Users\kingr\Downloads\pexels-lalesh-aldarwish-168938.jpg"
    r"C:\Users\kingr\Downloads\pexels-irina-iriser-1366957.jpg"
]

#Resixe the image 
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root , text='Play Slideshow' , command=start_slideshow)
play_button.pack()

root.mainloop()

