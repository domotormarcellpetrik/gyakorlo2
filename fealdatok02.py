kutyusok = []
with open("./kutyusok.txt", encoding="UTF-8") as f:
    i_betus = []
    nevek = {}
    van_ism = False
    for l in f.read().split("\n"):
        nev = l.replace(" ", "").upper()
        if not nev in nevek:
            nevek[nev] = 0
        nevek[nev] += 1
        if nevek[nev] > 1: van_ism = True
        if nev[-1] == "I":
            i_betus.append(nev)
        kutyusok.append(nev)
    print(str(len(kutyusok)) + " kutyanév szerepel a listában.")
    print("i betűs nevek:")
    print(*i_betus)
    if van_ism:
        for nev in nevek:
            print(nev + " : " + str(nevek[nev]))
    print("ABC sorrendben:")
    kutyusok.sort()
    print(*kutyusok)
    f2 = open("kutyusok_nagy.txt", "w", encoding="UTF-8")
    s = ""
    for k in kutyusok:
        s += k + "\n"
    f2.write(s[0:-1])
    f2.close()
    f.close()