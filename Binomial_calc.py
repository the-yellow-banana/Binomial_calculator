import math
import tkinter as tk

def BINOMIAL(E1, E2, E3):
    ##do the binomial formula!!!
    CHOOSE = (math.factorial(int(E2))) / ((math.factorial(int(E2) - int(E3))) * (math.factorial(int(E3))))
    FINAL_ANSWER = CHOOSE * ((float(E1)**int(E3)) * ((1 - float(E1))**(int(E2) - int(E3))))

    Answer['text'] = 'The probability for this event is' + str(FINAL_ANSWER)

WIDTH = 800
HEIGHT = 300

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#b4d3d4')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

L1 = tk.Label(frame, text='Enter the Probability of Success:')
L1.grid(row = 0, column = 0)
E1 = tk.Entry(frame, bg='#84d2df')
E1.grid(row=0, column = 1)

L2 = tk.Label(frame, text='Enter Number of Trials:')
L2.grid(row = 1, column = 0)
E2 = tk.Entry(frame, bg='#84d2df')
E2.grid(row = 1, column = 1)

L3 = tk.Label(frame, text='Number of Successful Trials:')
L3.grid(row = 2, column = 0)
E3 = tk.Entry(frame, bg= '#84d2df')
E3.grid(row = 2, column = 1)


B1 = tk.Button(frame, text="CALCULATE",activeforeground = 'blue', font = 20, command = lambda: BINOMIAL(E1.get(), E2.get(), E3.get()))
B1.grid(row =4, column = 1, ipady = 10, rowspan = 2)

Answer = tk.Label(frame)
Answer.grid(row = 7, column = 1, pady = 4)


root.mainloop()