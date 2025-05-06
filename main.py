utulek = vytvor_utulek()
pridej_zvire(utulek, "míca", "kocka", 3)
pridej_zvire(utulek, "baryk", "pes", 5)
pridej_zvire(utulek, "Bobek", "kralik", 2)

print("vsechna zvirata v utulku:")
vpis_zvirata(utulek)

print("jen psi:")
vypis_podle_druhu(utulek, "pes")

def vytvor_utulek():
return{}

def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek,}

    def vypis_zvirata(utulek):
        for jmeno, info in utulek.items():
            print(f"{jmeno} je {info["druh"]} a je mu {info["vek"]} let.")

def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            print(f"{jmeno} je {info["druh"]} a je mu {info["vek"]} lek.")

