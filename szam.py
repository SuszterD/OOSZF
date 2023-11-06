class Szam:
    def __init__(self, ertek):
        self.ertek = ertek

    def __str__(self):
        return f"szam: {self.ertek}"

    def __add__(self, masik):
        return Szam(self.ertek + masik.ertek)


szam1 = Szam(5)
szam2 = Szam(10)

szam3 = szam1 + szam2

print(szam3)
