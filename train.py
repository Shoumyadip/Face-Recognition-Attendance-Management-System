from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")

        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("Face img.png")
        img_top = img_top.resize((1530, 325))  # Ensure the size is a tuple (width, height)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Button Creation
        bt_1 = Button(self.root, text="Train Data", command=self.train_classifier,cursor="hand2", width=21, font=("times new roman", 30, "bold"), bg="green", fg="black")
        bt_1.place(x=0, y=380, width=1527, height=60)

        img_bottom = Image.open("train dataset2.jpeg")
        img_bottom = img_bottom.resize((1530, 325))  # Ensure the size is a tuple (width, height)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Create label and place the image on it
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        try:
            data_dir = "data"
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", f"Data directory '{data_dir}' does not exist!")
                return

            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.jpeg', '.png'))]

            faces = []
            ids = []

            for image in path:
                try:
                    img = Image.open(image).convert('L')  # Convert into grayscale
                    imageNp = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename
                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)==13  # Display image briefly
                except Exception as e:
                    print(f"Error processing image {image}: {e}")
                    continue

            ids = np.array(ids)

            # Train the classifier Using Local Binary Pattern Histogram
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")

            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Dataset Training Successfully Completed!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
