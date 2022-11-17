
import tkinter as tk #Imports the fucntion from the tkinter GUI
from tkinter import messagebox
from tkinter import * 
App = Tk()
App.geometry('400x400') #Creating the GUI 
date = IntVar()
App.title('Age Calculator App',)
NameLabels = Label(App, text = 'Welcome to the Age Calculator!',bg='Aqua').place(x=105, y=10)
App.configure(bg='Orange')
NameLabel = Label(App,text = 'Enter your Date of Birth:',bg='Aqua').place(x=70,y=50)

#String entered Label
Day = tk.StringVar()
Month = tk.StringVar()
Year = tk.StringVar()

#Creating the labels for the widgets for Month, Year, and month.
Day = tk.Label(text = 'Day',bg='Aqua')
Day.place(x=20,y=75)
Month = tk.Label(text = 'Month',bg='Aqua')
Month.place(x=20,y=105)
Year = tk.Label(text='Year',bg='Aqua')
Year.place(x=20,y=135,)

#Entry for the user to input the information
Day1 = Entry(App, textvariable=Day).place(x=70,y=75)
Day2= Entry(App, textvariable=Month).place(x=70,y=105)
Day3=Entry(App, textvariable=Year).place(x=70,y=135)

def calculate():
    pass 
cal_button=Button(App,
    text="Calculate",
    width=17,
    height=2,
    bg="Aqua",
    fg="Black",
    command=calculate
 ).place(x=70,y=165)















App.mainloop()

