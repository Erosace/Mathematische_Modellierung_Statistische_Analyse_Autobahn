from AutoObjekt import *
import random


def neueSpur(Fahrbahnlänge, Geschwindigkeitsbegrenzung):
    a = [[0, 0] for x in range(Fahrbahnlänge)]
    a = GeschwindigkeitsbegrenzungEinführen(a, Geschwindigkeitsbegrenzung)
    return (a)

def neueFahrzeuge(Fahrbahn, AnzahlFahrzeuge, vmax):
    b = int(len(Fahrbahn) / AnzahlFahrzeuge)
    for i in range(AnzahlFahrzeuge):
        Fahrbahn[b * i][0] = Auto(i, b*i, 3, vmax)
    return (Fahrbahn)

def AbstandzumVordermann(Spur, Autoindizes):
    a = len(Spur)
    counter = 0
    for i in range(1, a + 1):
        if (Autoindizes + i) % a == 0:
            return(7)
        if Spur[(Autoindizes + i) % a][0] != 0:
            counter += 1
            return (counter)
        else:
            counter += 1

def Fahrbahnkopieren(Autobahn):
    return [Autobahn[x] for x in range(len(Autobahn))]

def nächsteZeiteinheit(Autobahn, p, vmax, Geschwindigkeitsbegrenzung):
    neueS = neueSpur(len(Autobahn), Geschwindigkeitsbegrenzung)
    for i in range(len(Autobahn)):
        if Autobahn[i][0] != 0:
            b = AbstandzumVordermann(Autobahn, i) - 1
            c = random.uniform(0, 1)
            d = p[int(Autobahn[i][0].getV())]
            if Autobahn[i][0].getV() != 0 and c <= d:  # Trödeln
                Autobahn[i][0].changeV(Autobahn[i][0].getV() - 1)
            elif c > d and b > Autobahn[i][0].getV() and Autobahn[i][0].getV() < vmax and Autobahn[i][0].getV() < Autobahn[i][
                1]:  # Schnellestmögliches Fahren
                Autobahn[i][0].changeV(Autobahn[i][0].getV() + 1)
            if b < Autobahn[i][0].getV():  # Sicherheitsabstand
                Autobahn[i][0].changeV(b)
            if (i + Autobahn[i][0].getV()) >= len(Autobahn):#sorgt dafür, dass Autos die Fahrbahn verlassen
                continue
            else:
                neueS[i + Autobahn[i][0].getV()] = Autobahn[i]
    for i in range(len(Autobahn)):
        if neueS[i][0] != 0:
            neueS[i][0].changeIndex(i)
            neueS[i][0].changeFahrtdauer()
    a = random.uniform(0, 1)  # Wahrscheinlichkeit, dass ein neues Auto nachkommt
    if a >= 0.475:
        b = AbstandzumVordermann(Autobahn, 0) - 1
        if b != 0:
            neueS[0][0] = Auto(50, 0, max(min(b, neueS[0][1], vmax), 0), vmax) #50 willkürlich gewählt, normalerweise müsste hier das i-te Objekt Auto sein
    return (neueS)


def AutosZählen(Autobahn, ersteZelle, letzteZelle):
    a = 0
    for i in range(ersteZelle, letzteZelle):
        if Autobahn[i][0] == 0:
            continue
        else:
            a += 1
    return (a)

def Höchstgeschwindigkeit(Dichte, GLS):
    # bestimmt die Höchstgeschwindigkeit eines Abschnittes anhand der Verkehrsdichte
    if Dichte == 0:
        return 100
    else:
        return (int((1 / Dichte) - GLS))

def neueGeschwindigkeitsbegrenzung(Autobahn, GLS):
    #berechnet die Dichte Autos/Zelle
    a = AutosZählen(Autobahn, 0, int(len(Autobahn) / 7)) / (len(Autobahn) / 7)
    b = AutosZählen(Autobahn, int(len(Autobahn) / 7), int(2 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    c = AutosZählen(Autobahn, int(2 * len(Autobahn) / 7), int(3 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    d = AutosZählen(Autobahn, int(3 * len(Autobahn) / 7), int(4 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    e = AutosZählen(Autobahn, int(4 * len(Autobahn) / 7), int(5 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    f = AutosZählen(Autobahn, int(5 * len(Autobahn) / 7), int(6 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    g = AutosZählen(Autobahn, int(6 * len(Autobahn) / 7), int(7 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    return ([Höchstgeschwindigkeit(b, GLS), Höchstgeschwindigkeit(c, GLS), Höchstgeschwindigkeit(d, GLS), Höchstgeschwindigkeit(e, GLS), Höchstgeschwindigkeit(f, GLS), Höchstgeschwindigkeit(g, GLS), 10])

def GeschwindigkeitsbegrenzungEinführen(a, Geschwindigkeitsbegrenzung):
    for i in range(len(a)):
        if i < len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[0]
        elif i < 2*len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[1]
        elif i < 3 * len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[2]
        elif i < 4*len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[3]
        elif i < 5*len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[4]
        elif i < 6*len(a) / 7:
            a[i][1] = Geschwindigkeitsbegrenzung[5]
        elif i < len(a):
            a[i][1] = Geschwindigkeitsbegrenzung[6]
    return (a)


def glsÜberprüfen(GLS):
    Geschwindigkeitsbegrenzung = [10, 10, 10, 10, 10, 10, 10]
    vmax = 7  # Höchstgeschwindigkeit der Fahrzeuge
    p = [0.22, 0.2, 0.16, 0.13, 0.11, 0.08, 0.06, 0.05]  # Wahrscheinlichkeit, dass ein Auto trödelt
    a = 200  # 1/7 der Zellen
    Autobahn = neueSpur(7 * a, Geschwindigkeitsbegrenzung)
    Autobahn = neueFahrzeuge(Autobahn, 150, vmax)

    count = 0
    while count < 600:
        Geschwindigkeitsbegrenzung = neueGeschwindigkeitsbegrenzung(Autobahn, GLS)
        Autobahn = GeschwindigkeitsbegrenzungEinführen(Autobahn, Geschwindigkeitsbegrenzung)
        Autobahn = nächsteZeiteinheit(Autobahn, p, vmax, Geschwindigkeitsbegrenzung)
        if count > 10:
            for i in range(len(Autobahn)):
                if Autobahn[i][0] != 0:
                    if Autobahn[i][0].getAutonummer() == 1:
                        #if Autobahn[i][0].getIndex() < 9:#Für geschlossene Fahrbahn
                        if Autobahn[i][0].getIndex() > 1390:#Für offene Fahrbahn
                            return(Autobahn[i][0].getFahrtdauer())
        count += 1
    return(count)

def ohneGLS():#2:35min
    a = [glsÜberprüfen(-20) for i in range(100)]
    datei = open("ohneGLS.txt", "a")
    for i in range(len(a)):
        datei.write("{0}\n".format(a[i]))
    datei.close()

def posDaten():#14:55min
    a = [glsÜberprüfen(0) for i in range(100)]
    b = [glsÜberprüfen(1) for i in range(100)]
    c = [glsÜberprüfen(2) for i in range(100)]
    d = [glsÜberprüfen(3) for i in range(100)]
    e = [glsÜberprüfen(4) for i in range(100)]
    f = [glsÜberprüfen(5) for i in range(100)]
    datei = open("Daten_pos.txt", "a")
    for i in range(len(a)):
        datei.write("{0} {1} {2} {3} {4} {5}\n".format(a[i], b[i], c[i], d[i], e[i], f[i]))
    datei.close()

def negDaten():#13:55
    a = [glsÜberprüfen(-1) for i in range(100)]
    b = [glsÜberprüfen(-2) for i in range(100)]
    c = [glsÜberprüfen(-3) for i in range(100)]
    d = [glsÜberprüfen(-4) for i in range(100)]
    e = [glsÜberprüfen(-5) for i in range(100)]
    f = [glsÜberprüfen(-6) for i in range(100)]
    datei = open("Daten_neg.txt", "a")
    for i in range(len(a)):
        datei.write("{0} {1} {2} {3} {4} {5}\n".format(a[i],b[i],c[i],d[i],e[i],f[i]))
    datei.close()

def restlicheDaten():#30min
    a = [glsÜberprüfen(-7) for i in range(100)]
    b = [glsÜberprüfen(-8) for i in range(100)]
    c = [glsÜberprüfen(-9) for i in range(100)]
    d = [glsÜberprüfen(-10) for i in range(100)]
    e = [glsÜberprüfen(-11) for i in range(100)]
    f = [glsÜberprüfen(-12) for i in range(100)]
    g = [glsÜberprüfen(-13) for i in range(100)]
    h = [glsÜberprüfen(-14) for i in range(100)]
    i = [glsÜberprüfen(-15) for i in range(100)]
    j = [glsÜberprüfen(-16) for z in range(100)]
    k = [glsÜberprüfen(-17) for z in range(100)]
    l = [glsÜberprüfen(-18) for z in range(100)]
    m = [glsÜberprüfen(-19) for z in range(100)]
    datei = open("Daten_rest.txt", "a")
    for z in range(len(a)):
        datei.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}\n".format(a[z], b[z], c[z], d[z], e[z], f[z], g[z], h[z], i[z], j[z], k[z], l[z], m[z]))
    datei.close()