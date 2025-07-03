from tkinter import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from win10toast import ToastNotifier
import winsound as ws
import subprocess
import sys
import os
import json 
import random
import time 


# ==================== logic ====================

SETTINGS_FILE = "settings.json"
def load_settings():
    '''
    returns a dictionary of settings , 
    this function loads the settings from the settings.json file if it exists
    but if it doesn't it returns the default settings 
    '''
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {
        "font_size": "16",
        "theme": "dark",
        "color_theme": "blue",
        "sound": True,
        "notification": True,
        "time_per_question": 20
    }

def save_settings():
    """
    save settings, apply theme/font, and restart after user confirms.
    """
    # Save
    settings = {
        "font_size": font_size.get(),
        "theme": theme.get(),
        "color_theme": color_theme.get(),
        "sound": sound.get(),
        "notification": notification.get(),
        "time_per_question": int(s1.get())
    }

    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

    # apply
    set_theme(settings["theme"])
    main_font.configure(size=int(settings["font_size"]))
    font_preview.configure(font=main_font)

    # ask user to confirm restart
    msg = CTkMessagebox(
        title="Restart Required",
        message="Settings saved.\nRestart now to apply color theme?",
        icon="info",
        option_1="Restart", option_2="Later"
    )
    # Restart the app with the same file path
    if msg.get() == "Restart":
        python = sys.executable
        filepath = os.path.abspath(__file__)
        subprocess.Popen([python, filepath])
        root.destroy()


def set_theme(value): 
    ctk.set_appearance_mode(value)

def set_color_theme(value): 
    ctk.set_default_color_theme(value)
def update_time_label(value): 
    l5.configure(text=f"{int(float(value))} sec")

def update_font_preview(*_):
    font_preview.configure(font=("Arial", int(font_size.get())))


# ==================== GUI ====================

# set the main window
root = ctk.CTk()
root.geometry("800x600+280+50")
root.title("Quiz app")
root.iconbitmap(r"main\logo.ico")

# makeing the main tabs
tabview = ctk.CTkTabview(root, width=780, height=580, corner_radius=10, anchor="nw")
tabview.place(x=10 , y=5)

quiz = tabview.add("Quizs") 
score = tabview.add("Score board")  
settings = tabview.add("Settings")  
tabview.set("Quizs") 


# ==================== settings tab ====================

# some vars
data = load_settings()
ctk.set_appearance_mode(data.get("theme", "Dark"))
ctk.set_default_color_theme(data.get("color_theme", "blue"))

font_size = ctk.StringVar(value=str(data["font_size"]))
theme = ctk.StringVar(value=data["theme"])
color_theme = ctk.StringVar(value=data["color_theme"])
sound = ctk.BooleanVar(value=data["sound"])
notification = ctk.BooleanVar(value=data["notification"])
font_sizes_list = ["8", "10", "12", "14", "16","18", "20", "22", "24", "26"]
themes_list = ["Dark", "Light", "System"]
color_themes_list = ["blue","dark-blue", "green"]

main_font = ctk.CTkFont(size=int(font_size.get()))

# font size
l1 = ctk.CTkLabel(settings, text="Font Size", font=main_font)
l1.place(x=30, y=30)
o1 = ctk.CTkOptionMenu(settings, values=font_sizes_list, variable=font_size, font=main_font)
o1.place(x=200, y=30)

# font preview
font_preview = ctk.CTkLabel(settings, text="Font Preview", font=("Arial", int(font_size.get())))
font_preview.place(x=400, y=30)
font_size.trace_add("write", update_font_preview)

# theme
l2 = ctk.CTkLabel(settings, text="Theme", font=main_font)
l2.place(x=30, y=90)
o2 = ctk.CTkOptionMenu(settings, values=themes_list, variable=theme, font=main_font)
o2.place(x=200, y=90)

# color theme
l3 = ctk.CTkLabel(settings, text="Color Theme",font=main_font)
l3.place(x=30, y=150)
o3 = ctk.CTkOptionMenu(settings, values=color_themes_list, variable=color_theme, font=main_font)
o3.place(x=200, y=150)

# sound effects
c1 = ctk.CTkCheckBox(settings, text="Sound Effects", variable=sound, font=main_font)
c1.place(x=30, y=210)

# notifications
c2 = ctk.CTkCheckBox(settings, text="Notifications", variable=notification, font=main_font)
c2.place(x=30, y=260)

# time 
l4 = ctk.CTkLabel(settings, text="Time per Question", font=main_font)
l4.place(x=30, y=310)
s1 = ctk.CTkSlider(settings, from_=5, to=60, number_of_steps=11, width=300)
s1.place(x=280, y=320)
s1.set(data["time_per_question"])

l5 = ctk.CTkLabel(settings, text=f"{data['time_per_question']} sec", font=main_font)
l5.place(x=380, y=340)

s1.configure(command=update_time_label)

# save button
save_btn = ctk.CTkButton(settings, text="Save Settings",font=main_font,width=400, height=60, command=save_settings)
save_btn.place(x=180, y=420)

# ==================== score tab ====================

# ==================== main tab ====================


# run
root.mainloop()