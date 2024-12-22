from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import sqlite3
import cv2

class Help:
   def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System By Shoumyadip")


        title_lbl = Label(self.root, text="Welcome To Help Desk Technical Support", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # ******Bakground Image******
        img_top = Image.open("Tech Support.jpg")
        img_top = img_top.resize((1530, 727))  # Ensure the size is a tuple (width, height)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=727)


        help_lbl = Label(f_lbl, text="Email:-shoumyadipdey00@gmail.com", font=("times new roman", 30, "bold"),fg="dark blue")
        help_lbl.place(x=850, y=200)







if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()