# ==============================
# TASK MANAGER
# Projekt 1 - Engeto Testing Akademie
# ==============================

ukoly = []


def hlavni_menu():
    """
    Hlavní menu aplikace.
    Umožňuje uživateli přidat, zobrazit nebo odstranit úkol.
    Volba 4 ukončí program.
    """
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break
        else:
            print("Neplatná volba. Zadejte číslo od 1 do 4.")


def pridat_ukol():
    """
    Přidá nový úkol do seznamu.
    Uživatel musí zadat neprázdný název i popis.
    Pomocí 'q' se může vrátit do hlavního menu.
    """
    while True:
        nazev = input("\nZadejte název úkolu (nebo 'q' pro návrat do menu): ").strip()

        if nazev.lower() == "q":
            print("Návrat do hlavního menu.")
            return

        popis = input("Zadejte popis úkolu (nebo 'q' pro návrat do menu): ").strip()

        if popis.lower() == "q":
            print("Návrat do hlavního menu.")
            return

        if not nazev or not popis:
            print("Název ani popis nesmí být prázdný. Zkuste to znovu.")
            continue
        
        # Kontrola duplicitního názvu (nezávisle na velikosti písmen)
        if any(ukol["nazev"].lower() == nazev.lower() for ukol in ukoly):
            print("Úkol s tímto názvem již existuje. Zadejte jiný název.")
            continue
        
        ukol = {
            "nazev": nazev,
            "popis": popis
        }
        ukoly.append(ukol)
        print(f"Úkol '{nazev}' byl přidán.")
        break


def zobrazit_ukoly():
    """
    Zobrazí všechny uložené úkoly.
    Pokud seznam neobsahuje žádné úkoly, informuje uživatele.
    """
    print("\nSeznam úkolů:")

    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    """
    Odstraní úkol podle čísla zadaného uživatelem.
    Ošetřuje neplatné vstupy a rozsah seznamu.
    Pomocí 'q' se uživatel může vrátit do hlavního menu.
    """
    if not ukoly:
        print("Seznam úkolů je prázdný. Není co odstranit.")
        return

    zobrazit_ukoly()

    while True:
        volba = input("\nZadejte číslo úkolu, který chcete odstranit (nebo 'q' pro návrat): ").strip()

        if volba.lower() == "q":
            print("Návrat do hlavního menu.")
            return

        try:
            cislo = int(volba)

            if 1 <= cislo <= len(ukoly):
                odstraneny_ukol = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
                break
            else:
                print("Zadané číslo není v seznamu. Zkuste to znovu.")

        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo nebo 'q'.")


# ==============================
# Spuštění programu
# ==============================

if __name__ == "__main__":
    hlavni_menu()
