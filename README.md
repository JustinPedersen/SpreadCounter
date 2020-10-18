# SpreadCounter
A faster way to count petri dish spreads! 

# What is this? 
This project originally started as a cool excuse to mess around with OpenCV computer vision in an attempt to aid in
counting spots on a petri dish for my better half's lab work. 

Counting colonies on a dish can, in the best of times be a tedious task when you have a few hundred to get through.
However, counting circular objects in an image can be a trivial task for computers. This application aims to speed up
the process of counting spots as well as provide that data back in an easily manipulated and presentable format such
as excel spreadsheets and marked images.

# How does it work?
![Main UI](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/main_ui_000.png)

Spread counter takes an input set of images and performs some image processing on them, and then to the 
best of its ability will count all the circles it can find in the image. Almost all operations
performed on the images can be customised and fine-tuned by the user on a per-project basis.

First the image is read in, then it is scaled down by a factor so that it is easier to process.
Then the image is converted to greyscale so that it is even easier to work with. From there
if the user so chooses the Dish itself will be located within the image, and a mask will be created
so that all the pixels around the dish are black. This will alienate any false positives from being
counted outside of the dish. 

The image then has its contrast enhanced, so the particles are easier to pick out from the media.
If the user so chooses the image can then be processed further or just used as is. For some images
further processing is necessary. A threshold can be applied to the image so that all the values
are clamped. 

Finally, Image recognition is run on the image, circular spots are then detected and counted.

In this image on the right-hand side is the input image with the counted spots circled and on the 
left-hand side the grey, masked out image that the image recognition was run on. 

![Counted spots](https://github.com/JustinPedersen/SpreadCounter/blob/main/README_images/main_ui_001.png)

# UI Overview

# Project creation

# Input image Do's and Dont's

# Shortcuts and productivity


