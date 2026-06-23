# Zadání projektu: Procedurální textová hra "Útěk ze školy"

Tento projekt je určen pro začínající programátory k procvičení základních konstruktů jazyka Python: funkcí, větvení programu (podmínek), cyklů a práce s vestavěnými datovými strukturami (slovníky a seznamy).

Cílem je vytvořit jednoduchou terminálovou hru, ve které se hráč pokusí uniknout ze tří uzamčených místností školy. Na rozdíl od pokročilých verzí her je v tomto projektu veškerý text i logika spojen do jednoho zdrojového souboru.

---

## 1. Zadání úlohy

Naprogramujte konzolovou hru, která simuluje pohyb hráče mezi třemi místnostmi:
1. **Vestibul** (výchozí místnost, nachází se zde zamčený východ ze školy).
2. **Učebna** (místnost na západ od vestibulu, leží zde zapomenutý klíč).
3. **Kabinet** (místnost na sever od vestibulu, nachází se zde nápověda).

Hráč vyhrává v momentě, kdy z vestibulu použije klíč k odemčení hlavního východu. Hra končí úspěchem nebo ručním ukončením pomocí příkazu "konec".

---

## 2. Požadavky na implementaci

Pro zajištění přehlednosti a udržitelnosti kódu je nutné dodržet následující pravidla:

1. **Procedurální přístup:** Kód nesmí obsahovat žádné třídy (`class`). Stav hry je uložen v jednoduchém slovníku.
2. **Typové anotace (Type Hints):** Každá funkce musí mít explicitně definované typy parametrů a návratových hodnot.
3. **Dokumentace:** Každá funkce musí obsahovat dokumentační řetězec (docstring) v Google stylu popisující její účel.
4. **Ošetření vstupů:** Program musí tolerovat, pokud uživatel zadá příkaz velkými písmeny nebo s mezerami na začátku/konci.

---

## 3. Očekávaný výstup v terminálu

Program se po spuštění chová jako textové rozhraní. Příklad validního průchodu hrou:

```text
Stojíš ve vestibulu školy. Hlavní dveře ven jsou zamčené.
Můžeš jít na sever (kabinet) nebo na západ (učebna).

Zadej příkaz: jdi zapad

Přesunul ses do učebny. Na katedře leží rezavý klíč.
Můžeš jít na východ (vestibul).

Zadej příkaz: seber klic
Sebral jsi klíč. Nyní ho máš v inventáři.

Zadej příkaz: jdi vychod
Stojíš ve vestibulu školy. Hlavní dveře ven jsou zamčené.

Zadej příkaz: pouzij klic
Odemkl jsi hlavní dveře a úspěšně jsi utekl ze školy! Vyhrál jsi.

```

---

## 4. Struktura kódu a šablona pro studenty

Implementujte hru do jednoho souboru `hra_jednoducha.py`. Využijte následující předpřipravenou strukturu a doplňte kód označený jako `TODO`.

```python
from typing import Any, Dict


def inicializuj_stav() -> Dict[str, Any]:
    """Vytvoří a vrátí výchozí stav hry.

    Returns:
        Slovník reprezentující stav hry (poloha, inventář, aktivita).
    """
    return {
        "aktualni_mistnost": "vestibul",
        "inventar": [],
        "hra_bezi": True
    }


def vypis_popis(stav: Dict[str, Any]) -> None:
    """Vypíše do terminálu textový popis aktuální místnosti a možností.

    Args:
        stav: Slovník s aktuálním stavem hry.
    """
    mistnost = stav["aktualni_mistnost"]
    
    if mistnost == "vestibul":
        print("\nStojíš ve vestibulu školy. Hlavní dveře ven jsou zamčené.")
        print("Můžeš jít na sever (kabinet) nebo na západ (učebna).")
        
    elif mistnost == "ucebna":
        print("\nPřesunul ses do učebny. Na katedře leží rezavý klíč.")
        print("Můžeš jít na východ (vestibul).")
        
    elif mistnost == "kabinet":
        print("\nJsi v kabinetu. Na tabuli je napsáno: Klíč je v učebně.")
        print("Můžeš jít na jih (vestibul).")


def zpracuj_pohyb(smer: str, stav: Dict[str, Any]) -> None:
    """Ošetří logiku přesunu mezi místnostmi.

    Args:
        smer: Cílový směr zadaný uživatelem.
        stav: Slovník s aktuálním stavem hry.
    """
    mistnost = stav["aktualni_mistnost"]
    
    # TODO: Pomocí podmínek if-elif-else implementujte logiku přechodů:
    # - Z vestibulu lze jít na "sever" (kabinet) nebo "zapad" (ucebna)
    # - Z učebny lze jít na "vychod" (vestibul)
    # - Z kabinetu lze jít na "jih" (vestibul)
    # Pokud směr neexistuje, vypište chybovou hlášku.
    pass


def zpracuj_akci(akce: str, stav: Dict[str, Any]) -> None:
    """Zpracuje nekonečné akce jako sbírání předmětů nebo použití klíče.

    Args:
        akce: Textový příkaz uživatele (např. "seber klic").
        stav: Slovník s aktuálním stavem hry.
    """
    mistnost = stav["aktualni_mistnost"]
    
    if akce == "seber klic":
        if mistnost == "ucebna" and "klic" not in stav["inventar"]:
            stav["inventar"].append("klic")
            print("Sebral jsi klíč. Nyní ho máš v inventáři.")
        else:
            print("Zde není nic k sebrání.")
            
    elif akce == "pouzij klic":
        # TODO: Implementujte logiku použití klíče:
        # - Pokud je hráč ve vestibulu a má klíč v inventáři, vyhrává (hra_bezi = False).
        # - Pokud klíč nemá nebo je v jiné místnosti, vypište příslušné texty.
        pass
        
    else:
        print("Nerozpoznaný příkaz. Zkus to znovu.")


def hlavni_smycka() -> None:
    """Řídí hlavní cyklus hry (načítání vstupu, vyhodnocení)."""
    stav = inicializuj_stav()
    print("Vítej ve hře Útěk ze školy!")
    
    while stav["hra_bezi"]:
        vypis_popis(stav)
        
        # Načtení vstupu, převedení na malá písmena a odstranění bílých znaků
        vstup = input("\nZadej příkaz: ").strip().lower()
        
        if vstup == "konec":
            stav["hra_bezi"] = False
            print("Hra byla ukončena uživatelem.")
            
        elif vstup.startswith("jdi "):
            smer = vstup.replace("jdi ", "")
            zpracuj_pohyb(smer, stav)
            
        else:
            zpracuj_akci(vstup, stav)


if __name__ == "__main__":
    hlavni_smycka()

```