import sys
import tkinter as tk

def button_pressed():
    print("test")

root = tk.Tk()
root.title("Dark Green Window")

# Set window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Set window icon (replace 'icon_image.ico' with your icon file path)
if getattr(sys, 'frozen', False):
    root.iconbitmap(sys._MEIPASS + "\\Assets\icon_image.ico")
else:
    root.iconbitmap("Assets\icon_image.ico")

# Create a Canvas with a dark green background
canvas = tk.Canvas(root, bg='#006400')
canvas.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame for the button
frame = tk.Frame(canvas, bg='black')
frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Variable for the 8-digit string
number_var = tk.StringVar(value='12345678')

# Configure style for the button
button_style = {'background': '#333333',  # Dark background color
                'foreground': 'white',     # Text color
                'relief': 'raised',        # Raised border style
                'borderwidth': 3,          # Border width
                'highlightbackground': 'black',  # Highlight color when focused
                'highlightthickness': 2,   # Thickness of the highlight
                'font': ('Arial', 12),     # Font
                'bd': 0,                    # Border width, same as borderwidth, for consistency
                'highlightcolor': '#333333',   # Highlight color
                'activebackground': '#555555',  # Background color when clicked
                'activeforeground': 'white',    # Text color when clicked
                'cursor': 'hand2',               # Cursor style
                }

# Create a button
button = tk.Button(frame, text="Button", command=button_pressed, **button_style)
button.grid(row=0, column=0, sticky="w")

# Create text to display the 8-digit string
text_label = tk.Label(canvas, textvariable=number_var, fg='white', bg='black')
text_label.grid(row=100, column=0, sticky="w", padx=10, pady=10)

root.mainloop()
