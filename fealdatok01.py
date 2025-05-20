import math

gyujti = input("Mire gyűjti Anna a pénzét?")
kutyak_szama = int(input("Hány kutyát sétáltat a hétvégén?"))
ido = kutyak_szama*20
print(f"Összes időtöltés sétálással: {math.floor(ido/60)}:{ido%60}")
kereset = kutyak_szama*700
print(f"Anna {kereset} forintot keresett összesen.")
if kereset >= 5000:
    print(f"Anna {kutyak_szama} kutyát sétáltatott {math.floor(ido/60)}:{ido%60} óra alatt, ezért {kereset} Ft-ot kapott. Ez elég a {gyujti}-ra/re.")
else:
    print(f"Anna {kutyak_szama} kutyát sétáltatott {math.floor(ido/60)}:{ido%60} óra alatt, ezért {kereset} Ft-ot kapott. Ez még nem elég a {gyujti}-ra/re.")


