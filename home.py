# from tkinter import *
# root =Tk()
# root.title("Ride Booking App")


# def instant_ride():
#     root.destroy()
#     import instantride1

# def chartered_ride():
#     root.destroy
#     import casualride

# # Create the Ride Booking App text and home button
# app_label =Label(root, text="Ride Booking App", font=("Helvetica", 24, "bold"))
# app_label.grid(row=0, column=3, columnspan=2)
# home_button =Button(root, text="Home", command="")
# home_button.grid(row=2, column=0)

# # Create the instant ride and charted ride buttons
# instant_button =Button(root, text="Instant Ride", font=("Helvetica", 18, "bold"),command=instant_ride)
# instant_button.grid(row=5, column=3, columnspan=2, padx=10, pady=10)
# charted_button =Button(root, text="Charted Ride", font=("Helvetica", 18, "bold"),command=chartered_ride)
# charted_button.grid(row=5, column=7, columnspan=2, padx=10, pady=10)

# # Create the Next button
# next_button =Button(root, text="Next", font=("Helvetica", 18, "bold"))
# next_button.grid(row=11, column=10, pady=10)

# btn_help=Button(root,text="Help",font=("Arial",20),command="").grid(row=11,column=0)

# root.mainloop()


from tkinter import *
from tkinter import messagebox

def instant_ride():
    selected_option.set("Instant Ride")
    instant_button.config(bg="#3b5998")
    charted_button.config(bg="#4682B4")

def chartered_ride():
    selected_option.set("Chartered Ride")
    charted_button.config(bg="#3b5998")
    instant_button.config(bg="#4682B4")

def next_page():
    selected = selected_option.get()
    if selected == "":
        messagebox.showinfo("Error", "Please select a ride option.")
    elif selected == "Instant Ride":
        root.destroy()
        import instantride1
    elif selected == "Chartered Ride":
        root.destroy()
        import casualride

root = Tk()
root.title("Ride Booking App")

# Set window geometry and make it unchangeable
root.geometry("800x500")
root.resizable(False, False)

# Background color
root.configure(bg="#f0f0f0")

# Create the Ride Booking App text
app_label = Label(root, text="Ride Booking App", font=("Arial", 36, "bold"), fg="#333333", bg="#f0f0f0")
app_label.place(x=200, y=20)

# Home label
home_label = Label(root, text="Home", font=("Arial", 16), fg="#FFA500", bg="#f0f0f0")
home_label.place(x=20, y=20)

# Help button
btn_help = Button(root, text="Help", font=("Arial", 16), bg="#FFA500", fg="white", padx=10, pady=5)
btn_help.place(x=700, y=20)

# Create the options buttons
selected_option = StringVar()
selected_option.set("")
instant_button = Radiobutton(root, text="Instant Ride", font=("Arial", 18), bg="#4682B4", fg="white", variable=selected_option, value="Instant Ride", padx=20, pady=10, command=instant_ride)
instant_button.place(x=100, y=150, width=250, height=100)

charted_button = Radiobutton(root, text="Chartered Ride", font=("Arial", 18), bg="#4682B4", fg="white", variable=selected_option, value="Chartered Ride", padx=20, pady=10, command=chartered_ride)
charted_button.place(x=450, y=150, width=250, height=100)

# Create the Next button
next_button = Button(root, text="Next", font=("Arial", 18, "bold"), bg="#32CD32", fg="white", padx=20, pady=10, command=next_page)
next_button.place(x=350, y=350, width=100, height=50)

root.mainloop()
