import tkinter as tk
import model

ODMIK = 5
MAX_DOLZINA = 400
ENOTA = 50

class Othello:

    def __init__(self, okno):
        self.igra = model.Igra(8, 8)
        self.pripravi_gv(okno)

    def pripravi_gv(self, okno):
        prikaz = tk.Frame(okno)
        prikaz.grid(row=1, column=0)
        #gumb_print = tk.Button(prikaz, text='Izris', command=lambda:print(self.igra))
        #gumb_print.grid(row=1, column=0)
        #gumb_rezultat = tk.Button(prikaz, text='Rezultat', command=self.rezultat)
        #gumb_rezultat.grid(row=1, column=1)
        #gumb_osvezi = tk.Button(prikaz, text='Osvezi', command=self.osvezi)
        #gumb_osvezi.grid(row=1, column=2)
        prikaz.pack()

        self.plosca = tk.Canvas(width=MAX_DOLZINA, height=MAX_DOLZINA, bg='#006400')
        self.plosca.pack()
        self.plosca.bind('<Button-1>', self.obdelaj_tipko)
        self.osvezi()


    def narisi(self):
        for k in range(1,8):
            self.plosca.create_line(k * ENOTA, 0, k * ENOTA, MAX_DOLZINA)
            self.plosca.create_line(0, k * ENOTA, MAX_DOLZINA, k * ENOTA)
        for x, y in self.igra.tocke_B:
            self.plosca.create_oval(ENOTA * y + ODMIK, ENOTA * x + ODMIK, ENOTA * y + ENOTA - ODMIK, ENOTA * x + ENOTA - ODMIK, fill='white')
        for x, y in self.igra.tocke_C:
            self.plosca.create_oval(ENOTA * y + ODMIK, ENOTA * x + ODMIK, ENOTA * y + ENOTA - ODMIK, ENOTA* x + ENOTA - ODMIK, fill='black')

    def osvezi(self):
        self.plosca.delete('all')
        self.narisi()
        print(self.igra)

    def obdelaj_tipko(self, event):
        stolpec = 2*event.x // 100
        vrstica = 2*event.y // 100
        if self.igra.poteza_je_uredu(vrstica, stolpec):
            self.igra.dodaj(vrstica, stolpec)
            self.osvezi()
        else:
            print('Poteza ni veljavna.')

    def rezultat(self):
        print('B:{} C:{}'.format(len(self.igra.tocke_B), len(self.igra.tocke_C)))

okno = tk.Tk()
moj_program = Othello(okno)
okno.mainloop()
