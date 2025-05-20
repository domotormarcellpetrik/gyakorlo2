
class Kutya:
    def __init__(self, nev, fajta, eletkor, gazdi):
        self.nev = nev
        self.fajta = fajta
        self.eletkor = int(eletkor)
        self.gazdi = gazdi
    def __str__(self):
        return f"{self.nev} ({self.fajta}, {self.eletkor}) - gazdi: {self.gazdi}"

kutyak = []
fajtak = []
legidosebb = None
with open("kutyak.txt") as f:
    for l in f.read().split("\n"):
        if not ";" in l: continue
        data = l.split(";")
        k = Kutya(data[0],data[1],data[2],data[3])
        kutyak.append(k)
        if not k.fajta in fajtak:
            fajtak.append(k.fajta)
        if not legidosebb: legidosebb = k
        if k.eletkor > legidosebb.eletkor:
            legidosebb = k
    print("Kutyák száma: " + str(len(kutyak)))
    print("Fajták:")
    print(*fajtak)
    print("Legidősebb kutya: " + str(legidosebb))
    g = input("Gazdi neve:")
    print("-------")
    print("Kutyái:")
    s = ""
    for k in kutyak:
        if k.gazdi.lower() == g.lower():
            print(k)
            s += str(k) + "\n"
    print("-------")
    f2 = open(g.lower() + ".txt", "w")
    f2.write(s[0:-1])
    f2.close()
    print("8 évnél idősebbek:")
    for k in kutyak:
        if k.eletkor > 8: print(k)
    print("-------")
    print("Keverék kutyák:")
    for k in kutyak:
        if k.fajta == "keverék": print(k)
    print("-------")

