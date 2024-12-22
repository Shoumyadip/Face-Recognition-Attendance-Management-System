import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import itertools
from main import Face_Recognition_System  # Import the main face recognition system

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initialize the database with a users table."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Functions
def register_user():
    """Register a new user in the database."""
    username = entry_username_register.get()
    password = entry_password_register.get()

    if not username or not password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    finally:
        conn.close()

def login_user():
    """Log in the user and open the main system if credentials are valid."""
    username = entry_username_login.get()
    password = entry_password_login.get()

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Success", f"Welcome {username}! You are now in the Attendance Management System.")
        open_face_recognition_system()  # Open the main face recognition system
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def forgot_password():
    """Open the forgot password window."""
    global forgot_password_window, entry_username_forgot, entry_new_password

    forgot_password_window = tk.Toplevel(login_window)
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("400x250")
    forgot_password_window.configure(bg="#e6f7ff")

    tk.Label(forgot_password_window, text="Reset Password", font=("Helvetica", 18, "bold"), bg="#e6f7ff", fg="#007acc").pack(pady=10)
    tk.Label(forgot_password_window, text="Enter your username:", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=5)
    entry_username_forgot = tk.Entry(forgot_password_window, font=("Helvetica", 12), bg="#ffffff")
    entry_username_forgot.pack(pady=5)

    tk.Label(forgot_password_window, text="Enter new password:", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=5)
    entry_new_password = tk.Entry(forgot_password_window, font=("Helvetica", 12), bg="#ffffff", show="*")
    entry_new_password.pack(pady=5)

    tk.Button(forgot_password_window, text="Reset Password", font=("Helvetica", 12), bg="#007acc", fg="#ffffff", command=reset_password).pack(pady=15)

def reset_password():
    """Reset the password for a given username."""
    username = entry_username_forgot.get()
    new_password = entry_new_password.get()

    if not username or not new_password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        c.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
        conn.commit()
        messagebox.showinfo("Success", "Password has been reset!")
        forgot_password_window.destroy()
    else:
        messagebox.showerror("Error", "Username not found!")

    conn.close()

def open_register_window():
    """Open the register window."""
    global register_window, entry_username_register, entry_password_register

    register_window = tk.Toplevel(login_window)
    register_window.title("Register")
    register_window.geometry("400x300")
    register_window.configure(bg="#e6f2ff")

    tk.Label(register_window, text="Register", font=("Helvetica", 20, "bold"), fg="#0066cc", bg="#e6f2ff").pack(pady=10)
    tk.Label(register_window, text="Username:", font=("Helvetica", 12), bg="#e6f2ff").pack(pady=5)
    entry_username_register = tk.Entry(register_window, font=("Helvetica", 12), bg="#ffffff")
    entry_username_register.pack(pady=5)

    tk.Label(register_window, text="Password:", font=("Helvetica", 12), bg="#e6f2ff").pack(pady=5)
    entry_password_register = tk.Entry(register_window, font=("Helvetica", 12), bg="#ffffff", show="*")
    entry_password_register.pack(pady=5)

    tk.Button(register_window, text="Register", font=("Helvetica", 12), bg="#0066cc", fg="#ffffff", command=register_user).pack(pady=15)

def animate_logo():
    """Function to animate the logo."""
    for frame in itertools.cycle(logo_frames):
        logo_label.configure(image=frame)
        login_window.update_idletasks()
        login_window.after(100)

def open_face_recognition_system():
    """Open the main face recognition system window."""
    login_window.destroy()  # Close the login window
    root = tk.Tk()  # Create a new root window
    obj = Face_Recognition_System(root)  # Initialize the main system
    root.mainloop()  # Start the event loop

# Main window
login_window = tk.Tk()
login_window.title("Advanced Login System")
login_window.geometry("500x650")
login_window.configure(bg="#f5f5f5")

# Logo area with animation
try:
    logo_frames = [ImageTk.PhotoImage(Image.open(f"frame{i}.png").resize((120, 120), Image.ANTIALIAS)) for i in range(1, 5)]
except Exception as e:
    print("Could not load logo frames:", e)
    logo_frames = []

logo_label = tk.Label(login_window, bg="#f5f5f5")
logo_label.pack(pady=20)
if logo_frames:
    login_window.after(100, animate_logo)  # Start logo animation if frames exist
else:
    logo_label.configure(text="System Software", font=("Helvetica", 16, "bold"), fg="#0066cc")

# Welcome section
tk.Label(login_window, text="Welcome to Attendance Management System", 
         font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#4CAF50").pack(pady=10)

tk.Label(login_window, text="Please log in to access the system", font=("Helvetica", 12), bg="#f5f5f5", fg="#555555").pack()

# Login frame
frame_login = tk.Frame(login_window, bg="#ffffff", bd=0, relief="groove")
frame_login.pack(pady=20, padx=20)

tk.Label(frame_login, text="Username:", font=("Helvetica", 12), bg="#ffffff", fg="#555555").pack(pady=5)
entry_username_login = tk.Entry(frame_login, font=("Helvetica", 12), bg="#f9f9f9")
entry_username_login.pack(pady=5)

tk.Label(frame_login, text="Password:", font=("Helvetica", 12), bg="#ffffff", fg="#555555").pack(pady=5)
entry_password_login = tk.Entry(frame_login, font=("Helvetica", 12), bg="#f9f9f9", show="*")
entry_password_login.pack(pady=5)

tk.Button(frame_login, text="Login", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="#ffffff", command=login_user).pack(pady=15)

# Forgot Password and Register buttons
tk.Button(login_window, text="Forgot Password?", font=("Helvetica", 12), bg="#FF5733", fg="#ffffff", command=forgot_password).pack(pady=5)
tk.Label(login_window, text="Don't have an account?", font=("Helvetica", 10), bg="#f5f5f5").pack(pady=5)
tk.Button(login_window, text="Register Here", font=("Helvetica", 12), bg="#2196F3", fg="#ffffff", command=open_register_window).pack(pady=5)

# Footer decoration
footer_canvas = tk.Canvas(login_window, width=500, height=100, bg="#e6f2ff", highlightthickness=0)
footer_canvas.pack(side="bottom")
footer_canvas.create_oval(300, 300, 600, 50, fill="#0066cc", outline="")

# Initialize the database
init_db()

# Run the application (start the login window first)
login_window.mainloop()
