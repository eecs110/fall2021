from tkinter import Canvas, Tk
from helpers import make_grid

'''
INSTRUCTIONS:
1. Write a program that prompts the user for a color, which can be any string representation of a color
2. Then, draw a rectangle (of any dimensions) with that color

'''

# initialize window (ignore this code for now)
window = Tk()
canvas = Canvas(window, width=700, height=550, background='white')
canvas.pack()
# end initialize window

canvas.create_oval(
    [(100, 100), (200, 200)],  #  coords: top-left, bottom-right
    fill='pink'
)

make_grid(canvas, 700, 550)

canvas.mainloop()





