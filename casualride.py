# from tkinter import *
# root=Tk()
# root.title("Ride Booking App")
# root.geometry("800x700")

# def home():
#     root.destroy()
#     import home



# lbl_1=Label(root,text="Ride Boking App",font=("Arial Bold",40)).place(x=100,y=5)
# lbl_2=Label(root,text="Chartered Ride",font=("Arial",15)).place(x=0,y=70)
# lbl_pickuplocation=Label(root,text="Pickup Location",font=("Arial",15)).place(x=70,y=150)
# lbl_destination=Label(root,text="Destination",font=("Arial",15)).place(x=70,y=180)

# lbl_pickuplocation=Entry(root,width="40").place(x=250,y=155)
# lbl_destination=Entry(root,width="40").place(x=250,y=185)


# btn_home=Button(root,text="Home",font=("Arial",15),command=home).place(x=730,y=70)
# btn_book=Button(root,text="Book",font=("Arial",20),command="").place(x=700,y=630)
# btn_help=Button(root,text="Help",font=("Arial",20),command="").place(x=10,y=630)

# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

def home():
    root.destroy()
    import home

def calculate_fare():
    try:
        # Retrieve dates from DateEntry widgets
        start_date_str = entry_date_from.get_date()
        end_date_str = entry_date_to.get_date()

        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        # Calculate the number of days
        num_days = (end_date - start_date).days

        # Check if the end date is after the start date
        if num_days <= 0:
            messagebox.showerror("Error", "End date should be after start date.")
            return

        # Determine the vehicle type and calculate fare
        vehicle_type = var_vehicle_type.get()
        if vehicle_type == 1:  # Car
            fare = 2000 * num_days
        else:  # Bike
            fare = 600 * num_days

        # Display the fare to the user
        messagebox.showinfo("Fare", f"Total fare: NRP {fare}")
    except ValueError:
        # Handle the case where the date format is invalid
        messagebox.showerror("Error", "Invalid date format. Please enter dates in YYYY-MM-DD format.")


root = tk.Tk()
root.title("Ride Booking App")
root.geometry("800x700")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

header_label = tk.Label(main_frame, text="Ride Booking App", font=("Arial Bold", 40))
header_label.pack(pady=(20, 10))

chartered_label = tk.Label(main_frame, text="Chartered Ride", font=("Arial", 15))
chartered_label.pack()

pickup_label = tk.Label(main_frame, text="Pickup Location", font=("Arial", 15))
pickup_label.pack(pady=(20, 5))

pickup_entry = tk.Entry(main_frame, width=40)
pickup_entry.pack()

destination_label = tk.Label(main_frame, text="Destination", font=("Arial", 15))
destination_label.pack(pady=(20, 5))

destination_entry = tk.Entry(main_frame, width=40)
destination_entry.pack()

date_frame = tk.Frame(main_frame)
date_frame.pack(pady=(20, 10))

date_from_label = tk.Label(date_frame, text="Date From", font=("Arial", 12))
date_from_label.grid(row=0, column=0, padx=(0, 10))

entry_date_from = DateEntry(date_frame, width=12, background='darkblue',
                             foreground='white', borderwidth=2)
entry_date_from.grid(row=0, column=1)

date_to_label = tk.Label(date_frame, text="Date To", font=("Arial", 12))
date_to_label.grid(row=0, column=2, padx=(20, 10))

entry_date_to = DateEntry(date_frame, width=12, background='darkblue',
                           foreground='white', borderwidth=2)
entry_date_to.grid(row=0, column=3)

vehicle_frame = tk.Frame(main_frame)
vehicle_frame.pack(pady=(20, 10))

vehicle_label = tk.Label(vehicle_frame, text="Vehicle Type", font=("Arial", 15))
vehicle_label.pack(side=tk.LEFT)

var_vehicle_type = tk.IntVar()
car_radio = tk.Radiobutton(vehicle_frame, text="Car", variable=var_vehicle_type, value=1, font=("Arial", 12))
car_radio.pack(side=tk.LEFT, padx=10)

bike_radio = tk.Radiobutton(vehicle_frame, text="Bike", variable=var_vehicle_type, value=2, font=("Arial", 12))
bike_radio.pack(side=tk.LEFT)

buttons_frame = tk.Frame(main_frame)
buttons_frame.pack(pady=(30, 0))

home_button = tk.Button(buttons_frame, text="Home", font=("Arial", 15), command=home)
home_button.pack(side=tk.RIGHT, padx=10)

book_button = tk.Button(buttons_frame, text="Book", font=("Arial", 20), command=calculate_fare)
book_button.pack(side=tk.RIGHT, padx=10)

help_button = tk.Button(buttons_frame, text="Help", font=("Arial", 20))
help_button.pack(side=tk.LEFT, padx=10)

root.mainloop()

