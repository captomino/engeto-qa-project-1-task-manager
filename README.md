# Task Manager

## O projektu

Jednoduchá **konzolová aplikace v Pythonu pro správu úkolů**. Projekt vznikl jako součást ENGETO Testing Akademie a je zaměřen na implementaci funkcionality a návrh testovacích případů.

Aplikace umožňuje:
- přidání nového úkolu
- zobrazení všech uložených úkolů
- odstranění vybraného úkolu
- návrat do hlavního menu pomocí únikového znaku
- ukončení programu

Úkoly jsou – v souladu se zadáním – ukládány do seznamu v paměti aplikace po dobu běhu programu.  **Po ukončení aplikace nejsou data perzistentní**.

## Cíl projektu

Cílem projektu bylo navrhnout a otestovat jednoduchou konzolovou aplikaci se zaměřením na validační logiku, ošetření chybových stavů a pokrytí funkcionality testovacími scénáři.  

Součástí implementace je také **uživatelsky bezpečné ovládání**, které umožňuje kdykoliv opustit některé operace a vrátit se zpět do hlavního menu.

## Funkce aplikace

### `hlavni_menu()`
Řídicí funkce aplikace. Zobrazuje hlavní menu a zpracovává uživatelské vstupy.

Možnosti:
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Obsahuje validaci:
- neplatná volba (mimo rozsah 1–4)
- nečíselný vstup
- prázdný vstup
- vstup s mezerami (ošetřeno pomocí `strip()`)

### `pridat_ukol()`
Přidá nový úkol do seznamu.

Validace:
- název nesmí být prázdný
- popis nesmí být prázdný
- název musí být unikátní (case insensitive kontrola)  

Funkce také umožňuje **kdykoliv opustit přidávání úkolu** zadáním únikového znaku:  
```
q
```
Po jeho zadání se aplikace vrátí do hlavního menu bez vytvoření úkolu.

Po úspěšném přidání je vypsána potvrzovací zpráva.

### `zobrazit_ukoly()`
Zobrazí všechny uložené úkoly ve formátu:

```
1. Název - Popis
```

Pokud je seznam prázdný, aplikace zobrazí informativní hlášení.

### `odstranit_ukol()`
Odstraní úkol podle čísla zadaného uživatelem.

Ošetřuje:
- pokus o odstranění z prázdného seznamu
- nečíselný vstup
- záporné číslo
- hodnotu 0
- číslo mimo rozsah seznamu
- opakované zadání po chybě  

Stejně jako při přidávání úkolu může uživatel operaci kdykoliv opustit zadáním:  
```
q
```
Aplikace se následně vrátí zpět do hlavního menu bez provedení změny.

## Použité technologie

- Python 3.13+
- Konzolové rozhraní (CLI)
- Manuální testování
- Microsoft Excel (testovací dokumentace)

## Požadavky

- Python 3.13+
- Windows / macOS / Linux
- Terminál nebo VS Code


## Spuštění aplikace

1. Naklonujte repozitář nebo stáhněte projekt.
2. Otevřete terminál ve složce projektu.
3. Spusťte:

```bash
python main.py
```

## Struktura projektu

```
engeto-qa-project-1-task-manager/
│
├── main.py
├── test_cases.xlsx
├── README.md
└── .gitignore
```

- `main.py` – zdrojový kód aplikace  
- `test_cases.xlsx` – dokumentace testovacích případů  
- `README.md` – popis projektu  
- `.gitignore` – definice ignorovaných souborů (venv, cache apod.)

## Testování

Testování bylo provedeno manuálně ve finální verzi aplikace.

Testovací dokumentace obsahuje:

- pozitivní testy
- negativní testy
- hraniční případy
- integrační (E2E) scénář

Každý testovací případ obsahuje:

- ID testu
- název testu
- typ testu
- vstupní podmínky
- kroky testu
- očekávaný výsledek
- skutečný výsledek
- stav (Pass / Fail)

## Omezení projektu

- Data nejsou ukládána mezi spuštěními aplikace.
- Aplikace běží pouze v konzolovém prostředí.
- Testování je manuální (není implementována automatizovaná testovací sada).

## Možná rozšíření

- Ukládání úkolů do JSON souboru (perzistence dat)
- Načítání uložených úkolů při spuštění aplikace
- Editace existujícího úkolu
- Omezení délky názvu a popisu
- Implementace automatizovaných testů (např. pomocí pytest)
- Refaktor do objektově orientovaného návrhu


## Autor

**Tomáš Čáp**  
Projekt vytvořen v rámci ENGETO Testing Akademie (2026)  
GitHub: [github.com/captomino](https://github.com/captomino) 

## Licence

Tento projekt je určen výhradně pro vzdělávací účely.
