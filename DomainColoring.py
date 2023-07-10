import tkinter as tk
from tkinter import ttk
import math, cmath
import colorsys, time

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

color_ramp = []
color_ramp.append("#000000")
color_ramp.append("#888888")

def color_ramp_bw(phase):
    #scaling of phase to 0-1-0
    t = phase / math.pi + 1
    if t > 1:
        t = 2 - t
    
    if t <= 0:
        return '#ffffff'
        #return color_ramp[0] #TODO
    elif t >= 1:
        return '#000000'
        #return color_ramp[color_ramp.len - 1] #TODO
        
    #ToDo: lerp between colors
    
    value = t * 255
    
    return '#{0:02x}{1:02x}{2:02x}'.format(clamp(int(round(value))), clamp(int(round(value))), clamp(int(round(value))))

#alternative return
#return '#{0:02x}{1:02x}{2:02x}'.format(clamp(int(round(val))), clamp(0), clamp(255))

def hsv_to_hex(m, p):
    #scaling of phase to 1 - 0
    t = p / (math.pi * 2) + 0.5
    #if t > 1:
        #t = 2 - t
        
    #clamping ... just to be sure
    m = max(0, min(m, 1))
    t = max(0, min(t, 1))
    
    #conversion to rgb
    (r, g, b) = colorsys.hsv_to_rgb(t, 1, m)
    #conversion to hex
    return '#{0:02x}{1:02x}{2:02x}'.format(clamp(int(round(r * 255))), clamp(int(round(g * 255))), clamp(int(round(b * 255))))

#---Complex Functions---------------------------------------
def complex_function(z):
    if z == 0:
        return 0

    # various functions
    #return cmath.sin(1 / z)
    return cmath.tan(1 / z)
    #return z

def complex_color(z):
    phase = cmath.phase(z)
    amplitude = abs(z)
    
    #return color_ramp_bw(phase) # black white colorramp
    return hsv_to_hex(amplitude, phase) # colorful ramp

#---Drawing---------------------------------------
def center_and_invert(y, height):
    return int(height/2 - y)

def pixel_coordinates(px, py):
    x = (px/(sw - 1) * 2 - 1) * aspectratio * halffovy + centerreal
    y = ((sh - py - 1)/(sh - 1) * 2 - 1) *halffovy + centerimag
    return (x, y)

def clamp(x):
  return max(0, min(x, 255))

def f(x):
    num_cycles = 4
    amplitude = 200
    return amplitude * math.sin(2 * math.pi * (num_cycles / width) * x)

def graph(f, x_range, height):
    for x in x_range:
        y = center_and_invert(f(x), height)
        img.put("#ffffff", (x, y))

#fucking slow, find better way! pil, pillow, cython, ...
def calc(width, height):
    #framing
    (x0, y0) = pixel_coordinates(0, 0)
    (x1, y1) = pixel_coordinates(sw - 1, sh - 1)
    dx = (x1 - x0) / (sw - 1)
    dy = (y1 - y0) / (sh - 1)
    
    y = y0
    for h in range(height):
        x = x0
        for w in range(width):
            #complex calc
            c_z = complex_function(complex(x, y))
            c_c = complex_color(c_z)
            img.put(c_c, (w, h))
            x += dx
            #write values
            #img.put("#{0:02x}{1:02x}{2:02x}".format(clamp(math.floor(h / height * 255)), clamp(math.floor(w / width * 255)), clamp(255)), (w, h))
        y += dy
    
    #write image to file
    datetime = time.strftime("%H%M%d%m%Y")
    img.write('output_' + datetime + '.png', format='png')

# Button Click Event Callback Function
def click_me():
    calc(width, height)
    #graph(f, range(width), height)

#---GUI---------------------------------------
win = tk.Tk()
win.title("Python GUI")
    
#win.resizable(1024, 1024)      Disable resizing the GUI

canvas = tk.Canvas(win, width=width, height=height, bg="#000000")
canvas.pack()
canvas.grid(column=0,row=0, sticky='WE', columnspan=3)
img = tk.PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")

# Adding a Label
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
