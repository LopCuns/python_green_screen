""""Green screen algorithm in python"""

from functools import partial
# pylint: disable=import-error
from PIL import Image
from funcs import set_widget_image, clear_widget


def get_image(frame):
    """Get image associated to frame"""
    return frame.image


def get_image_pixels(image):
    """Get the pixels of a given image"""
    return list(image.getdata())


def swap_green(new_pixels, current_pixel):
    """Def to swap green pixels in image"""
    # Get the pixel index
    idx = current_pixel[0]
    # Get the pixel current colors
    current_colors = current_pixel[1]
    # If the pixel is green, return the new colors in that index
    if current_colors[1] > current_colors[0] + current_colors[2] or sum(current_colors) == 0:
        return new_pixels[idx]
    else:
        # If the pixel is not green, return the current pixel colors
        return current_colors


def green_screen_alogrithm(background, foreground, img_wrapper):
    """Def to apply green screen algorithm"""
    # If an image is missing, exit the function
    if not hasattr(background, 'image') or not hasattr(foreground, 'image'):
        return
    # Get the background and the foreground image
    bgimg = get_image(background)
    frimg = get_image(foreground)
    # Create the new image
    new_image = Image.new(mode='RGB', size=(frimg.width, frimg.height))
    # Get the pixels from the background and the foreground image
    bgimg_pixels = get_image_pixels(bgimg)
    frimg_pixels = get_image_pixels(frimg)
    # Map the foreground image to change the green pixels for the background image ones
    newimg_pixels = list(
        map(partial(swap_green, bgimg_pixels), enumerate(frimg_pixels)))
    # Put the data in the new image and create a PhotoImage
    new_image.putdata(data=newimg_pixels)
    # Remove all widget children
    clear_widget(img_wrapper)
    # Set widget image
    set_widget_image(img_wrapper, new_image)
