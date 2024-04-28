from tkinter import *


def mile_to_km():
    read_input = int(input_miles.get())
    changed_km["text"] = round(read_input*1.6, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=40, pady=10)


input_miles = Entry(width=10)
input_miles.grid(row=0, column=2)


miles_label = Label(font=("Arial", 10))
miles_label["text"] = "Miles"
miles_label.grid(row=0, column=4)


my_label = Label(font=("Arial", 10))
my_label["text"] = "is equal to"
my_label.grid(row=2, column=1)

changed_km = Label(font=("Arial", 10))
changed_km.grid(row=2, column=2)


km = Label(font=("Arial", 10))
km["text"] = "km"
km.grid(row=2, column=4)

button2 = Button(text="Calculate", command=mile_to_km)
button2.grid(column=2, row=3)

window.mainloop()
