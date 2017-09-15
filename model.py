BELA, CRNA = 'O', 'X'

class Figure:
    #Stevec za bele in crne figure

    def __init__(self, igra):
        self.bele_figure = len(igra.tocke_B)
        self.crne_figure = len(igra.tocke_C)
        self.cas = 0


    def __repr__(self):
        return 'Na plosci je {} belih in {} crnih figur.'.format(self.bele_figure, self.crne_figure)


class Igra():
    # Zacne igralec z belimi figurami

    def __init__(self, dolzina, sirina):
        self.dolzina = dolzina
        self.sirina = sirina
        self.seznam = []
        self.tocke_B = [[3, 3], [4, 4]]
        self.tocke_C = [[3, 4], [4, 3]]

        self.figure = Figure(self)

    def __str__(self):
        self.seznam = []
        for _ in range(8):
            self.seznam.append(8*[0])
        for x, y in self.tocke_B:
            self.seznam[x][y] = BELA
        for x, y in self.tocke_C:
            self.seznam[x][y] = CRNA
        izpis = ''
        meja = '+'+self.dolzina*'-'+'+\n'
        for i in range(self.sirina):
            vrstica = ''
            for k in self.seznam[i]:
                if k == 0:
                    vrstica += ' '
                else:
                    vrstica += k
            izpis += '|'+vrstica+'|'+'\n'
        print(self.tocke_B, len(self.tocke_B), self.tocke_C, len(self.tocke_C))
        return '{}{}{}Belih: {}\nCrnih: {}\nNa potezi je {} igralec.'.format(meja, izpis, meja, len(self.tocke_B), len(self.tocke_C), self.na_potezi())

    def dodaj(self, x, y):
        if self.poteza_je_uredu(x, y):
            if self.na_potezi() == BELA:
                if self.vodoravno(x, y):
                    self.zamenjaj_vodoravno(x, y)
                if self.navpicno(x, y):
                    self.zamenjaj_navpicno(x, y)
                self.tocke_B.append([x, y])
                self.tocke_B.sort()

            else:
                if self.vodoravno(x, y):
                    self.zamenjaj_vodoravno(x, y)
                if self.navpicno(x, y):
                    self.zamenjaj_navpicno(x, y)
                self.tocke_C.append([x, y])
                self.tocke_C.sort()

            self.figure.cas += 1

        else:
            print('Poteza ni veljavna.')

    def poteza_je_uredu(self, x, y):
        if x not in range(igra.dolzina) and y not in range(igra.sirina):
            return False
        if [x, y] in self.tocke_B and [x, y] in self.tocke_C:
            return False
        return self.navpicno(x, y) or self.vodoravno(x, y)

    def navpicno(self, x, y):
        if self.na_potezi() == BELA:
            if x <= len(self.seznam) - 2:
                if self.seznam[x+1][y] == CRNA:
                    for k in self.seznam[x+1:]:
                        if k[y] == BELA:
                            return True
            if self.seznam[x-1][y] == CRNA:
                for k in self.seznam[:x]:
                    if k[y] == BELA:
                        return True
            else:
                return False
        else:
            if x+1 < len(self.seznam):
                if self.seznam[x+1][y] == BELA:
                    for k in self.seznam[x+1:]:
                        if k[y] == CRNA:
                            return True
            if self.seznam[x-1][y] == BELA:
                for k in self.seznam[:x]:
                    if k[y] == CRNA:
                        return True
            else:
                return False

    def vodoravno(self, x, y):
        if self.na_potezi() == BELA:
            if y <= len(self.seznam) - 2:
                if self.seznam[x][y+1] == CRNA:
                    for k in self.seznam[x][y+1:]:
                        if k == BELA:
                            return True
            if self.seznam[x][y-1] == CRNA:
                for k in self.seznam[x][::-1][len(self.seznam)-y+1:]:
                    if k == BELA:
                        return True
            else:
                return False
        else:
            if y+1 < len(self.seznam):
                if self.seznam[x][y+1] == BELA:
                    for k in self.seznam[x][y+1:]:
                        if k == CRNA:
                            return True
            if self.seznam[x][y-1] == BELA:
                for k in self.seznam[x][::-1][len(self.seznam)-y+1:]:
                    if k == CRNA:
                        return True
            else:
                return False


    def zamenjaj_vodoravno(self, x, y):
        if self.na_potezi() == BELA:
            if y + 1 < len(self.seznam):
                if self.seznam[x][y + 1] == CRNA:
                    for k in range(y+1, len(self.seznam)):
                        if self.seznam[x][k] == BELA or self.seznam[x][k] == ' ':
                            break
                        self.tocke_B.append([x, k])
                        self.tocke_C.remove([x, k])

            if self.seznam[x][y-1] == CRNA:
                for k in range(y-1, -1, -1):
                    if self.seznam[x][k] == BELA or self.seznam[x][k] == ' ':
                        break
                    self.tocke_B.append([x, k])
                    self.tocke_C.remove([x, k])
        else:
            if y+1 < len(self.seznam):
                if self.seznam[x][y + 1] == BELA:
                    for k in range(y+1, len(self.seznam)):
                        if self.seznam[x][k] == CRNA or self.seznam[x][k] == ' ':
                            break
                        self.tocke_C.append([x, k])
                        self.tocke_B.remove([x, k])
            if self.seznam[x][y-1] == BELA:
                for k in range(y-1, -1, -1):
                    if self.seznam[x][k] == CRNA or self.seznam[x][k] == ' ':
                        break
                    self.tocke_C.append([x, k])
                    self.tocke_B.remove([x, k])

    def zamenjaj_navpicno(self, x, y):
        if self.na_potezi() == BELA:
            if x + 1 < len(self.seznam):
                if self.seznam[x+1][y] == CRNA:
                    for k in range(x+1, len(self.seznam)):
                        if self.seznam[k][y] == BELA or self.seznam[k][y] == ' ':
                            break
                        self.tocke_B.append([k, y])
                        self.tocke_C.remove([k, y])

            if self.seznam[x-1][y] == CRNA:
                for k in range(x-1, -1, -1):
                    if self.seznam[k][y] == BELA or self.seznam[k][y] == ' ':
                        break
                    self.tocke_B.append([k, y])
                    self.tocke_C.remove([k, y])

        else:
            if x+1 < len(self.seznam):
                if self.seznam[x+1][y] == BELA:
                    for k in range(x+1, len(self.seznam)):
                        if self.seznam[k][y] == CRNA or self.seznam[k][y] == ' ':
                            break
                        self.tocke_C.append([k, y])
                        self.tocke_B.remove([k, y])
            if self.seznam[x-1][y] == BELA:
                for k in range(x-1, -1, -1):
                    if self.seznam[k][y] == CRNA or self.seznam[k][y] == ' ':
                        break
                    self.tocke_C.append([k, y])
                    self.tocke_B.remove([k, y])



    def na_potezi(self):
        if self.figure.cas % 2 == 0:
            return BELA
        else:
            return CRNA


igra = Igra(8, 8)
