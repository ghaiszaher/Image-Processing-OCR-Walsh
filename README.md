# Image-Processing-OCR-Walsh

This project contains a demonstration of using Walsh Functions to recognize characters in a clear image (without any noise, rotation or skew).

## Requirements
* Python3
* Jupyter Notebook
* Matplotlib
* Numpy
* Opencv2
* Pillow
* Difflib

## 01 - Generate Walsh Functions
The file "jupyter/01-generate_walsh_functions.ipynb" contains the generation of 64 matrices obtained using Walsh Transformation and saved to a json file. Each is a 64x64 matrix.

## 02 - Build Database
The file "jupyter/02-build_database.ipynb" uses Pillow to generate a database that contains a set of characters, and a "Walsh Vector" for each character (consists of 64 values). Steps for each character:
- Generate blank Image, write the character on it
- Use vertical and horizontal segmentation to isolate the character
- Resize the image to 64x64
- Apply "Inner Product" between the image and each of the walsh matrices, resulting with 64 values that are considered as the character's "Walsh Vector"

The database is saved in a json file.

Note: some combinations of more than 1 character are considered as a whole character here, because they're very close to each other in Times font.


## 03 - Characters Segmentation
The file "jupyter/03-characters_segmentation.ipynb" uses Walsh matrices and the generated database to predict the values of the segmented characters in an image. Steps:
- Vertical Segmentation: gets the start and end pixel of each line.
- Horizontal Segmentaion for each line: gets the start and end pixel of each character in that line.
- Vertical Segmentation for each character: to remove spaces above & below the character
- Resize the character to 64x64
- Calculate the Walsh Vector for the character
- Search for the closest vector in the database using Manhattan Distance, and set the prediction to the character belonging to this vector
