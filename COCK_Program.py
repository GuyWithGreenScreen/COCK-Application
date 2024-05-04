import sys
import tkinter as tk
from PIL import Image, ImageTk

def button_pressed():
    print("test")

root = tk.Tk()
root.title("Dark Green Window")

# Determine the path to the image file
if getattr(sys, 'frozen', False):
    # If the script is frozen (compiled into a single executable)
    image_path = sys._MEIPASS + "\\background_image.jpg"  # Use the image file bundled with the executable
else:
    # If the script is run as a Python script
    image_path = "background_image.jpg"  # Use the image file in the project directory

# Load the background image
background_image = Image.open(image_path)
background_photo = ImageTk.PhotoImage(background_image)

# Set window size
root.geometry(f"{background_image.width}x{background_image.height}")

# Create a Canvas
canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack()

# Place the background image on the canvas
canvas.create_image(0, 0, anchor='nw', image=background_photo)

# Create a frame for the button and text
frame = tk.Frame(root, bg='black')
frame.place(relx=0.02, rely=0.85, relwidth=0.3, relheight=0.1)

# Variable for the 8-digit string
number_var = tk.StringVar(value='12345678')

# Create a button
button = tk.Button(frame, text="Button", command=button_pressed)
button.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

# Create text to display the 8-digit string
text_label = tk.Label(root, textvariable=number_var, fg='white', bg='black')
text_label.place(relx=0.02, rely=0.96)

root.mainloop()
