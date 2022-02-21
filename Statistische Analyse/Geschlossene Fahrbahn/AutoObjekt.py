class Auto:

    index = None
    vmax = None
    fahrtdauer = 0
    v = 0
    autonummer = None
    def __init__(self, autonummer, index, v, vmax):
        self.autonummer = autonummer
        self.index = index
        self.vmax = vmax
        self.v = v

    def getIndex(self):
        return self.index

    def getVmax(self):
        return self.vmax

    def getV(self):
        return self.v

    def getFahrtdauer(self):
        return self.fahrtdauer

    def getAutonummer(self):
        return self.autonummer

    def changeVmax(self, vmax):
        self.vmax = vmax

    def changeV(self, v):
        self.v = v

    def changeFahrtdauer(self):
        self.fahrtdauer += 1

    def changeIndex(self, neuerIndex):
        self.index = neuerIndex