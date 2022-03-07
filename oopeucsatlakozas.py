class Csatlakozas:
    def __init__(self, sor):
        orszag, datum = sor.strip().split(';')
        self.orszag = orszag
        self.datum  = datum

with open("EUtagallamai.txt", encoding="UTF-8") as f:
    lista = [ Csatlakozas(sor) for sor in f ]
    
# 3. feladat: EU tagállamainak szama
print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")

# 4. feladat: 2007-ben ? ország csatlakozott.
darab = len( [ sor for sor in lista if sor.datum[:4] == "2007"] )
print(f"4. feladat: 2007-ben {darab} ország csatlakozott.")

# 5. feladat: Magyarország csatlakozásának dátuma:
cs_datum = [sor.datum for sor in lista if sor.orszag == "Magyarország"][0]
print(f"5. feladat: Magyarország csatlakozásának dátuma: {cs_datum}")

# 6. feladat: Májusban volt? csatlakozás!
majus = [sor.orszag for sor in lista if sor.datum[5:7] == "05"]
message = "volt" if majus else "nem volt"
print(f"6. feladat: Májusban {message} csatlakozás!")

# 7. feladat: Legutoljára csatlakozott ország: ?
utoljara = max( [(sor.datum, sor.orszag) for sor in lista] )[1]
print(f"7. feladat: Legutoljára csatlakozott ország: {utoljara}")

# 8. feladat: Statisztika
print(f"8. feladat: Statisztika")
statisztika = dict()
for sor in lista:
    statisztika[ sor.datum[:4] ] = statisztika.get( sor.datum[:4], 0 ) + 1

for i in statisztika.items():
    print(f"        {i[0]} -  {i[1]} ország")
