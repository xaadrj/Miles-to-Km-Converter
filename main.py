from tkinter import *

FONT = ('Arial', 10, 'bold')


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609,2)
    result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

input = Entry(width=10 , font=FONT)
input.grid(row=0,column=1)

label_1 = Label(text="Miles", font=FONT)
label_1.grid(row=0,column=2)

label_2 = Label(text="is equal to", font=FONT)
label_2.grid(row=1, column=0)

label_3 = Label(text="Km", font=FONT)
label_3.grid(row=1, column=2)

result = Label(text=0,  font=FONT)
result.grid(row=1, column=1)

button = Button(text="Calculate",width=10, command=miles_to_km, font=FONT)
button.grid(row=2, column=1)

window.mainloop()