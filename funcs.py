"""Application functionality"""

from tkinter.filedialog import askopenfilename
import tkinter as tk
# pylint: disable=import-error
from PIL import Image, ImageTk
def wwidth(widget):
    """Get widget width"""
    return widget.winfo_reqwidth()
def wheight(widget):
    """Get widget height"""
    return widget.winfo_reqheight()
def open_img(img_wrapper):
    """Def to open image and retrieve it"""
    img_file_name = askopenfilename(filetypes=[('Image files', '.png .jpg .webp')])
    img_file = ImageTk.PhotoImage(
        Image.open(img_file_name).resize((wwidth(img_wrapper),wheight(img_wrapper)))
    )
    img_wrapper.image= img_file
    img_element = tk.Label(img_wrapper,image=img_file)
    img_element.pack()

def img_holder(parent,**args):
    """Return image holder"""
    return tk.Frame(
        parent,
        width=args.pop('width') if 'width' in args else wwidth(parent) - 100,
        height=args.pop('height') if 'height' in args else wheight(parent) - 100,
        **args
    )
