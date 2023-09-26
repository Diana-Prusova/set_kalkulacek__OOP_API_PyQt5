
# Set kalkulaček (OOP, PyQt5, API)

Tento projekt byl vytvořen pro prohloubení a znalostí v OOP, PyQt5 a API. Jedná se o aplikaci, která uvítá uživatele informací o aktuálním čase a venkovní teplotě a nabídne mu dvě kalkulačky. Aritmetická kalkulačka je velmi jednoduchá (cíl byl spíše naučit se pracovat s PyQt5 než vytvořit plnohodnotnou kalkulačku). Kalkulačka na převod měn pak zadaná data převede pomocí API a vrátí uživateli výsledek.

## Instalace knihoven

Ke spuštění programu je potřeba stáhnout knihovny třetích stran. Jejich seznam je uložený v souboru requirements.txt a naistalovat je můžete pomocí příkazu: 

    pip install -r requirements.txt

## Spuštění aplikace

Aplikace se spouští pomocí hlavního souboru main.py. Z příkazového řádku (je nutné být ve složce aplikace) jej můžete spustit pomocí příkazu: 

    python main.py 

případně

    python3 main.py 
    
## Seznam souborů

1. main.py: Hlavní soubor aplikace. Spouští ji a obsahuje kód hlavního okna aplikace.

2. kalkulacka_clas.py: Soubor s kódem kalkulačky aritmetických operací.

3. Kalkulacka_prevod.py: Soubor s kódem kalkulačky pro převod měn.

4. api_keys.py: Soubor obsahuje api klíče, které jsou pro běh kódu nezbytné. 

5. requiremen.txt: Soubor se seznamem knihoven, které tento projekt používá.

6. __init__.py: Soubor, který pythonu naznačuje, že tento set souborů má považovat za balíček.

7. __pycache_: Složka vytvořená pythonem pro rychlejší běh programu. Lze vymazat.