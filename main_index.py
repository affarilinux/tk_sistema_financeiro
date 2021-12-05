import tkinter as tk


root = tk.Tk() # create a Tk root window

WIDTH = 1000 # width for the Tk root
HEIGHT = 800 # height for the Tk root

# get screen width and height
WS = root.winfo_screenwidth() # width of the screen
HS = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
CALCULO_X = (WS/2) - (WIDTH/2)
CALCULO_Y = (HS/2) - (HEIGHT/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, CALCULO_X, CALCULO_Y))

root.mainloop() # starts the mainloop