import tkinter as tk

days_30 = {"April", "Juni", "September", "November"}
days_31 = {"Januari", "Mars", "Maj", "Juli","August", "Oktober", "December"}
days_28 = {"Februari"}

months = ["Januari","Februari", "Mars","April", "Maj","Juni", "Juli","August","September", "Oktober","November", "December"]

frame = tk.Tk()
frame.geometry('300x200')

def countNewDate():
    int_month = int(inputtxt.get())
    int_dag = int(inputtxt2.get())
    int_step = int(daysStep.get())
    
    current_month = months[int_month-1]
    days_left = int_step
    current_day = int_dag

    while days_left > 0:
        if current_month in days_31:
            days_in_month = 31
        elif current_month in days_30:
            days_in_month = 30
        else:
            days_in_month = 28

        #if int_step - days_left > days_in_month:
        #    days_left = days_left + days_in_month
        #    current_month = months[months.index(current_month)+1]
        #else:
        #    new_month = months.index(current_month) + 1
        #    new_day = int_step - days_left
        #    days_left = days_left + (days_left - int_step)

        if days_left > days_in_month:
            current_month = months[months.index(current_month)+1]
            days_left = days_left - days_in_month
        elif days_left + current_day <= days_in_month:
            current_day = days_left + current_day
            days_left = 0
        else:
            current_month = months[months.index(current_month)+1]
            days_left = days_left + current_day - days_in_month
            current_day = days_left
            days_left = 0
        
        new_day = current_day
        new_month = months.index(current_month) + 1

    output.config(text=str(new_day) + "/" + str(new_month))

lbl = tk.Label(frame, text = "Startmånad")
lbl.pack()

#Create textbox
inputtxt = tk.Entry(frame, width=20)
inputtxt.pack()

lbl2 = tk.Label(frame, text = "Startdag")
lbl2.pack()

inputtxt2 = tk.Entry(frame, width=20)
inputtxt2.pack()

lbl3 = tk.Label(frame, text = "Dagar fram")
lbl3.pack()

daysStep = tk.Entry(frame, width=20)
daysStep.pack()

output = tk.Label(frame, text = "Nytt datum:")

printButton = tk.Button(frame, text="Räkna", command=countNewDate)
printButton.pack()

output.pack()

frame.mainloop()