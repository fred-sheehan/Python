# Miles to Km converter
import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)

enter_miles = tk.Entry(width=10, font=("Arial", 24))
enter_miles.grid(row=0, column=2)

miles_label = tk.Label(text="Miles", font=("Arial", 24))
miles_label.grid(row=0, column=3)
miles_label.config(padx=20)

is_equal = tk.Label(text="is equal to", font=("Arial", 24))
is_equal.grid(row=2, column=1)
is_equal.config(padx=20)

km_result = tk.Label(text="0", font=("Arial", 24))
km_result.grid(row=2, column=2)
km_result.config(padx=20, pady=10)

km_label = tk.Label(text="Km", font=("Arial", 24))
km_label.grid(row=2, column=3)

def miles_to_km():
    user_input = float(enter_miles.get())
    km = round(user_input * 1.609, 1)
    km_result.config(text=km)

calculate_button = tk.Button(
    text='Calculate', font=("Arial", 20), command=miles_to_km)
calculate_button.grid(row=3, column=2)

window.mainloop()
