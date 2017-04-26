# from tkinter import *

import tkinter as tk


class CelsiusGUI:
    def __init__(self):
        # Create Tk object for the window
        self.window = tk.Tk()

        # Create three frames to be packed on top of each other in the window
        self.input = tk.Frame(self.window)
        self.output = tk.Frame(self.window)
        self.buttons = tk.Frame(self.window)

        # Add controls to top frame
        self.lbl_input = tk.Label(self.input, text="Enter Celsius temperature: ")
        self.txt_celsius = tk.Entry(self.input, width=10)

        self.lbl_input.pack(side='left')
        self.txt_celsius.pack(side='left')

        # Add controls to middle
        self.fah = tk.StringVar()
        self.lbl_results = tk.Label(self.output, textvariable=self.fah)

        self.lbl_results.pack()

        # Add controls to bottom frame
        self.btn_calc = tk.Button(self.buttons, text='Calc F Temp', command=self.c_to_f)
        self.btn_calc.pack()

        # Pack the three frames into the window
        self.input.pack()
        self.output.pack()
        self.buttons.pack()

        # Display window
        tk.mainloop()

    def c_to_f(self):
        # Get Celsius value
        self.celsius = float(self.txt_celsius.get())

        #       Perform Calculation
        self.fahrenheit = (9 / 5) * self.celsius + 32

        #       Set the fah variable
        self.fah.set("F Temp:" + str(self.fahrenheit))


# creates the window object
celsius = CelsiusGUI()
