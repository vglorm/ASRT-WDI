# ====================================================================================================>
# Zadanie 5
# Pierwiastek całkowito liczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1+3+5+...=n2.
# ====================================================================================================>
# return (pierwiastek)


def Zadanie_5(liczba: int): ...


if __name__ == "__main__":
    from testy05 import odpal_testy

    Zadanie_5(int(input('Podaj liczba: ')))

    # odpal_testy()
