from tkinter import *
from tkinter import messagebox


bmi = Tk()
bmi.title(" BMI CALCULATOR")
bmi.geometry('500x300')
bmi.config(bg='#f8d3e2')

name_label = Label(bmi, text="Enter name of a Person",
                   font=("Arial", 9), fg='#0c1236', bg='#f8d3e2').grid(row=0, column=0)

nameentry = Entry(bmi, width=30,
                  border=0, borderwidth=0, fg="Black")
nameentry.grid(row=0, column=1)

weight_lb = Label(bmi, text="Enter Weight in Kg",
                  font=("Arial", 9), fg='#0c1236', bg='#f8d3e2').grid(row=1, column=0)

weightentry = Entry(bmi, width=30, border=0, borderwidth=0)
weightentry.grid(row=1, column=1)

height_lb = Label(bmi, text="Enter Height in cm",
                  font=("Arial", 9), fg='#0c1236', bg='#f8d3e2').grid(row=2, column=0)

heightentry = Entry(bmi, width=30, border=0, borderwidth=0)
heightentry.grid(row=2, column=1)

age_lb = Label(bmi, text=" Enter Age of a Person",
               font=("Arial", 9), fg='#0c1236', bg='#f8d3e2').grid(row=3, column=0)

age = Entry(bmi, width=30, border=0, borderwidth=0)
age.grid(row=3, column=1)

gender_lb = Label(bmi, text=" Enter gender of a person",
                  font=("Arial", 9), fg='#0c1236', bg='#f8d3e2').grid(row=4, column=0)

myvar = IntVar()

rb1 = Radiobutton(bmi, text="Male", variable=myvar,
                  font=("Arial", 9), fg='#0c1236', bg='#f8d3e2', value=1, anchor='w')
rb1.grid(row=4, column=1, padx=3, pady=15)

rb2 = Radiobutton(bmi, text="Female", variable=myvar,
                  font=("Arial", 9), fg='#0c1236', bg='#f8d3e2', value=2, anchor='w')
rb2.grid(row=4, column=2, columnspan=2, padx=3, pady=15)


def calculate_bmi():
    weight = float(weightentry.get())
    height = float(heightentry.get())/100
    name = str(nameentry.get())
    x = float(weight)/float(height*height)
    x = round(x, 1)
    bmi_index(x, name)


def reset_entry():
    age.delete(0, 'end')
    nameentry.delete(0, 'end')
    weightentry.delete(0, 'end')
    heightentry.delete(0, 'end')


def bmi_index(x, name):
    if x < 18.5:
        messagebox.showinfo(
            'bmi', f' {name} has BMI = {x} that is Underweight ')
    if x >= 18.5 and x < 25:
        messagebox.showinfo('bmi', f' {name} has  BMI = {x} that is Normal ')
    if x >= 25 and x < 30:
        messagebox.showinfo(
            'bmi', f' {name} has  BMI = {x} that is Overweight ')
    if x >= 30:
        messagebox.showinfo('bmi', f'{name} has BMI = {x} that  is Obeseity ')


# buttons
buttn_calculate = Button(bmi, text="Calculate BMI",
                         padx=20, pady=10, command=calculate_bmi, bg='#f8d3e2')
buttn_calculate.grid(row=5, column=1)
reset_button = Button(bmi, text="RESET", padx=20, pady=10,
                      command=reset_entry, bg='#f8d3e2')
reset_button.grid(row=5, column=2)

bmi.mainloop()
