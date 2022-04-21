from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 200, height = 150)
window.config(padx = 25, pady = 25)

#Entry area
input = Entry(width = 10)
input.grid(row = 0, column = 1)

#Mile Label
Mile_label = Label(text = "Miles")
Mile_label.grid(row = 0, column = 2, ipady= 10, ipadx = 10)

#Is equal to Label
equal_label = Label(text = "Miles")
equal_label.grid(row = 1, column = 0, ipady= 10, ipadx = 10)

# answer label 
answer_label = Label(text = "0")
answer_label.grid(row = 1, column = 1, ipady= 10, ipadx = 10)

#Km Label
km_label = Label(text = "Km")
km_label.grid(row = 1, column = 2, ipady= 10, ipadx = 10)

#Calculate Button
def calculate():
  answer = int(input.get())*1.60934
  answer_label["text"] = answer
calc_button = Button(text = "calculate", command = calculate)
calc_button.grid(row = 2, column = 1)

window.mainloop()
