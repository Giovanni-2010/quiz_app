# from tkinter import *
# import customtkinter as ctk
# from CTkMessagebox import CTkMessagebox
# import arabic_reshaper
# from bidi.algorithm import get_display
# from win10toast import ToastNotifier
# from datetime import datetime
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import seaborn as sns
# import winsound as ws
# import subprocess
# import sys
# import os
# import json
# import random
# import warnings

# warnings.simplefilter(action='ignore', category=FutureWarning)

# # ==================== questions dataset ====================
# with open(r"main\questions.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# # ==================== logic ====================

# SETTINGS_FILE = "settings.json"
# SCORES_FILE = "scores.json"

# def load_settings():
#     if os.path.exists(SETTINGS_FILE):
#         with open(SETTINGS_FILE, "r") as f:
#             return json.load(f)
#     return {
#         "font_size": "18",
#         "theme": "dark",
#         "color_theme": "blue",
#         "sound": True,
#         "notification": True,
#         "time_per_question": 20
#     }

# def save_settings():
#     settings = {
#         "font_size": font_size.get(),
#         "theme": theme.get(),
#         "color_theme": color_theme.get(),
#         "sound": sound.get(),
#         "notification": notification.get(),
#         "time_per_question": int(s1.get())
#     }
#     with open(SETTINGS_FILE, "w") as f:
#         json.dump(settings, f, indent=4)

#     set_theme(settings["theme"])
#     main_font.configure(size=int(settings["font_size"]))
#     font_preview.configure(font=main_font)

#     msg = CTkMessagebox(
#         title="Restart Required",
#         message="Settings saved.\nRestart now to apply color theme?",
#         icon="warning",
#         option_1="Restart", option_2="Later"
#     )
#     if msg.get() == "Restart":
#         python = sys.executable
#         filepath = os.path.abspath(__file__)
#         subprocess.Popen([python, filepath])
#         root.destroy()

# def set_theme(value):
#     ctk.set_appearance_mode(value)

# def set_color_theme(value):
#     ctk.set_default_color_theme(value)

# def update_time_label(value):
#     l5.configure(text=f"{int(float(value))} sec")

# def update_font_preview(*_):
#     font_preview.configure(font=("Arial", int(font_size.get())))

# def correct_answer_sound():
#     if sound.get():
#         ws.PlaySound(r"main\correct.wav", ws.SND_FILENAME | ws.SND_ASYNC)

# def wrong_answer_sound():
#     if sound.get():
#         ws.PlaySound(r"main\wrong.wav", ws.SND_FILENAME | ws.SND_ASYNC)

# def arbic(text):
#     reshaped_text = arabic_reshaper.reshape(text)
#     bidi_text = get_display(reshaped_text)
#     return bidi_text

# # User state
# score_value = 0
# asked_questions_ids = set()
# current_question = None
# timer_id = None

# def add_score():
#     global score_value
#     score_value += 10
#     score_label.configure(text=str(score_value))

# def countdown(seconds):
#     global timer_id
#     if seconds >= 0:
#         time_str = f"{seconds:02}"
#         timer.configure(text=time_str)
#         timer_id = quiz.after(1000, countdown, seconds - 1)
#     else:
#         timer.configure(text="00")
#         CTkMessagebox(title="Time's up!", message="You ran out of time!", icon="cancel")
#         reset_quiz()

# def save_score():
#     entry = {
#         "date": datetime.now().strftime("%Y-%m-%d"),
#         "score": score_value
#     }

#     if os.path.exists(SCORES_FILE):
#         with open(SCORES_FILE, "r", encoding="utf-8") as f:
#             scores = json.load(f)
#     else:
#         scores = []

#     scores.append(entry)

#     with open(SCORES_FILE, "w", encoding="utf-8") as f:
#         json.dump(scores, f, ensure_ascii=False, indent=4)


# def load_scores():
#     try:
#         scores = pd.read_json(SCORES_FILE, encoding="utf-8", lines=True)
#         return scores
#     except FileNotFoundError:
#         return [] 

# def game_over(correct_answer):
#     save_score()
#     msg = CTkMessagebox(
#         title="Wrong Answer",
#         message=f"You lost!\nCorrect answer was:\n{arbic(correct_answer)}\n\nPlay again?",
#         icon="cancel",
#         option_1="Yes", option_2="No"
#     )
#     if msg.get() == "Yes":
#         reset_quiz()
#     else:
#         root.destroy()

# def reset_quiz():
#     global asked_questions_ids, score_value, timer_id
#     if timer_id:
#         quiz.after_cancel(timer_id)
#     asked_questions_ids.clear()
#     score_value = 0
#     score_label.configure(text="0")
#     load_new_question()

# def load_new_question():
#     global current_question, timer_id
#     if timer_id:
#         quiz.after_cancel(timer_id)

#     if len(asked_questions_ids) == len(data):
#         CTkMessagebox(title="Quiz Complete", message="You answered all questions correctly!", icon="check")
#         reset_quiz()
#         return

#     while True:
#         current_question = random.choice(data)
#         if current_question["id"] not in asked_questions_ids:
#             break

#     asked_questions_ids.add(current_question["id"])
#     display_question(current_question)
#     countdown(time_per_question.get())

# def display_question(question):
#     add_question(arbic(question["question"]))
#     catagory_label.configure(text=arbic(question["topic"]))
#     user_answer.set(None)

#     for widget in answers_frame.winfo_children():
#         widget.destroy()

#     choices = question["choices"]

#     for ans in choices:
#         btn = ctk.CTkButton(
#             answers_frame,
#             text=arbic(ans),
#             font=main_font,
#             command=lambda a=ans: answer_clicked(a)
#         )
#         btn.pack(anchor="e", pady=5, padx=10)

# def add_question(question):
#     question_box.configure(state="normal")
#     question_box.delete("1.0", "end")
#     question_box.insert("1.0", question)
#     question_box._textbox.tag_configure("right", justify="right")
#     question_box._textbox.tag_add("right", "1.0", "end")
#     question_box.configure(state="disabled")

# def answer_clicked(value):
#     user_answer.set(value)
#     check_answer()

# def check_answer():
#     global timer_id
#     if timer_id:
#         quiz.after_cancel(timer_id)
#     selected = user_answer.get()
#     if selected == current_question["right_answer"]:
#         correct_answer_sound()
#         add_score()
#         load_new_question()
#     else:
#         wrong_answer_sound()
#         game_over(current_question["right_answer"])

# def plot_bar_chart(parent, x, y, xlabel, ylabel, title):
#     fig, ax = plt.subplots(figsize=(7,4), dpi=100)
#     sns.barplot(x=x, y=y, ax=ax, palette='viridis')
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     ax.set_title(title)
#     plt.xticks(rotation=45)

#     for i, val in enumerate(y):
#         ax.text(i, val / 2 if val > 0 else 0.1, f'{int(val)}', ha='center', va='center', color='white', fontsize=10, fontweight='bold')

#     canvas = FigureCanvasTkAgg(fig, master=parent)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill="both", expand=True)

# # ==================== GUI ====================

# root = ctk.CTk()
# root.geometry("800x600+280+50")
# root.title("Quiz app")
# root.resizable(False, False)
# root.iconbitmap(r"main\logo.ico")

# tabview = ctk.CTkTabview(root, width=780, height=580, corner_radius=10, anchor="nw")
# tabview.place(x=10, y=5)

# quiz = tabview.add("Quizs")
# score = tabview.add("Score board")
# settings = tabview.add("Settings")
# tabview.set("Quizs")

# # Settings tab
# settings_data = load_settings()
# ctk.set_appearance_mode(settings_data.get("theme", "dark"))
# ctk.set_default_color_theme(settings_data.get("color_theme", "blue"))

# font_size = ctk.StringVar(value=str(settings_data["font_size"]))
# theme = ctk.StringVar(value=settings_data["theme"])
# color_theme = ctk.StringVar(value=settings_data["color_theme"])
# sound = ctk.BooleanVar(value=settings_data["sound"])
# notification = ctk.BooleanVar(value=settings_data["notification"])
# time_per_question = ctk.IntVar(value=settings_data["time_per_question"])

# font_sizes_list = ["8", "10", "12", "14", "16", "18", "20", "22", "24", "26"]
# themes_list = ["dark", "light", "system"]
# color_themes_list = ["blue", "dark-blue", "green"]

# main_font = ctk.CTkFont(size=int(font_size.get()))

# l1 = ctk.CTkLabel(settings, text="Font Size", font=main_font)
# l1.place(x=30, y=30)
# o1 = ctk.CTkOptionMenu(settings, values=font_sizes_list, variable=font_size, font=main_font)
# o1.place(x=200, y=30)

# font_preview = ctk.CTkLabel(settings, text="Font Preview", font=("Arial", int(font_size.get())))
# font_preview.place(x=400, y=30)
# font_size.trace_add("write", update_font_preview)

# l2 = ctk.CTkLabel(settings, text="Theme", font=main_font)
# l2.place(x=30, y=90)
# o2 = ctk.CTkOptionMenu(settings, values=themes_list, variable=theme, font=main_font)
# o2.place(x=200, y=90)

# l3 = ctk.CTkLabel(settings, text="Color Theme", font=main_font)
# l3.place(x=30, y=150)
# o3 = ctk.CTkOptionMenu(settings, values=color_themes_list, variable=color_theme, font=main_font)
# o3.place(x=200, y=150)

# c1 = ctk.CTkCheckBox(settings, text="Sound Effects", variable=sound, font=main_font)
# c1.place(x=30, y=210)

# c2 = ctk.CTkCheckBox(settings, text="Notifications", variable=notification, font=main_font)
# c2.place(x=30, y=260)

# l4 = ctk.CTkLabel(settings, text="Time per Question", font=main_font)
# l4.place(x=30, y=310)
# s1 = ctk.CTkSlider(settings, from_=5, to=60, number_of_steps=11, width=300, variable=time_per_question, command=update_time_label)
# s1.place(x=280, y=320)
# s1.set(settings_data["time_per_question"])

# l5 = ctk.CTkLabel(settings, text=f"{settings_data['time_per_question']} sec", font=main_font)
# l5.place(x=380, y=340)

# save_btn = ctk.CTkButton(settings, text="Save Settings", font=main_font, width=400, height=60, command=save_settings)
# save_btn.place(x=180, y=420)

# # Quiz tab widgets
# l6 = ctk.CTkLabel(quiz, text=" : التصنيف", font=main_font)
# l6.pack(pady=10, padx=20, anchor="ne")

# catagory_label = ctk.CTkLabel(quiz, text=arbic("تصنيف السؤال"), font=main_font)
# catagory_label.place(x=520, y=10)

# l7 = ctk.CTkLabel(quiz, text=" : النقاط", font=main_font)
# l7.place(x=360, y=10)

# score_label = ctk.CTkLabel(quiz, text="0", font=main_font)
# score_label.place(x=300, y=10)

# l8 = ctk.CTkLabel(quiz, text=" : الوقت", font=main_font)
# l8.place(x=80, y=10)

# timer = ctk.CTkLabel(quiz, text=str(time_per_question.get()), font=main_font)
# timer.place(x=40, y=10)

# question_box = ctk.CTkTextbox(quiz, width=700, height=140, font=main_font, wrap="word", fg_color="light blue", text_color="black", state="disabled")
# question_box.pack(pady=10, padx=20, anchor="ne")

# answers_frame = ctk.CTkScrollableFrame(quiz, width=680, height=200, fg_color="transparent")
# answers_frame.pack(pady=10, padx=20, anchor="ne")

# user_answer = ctk.StringVar()

# # score board
# # ==================== Score tab ====================

# score_tabs = ctk.CTkTabview(score, width=760, height=540)
# score_tabs.pack(padx=10, pady=10)

# month_tab = score_tabs.add("By Month")
# year_tab = score_tabs.add("By Year")
# day_tab = score_tabs.add("By Day")

# # Load score data and prepare for plotting
# df = load_scores()

# if not df.empty:
#     df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
#     df['year'] = df['date'].dt.year
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day_name()

#     # Monthly aggregation
#     df_month = df.groupby('month')['score'].sum().reset_index()
#     month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
#                    'July', 'August', 'September', 'October', 'November', 'December']
#     df_month['month_num'] = df_month['month'].apply(lambda x: month_order.index(x) + 1 if x in month_order else 0)
#     df_month = df_month[df_month['month_num'] > 0]
#     df_month = df_month.sort_values('month_num').reset_index(drop=True)

#     # Yearly aggregation
#     df_year = df.groupby('year')['score'].sum().reset_index().sort_values('year')

#     # Daily aggregation
#     df_day = df.groupby('day')['score'].sum().reset_index()
#     day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     df_day['day_num'] = df_day['day'].apply(lambda x: day_order.index(x) + 1 if x in day_order else 0)
#     df_day = df_day[df_day['day_num'] > 0]
#     df_day = df_day.sort_values('day_num').reset_index(drop=True)
# else:
#     df_month = pd.DataFrame(columns=['month', 'score'])
#     df_year = pd.DataFrame(columns=['year', 'score'])
#     df_day = pd.DataFrame(columns=['day', 'score'])

# plot_bar_chart(month_tab,
#                df_month['month'] if not df_month.empty else [],
#                df_month['score'] if not df_month.empty else [],
#                "Month", "Score", "Total Score by Month")

# plot_bar_chart(year_tab,
#                df_year['year'] if not df_year.empty else [],
#                df_year['score'] if not df_year.empty else [],
#                "Year", "Score", "Total Score by Year")

# plot_bar_chart(day_tab,
#                df_day['day'] if not df_day.empty else [],
#                df_day['score'] if not df_day.empty else [],
#                "Day of Week", "Score", "Total Score by Day")




















# # run
# load_new_question()
# root.mainloop()
