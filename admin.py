import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *

# Connect to the SQLite database
conn = sqlite3.connect("userdb.db")
cursor = conn.cursor()

# Create a table named 'users' if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT,
        dob TEXT
    )
""")
conn.commit()

def admin_login():
    global username_entry, password_entry
    username = username_entry.get()
    password = password_entry.get()

    # Dummy admin credentials for demonstration
    if username == "admin" and password == "admin":
        login_success()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def login_success():
    login_window.destroy()

    # Open the admin dashboard
    admin_dashboard()

def add_user():
    global user_id_entry, name_entry, email_entry, phone_entry, gender_var, dob_entry
    try:
        user_id = int(user_id_entry.get())
    except ValueError:
        messagebox.showerror("Error", "User ID must be an integer")
        return

    # Insert user data into the database
    cursor.execute("""
        INSERT INTO users (id, name, email, phone, gender, dob) VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, name_entry.get(), email_entry.get(), phone_entry.get(), gender_var.get(), dob_entry.get()))
    conn.commit()

    messagebox.showinfo("Success", "User added successfully")

def update_user():
    global user_id_entry, name_entry, email_entry, phone_entry, gender_var, dob_entry
    try:
        user_id = int(user_id_entry.get())
    except ValueError:
        messagebox.showerror("Error", "User ID must be an integer")
        return

    # Update user data in the database
    cursor.execute("""
        UPDATE users SET name=?, email=?, phone=?, gender=?, dob=? WHERE id=?
    """, (name_entry.get(), email_entry.get(), phone_entry.get(), gender_var.get(), dob_entry.get(), user_id))
    conn.commit()

    messagebox.showinfo("Success", "User updated successfully")

def display_details():
    # Create a new window to display the details in a table
    details_window = Toplevel()
    details_window.title("Details Table")

    # Create a Treeview widget
    tree = ttk.Treeview(details_window)
    tree["columns"] = ("ID", "Name", "Email", "Phone", "Gender", "Date of Birth")
    tree.heading("#0", text="Type")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Email", text="Email")
    tree.heading("Phone", text="Phone")
    tree.heading("Gender", text="Gender")
    tree.heading("Date of Birth", text="Date of Birth")

    # Fetch user details from the database
    cursor.execute("SELECT * FROM users")
    users_data = cursor.fetchall()

    # Insert user details into the Treeview
    for user in users_data:
        tree.insert("", "end", text="User", values=user)

    tree.pack(expand=True, fill="both")

def admin_dashboard():
    # Create the admin dashboard window
    global user_id_entry, name_entry, email_entry, phone_entry, gender_var, dob_entry
    dashboard_window = Tk()
    dashboard_window.title("Admin Dashboard")

    # Custom frame with styling
    frame_mid = CTkFrame(dashboard_window, width=800, height=500, bg_color="#f8f9fa", border_color="#adb5bd")
    frame_mid.place(x=50, y=50)

    # User data input
    Label(frame_mid, text="User ID:", font=("Arial", 14)).place(x=50, y=50)
    user_id_entry = Entry(frame_mid, font=("Arial", 14))
    user_id_entry.place(x=200, y=50)

    Label(frame_mid, text="Name:", font=("Arial", 14)).place(x=50, y=100)
    name_entry = Entry(frame_mid, font=("Arial", 14))
    name_entry.place(x=200, y=100)

    Label(frame_mid, text="Email:", font=("Arial", 14)).place(x=50, y=150)
    email_entry = Entry(frame_mid, font=("Arial", 14))
    email_entry.place(x=200, y=150)

    Label(frame_mid, text="Phone:", font=("Arial", 14)).place(x=50, y=200)
    phone_entry = Entry(frame_mid, font=("Arial", 14))
    phone_entry.place(x=200, y=200)

    Label(frame_mid, text="Gender:", font=("Arial", 14)).place(x=50, y=250)
    gender_var = StringVar(frame_mid)
    gender_var.set("Male")
    Radiobutton(frame_mid, text="Male", variable=gender_var, value="Male", font=("Arial", 14)).place(x=200, y=250)
    Radiobutton(frame_mid, text="Female", variable=gender_var, value="Female", font=("Arial", 14)).place(x=300, y=250)

    Label(frame_mid, text="Date of Birth (YYYY-MM-DD):", font=("Arial", 14)).place(x=50, y=300)
    dob_entry = Entry(frame_mid, font=("Arial", 14))
    dob_entry.place(x=300, y=300)

    add_button = Button(frame_mid, text="Add User", command=add_user, font=("Arial", 14))
    add_button.place(x=50, y=350)

    # Update User button
    update_button = Button(frame_mid, text="Update User", command=update_user, font=("Arial", 14))
    update_button.place(x=200, y=350)

    # Display ride details
    ride_label = Label(frame_mid, text="Ride Details", font=("Arial", 16))
    ride_label.place(x=50, y=400)

    # Button to display details in a table
    details_button = Button(frame_mid, text="Display Details", command=display_details, font=("Arial", 14))
    details_button.place(x=50, y=450)

    dashboard_window.geometry("900x600")
    dashboard_window.mainloop()

# Create the login window
login_window = Tk()
login_window.title("Admin Login")

# Custom frame with styling
frame_mid = CTkFrame(login_window, width=400, height=250, bg_color="#f8f9fa", border_color="#adb5bd")
frame_mid.place(x=100, y=50)

Label(frame_mid, text="Username:", font=("Arial", 14)).place(x=50, y=50)
username_entry = Entry(frame_mid, font=("Arial", 14))
username_entry.place(x=200, y=50)

Label(frame_mid, text="Password:", font=("Arial", 14)).place(x=50, y=100)
password_entry = Entry(frame_mid, show="*", font=("Arial", 14))
password_entry.place(x=200, y=100)

login_button = Button(frame_mid, text="Login", command=admin_login, font=("Arial", 14))
login_button.place(x=150, y=150)

login_window.geometry("600x400")
login_window.mainloop()
