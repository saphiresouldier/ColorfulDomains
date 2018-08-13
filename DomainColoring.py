import tkinter as tk
from tkinter import ttk
import math, cmath

#---Constants---------------------------------------

width = 1000
height = 600

supersample = 1

centerreal = 0
centerimag = 0

fovy = 1

sw = supersample * width
sh = supersample * height

aspectratio = width / height
halffovy    = fovy / 2

#---Color Ramps---------------------------------------
#ToDo

#---Complex Functions---------------------------------------
def complex_function(z):
    return cmath.sin(1 / z)

def complex_color(z):
    phase = cmath.phase(z)
    t = phase / math.pi + 1
    if t > 1:
        t = 2 - t
    #return colormap.at(t)
    return '#888888'

#---Drawing---------------------------------------
def center_and_invert(y, height):
    return int(height/2 - y)

def f(x):
    num_cycles = 4
    amplitude = 200
    return amplitude * math.sin(2 * math.pi * (num_cycles / width) * x)

def graph(f, x_range, height):
    for x in x_range:
        y = center_and_invert(f(x), height)
        img.put("#ffffff", (x, y))
		
#fucking slow, find better way! pil, pillow, cython, ...
def fill(width, height):
	for h in range(height):
		for w in range(width):
			img.put("#888888", (w, h))

# Button Click Event Callback Function
def click_me():
	action.configure(text="** I have been Clicked! **")
	aLabel.configure(foreground='red')
	graph(f, range(width), height)

#---GUI---------------------------------------
win = tk.Tk()
win.title("Python GUI")
    
#win.resizable(1024, 1024)      Disable resizing the GUI

canvas = tk.Canvas(win, width=width, height=height, bg="#000000")
canvas.pack()
canvas.grid(column=0,row=0, sticky='WE', columnspan=3)
img = tk.PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")

# Modify adding a Label
aLabel = ttk.Label(win, text="Enter complex formula here:")
aLabel.grid(column=0, row=1)

# Adding a Textbox Entry widget
formula = tk.StringVar()
nameEntered = ttk.Entry(win, width=70, textvariable=formula)
nameEntered.grid(column=1, row=1)

# Adding a Button
action = ttk.Button(win, text="Show me!", command=click_me)
action.grid(column=2, row=1)

#---Gui Main Loop---------------------------------------
win.mainloop()