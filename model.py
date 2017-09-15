class Figure:
    #Stevec za bele in crne figure

    def __init__(self, bele_figure, crne_figure):
        self.bele_figure = bele_figure
        self.crne_figure = crne_figure
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

        self.figure = Figure(2, 2)

    def __str__(self):
        self.seznam = []
        for _ in range(8):
            self.seznam.append(8*[0])
        for x, y in self.tocke_B:
            self.seznam[x][y] = 'o'
        for x, y in self.tocke_C:
            self.seznam[x][y] = 'x'
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
        return '{}{}{}Belih: {}\nCrnih: {}\nNa potezi je {} igralec.'.format(meja, izpis, meja, self.figure.bele_figure, self.figure.crne_figure, self.na_potezi())

    def dodaj(self, x, y):
        if self.poteza_je_uredu(x, y):
            if self.na_potezi() == 'beli':
                if self.vodoravno(x, y):
                    self.zamenjaj_vodoravno(x, y)
                if self.navpicno(x, y):
                    self.zamenjaj_navpicno(x, y)
                self.tocke_B.append([x, y])
                self.tocke_B.sort()
                self.figure.bele_figure += 1

            else:
                if self.vodoravno(x, y):
                    self.zamenjaj_vodoravno(x, y)
                if self.navpicno(x, y):
                    self.zamenjaj_navpicno(x, y)
                self.tocke_C.append([x, y])
                self.tocke_C.sort()
                self.figure.crne_figure += 1

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
        if self.na_potezi() == 'beli':
            if x <= len(self.seznam) - 2:
                if self.seznam[x+1][y] == 'x':
                    for k in self.seznam[x+1:]:
                        if k[y] == 'o':
                            return True
            if self.seznam[x-1][y] == 'x':
                for k in self.seznam[:x]:
                    if k[y] == 'o':
                        return True
            else:
                return False
        else:
            if x+1 < len(self.seznam):
                if self.seznam[x+1][y] == 'o':
                    for k in self.seznam[x+1:]:
                        if k[y] == 'x':
                            return True
            if self.seznam[x-1][y] == 'o':
                for k in self.seznam[:x]:
                    if k[y] == 'x':
                        return True
            else:
                return False

    def vodoravno(self, x, y):
        if self.na_potezi() == 'beli':
            if y <= len(self.seznam) - 2:
                if self.seznam[x][y+1] == 'x':
                    for k in self.seznam[x][y+1:]:
                        if k == 'o':
                            return True
            if self.seznam[x][y-1] == 'x':
                for k in self.seznam[x][::-1][len(self.seznam)-y+1:]:
                    if k == 'o':
                        return True
            else:
                return False
        else:
            if y+1 < len(self.seznam):
                if self.seznam[x][y+1] == 'o':
                    for k in self.seznam[x][y+1:]:
                        if k == 'x':
                            return True
            if self.seznam[x][y-1] == 'o':
                for k in self.seznam[x][::-1][len(self.seznam)-y+1:]:
                    if k == 'x':
                        return True
            else:
                return False


    def zamenjaj_vodoravno(self, x, y):
        if self.na_potezi() == 'beli':
            if y + 1 < len(self.seznam):
                if self.seznam[x][y + 1] == 'x':
                    a = 0 #število novih belih
                    for k in range(y+1, len(self.seznam)):
                        if self.seznam[x][k] == 'o' or self.seznam[x][k] == ' ':
                            self.figure.bele_figure += a
                            self.figure.crne_figure -= a
                            break
                        a += 1
                        self.tocke_B.append([x, k])
                        self.tocke_C.remove([x, k])

            if self.seznam[x][y-1] == 'x':
                a = 0
                for k in range(y-1, -1, -1):
                    if self.seznam[x][k] == 'o' or self.seznam[x][k] == ' ':
                        self.figure.bele_figure += a
                        self.figure.crne_figure -= a
                        break
                    a += 1
                    self.tocke_B.append([x, k])
                    self.tocke_C.remove([x, k])
        else:
            if y+1 < len(self.seznam):
                if self.seznam[x][y + 1] == 'o':
                    a = 0 #število novih crnih
                    for k in range(y+1, len(self.seznam)):
                        if self.seznam[x][k] == 'x' or self.seznam[x][k] == ' ':
                            self.figure.crne_figure += a
                            self.figure.bele_figure -= a
                            break
                        a += 1
                        self.tocke_C.append([x, k])
                        self.tocke_B.remove([x, k])
            if self.seznam[x][y-1] == 'o':
                a = 0
                for k in range(y-1, -1, -1):
                    if self.seznam[x][k] == 'x' or self.seznam[x][k] == ' ':
                        self.figure.crne_figure += a
                        self.figure.bele_figure -= a
                        break
                    a += 1
                    self.tocke_C.append([x, k])
                    self.tocke_B.remove([x, k])

    def zamenjaj_navpicno(self, x, y):
        if self.na_potezi() == 'beli':
            if x + 1 < len(self.seznam):
                if self.seznam[x+1][y] == 'x':
                    a = 0 #število novih belih
                    for k in range(x+1, len(self.seznam)):
                        if self.seznam[k][y] == 'o' or self.seznam[k][y] == ' ':
                            self.figure.bele_figure += a
                            self.figure.crne_figure -= a
                            break
                        a += 1
                        self.tocke_B.append([k, y])
                        self.tocke_C.remove([k, y])

            if self.seznam[x-1][y] == 'x':
                a = 0
                for k in range(x-1, -1, -1):
                    if self.seznam[k][y] == 'o' or self.seznam[k][y] == ' ':
                        self.figure.bele_figure += a
                        self.figure.crne_figure -= a
                        break
                    a += 1
                    self.tocke_B.append([k, y])
                    self.tocke_C.remove([k, y])

        else:
            if x+1 < len(self.seznam):
                if self.seznam[x+1][y] == 'o':
                    a = 0 #število novih crnih
                    for k in range(x+1, len(self.seznam)):
                        if self.seznam[k][y] == 'x' or self.seznam[k][y] == ' ':
                            self.figure.crne_figure += a
                            self.figure.bele_figure -= a
                            break
                        a += 1
                        self.tocke_C.append([k, y])
                        self.tocke_B.remove([k, y])
            if self.seznam[x-1][y] == 'o':
                a = 0
                for k in range(x-1, -1, -1):
                    if self.seznam[k][y] == 'x' or self.seznam[k][y] == ' ':
                        self.figure.crne_figure += a
                        self.figure.bele_figure -= a
                        break
                    a += 1
                    self.tocke_C.append([k, y])
                    self.tocke_B.remove([k, y])



    def na_potezi(self):
        if self.figure.cas % 2 == 0:
            return 'beli'
        else:
            return 'crni'


igra = Igra(8, 8)
