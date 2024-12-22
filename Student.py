from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import sqlite3
import cv2

def create_table():
    conn = sqlite3.connect("face_recognize.db")  # Connect to SQLite database
    my_cursor = conn.cursor()
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            dep TEXT,
            course TEXT,
            year TEXT,
            sem TEXT,
            ID TEXT PRIMARY KEY,
            name TEXT,
            Div TEXT,
            roll TEXT,
            Gen TEXT,
            DOB TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            teacher TEXT,
            photo TEXT
        )
    """)
    conn.commit()
    conn.close()
create_table()




class student:
   def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")



        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_ID=StringVar()
        self.var_name=StringVar()
        self.var_Div=StringVar()
        self.var_roll=StringVar()
        self.var_Gen=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img = Image.open("student img 2.jpeg")
        img = img.resize((550, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg = ImageTk.PhotoImage(img)

        # Create label and place the image on it 
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=550, height=130)

# Img2
        img1 = Image.open("student 3.jpg")
        img1 = img1.resize((550, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create label and place the image on it 
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

#Img3
        img2 = Image.open("student img 4.jpeg")
        img2 = img2.resize((547, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)


        img3 = Image.open("Background Full.jpg")
        img3 = img3.resize((1530, 710))  # Ensure the size is a tuple (width, height)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Create label and place the image on it
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=131, width=1530, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Build frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=8,y=52,width=1510,height=600)
        
        #left side lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=800,height=580)

        #Add image
        img_left = Image.open("Hand raise img.jpg")
        img_left = img_left.resize((550, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        # Create label and place the image on it
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #Current Course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="CurrentCourse Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=780,height=110)
        #making label
        depart_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        depart_label.grid(row=0,column=0,padx=10)

        depart_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        depart_combo["values"]=("Select Department","BCA in INFORMATION TECHNOLOGY","BS in DATA SCIENCE","MCA in AI & ML","MS in DATA SCIENCE","GIS & IMAGE PROCESSING(GIS & DIP)")
        depart_combo.current(0)
        depart_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","PROFESSIONAL UG","BS","MS","PGD","PROFESSIONAL PG")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Academic Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Current Semester","Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Department Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=780,height=310)

        # StudentID
        studentId_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=Entry(class_student_frame,textvariable=self.var_ID,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Division
        class_div_label_label=Label(class_student_frame,text="Student Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_label_entry=Entry(class_student_frame,textvariable=self.var_Div,width=20,font=("times new roman",12,"bold"))
        #class_div_label_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B", "C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

        # Roll Number
        roll_no_label=Label(class_student_frame,text="Student Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=Entry(class_student_frame,textvariable=self.var_Gen,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gen,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label=Label(class_student_frame,text="Date Of Birth",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_entry=Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email ID",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone Number
        phone_label=Label(class_student_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        Address_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Sample Image",value="YES")
        radiobutton1.grid(row=6,column=0)
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Sample Image",value="NO")
        radiobutton2.grid(row=6,column=1)

        #Button Frame
        # Button Frame
        btm_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btm_frame.place(x=0, y=210, width=775, height=35)

# Save Button
        save_btn = Button(btm_frame, text="Save", command=self.add_data, width=21, 
                  font=("times new roman", 12, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0)

# Update Button
        update_btn = Button(btm_frame, text="Update", command=self.update_data, width=21, 
                    font=("times new roman", 12, "bold"), bg="skyblue", fg="white")
        update_btn.grid(row=0, column=1)

# Reset Button
        reset_btn = Button(btm_frame, text="Reset", command=self.reset_fields, width=21, 
                   font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)

# Delete Button
        delete_btn = Button(btm_frame, text="Delete", command=self.delete_data, width=21, 
                    font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=3)


        # 2nd Frame
        btm_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btm_frame1.place(x=0,y=250,width=776,height=36)
        take_photo_btn=Button(btm_frame1,command=self.take_sample_image,text="Take Image Sample",width=45,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btm_frame1,text="Update Sample Image",command=self.update_sample_image,width=45,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        

        #Right side lable frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Right_frame.place(x=830,y=10,width=670,height=580)

        #Right Side add img
        img_right = Image.open("images.jpeg")
        img_right = img_right.resize((550, 130))  # Ensure the size is a tuple (width, height)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        # Create label and place the image on it
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=660, height=130)


        # *********Search System*******
        class_search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        class_search_frame.place(x=5,y=135,width=660,height=70)

        search_label=Label(class_search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        serch_combo=ttk.Combobox(class_search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        serch_combo["values"]=("Select","Roll Number","Phone Number")
        serch_combo.current(0)
        serch_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=Entry(class_search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(class_search_frame,text="Search Information",width=15,font=("times new roman",10,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(class_search_frame,text="Show All",width=15,font=("times new roman",10,"bold"),bg="green",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # Table Frame
        class_table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        class_table_frame.place(x=5,y=210,width=658,height=340)

        #scroolbar
        scrool_x=ttk.Scrollbar(class_table_frame,orient=HORIZONTAL)
        scrool_y=ttk.Scrollbar(class_table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(class_table_frame,columns=("dep","course","year","sem","ID","name","Div","roll","Gen","DOB","email","phone","address","teacher","photo"),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_x.config(command=self.student_table.xview)
        scrool_y.config(command=self.student_table.yview)

        #Header
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("Gen",text="Gender")
        self.student_table.heading("DOB",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Image Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("Gen",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

   def add_data(self):
      if self.var_dep.get() == "Select Department" or self.var_ID.get() == "" or self.var_name.get() == "":
        messagebox.showerror("Error", "All Fields are required*", parent=self.root)
      else:
        try:
            conn = sqlite3.connect("face_recognize.db")  # Connect to SQLite database
            my_cursor = conn.cursor()
            my_cursor.execute("""
                INSERT INTO student (dep, course, year, sem, ID, name, Div, roll, Gen, DOB, email, phone, address, teacher, photo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_ID.get(),
                self.var_name.get(),
                self.var_Div.get(),
                self.var_roll.get(),
                self.var_Gen.get(),
                self.var_DOB.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


   def fetch_data(self):
    try:
        conn = sqlite3.connect("face_recognize.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if data:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
        conn.close()
    except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   def get_cursor(self,event=""):
       cursor_focus = self.student_table.focus()
       content = self.student_table.item(cursor_focus)
       data = content["values"]
       if data:
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_ID.set(data[4])
        self.var_name.set(data[5])
        self.var_Div.set(data[6])
        self.var_roll.set(data[7])
        self.var_Gen.set(data[8])
        self.var_DOB.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
   def delete_data(self):
    if self.var_ID.get() == "":
        messagebox.showerror("Error", "Student ID is required to delete a record", parent=self.root)
    else:
        try:
            conn = sqlite3.connect("face_recognize.db")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM student WHERE ID=?", (self.var_ID.get(),))
            conn.commit()
            self.fetch_data()
            self.reset_fields()
            conn.close()
            messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   def reset_fields(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Academic Year")
      self.var_sem.set("Select Current Semester")
      self.var_ID.set("")
      self.var_name.set("")
      self.var_Div.set("")
      self.var_roll.set("")
      self.var_Gen.set("")
      self.var_DOB.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")
   def update_data(self):
    if self.var_ID.get() == "":
        messagebox.showerror("Error", "Student ID is required to update the record", parent=self.root)
    else:
        try:
            conn = sqlite3.connect("face_recognize.db")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE student 
                SET dep=?, course=?, year=?, sem=?, name=?, Div=?, roll=?, Gen=?, DOB=?, email=?, phone=?, address=?, teacher=?, photo=?
                WHERE ID=?
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_name.get(),
                self.var_Div.get(),
                self.var_roll.get(),
                self.var_Gen.get(),
                self.var_DOB.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_ID.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    
   def take_sample_image(self):
    if self.var_ID.get() == "":
        messagebox.showerror("Error", "Student ID is required to take a sample image", parent=self.root)
        return

    try:
        cap = cv2.VideoCapture(0)  # Open the camera
        img_id = 0
        while True:
            ret, frame = cap.read()  # Capture frame-by-frame
            if not ret:
                messagebox.showerror("Error", "Failed to access camera", parent=self.root)
                break

            cv2.imshow("Capture Image", frame)

            # Save image when 's' is pressed
            if cv2.waitKey(1) & 0xFF == ord('s'):
                img_id += 1
                file_name = f"data/user.{self.var_ID.get()}.{img_id}.jpg"
                cv2.imwrite(file_name, frame)
                cv2.putText(frame, f"Image {img_id} Captured", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.imshow("Capture Image", frame)

            # Exit the capture when 'q' is pressed
            elif cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        if img_id > 0:
            messagebox.showinfo("Success", f"{img_id} images captured successfully!", parent=self.root)
        else:
            messagebox.showerror("Error", "No images captured", parent=self.root)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
   def update_sample_image(self):
        try:
            # Logic for updating sample images can be similar or customized
            messagebox.showinfo("Info", "Update Sample Image functionality not yet implemented", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()