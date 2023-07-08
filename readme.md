# Green screen algorithm in python
Green screen image background replacer built using [Python](https://docs.python.org) and it's library [Tkinter](https://tkdocs.com/shipman/).

# Functinalities
The user provides two images, a new background image and an image with green background.As the result, the user receives a new image that has the background of the first one and the foreground of the second one.
This application has a gui buil with tkinter while the logic of the algorithm is performed with Python programming language.

# Steps in the algorithm
  1. Get the background and the foreground image
  2. Select the pixels in the foreground image that have more green value than red and blue added
  3. Replace those pixels with the pixels in the background image in the same position
  4. Show the result to the user
  5. Enable the download button to download the image