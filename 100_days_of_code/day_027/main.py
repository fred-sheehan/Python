# TKinter GUI program
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("GUI is best")
window.minsize(width=600, height=400)

# Create a label
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()

btn_standard = tk.Button(window, text='Standard Button')
btn_standard.pack()



# Setting a theme for TTK widgets
# ttk.Style().theme_use('alt')
# btn_ttk = ttk.Button(window, text='TTK Button')
# btn_ttk.pack()

window.mainloop()
