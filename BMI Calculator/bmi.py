# Important Libraries
import tkinter
from tkinter import *
import customtkinter
from customtkinter import *

# Function 
def bmi_calc():
    try:
        w = int(weight.get())
        h = int(height.get())
        h /= 100
        h = round(h,3)
        ybmi = w/h**2
        ybmi = round(ybmi,2)
        result1.configure(text=f"Your weight is {w} Kg\nYour height is {h} m\n\nYour BMI is {ybmi} kg per m square")
        if 18.5<=ybmi<25:
            result2.configure(text="You are Healthy")
        elif 18.5>ybmi:
            result2.configure(text="You have low body weight")
        elif ybmi>=25:
            result2.configure(text="You have obesity")

    except:
        result1.configure(text="Oh ! It seems you entered some wrong values\nEnter details in given unit please !!!")
        result2.configure(text="Don't play with your health")


# System setting
customtkinter.set_appearance_mode("System")

# Framing 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("BMI Calculator")

# UI elements
# frame 1
frame1 = CTkFrame(app)
frame1.pack(padx=10, pady=10)

label_1 = CTkLabel(frame1, text="Enter your body's weight")
label_1.pack(side = LEFT, padx=10, pady=10)

unit1 = CTkLabel(frame1, text="in Kg")
unit1.pack(side = RIGHT, padx=10, pady=10)

weight_var = StringVar()
weight = CTkEntry(frame1, width=50, height=50, textvariable=weight_var)
weight.pack(side = RIGHT, padx=0, pady=10)

# frame 2
frame2 = CTkFrame(app)
frame2.pack()

label_2 = CTkLabel(frame2, text="Enter your height")
label_2.pack(side = LEFT, padx=10, pady=10)

unit2 = CTkLabel(frame2, text="in cm")
unit2.pack(side = RIGHT, padx=10, pady=10)

height_var = StringVar()
height = CTkEntry(frame2, width=50, height=50, textvariable=height_var)
height.pack(side = RIGHT, padx=0, pady=10)

button = CTkButton(master=app, text="Calculate", command=bmi_calc)
button.pack(padx=10, pady=10)

# frame 3
frame3 = CTkFrame(app)
frame3.pack()

result1 = CTkLabel(frame3, text="Let's check")
result1.pack(padx=10, pady=5)

result2 = CTkLabel(frame3, text="Your Health")
result2.pack(padx=10, pady=5)


# Running app
app.mainloop()