#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://m365.cloud.microsoft/chat/?titleId=T_fa7479b0-0972-5ee7-ba41-8bb4bacf5a39&source=embedded-builder
"""
Build script - Vytvoreni spustitelne aplikace (.exe) bez nutnosti instalace Python.

Tento skript prevede Python projekt na samostatny .exe soubor pomoci PyInstaller.
Vyslednou aplikaci pak lze spoustet kliknutim, bez nutnosti instalovat Python.

NAVOD PRO STUDENTY:
===================

1. Instalace PyInstaller:
   - Otevri terminal (PowerShell, CMD)
   - Jdi do slozky projektu
   - Spusti: pip install pyinstaller
   
2. Spusteni build skriptu:
   - V tomto souboru si eventualne prizpusob konstanty nize
   - Spusti: python build.py
   
3. Vysledek:
   - Vedle slozky 'dist/' se vytvoří slozka 'dist/ZahadaZtraceneSkoly/'
   - V ni je soubor 'main.exe'
   - Zkopiruj si celou slozku 'ZahadaZtraceneSkoly/' kamkoliv chces
   - Spusti 'main.exe' dvojklikem a hra se spusti

PRIZPUSOBENI PRO SVUJ PROJEKT:
==============================
Na zacatku tohoto souboru (sekce KONFIGURACE) si nastav tyto konstanty:

- PROJECT_NAME: Nazev tveho projektu (bude jmeno .exe i vysledne slozky)
- ENTRY_POINT: Cesta k main souboru (obvykle "main.py")
- PROJECT_ICON: Cesta k ikone .ico (volitelne, pro hezci .exe)
- CONSOLE_MODE: True = terminal videt, False = ticho (pro hry/GUI apps)
- HIDDEN_IMPORTS: Seznam importu, ktere PyInstaller nemusi videt automaticky
"""

import subprocess
import sys
import os
from pathlib import Path

# ===========================================================================
# KONFIGURACE – Přizpůsob si pro svůj projekt
# ===========================================================================

PROJECT_NAME = "Prokop_hra_skola"
"""Název projektu a výsledné .exe aplikace."""

ENTRY_POINT = "zahada_ztracene_skola.py"
"""Cesta k hlavnímu Python souboru (vstupní bod aplikace)."""

PROJECT_ICON = None  # Nastavit např. na "assets/icon.ico"
"""Ikona pro .exe soubor (volitelně). Formát: .ico soubor."""

CONSOLE_MODE = True
"""True = zobrazit terminál, False = schovat (pro GUI aplikace)."""

HIDDEN_IMPORTS = []
"""Seznam modulů, které PyInstaller nemusí detekovat automaticky.
Příklad: ["src.hra", "src.parser"] – pokudby přidáš moduly,
které normální statická analýza nenajde."""

# ===========================================================================
# SKRIPT – Obvykle nemusíš měnit
# ===========================================================================

def check_pyinstaller() -> bool:
    """Zkontroluje, jestli je PyInstaller nainstalovany."""
    try:
        import PyInstaller
        print("[OK] PyInstaller nalezen")
        return True
    except ImportError:
        print("[ERROR] PyInstaller neni nainstalovany")
        print("\nInstall help:")
        print("  pip install pyinstaller")
        return False


def check_entry_point() -> bool:
    """Zkontroluje, jestli existuje vstupni soubor."""
    if not Path(ENTRY_POINT).exists():
        print(f"[ERROR] Soubor '{ENTRY_POINT}' nenalezen")
        print(f"  Zkontroluj ENTRY_POINT konstantu v {__file__}")
        return False
    print(f"[OK] Vstupni bod '{ENTRY_POINT}' nalezen")
    return True


def build_executable() -> None:
    """Spustí PyInstaller a vytvoří .exe soubor."""
    print(f"\n{'='*60}")
    print(f"Vytvareni spustitelne aplikace: {PROJECT_NAME}")
    print(f"{'='*60}\n")

    # Priprava PyInstaller argumentu
    pyinstaller_args = [
        "-y",  # Overwrite bez potvrzeni
        "--onedir",
        f"--name={PROJECT_NAME}",
        f"--distpath=dist",
        f"--specpath=.",
    ]

    # Režim konzole
    if CONSOLE_MODE:
        pyinstaller_args.append("--console")
    else:
        pyinstaller_args.append("--windowed")

    # Ikona (volitelně)
    if PROJECT_ICON and Path(PROJECT_ICON).exists():
        pyinstaller_args.append(f"--icon={PROJECT_ICON}")
        print(f"  Ikona: {PROJECT_ICON}")

    # Skryté importy
    for imp in HIDDEN_IMPORTS:
        pyinstaller_args.append(f"--hidden-import={imp}")
        print(f"  Hidden import: {imp}")

    # Hlavní soubor
    pyinstaller_args.append(ENTRY_POINT)

    print(f"  Vstupní soubor: {ENTRY_POINT}")
    print(f"  Režim: {'Terminál' if CONSOLE_MODE else 'Skrytý'}\n")

    # Spuštění PyInstaller
    print("Běží PyInstaller...")
    cmd = [sys.executable, "-m", "PyInstaller"] + pyinstaller_args

    try:
        result = subprocess.run(cmd, check=True)
        if result.returncode == 0:
            print_success()
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Chyba behem buildovani: {e}")
        sys.exit(1)


def print_success() -> None:
    """Vypíše zprávu o úspěšném buildování."""
    dist_path = Path("dist") / PROJECT_NAME
    exe_path = dist_path / f"{PROJECT_NAME}.exe"

    print(f"\n{'='*60}")
    print(f"[SUCCESS] BUILDOVANI USPESNE!")
    print(f"{'='*60}\n")

    print(f"[INFO] Vysledna aplikace:")
    print(f"   {exe_path.resolve()}\n")

    print(f"[HOW] Jak ji spustit:")
    print(f"   1. Jdi do slozky: {dist_path.resolve()}")
    print(f"   2. Dvojklik na {PROJECT_NAME}.exe")
    print(f"   3. Hra se spusti v terminalu\n")

    print(f"[DIST] Distribuce:")
    print(f"   * Chces-li poslat aplikaci kamaradovi:")
    print(f"   * Zkopiruj CELOU slozku: {dist_path}")
    print(f"   * Posli mu ji (ZIP, OneDrive, atd.)")
    print(f"   * On si jenom rozbali a spusti .exe\n")

    print(f"[TIPS] Tipy:")
    print(f"   * Slozka 'dist/' je tva finalni distribuce")
    print(f"   * Slozku 'build/' a '.spec' soubory smazs (nejsou potreba)")
    print(f"   * Pri pristim buildovani si je znova vytvori")
    print(f"   * Zkus: python build.py (a znova vygeneruj s novejsi verzi)")


def main() -> None:
    """Hlavní funkce."""
    print("\n[BUILD] Build script -  {PROJECT_NAME}\n")

    # Kontroly
    if not check_pyinstaller():
        print("\n[INFO] Nainstaluj PyInstaller: pip install pyinstaller")
        sys.exit(1)

    if not check_entry_point():
        sys.exit(1)

    # Build
    try:
        build_executable()
    except Exception as e:
        print(f"\n[ERROR] Neocekavana chyba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
