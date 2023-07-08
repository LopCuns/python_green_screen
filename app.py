"""Define interface"""

import tkinter as tk
from tkinter import ttk
import funcs

# Main window
ROOT = tk.Tk()
# Screen dimensions
FULLWIDTH = ROOT.winfo_screenwidth()
FULLHEIGHT = ROOT.winfo_screenheight()
# Top side
INPUT = ttk.Frame(ROOT,width=FULLWIDTH,height=FULLHEIGHT/ 2,padding= '10 10 10 10')
# Bottom side
OUTPUT = ttk.Frame(ROOT,width=FULLWIDTH,height=FULLHEIGHT / 2,padding= '10 10 10 10')


# First top side (get the new background image)
INPUT_BG = tk.Frame(INPUT,width=FULLWIDTH / 2,height=FULLHEIGHT / 2,padx=10)
# New background image host
INPUT_BG_IMAGE = funcs.img_holder(INPUT_BG,bg='#333')
# New background image button (file getter)
INPUT_BG_BTN = tk.Button(
    INPUT_BG,text='New background',
    command=lambda: funcs.open_img(INPUT_BG_IMAGE)
)

# Second top side (get the foreground image)

INPUT_FR = tk.Frame(INPUT,width=FULLWIDTH / 2,height=FULLHEIGHT / 2,padx=10)
# Foreground image host
INPUT_FR_IMAGE = funcs.img_holder(INPUT_FR,bg='#333')
# Foreground image button (file getter)
INPUT_FR_BTN = tk.Button(
    INPUT_FR,text='Foreground image',
    command = lambda: funcs.open_img(INPUT_FR_IMAGE)
)

# Bottom side

# Output image host
OUTPUT_IMAGE = funcs.img_holder(OUTPUT,bg='#333',width=funcs.wwidth(OUTPUT) / 2)

# Get the resultant image btn
OUTPUT_GETBTN = tk.Button(
    OUTPUT,text='Get the result image',
      # pylint: disable=no-member
    command=lambda: print(INPUT_BG_IMAGE.image,INPUT_FR_IMAGE.image)
)

# Downlaod image btn
OUTPUT_DOWNLOADBTN = tk.Button(
    OUTPUT,text='Download the result'
)

# Set the top and bottom side of the application in the grid

INPUT.grid(column=0, row=0)
OUTPUT.grid(column=0,row=1)
# Set the top side child elements in the grid
# Set the first top side child elements in the grid
INPUT_BG.grid(column=0,row=0)
INPUT_BG_BTN.grid(column=0,row=0)
INPUT_BG_IMAGE.grid(column=0,row=1)
# Set the second top side child elements in the grid
INPUT_FR.grid(column=1,row=0)
INPUT_FR_BTN.grid(column=0,row=0)
INPUT_FR_IMAGE.grid(column=0,row=1)

# Set the bottom side child elements in the grid
OUTPUT_GETBTN.grid(column=0,row=0)
OUTPUT_IMAGE.grid(column=0,row=1)
OUTPUT_DOWNLOADBTN.grid(column=0,row=2)

ROOT.mainloop()
