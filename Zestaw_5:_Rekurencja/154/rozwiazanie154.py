# ====================================================================================================>
# Zadanie 154
# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>

# cos czesto psuje sie ta funkcja bedzie jeszcze poprawiana


def Zadanie_154(T, k):
    def rek(
        T, k, s, W, K
    ):  # W, K przechowują wartości False (True możemy wziąc, False nie możemy) np. W[4] == True, to z niej nie wzięliśmy
        if s > k:
            return False
        if s == k and s != 0:
            return True
        # end if

        for y in range(8):
            if W[y]:
                for x in range(8):
                    if K[x]:
                        W[y] = False
                        K[x] = False

                        if rek(T, k, s + T[y][x], W, K):
                            return True
                        else:
                            W[y] = True
                            K[x] = True

                    # end if
        # end for
        return False

    # end rek
    return rek(T, k, 0, [True] * 8, [True] * 8)


