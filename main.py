from tkinter import *

suma = ""
def dodaj_do_obliczen(liczba):
    global suma
    suma += str(liczba)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, suma)

def oblicz():
    global suma
    try:
        suma = str(eval(suma))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, suma)
    except:
        wyczysc_pole()
        text_result.insert(1.0, "Error")

def wyczysc_pole():
    print('test')
    global suma
    suma = ""
    text_result.delete(1.0, "end")

window = Tk()
window.title('Różowy Kalkulator')
window.geometry("470x600")
bg = PhotoImage(file="Unknown.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)
window.resizable(False,False)

text_result = Text(window, height=2, width=20, font="Courier_New, 30", fg='pink', bg='white', highlightbackground='pink')
text_result.grid(columnspan=5)

przyciski=[]
for row in range(2, 5):
    for column in range(1, 4):
        liczba = (row - 2) * 3 + column
        przycisk = Button(window, text=str(liczba), command=lambda liczba=liczba:dodaj_do_obliczen(str(liczba)), width=5, height=4, font="Courier_New, 25", highlightbackground='pink', fg='white')
        przycisk.grid(row=row, column=column)
        przyciski.append(przycisk)
przycisk0 = Button(window, text="0", command=lambda:dodaj_do_obliczen(0), width=5, height=4, highlightbackground='pink', fg='white', font="Courier_New, 25")
przycisk0.grid(row=5, column=2)
przycisk_dodaj = Button(window, text="+", command=lambda:dodaj_do_obliczen("+"), width=5, height=4, font="Courier_New, 25", highlightbackground='pink', fg='white')
przycisk_dodaj.grid(row=2, column=4)
przycisk_odejmij = Button(window, text="-", command=lambda:dodaj_do_obliczen("-"), width=5, height=4, font="Courier_New, 25", highlightbackground='pink', fg='white')
przycisk_odejmij.grid(row=3, column=4)
przycisk_podziel = Button(window, text=":", command=lambda:dodaj_do_obliczen("/"), width=5, height=4, font="Courier_New, 25", highlightbackground='pink', fg='white')
przycisk_podziel.grid(row=4, column=4)
przycisk_pomnoz = Button(window, text="*", command=lambda:dodaj_do_obliczen("*"), width=5, height=4, font="Courier_New, 25", highlightbackground='pink', fg='white')
przycisk_pomnoz.grid(row=5, column=4)
przyciskusun = Button(window, text="C", command=lambda:wyczysc_pole(), width=5, height=4, highlightbackground='pink', fg='white', font="Courier_New, 25")
przyciskusun.grid(row=5, column=1)
przyciskrownasie = Button(window, text="=", command=lambda:oblicz(), width=5, height=4, highlightbackground='pink', fg='white', font="Courier_New, 25")
przyciskrownasie.grid(row=5, column=3)

window.mainloop()
