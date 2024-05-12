from customtkinter import *
from PIL import Image
import json

window = CTk()
window.geometry("1290x800")

with open("Assets/settings.json") as json_file:
    json_data = json.load(json_file)
    settings = [json_data["ColorMode"]]
    print(settings[0])

global window_resize, colormode, danger_settings_toggle

window_resize = False
colormode = settings[0]
danger_settings_toggle = False
button_colors_light1 = "f8f9fa"
button_colors_light2 = "4D194D"
button_colors_dark1 = "212529"
button_colors_dark2 = "e9ecef"

def settings_resize_check_func():
    global window_resize
    window_resize = not(window_resize)
    print(window_resize)
    window.resizable(width = window_resize, height = window_resize)
    if not(window_resize):
        window.geometry("1290x800")


def settings_colormode_check_func():
    global colormode
    colormode = not(colormode)
    if colormode:
        set_appearance_mode("light")
        btn.configure(fg_color = "#ced4da", hover_color = f"#{button_colors_dark2}", text_color = f"#{button_colors_dark1}")
    else:
        set_appearance_mode("dark")
        btn.configure(fg_color = "#3E1F47", hover_color = f"#{button_colors_light2}", text_color = f"#{button_colors_light1}")

    with open("Assets/settings.json") as json_file:
        settingsupdate = json.load(json_file)

    settingsupdate['ColorMode'] = colormode
    
    with open("Assets/settings.json", "w") as json_file:
        json.dump(settingsupdate, json_file)

def dangerous_settings_toggle_func():
    global danger_settings_toggle
    danger_settings_toggle = not(danger_settings_toggle)
    if danger_settings_toggle:
        settings_colorMode_checkbox.configure(state = "normal")
        settings_resizableWindow_checkbox.configure(state = "normal")
        dangerous_settings_toggle_label.configure(text = "Dangerous settings enabled, stay safe!", text_color = "#FF3131")
    else:
        settings_colorMode_checkbox.configure(state = "disabled")
        settings_resizableWindow_checkbox.configure(state = "disabled")
        dangerous_settings_toggle_label.configure(text = "Dangerous settings disabled, you're good!", text_color = "#38b000")


home_button_light_img = Image.open("Assets/home_button_light.png")
home_button_dark_img = Image.open("Assets/home_button_dark.png")

taskbar_frame = CTkFrame(window, width = 1000, height = 58)
taskbar_frame.place(relx = 0.5, rely = 0.05, anchor="center")

settings_frame = CTkFrame(window, width = 800, height = 600)
settings_frame.place(relx = 0.5, rely = 0.55, anchor="center")

# dangerous_settings_frame = CTkFrame(settings_frame, bg_color="#dc2f02", width = 150, height = 150)
# dangerous_settings_frame.place()

# regular settings

ButtonColorStateEntry = CTkEntry(settings_frame, placeholder_text = "Button Colors")
ButtonColorStateButton = CTkButton(settings_frame, text = "Change")




# dangerous settings label

dangerous_settings_label = CTkLabel(settings_frame, text = 
                                    "WARNING! Dangerous settings ahead!",
                                    text_color = "#dc2f02",
                                    font = ("Ariel", 24))
dangerous_settings_label.place(relx = 0.01, rely = 0.67, anchor="sw")

dangerous_settings_toggle = CTkSwitch(settings_frame, text = "Enable dangerous settings?", command = dangerous_settings_toggle_func)
dangerous_settings_toggle.place(relx = 0.01, rely = 0.72, anchor="sw")

dangerous_settings_toggle_label = CTkLabel(settings_frame, text = "Dangerous settings disabled, you're good!", text_color = "#38b000")
dangerous_settings_toggle_label.place(relx = 0.01, rely = 0.77, anchor="sw")

# window resize

settings_resizableWindow_checkbox = CTkSwitch(settings_frame, text = "Enable window resize", command = settings_resize_check_func, state = "disabled")
settings_resizableWindow_checkbox.place(relx = 0.01, rely = 0.92, anchor="sw")
settings_resizableWindow_checkbox_label = CTkLabel(settings_frame, text = "(Restarts page + it will not scale correctly! Use with caution!)", text_color = "#FF3131")
settings_resizableWindow_checkbox_label.place(relx = 0.01, rely = 0.97, anchor="sw")

# color mode switch

settings_colorMode_checkbox = CTkSwitch(settings_frame, text = "Light/Dark Mode Switch", command = settings_colormode_check_func, state = "enabled")
settings_colorMode_checkbox.place(relx = 0.01, rely = 0.82, anchor="sw")
settings_colorMode_checkbox_label = CTkLabel(settings_frame, text = "(Restarts page + colors aren't fully optimized)", text_color = "#FF3131")
settings_colorMode_checkbox_label.place(relx = 0.01, rely = 0.87, anchor="sw")


btn = CTkButton(window, text = "Home", corner_radius = 8, 
                fg_color = "#3E1F47", hover_color="#4D194D", 
                font=("Ariel bold",24), width=100, height= 50,
                image = CTkImage(dark_image = home_button_light_img, light_image = home_button_dark_img))
btn.place(relx = 0.01, rely = 0.1, anchor="nw")

settings_label = CTkLabel(window, text = "Settings", font = ("Ariel", 55))
settings_label.place(relx = 0.2, rely = 0.0858, anchor = "nw")

if settings[0]:
    settings_colorMode_checkbox.toggle()

    settings_colormode_check_func()

settings_colorMode_checkbox.configure(state = "disabled")
window.resizable(width = window_resize, height = window_resize)
window.mainloop()