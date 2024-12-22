from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from Student import student
from train import Train
from face_recognize import Face_recognize
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")

        # Load the image and resize it img 1
        img = Image.open("Side1.jpeg")
        img = img.resize((500, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg = ImageTk.PhotoImage(img)

        # Create label and place the image on it 
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Img2
        img1 = Image.open("Face img.png")
        img1 = img1.resize((500, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create label and place the image on it 
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        # Img3
        img2 = Image.open("Side 2.jpg")
        img2 = img2.resize((500, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=555, height=130)

        # Image4 BG Image
        img3 = Image.open("Background Full.jpg")
        img3 = img3.resize((1530, 710))  # Ensure the size is a tuple (width, height)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Create label and place the image on it
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=131, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE MANAGEMENT SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # **************Time Show**************
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl=Label(bg_img, font=('time new roman',20,'bold'),background='yellow',foreground='green')
        lbl.place(x=10,y=70,width=170,height=100)
        time()

        # Button img
        img4 = Image.open("Student img.jpg")
        img4 = img4.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_a = Button(bg_img, text="Student Information", command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=200, y=300, width=220, height=40)

        # Face Detection
        img5 = Image.open("Face Detect.webp")
        img5 = img5.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_a = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=500, y=300, width=220, height=40)

        # Attendance Management Button
        img6 = Image.open("Attandence.jpg")
        img6 = img6.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_a = Button(bg_img, text="Attendance Management", cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=800, y=300, width=220, height=40)

        # HelpDesk Button
        img7 = Image.open("Helpdesk.jpg")
        img7 = img7.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_a = Button(bg_img, text="HelpDesk", cursor="hand2",command=self.help_data,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=1100, y=300, width=220, height=40)

        # Train Face
        img8 = Image.open("Train Data.png")
        img8 = img8.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_a = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=200, y=580, width=220, height=40)

        # Photo Button
        img9 = Image.open("Photo button.jpg")
        img9 = img9.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_a = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img10 = Image.open("Developer.jpg")
        img10 = img10.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_a = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img11 = Image.open("Exit button.jpg")
        img11 = img11.resize((220, 220))  # Ensure the size is a tuple (width, height)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_a = Button(bg_img, text="Exit", cursor="hand2",command=self.exit,
                      font=("times new roman", 15, "bold"), bg="green", fg="white")
        b1_a.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognize(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition System","Are you sure exit this software",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()