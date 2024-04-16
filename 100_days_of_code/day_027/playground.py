# TKinter GUI program
import tkinter as tk

window = tk.Tk()
window.title("GUI is best")
window.minsize(width=600, height=400)

# Create a label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

# change the text of the label directly or using the config method, last change will be the one displayed
# my_label['text'] = 'New Text'
my_label.config(text='New Label Text')


def button_clicked():
    user_input = entry.get()
    my_label.config(text=user_input)


# Create a button displayed in the window
my_button = tk.Button(text='Click Me', command=button_clicked)
my_button.pack()

#Entries
entry = tk.Entry(width=30)
#Add some text to begin with
entry.insert(0, string="Some text to begin with.")
#Gets text in entry
entry.pack()

#Text
text = tk.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(0, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", 0))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
