# image-hex-mapper-vhdl
**imgProcesser.py** --- Python script for mapping pixels of given images to their hex RGBA values and formatting output for usage in VHDL files

**palette_maker.py** --- Python script for making color palette from given color data, in this case that's output from imgProcesser.py

## Usage:
**imgProcesser.py** --- Put script in a folder with all the images you want processed and start the script.

Output file is opened in append mode so you have to delete the output.txt file before using the script again.

**palette_maker.py** --- Put script in a folder with "output.txt" file and start the script.

Output file is opened in append mode so you have to delete the palette.txt file before using the script again.

### Dependencies:
Pillow - Python Imaging Library
