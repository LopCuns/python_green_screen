"""Application functionality"""

from tkinter.filedialog import askopenfilename,asksaveasfile
import tkinter as tk
# pylint: disable=import-error
from PIL import Image, ImageTk
def wwidth(widget):
    """Get widget width"""
    return widget.winfo_reqwidth() - 4
def wheight(widget):
    """Get widget height"""
    return widget.winfo_reqheight() - 4
def clear_widget(widget):
    """Destroy all widget children"""
    for item in widget.winfo_children():
        item.destroy()
def set_widget_image(widget,img_file):
    """Set an image to a widget"""
    # Create a PhotoImage from the file
    img_photo = ImageTk.PhotoImage(img_file)
    # Save references to both the image file and the PhotoImage
    widget.image = img_file
    widget.photo = img_photo
    # Create a label to host the PhotoImage
    img_element = tk.Label(widget,image=img_photo)
    img_element.pack()
def open_img(img_wrapper):
    """Def to open image and retrieve it"""
    # Get the filename
    img_file_name = askopenfilename(filetypes=[('Image files', '.png .jpg .webp')])
    # Clear image wrapper
    clear_widget(img_wrapper)
    # Create an image file
    img_file = Image.open(img_file_name).resize((wwidth(img_wrapper),wheight(img_wrapper)))
    # Set the image in the wrapper
    set_widget_image(img_wrapper,img_file)
    print(img_wrapper.image,img_wrapper.photo)


def img_holder(parent,**args):
    """Return image holder"""
    return tk.Frame(
        parent,
        width=args.pop('width') if 'width' in args else wwidth(parent) - 100,
        height=args.pop('height') if 'height' in args else wheight(parent) - 100,
        **args
    )

def download_frame_img(frame,filename):
    """Download image"""
    if not hasattr(frame,'image'):
        return
    frame.image.save(fp=f'downloads/{filename[:-1]}.png',format='PNG')
