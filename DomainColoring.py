import tkinter as tk        # 1 imports
from tkinter import ttk
import math

width = 1000
height = 600

win = tk.Tk()               # 2 Create instance
win.title("Python GUI")     # 3 Add a title       
    
#win.resizable(1024, 1024)         # 4 Disable resizing the GUI

canvas = tk.Canvas(win, width=width, height=height, bg="#000000")
canvas.pack()
canvas.grid(column=0,row=0)
img = tk.PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")

# Modify adding a Label                                      # 1
aLabel = ttk.Label(win, text="A Label")                      # 2
aLabel.grid(column=0, row=1)                                 # 3

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

# Button Click Event Callback Function                       # 4
def clickMe():                                               # 5
	action.configure(text="** I have been Clicked! **")
	aLabel.configure(foreground='red')
	graph(f, range(width), height)
	
# Adding a Button                                            # 6
action = ttk.Button(win, text="Click Me!", command=clickMe)  # 7
action.grid(column=1, row=1)                                 # 8

win.mainloop()              # 5 Start GUI