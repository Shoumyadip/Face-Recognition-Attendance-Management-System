from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import sqlite3
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")

        # ******* Text Variables *******
        self.var_attendanceId = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()

        # Image 1
        img1 = Image.open("AT 1.webp")
        img1 = img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Image 2
        img2 = Image.open("AT2.jpeg")
        img2 = img2.resize((800, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root, image=self.photoimg2)
        f_lb2.place(x=800, y=0, width=800, height=200)

        # BG Image
        img3 = Image.open("AI BG.jpeg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=8, y=52, width=1510, height=600)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Information", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=800, height=580)

        img_left = Image.open("ATT BG Left.jpeg")
        img_left = img_left.resize((550, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=790, height=370)

        # Labels & Entry
        attendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=("comicsansns 12 bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attendanceId, font=("comicsansns 12 bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        rollLable_label = Label(left_inside_frame, text="Roll:", font=("comicsansns 12 bold"), bg="white")
        rollLable_label.grid(row=0, column=2, padx=4, pady=8)
        atten_roll = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("comicsansns 12 bold"))
        atten_roll.grid(row=0, column=3, pady=8)

        nameLable_label = Label(left_inside_frame, text="Name:", font=("comicsansns 12 bold"), bg="white")
        nameLable_label.grid(row=1, column=0)
        atten_name = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("comicsansns 12 bold"))
        atten_name.grid(row=1, column=1, pady=8)

        depLable_label = Label(left_inside_frame, text="Department:", font=("comicsansns 12 bold"), bg="white")
        depLable_label.grid(row=1, column=2)
        atten_dep = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("comicsansns 12 bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        timeLable_label = Label(left_inside_frame, text="Time:", font=("comicsansns 12 bold"), bg="white")
        timeLable_label.grid(row=2, column=0)
        atten_time = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("comicsansns 12 bold"))
        atten_time.grid(row=2, column=1, pady=8)

        dateLable_label = Label(left_inside_frame, text="Date:", font=("comicsansns 12 bold"), bg="white")
        dateLable_label.grid(row=2, column=2)
        atten_date = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("comicsansns 12 bold"))
        atten_date.grid(row=2, column=3, pady=8)

        attendanceLable_label = Label(left_inside_frame, text="Attendance Status", font=("comicsansns 12 bold"), bg="white")
        attendanceLable_label.grid(row=3, column=0)
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_status, font="comicsansns 12 bold", state="readonly", cursor="hand2")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btm_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btm_frame.place(x=0, y=300, width=785, height=36)

        save_btn = Button(btm_frame, text="Import CSV", command=self.importCsv, width=21, font=("times new roman", 12, "bold"), bg="green", fg="white", cursor="hand2")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btm_frame, text="Export CSV", command=self.exportCsv, width=21, font=("times new roman", 12, "bold"), bg="skyblue", fg="white",cursor="hand2")
        update_btn.grid(row=0, column=1)

        reset_btn = Button(btm_frame, text="Update", width=21, font=("times new roman", 12, "bold"), bg="blue", fg="white",cursor="hand2")
        reset_btn.grid(row=0, column=2)

        delete_btn = Button(btm_frame, text="Reset", command=self.reset_data, width=20, font=("times new roman", 12, "bold"), bg="red", fg="white",cursor="hand2")
        delete_btn.grid(row=0, column=3)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Information", font=("times new roman", 12, "bold"))
        Right_frame.place(x=830, y=10, width=670, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=655, height=485)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("Id", "Roll", "Name", "Department", "Time", "Date", "Attendance Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id", text="Attendance ID")
        self.AttendanceReportTable.heading("Roll", text="Roll")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance Status", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) == 0:
                messagebox.showerror("No Data", "No Data Found To Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Data Export", f"Your Data Exported to {os.path.basename(fln)} Successfully Completed")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attendanceId.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_status.set(rows[6])

    def reset_data(self):
        self.var_attendanceId.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()