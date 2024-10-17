import pdfplumber
import os


# test
def GenerujTest(numer_zadania):
    return f"""import unittest
import sys
import io
import os
import importlib

# Dodanie dynamicznej ścieżki do katalogu nadrzędnego
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, os.pardir)))
Zadanie_{numer_zadania} = importlib.import_module("{numer_zadania:02}").Zadanie_{numer_zadania}

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly


class Test_{numer_zadania}(unittest.TestCase):
    def test_BrakTestow(self):  # po napisaniu testu usunac ta funkcje
        self.assertEqual("brak napisanych testow do tego zadania", "")

    def test_wypisujacy(self):
        # te komendy przejmuja wyniki printa
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_{numer_zadania}()

        # przestajemy przejmowac wyniki printa i zwracamy jakie zmienne wypisalo po odpaleniu funkcji
        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)

    def test_zwracajacy(self):
        wynik = Zadanie_{numer_zadania}()
        prawdziwyWynik = None
        self.assertEqual(wynik, prawdziwyWynik)


if __name__ == "__main__":
    unittest.main()
"""


def PodzielTextNaZestawy(text):
    # usuwanie textu przed Zestawem
    numerZestawu = 1
    indexKoncaZestawu = text.find(f"Zestaw {numerZestawu}:")
    text = text[indexKoncaZestawu:]

    Zestawy = []
    while indexKoncaZestawu != -1:
        indexKoncaZestawu = text.find(f"Zestaw {numerZestawu+1}:")
        Zestawy.append(text[:indexKoncaZestawu])
        text = text[indexKoncaZestawu:]
        numerZestawu += 1
    return Zestawy


def StworzPlikTestowy(nrZadania, DirTestowe):
    sciezka_pliku = os.path.join(DirTestowe, f"t{nrZadania:02}.py")
    try:
        with open(sciezka_pliku, "w") as plik:
            plik.write(GenerujTest(nrZadania))
    except IOError as e:
        print(f"Nie udało się zapisać pliku testowego {sciezka_pliku}: {e}")


def StworzPlikPython(zadanie, nrZadania, nazwaZestawu):
    obramowka = "# ====================================================================================================>\n"
    zadanie_tresc = zadanie[zadanie.find(".") + 2 :].replace("\n", "\n# ")

    # czasami to sie przedluzalo nwm czemu ale to naprawia xd
    if zadanie_tresc[-2] == "#":
        zadanie_tresc = zadanie_tresc[:-3]

    zawartoscPliku = (
        f"{obramowka}"
        f"# Zadanie {nrZadania}\n"
        f"# {zadanie_tresc}\n"
        f"{obramowka}\n\n"
        f"def Zadanie_{nrZadania}(): ...\n\n\n"
        f"Zadanie_{nrZadania}()\n"
    )

    sciezka_pliku = os.path.join(nazwaZestawu, f"{nrZadania:02}.py")
    try:
        with open(sciezka_pliku, "w") as plik:
            plik.write(zawartoscPliku)
    except IOError as e:
        print(f"Nie udało się zapisać pliku {sciezka_pliku}: {e}")


def Skrypt():
    with pdfplumber.open("ZbiorZadan.pdf") as pdf:
        # lacze cale strony zbioru zadan po za ostatnimy 2 literami bo to numery strony
        TextCalegoZbioru = "".join(page.extract_text()[:-2] for page in pdf.pages)

        Zestawy = PodzielTextNaZestawy(TextCalegoZbioru)

        nrZadania = 1
        for zestaw in Zestawy:
            PoczatekNastZad = zestaw.find("Zadanie")
            nazwaZestawu = zestaw[:PoczatekNastZad].replace(" ", "_").replace("\n", "")
            os.makedirs(nazwaZestawu)
            os.makedirs(nazwaZestawu + "/testy")

            while PoczatekNastZad != -1:
                zestaw = zestaw[PoczatekNastZad:]
                PoczatekNastZad = zestaw.find(f"Zadanie {nrZadania+1}.")
                if PoczatekNastZad == -1:  # czasami pdf reader usuwa spacje pomiedzy
                    PoczatekNastZad = zestaw.find(f"Zadanie{nrZadania+1}.")

                StworzPlikPython(zestaw[:PoczatekNastZad], nrZadania, nazwaZestawu)
                StworzPlikTestowy(nrZadania, nazwaZestawu + "/testy")

                nrZadania += 1


if __name__ == "__main__":
    Skrypt()