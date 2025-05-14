import sys, PIL
from PIL import Image


input_file = sys.argv[1] #decided to make these 2 variables since those are being used multiple times
output_file = sys.argv[2] #will be easier to understand looking at these variables

def checking_input():
    if len(sys.argv) == 3:
        if (input_file.endswith(".jpg") and output_file.endswith(".jpg")) or (input_file.endswith(".png") and output_file.endswith(".png")) :
            converting_files(input_file)
        elif not input_file.endswith((".jpg", ".png")) or not output_file.endswith((".jpg", ".png")):
            print("Invalid input")
        else:
            print("Input and output have different extensions")
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

def converting_files(input_file):
    input_image = Image.open(input_file)
    shirt = Image.open("shirt.png")
    converted_image = PIL.ImageOps.fit(input_image, [600, 600])
    pasting_shirt(converted_image, shirt)

def pasting_shirt(converted_image, shirt):
    converted_image.paste(shirt, (0, 0), shirt) # Paste directly onto converted_image
    saving_image(converted_image)

def saving_image(image_to_save): # Rename the argument for clarity
    image_to_save.save("completed.png")

def main():
   checking_input()

main()