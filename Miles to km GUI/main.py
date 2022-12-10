import tkinter

window = tkinter.Tk()
window.title("Miles to kilometer converter")
# window.minsize(width=500, height=500)
window.config(padx=30,pady=30)
entry = tkinter.Entry()
entry.grid(row=0,column=1)

def milesToKm(miles):
    return round(int(miles) * 1.6)



miles = tkinter.Label(text="MILES")
miles.grid(row=0,column=2)

Km = tkinter.Label(text="Km")
Km.grid(row=1,column=2)

equal = tkinter.Label(text="Is equal to")
equal.grid(row=1,column=0)

answer = tkinter.Label(text=0)
answer.grid(row=1,column=1)

def calc():
    val = entry.get()
    ans = milesToKm(val)
    answer.config(text=ans)

button = tkinter.Button(text="Calculate", command=calc)
button.grid(row=2,column=1)




window.mainloop()