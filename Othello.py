import tkinter as tk
import model

class Othello:

    def __init__(self, okno):
        self.igra = model.Igra(8, 8)
        self.pripravi_gv(okno)

    def pripravi_gv(self, okno):
        prikaz = tk.Frame(okno)
        prikaz.grid(row=1, column=0)
        gumb_print = tk.Button(prikaz, text='Izris', command=lambda:print(self.igra))
        gumb_print.grid(row=1, column=0)
        #gumb_rezultat = tk.Button(prikaz, text='Rezultat', command=self.rezultat)
        #gumb_rezultat.grid(row=1, column=1)
        #gumb_osvezi = tk.Button(prikaz, text='Osvezi', command=self.osvezi)
        #gumb_osvezi.grid(row=1, column=2)
        prikaz.pack()

        self.plosca = tk.Canvas(width=400, height=400, bg='Green')
        self.plosca.pack()
        self.plosca.bind('<Button-1>', self.obdelaj_tipko)
        self.osvezi()


    def narisi(self):
        for k in range(1,8):
            self.plosca.create_line(k*50, 0, k*50, 400)
            self.plosca.create_line(0, k*50, 400, k*50)
        for x, y in self.igra.tocke_B:
            self.plosca.create_oval(50 * y +5, 50 * x +5, 50 * y + 50 -5, 50 * x + 50 -5, fill='white')
        for x, y in self.igra.tocke_C:
            self.plosca.create_oval(50 * y +5, 50 * x +5, 50 * y + 50 -5 , 50* x + 50-5, fill='black')

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
        print('B:{} C:{}'.format(self.igra.figure.bele_figure, self.igra.figure.crne_figure))

okno = tk.Tk()
moj_program = Othello(okno)
okno.mainloop()