from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import sqlite3
import cv2

class Developer:
   def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System By SHOUMYADIP")


        title_lbl = Label(self.root, text="WELCOME TO DEVELOPER PAGE", font=("times new roman", 35, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # ******Bakground Image******
        img_top = Image.open("dev img.png")
        img_top = img_top.resize((1530, 727))  # Ensure the size is a tuple (width, height)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=727)

        # Build frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=1000,y=0,width=500,height=650)

        # ******Frame Image********
        img_top1 = Image.open("DSC_0312.JPG")
        img_top1 = img_top1.resize((250, 250))  # Ensure the size is a tuple (width, height)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # Create label and place the image on it
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=250, height=250)

        # Developer Details
        course_label=Label(main_frame,text="Hello My Name, SHOUMYADIP",font=("times new roman",12,"bold"),bg="white")
        course_label.place(x=0,y=5)

        course_label=Label(main_frame,text="I am AI & ML Developer",font=("times new roman",12,"bold"),bg="white")
        course_label.place(x=0,y=40)

        course_label=Label(main_frame,text="Department Of Computer Application & IT",font=("times new roman",12,"bold"),bg="white")
        course_label.place(x=0,y=80)

        img2 = Image.open("Dev Window.jpeg")
        img2 = img2.resize((500, 370))  # Ensure the size is a tuple (width, height)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create label and place the image on it
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=250, width=500, height=425)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()