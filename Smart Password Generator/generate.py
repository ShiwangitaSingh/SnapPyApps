# Importing required libraries
import tkinter  
from tkinter import *  
import customtkinter  
from customtkinter import *  
import random  
import string  

# Function to generate a password based on user input
def gen():
    try:
        # Initialize lists for components of the password
        name = [] 
        year = []  
        day = []  
        punc = ["@", "#", "$", "%", "&", "*", "!", "?", ","] 
        letter = string.ascii_letters  

        # Get user input
        fname = str(ffname.get())  # First name
        lname = str(llname.get())  # Last name
        mm = str(mmm.get())  # Birth date
        yr = str(yyear.get())  # Birth year

        # Create variations of the name
        name.append(fname[0].lower() + lname[0].upper())
        name.append(fname[0].upper() + lname[0].lower())

        # Add birth year and date to their respective lists
        year.append(yr)
        day.append(mm)

        # Create a list of lists for password components
        pw = [name, year, day, punc]
        spw = []  # To store the selected password components

        # Select one element from each sublist randomly
        for _ in range(4):
            temp = random.choice(pw)
            spw.append(random.choice(temp))
            pw.remove(temp)  # Remove the used list to ensure no duplicates

        # Create the password string
        pw_str = ''.join(spw)
        pw_str += random.choice(letter)  # Add a random letter for additional complexity

        # Display the generated password
        result1.configure(text=f"Your Smartly Generated Password is {pw_str}")

    except:
        # Handle any errors (e.g., if user inputs are invalid)
        result1.configure(text="Oh! It seems you entered some wrong values\nEnter valid details please !!!")


# Setting the appearance of the app to match the system's theme
customtkinter.set_appearance_mode("System")

# Creating the main app window
app = customtkinter.CTk()
app.geometry("720x480")  # Setting the window size
app.title("Smart Password Generator")  # Setting the window title

# UI Elements
# Frame 1: Collecting user's first and last name
frame1 = CTkFrame(app)
frame1.pack(padx=10, pady=10)

label_1 = CTkLabel(frame1, text="Enter your First Name")
label_1.pack(side=LEFT, padx=10, pady=10)

Fname = StringVar()  # Variable to hold first name
ffname = CTkEntry(frame1, width=100, height=40, textvariable=Fname)
ffname.pack(side=LEFT, padx=10, pady=10)

label_2 = CTkLabel(frame1, text="Enter your Last Name")
label_2.pack(side=LEFT, padx=10, pady=10)

Lname = StringVar()  # Variable to hold last name
llname = CTkEntry(frame1, width=100, height=40, textvariable=Lname)
llname.pack(side=RIGHT, padx=10, pady=10)

# Frame 2: Collecting user's birth year and date
frame2 = CTkFrame(app)
frame2.pack(padx=10, pady=10)

label_3 = CTkLabel(frame2, text="Enter your Birth Year")
label_3.pack(side=LEFT, padx=10, pady=10)

Year = StringVar()  # Variable to hold birth year
yyear = CTkEntry(frame2, width=100, height=40, textvariable=Year)
yyear.pack(side=LEFT, padx=10, pady=10)

label_4 = CTkLabel(frame2, text="Enter your Birth Date")
label_4.pack(side=LEFT, padx=10, pady=10)

MM = StringVar()  # Variable to hold birth date
mmm = CTkEntry(frame2, width=100, height=40, textvariable=MM)
mmm.pack(side=RIGHT, padx=10, pady=10)

# Button to trigger password generation
button = CTkButton(master=app, text="Generate", command=gen)
button.pack(padx=10, pady=10)

# Frame 3: Display the generated password
frame3 = CTkFrame(app)
frame3.pack(padx=10, pady=5)

result1 = CTkLabel(frame3, text="Let's Go")
result1.pack(padx=10, pady=10)

# Running the app
app.mainloop()
