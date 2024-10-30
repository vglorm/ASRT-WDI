import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon01 import Zadanie_1


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_1_argumenty_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_1_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_1_argumenty_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(5)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_1_argumenty_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(6)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_1_argumenty_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_1_argumenty_11(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(11)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n6 8 10.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_1_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n5 12 13.0\n6 8 10.0\n8 15 17.0\n9 12 15.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_1_argumenty_30(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(30)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n5 12 13.0\n6 8 10.0\n7 24 25.0\n8 15 17.0\n9 12 15.0\n10 24 26.0\n12 16 20.0\n15 20 25.0\n20 21 29.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_1_argumenty_40(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(40)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n5 12 13.0\n6 8 10.0\n7 24 25.0\n8 15 17.0\n9 12 15.0\n10 24 26.0\n12 16 20.0\n12 35 37.0\n15 20 25.0\n15 36 39.0\n16 30 34.0\n18 24 30.0\n20 21 29.0\n21 28 35.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_1_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n5 12 13.0\n6 8 10.0\n7 24 25.0\n8 15 17.0\n9 12 15.0\n9 40 41.0\n10 24 26.0\n11 60 61.0\n12 16 20.0\n12 35 37.0\n13 84 85.0\n14 48 50.0\n15 20 25.0\n15 36 39.0\n16 30 34.0\n16 63 65.0\n18 24 30.0\n18 80 82.0\n20 21 29.0\n20 48 52.0\n21 28 35.0\n21 72 75.0\n24 32 40.0\n24 45 51.0\n24 70 74.0\n25 60 65.0\n27 36 45.0\n28 45 53.0\n30 40 50.0\n30 72 78.0\n32 60 68.0\n33 44 55.0\n33 56 65.0\n35 84 91.0\n36 48 60.0\n36 77 85.0\n39 52 65.0\n39 80 89.0\n40 42 58.0\n40 75 85.0\n42 56 70.0\n45 60 75.0\n48 55 73.0\n48 64 80.0\n51 68 85.0\n54 72 90.0\n57 76 95.0\n60 63 87.0\n65 72 97.0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_1_argumenty_2115(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(2115)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5.0\n5 12 13.0\n6 8 10.0\n7 24 25.0\n8 15 17.0\n9 12 15.0\n9 40 41.0\n10 24 26.0\n11 60 61.0\n12 16 20.0\n12 35 37.0\n13 84 85.0\n14 48 50.0\n15 20 25.0\n15 36 39.0\n15 112 113.0\n16 30 34.0\n16 63 65.0\n17 144 145.0\n18 24 30.0\n18 80 82.0\n19 180 181.0\n20 21 29.0\n20 48 52.0\n20 99 101.0\n21 28 35.0\n21 72 75.0\n21 220 221.0\n22 120 122.0\n23 264 265.0\n24 32 40.0\n24 45 51.0\n24 70 74.0\n24 143 145.0\n25 60 65.0\n25 312 313.0\n26 168 170.0\n27 36 45.0\n27 120 123.0\n27 364 365.0\n28 45 53.0\n28 96 100.0\n28 195 197.0\n29 420 421.0\n30 40 50.0\n30 72 78.0\n30 224 226.0\n31 480 481.0\n32 60 68.0\n32 126 130.0\n32 255 257.0\n33 44 55.0\n33 56 65.0\n33 180 183.0\n33 544 545.0\n34 288 290.0\n35 84 91.0\n35 120 125.0\n35 612 613.0\n36 48 60.0\n36 77 85.0\n36 105 111.0\n36 160 164.0\n36 323 325.0\n37 684 685.0\n38 360 362.0\n39 52 65.0\n39 80 89.0\n39 252 255.0\n39 760 761.0\n40 42 58.0\n40 75 85.0\n40 96 104.0\n40 198 202.0\n40 399 401.0\n41 840 841.0\n42 56 70.0\n42 144 150.0\n42 440 442.0\n43 924 925.0\n44 117 125.0\n44 240 244.0\n44 483 485.0\n45 60 75.0\n45 108 117.0\n45 200 205.0\n45 336 339.0\n45 1012 1013.0\n46 528 530.0\n47 1104 1105.0\n48 55 73.0\n48 64 80.0\n48 90 102.0\n48 140 148.0\n48 189 195.0\n48 286 290.0\n48 575 577.0\n49 168 175.0\n49 1200 1201.0\n50 120 130.0\n50 624 626.0\n51 68 85.0\n51 140 149.0\n51 432 435.0\n51 1300 1301.0\n52 165 173.0\n52 336 340.0\n52 675 677.0\n53 1404 1405.0\n54 72 90.0\n54 240 246.0\n54 728 730.0\n55 132 143.0\n55 300 305.0\n55 1512 1513.0\n56 90 106.0\n56 105 119.0\n56 192 200.0\n56 390 394.0\n56 783 785.0\n57 76 95.0\n57 176 185.0\n57 540 543.0\n57 1624 1625.0\n58 840 842.0\n59 1740 1741.0\n60 63 87.0\n60 80 100.0\n60 91 109.0\n60 144 156.0\n60 175 185.0\n60 221 229.0\n60 297 303.0\n60 448 452.0\n60 899 901.0\n61 1860 1861.0\n62 960 962.0\n63 84 105.0\n63 216 225.0\n63 280 287.0\n63 660 663.0\n63 1984 1985.0\n64 120 136.0\n64 252 260.0\n64 510 514.0\n64 1023 1025.0\n65 72 97.0\n65 156 169.0\n65 420 425.0\n65 2112 2113.0\n66 88 110.0\n66 112 130.0\n66 360 366.0\n66 1088 1090.0\n68 285 293.0\n68 576 580.0\n68 1155 1157.0\n69 92 115.0\n69 260 269.0\n69 792 795.0\n70 168 182.0\n70 240 250.0\n70 1224 1226.0\n72 96 120.0\n72 135 153.0\n72 154 170.0\n72 210 222.0\n72 320 328.0\n72 429 435.0\n72 646 650.0\n72 1295 1297.0\n74 1368 1370.0\n75 100 125.0\n75 180 195.0\n75 308 317.0\n75 560 565.0\n75 936 939.0\n76 357 365.0\n76 720 724.0\n76 1443 1445.0\n77 264 275.0\n77 420 427.0\n78 104 130.0\n78 160 178.0\n78 504 510.0\n78 1520 1522.0\n80 84 116.0\n80 150 170.0\n80 192 208.0\n80 315 325.0\n80 396 404.0\n80 798 802.0\n80 1599 1601.0\n81 108 135.0\n81 360 369.0\n81 1092 1095.0\n82 1680 1682.0\n84 112 140.0\n84 135 159.0\n84 187 205.0\n84 245 259.0\n84 288 300.0\n84 437 445.0\n84 585 591.0\n84 880 884.0\n84 1763 1765.0\n85 132 157.0\n85 204 221.0\n85 720 725.0\n86 1848 1850.0\n87 116 145.0\n87 416 425.0\n87 1260 1263.0\n88 105 137.0\n88 165 187.0\n88 234 250.0\n88 480 488.0\n88 966 970.0\n88 1935 1937.0\n90 120 150.0\n90 216 234.0\n90 400 410.0\n90 672 678.0\n90 2024 2026.0\n91 312 325.0\n91 588 595.0\n92 525 533.0\n92 1056 1060.0\n93 124 155.0\n93 476 485.0\n93 1440 1443.0\n95 168 193.0\n95 228 247.0\n95 900 905.0\n96 110 146.0\n96 128 160.0\n96 180 204.0\n96 247 265.0\n96 280 296.0\n96 378 390.0\n96 572 580.0\n96 765 771.0\n96 1150 1154.0\n98 336 350.0\n99 132 165.0\n99 168 195.0\n99 440 451.0\n99 540 549.0\n99 1632 1635.0\n100 105 145.0\n100 240 260.0\n100 495 505.0\n100 621 629.0\n100 1248 1252.0\n102 136 170.0\n102 280 298.0\n102 864 870.0\n104 153 185.0\n104 195 221.0\n104 330 346.0\n104 672 680.0\n104 1350 1354.0\n105 140 175.0\n105 208 233.0\n105 252 273.0\n105 360 375.0\n105 608 617.0\n105 784 791.0\n105 1100 1105.0\n105 1836 1839.0\n108 144 180.0\n108 231 255.0\n108 315 333.0\n108 480 492.0\n108 725 733.0\n108 969 975.0\n108 1456 1460.0\n110 264 286.0\n110 600 610.0\n111 148 185.0\n111 680 689.0\n111 2052 2055.0\n112 180 212.0\n112 210 238.0\n112 384 400.0\n112 441 455.0\n112 780 788.0\n112 1566 1570.0\n114 152 190.0\n114 352 370.0\n114 1080 1086.0\n115 252 277.0\n115 276 299.0\n115 1320 1325.0\n116 837 845.0\n116 1680 1684.0\n117 156 195.0\n117 240 267.0\n117 520 533.0\n117 756 765.0\n119 120 169.0\n119 408 425.0\n119 1008 1015.0\n120 126 174.0\n120 160 200.0\n120 182 218.0\n120 209 241.0\n120 225 255.0\n120 288 312.0\n120 350 370.0\n120 391 409.0\n120 442 458.0\n120 594 606.0\n120 715 725.0\n120 896 904.0\n120 1197 1203.0\n120 1798 1802.0\n121 660 671.0\n123 164 205.0\n123 836 845.0\n124 957 965.0\n124 1920 1924.0\n125 300 325.0\n125 1560 1565.0\n126 168 210.0\n126 432 450.0\n126 560 574.0\n126 1320 1326.0\n128 240 272.0\n128 504 520.0\n128 1020 1028.0\n128 2046 2050.0\n129 172 215.0\n129 920 929.0\n130 144 194.0\n130 312 338.0\n130 840 850.0\n132 176 220.0\n132 224 260.0\n132 351 375.0\n132 385 407.0\n132 475 493.0\n132 720 732.0\n132 1085 1093.0\n132 1449 1455.0\n133 156 205.0\n133 456 475.0\n133 1260 1267.0\n135 180 225.0\n135 324 351.0\n135 352 377.0\n135 600 615.0\n135 1008 1017.0\n135 1820 1825.0\n136 255 289.0\n136 273 305.0\n136 570 586.0\n136 1152 1160.0\n138 184 230.0\n138 520 538.0\n138 1584 1590.0\n140 147 203.0\n140 171 221.0\n140 225 265.0\n140 336 364.0\n140 480 500.0\n140 693 707.0\n140 975 985.0\n140 1221 1229.0\n141 188 235.0\n141 1100 1109.0\n143 780 793.0\n143 924 935.0\n144 165 219.0\n144 192 240.0\n144 270 306.0\n144 308 340.0\n144 420 444.0\n144 567 585.0\n144 640 656.0\n144 858 870.0\n144 1292 1300.0\n144 1725 1731.0\n145 348 377.0\n145 408 433.0\n145 2100 2105.0\n147 196 245.0\n147 504 525.0\n147 1196 1205.0\n147 1540 1547.0\n148 1365 1373.0\n150 200 250.0\n150 360 390.0\n150 616 634.0\n150 1120 1130.0\n150 1872 1878.0\n152 285 323.0\n152 345 377.0\n152 714 730.0\n152 1440 1448.0\n153 204 255.0\n153 420 447.0\n153 680 697.0\n153 1296 1305.0\n154 528 550.0\n154 840 854.0\n155 372 403.0\n155 468 493.0\n156 208 260.0\n156 320 356.0\n156 455 481.0\n156 495 519.0\n156 667 685.0\n156 1008 1020.0\n156 1517 1525.0\n156 2025 2031.0\n159 212 265.0\n159 1400 1409.0\n160 168 232.0\n160 231 281.0\n160 300 340.0\n160 384 416.0\n160 630 650.0\n160 792 808.0\n160 1275 1285.0\n160 1596 1604.0\n161 240 289.0\n161 552 575.0\n161 1848 1855.0\n162 216 270.0\n162 720 738.0\n164 1677 1685.0\n165 220 275.0\n165 280 325.0\n165 396 429.0\n165 532 557.0\n165 900 915.0\n165 1232 1243.0\n165 1508 1517.0\n168 224 280.0\n168 270 318.0\n168 315 357.0\n168 374 410.0\n168 425 457.0\n168 490 518.0\n168 576 600.0\n168 775 793.0\n168 874 890.0\n168 1001 1015.0\n168 1170 1182.0\n168 1760 1768.0\n169 1092 1105.0\n170 264 314.0\n170 408 442.0\n170 1440 1450.0\n171 228 285.0\n171 528 555.0\n171 760 779.0\n171 1620 1629.0\n172 1845 1853.0\n174 232 290.0\n174 832 850.0\n175 288 337.0\n175 420 455.0\n175 600 625.0\n176 210 274.0\n176 330 374.0\n176 468 500.0\n176 693 715.0\n176 960 976.0\n176 1932 1940.0\n177 236 295.0\n177 1736 1745.0\n180 189 261.0\n180 240 300.0\n180 273 327.0\n180 299 349.0\n180 385 425.0\n180 432 468.0\n180 525 555.0\n180 663 687.0\n180 800 820.0\n180 891 909.0\n180 1344 1356.0\n180 1615 1625.0\n180 2021 2029.0\n182 624 650.0\n182 1176 1190.0\n183 244 305.0\n183 1856 1865.0\n184 345 391.0\n184 513 545.0\n184 1050 1066.0\n185 444 481.0\n185 672 697.0\n186 248 310.0\n186 952 970.0\n187 1020 1037.0\n187 1584 1595.0\n189 252 315.0\n189 340 389.0\n189 648 675.0\n189 840 861.0\n189 1980 1989.0\n190 336 386.0\n190 456 494.0\n190 1800 1810.0\n192 220 292.0\n192 256 320.0\n192 360 408.0\n192 494 530.0\n192 560 592.0\n192 756 780.0\n192 1015 1033.0\n192 1144 1160.0\n192 1530 1542.0\n195 216 291.0\n195 260 325.0\n195 400 445.0\n195 468 507.0\n195 748 773.0\n195 1260 1275.0\n195 1456 1469.0\n196 315 371.0\n196 672 700.0\n196 1365 1379.0\n198 264 330.0\n198 336 390.0\n198 880 902.0\n198 1080 1098.0\n200 210 290.0\n200 375 425.0\n200 480 520.0\n200 609 641.0\n200 990 1010.0\n200 1242 1258.0\n200 1995 2005.0\n201 268 335.0\n203 396 445.0\n203 696 725.0\n204 253 325.0\n204 272 340.0\n204 560 596.0\n204 595 629.0\n204 855 879.0\n204 1147 1165.0\n204 1728 1740.0\n205 492 533.0\n205 828 853.0\n207 224 305.0\n207 276 345.0\n207 780 807.0\n207 920 943.0\n208 306 370.0\n208 390 442.0\n208 660 692.0\n208 819 845.0\n208 1344 1360.0\n209 1140 1159.0\n209 1980 1991.0\n210 280 350.0\n210 416 466.0\n210 504 546.0\n210 720 750.0\n210 1216 1234.0\n210 1568 1582.0\n213 284 355.0\n215 516 559.0\n215 912 937.0\n216 288 360.0\n216 405 459.0\n216 462 510.0\n216 630 666.0\n216 713 745.0\n216 960 984.0\n216 1287 1305.0\n216 1450 1466.0\n216 1938 1950.0\n217 456 505.0\n217 744 775.0\n219 292 365.0\n220 231 319.0\n220 459 509.0\n220 528 572.0\n220 585 625.0\n220 1089 1111.0\n220 1200 1220.0\n221 1428 1445.0\n221 1872 1885.0\n222 296 370.0\n222 1360 1378.0\n224 360 424.0\n224 420 476.0\n224 768 800.0\n224 882 910.0\n224 1560 1576.0\n224 1785 1799.0\n225 272 353.0\n225 300 375.0\n225 540 585.0\n225 924 951.0\n225 1000 1025.0\n225 1680 1695.0\n228 304 380.0\n228 325 397.0\n228 665 703.0\n228 704 740.0\n228 1071 1095.0\n228 1435 1453.0\n230 504 554.0\n230 552 598.0\n231 308 385.0\n231 392 455.0\n231 520 569.0\n231 792 825.0\n231 1260 1281.0\n232 435 493.0\n232 825 857.0\n232 1674 1690.0\n234 312 390.0\n234 480 534.0\n234 1040 1066.0\n234 1512 1530.0\n235 564 611.0\n235 1092 1117.0\n237 316 395.0\n238 240 338.0\n238 816 850.0\n238 2016 2030.0\n240 252 348.0\n240 275 365.0\n240 320 400.0\n240 364 436.0\n240 418 482.0\n240 450 510.0\n240 551 601.0\n240 576 624.0\n240 700 740.0\n240 782 818.0\n240 884 916.0\n240 945 975.0\n240 1188 1212.0\n240 1430 1450.0\n240 1591 1609.0\n240 1792 1808.0\n242 1320 1342.0\n243 324 405.0\n243 1080 1107.0\n245 588 637.0\n245 840 875.0\n245 1188 1213.0\n246 328 410.0\n246 1672 1690.0\n247 1596 1615.0\n248 465 527.0\n248 945 977.0\n248 1914 1930.0\n249 332 415.0\n250 600 650.0\n252 275 373.0\n252 336 420.0\n252 405 477.0\n252 539 595.0\n252 561 615.0\n252 735 777.0\n252 864 900.0\n252 1120 1148.0\n252 1311 1335.0\n252 1755 1773.0\n253 1380 1403.0\n255 340 425.0\n255 396 471.0\n255 612 663.0\n255 700 745.0\n255 1288 1313.0\n255 1904 1921.0\n256 480 544.0\n256 1008 1040.0\n256 2040 2056.0\n258 344 430.0\n258 1840 1858.0\n259 660 709.0\n259 888 925.0\n260 273 377.0\n260 288 388.0\n260 624 676.0\n260 651 701.0\n260 825 865.0\n260 1287 1313.0\n260 1680 1700.0\n261 348 435.0\n261 380 461.0\n261 1160 1189.0\n261 1248 1275.0\n264 315 411.0\n264 352 440.0\n264 448 520.0\n264 495 561.0\n264 702 750.0\n264 770 814.0\n264 950 986.0\n264 1073 1105.0\n264 1440 1464.0\n264 1573 1595.0\n264 1927 1945.0\n265 636 689.0\n265 1392 1417.0\n266 312 410.0\n266 912 950.0\n267 356 445.0\n270 360 450.0\n270 648 702.0\n270 704 754.0\n270 1200 1230.0\n270 2016 2034.0\n272 510 578.0\n272 546 610.0\n272 1071 1105.0\n272 1140 1172.0\n273 364 455.0\n273 560 623.0\n273 736 785.0\n273 936 975.0\n273 1764 1785.0\n275 660 715.0\n275 1500 1525.0\n276 368 460.0\n276 493 565.0\n276 805 851.0\n276 1040 1076.0\n276 1575 1599.0\n279 372 465.0\n279 440 521.0\n279 1240 1271.0\n279 1428 1455.0\n280 294 406.0\n280 342 442.0\n280 351 449.0\n280 450 530.0\n280 525 595.0\n280 672 728.0\n280 759 809.0\n280 960 1000.0\n280 1209 1241.0\n280 1386 1414.0\n280 1950 1970.0\n282 376 470.0\n285 380 475.0\n285 504 579.0\n285 684 741.0\n285 880 925.0\n285 1612 1637.0\n286 1560 1586.0\n286 1848 1870.0\n287 816 865.0\n287 984 1025.0\n288 330 438.0\n288 384 480.0\n288 540 612.0\n288 616 680.0\n288 741 795.0\n288 840 888.0\n288 1134 1170.0\n288 1280 1312.0\n288 1716 1740.0\n290 696 754.0\n290 816 866.0\n291 388 485.0\n294 392 490.0\n294 1008 1050.0\n295 708 767.0\n295 1728 1753.0\n296 555 629.0\n296 1353 1385.0\n297 304 425.0\n297 396 495.0\n297 504 585.0\n297 1320 1353.0\n297 1620 1647.0\n299 1932 1955.0\n300 315 435.0\n300 400 500.0\n300 455 545.0\n300 589 661.0\n300 720 780.0\n300 875 925.0\n300 1105 1145.0\n300 1232 1268.0\n300 1485 1515.0\n300 1863 1887.0\n301 900 949.0\n301 1032 1075.0\n303 404 505.0\n304 570 646.0\n304 690 754.0\n304 1197 1235.0\n304 1428 1460.0\n305 732 793.0\n305 1848 1873.0\n306 408 510.0\n306 840 894.0\n306 1360 1394.0\n308 435 533.0\n308 495 583.0\n308 819 875.0\n308 1056 1100.0\n308 1680 1708.0\n309 412 515.0\n310 744 806.0\n310 936 986.0\n312 416 520.0\n312 459 555.0\n312 585 663.0\n312 640 712.0\n312 910 962.0\n312 990 1038.0\n312 1334 1370.0\n312 1505 1537.0\n312 1859 1885.0\n312 2016 2040.0\n315 420 525.0\n315 572 653.0\n315 624 699.0\n315 756 819.0\n315 988 1037.0\n315 1080 1125.0\n315 1400 1435.0\n315 1824 1851.0\n315 1972 1997.0\n318 424 530.0\n319 360 481.0\n319 1740 1769.0\n320 336 464.0\n320 462 562.0\n320 600 680.0\n320 768 832.0\n320 999 1049.0\n320 1260 1300.0\n320 1584 1616.0\n321 428 535.0\n322 480 578.0\n322 1104 1150.0\n324 432 540.0\n324 693 765.0\n324 945 999.0\n324 1440 1476.0\n325 360 485.0\n325 780 845.0\n327 436 545.0\n328 615 697.0\n328 1665 1697.0\n329 1080 1129.0\n329 1128 1175.0\n330 440 550.0\n330 560 650.0\n330 792 858.0\n330 1064 1114.0\n330 1800 1830.0\n333 444 555.0\n333 644 725.0\n333 1480 1517.0\n333 2040 2067.0\n335 804 871.0\n336 377 505.0\n336 385 511.0\n336 448 560.0\n336 527 625.0\n336 540 636.0\n336 630 714.0\n336 748 820.0\n336 850 914.0\n336 980 1036.0\n336 1152 1200.0\n336 1323 1365.0\n336 1550 1586.0\n336 1748 1780.0\n336 2002 2030.0\n339 452 565.0\n340 357 493.0\n340 528 628.0\n340 816 884.0\n340 1131 1181.0\n340 1425 1465.0\n340 1683 1717.0\n341 420 541.0\n341 1860 1891.0\n342 456 570.0\n342 1056 1110.0\n342 1520 1558.0\n343 1176 1225.0\n344 645 731.0\n344 1833 1865.0\n345 460 575.0\n345 756 831.0\n345 828 897.0\n345 1300 1345.0\n348 464 580.0\n348 805 877.0\n348 1015 1073.0\n348 1664 1700.0\n350 576 674.0\n350 840 910.0\n350 1200 1250.0\n351 468 585.0\n351 720 801.0\n351 1560 1599.0\n352 420 548.0\n352 660 748.0\n352 936 1000.0\n352 1386 1430.0\n352 1920 1952.0\n354 472 590.0\n355 852 923.0\n357 360 507.0\n357 476 595.0\n357 980 1043.0\n357 1224 1275.0\n357 1276 1325.0\n360 378 522.0\n360 480 600.0\n360 546 654.0\n360 598 698.0\n360 627 723.0\n360 675 765.0\n360 770 850.0\n360 864 936.0\n360 1050 1110.0\n360 1173 1227.0\n360 1271 1321.0\n360 1326 1374.0\n360 1600 1640.0\n360 1782 1818.0\n360 2009 2041.0\n363 484 605.0\n363 616 715.0\n363 1980 2013.0\n364 585 689.0\n364 627 725.0\n364 1155 1211.0\n364 1248 1300.0\n365 876 949.0\n366 488 610.0\n368 465 593.0\n368 690 782.0\n368 1026 1090.0\n368 1449 1495.0\n369 492 615.0\n369 800 881.0\n369 1640 1681.0\n370 888 962.0\n370 1344 1394.0\n371 1272 1325.0\n371 1380 1429.0\n372 496 620.0\n372 925 997.0\n372 1085 1147.0\n372 1904 1940.0\n374 2040 2074.0\n375 500 625.0\n375 900 975.0\n375 1540 1585.0\n376 705 799.0\n378 504 630.0\n378 680 778.0\n378 1296 1350.0\n378 1680 1722.0\n380 399 551.0\n380 672 772.0\n380 912 988.0\n380 1419 1469.0\n380 1785 1825.0\n380 1881 1919.0\n381 508 635.0\n384 440 584.0\n384 512 640.0\n384 720 816.0\n384 988 1060.0\n384 1120 1184.0\n384 1512 1560.0\n384 2030 2066.0\n385 552 673.0\n385 924 1001.0\n385 1320 1375.0\n385 1488 1537.0\n387 516 645.0\n387 884 965.0\n387 1720 1763.0\n390 432 582.0\n390 520 650.0\n390 800 890.0\n390 936 1014.0\n390 1496 1546.0\n392 630 742.0\n392 735 833.0\n392 1344 1400.0\n393 524 655.0\n395 948 1027.0\n396 403 565.0\n396 528 660.0\n396 672 780.0\n396 847 935.0\n396 1053 1125.0\n396 1155 1221.0\n396 1425 1479.0\n396 1760 1804.0\n399 468 615.0\n399 532 665.0\n399 1232 1295.0\n399 1368 1425.0\n399 1600 1649.0\n400 420 580.0\n400 561 689.0\n400 750 850.0\n400 960 1040.0\n400 1218 1282.0\n400 1575 1625.0\n400 1980 2020.0\n402 536 670.0\n405 540 675.0\n405 972 1053.0\n405 1056 1131.0\n405 1800 1845.0\n406 792 890.0\n406 1392 1450.0\n407 624 745.0\n408 506 650.0\n408 544 680.0\n408 765 867.0\n408 819 915.0\n408 1120 1192.0\n408 1190 1258.0\n408 1710 1758.0\n410 984 1066.0\n410 1656 1706.0\n411 548 685.0\n413 1416 1475.0\n413 1716 1765.0\n414 448 610.0\n414 552 690.0\n414 1560 1614.0\n414 1840 1886.0\n415 996 1079.0\n416 612 740.0\n416 780 884.0\n416 1320 1384.0\n416 1638 1690.0\n417 556 695.0\n420 441 609.0\n420 513 663.0\n420 560 700.0\n420 637 763.0\n420 675 795.0\n420 832 932.0\n420 851 949.0\n420 935 1025.0\n420 1008 1092.0\n420 1189 1261.0\n420 1225 1295.0\n420 1440 1500.0\n420 1547 1603.0\n420 1739 1789.0\n423 564 705.0\n423 1064 1145.0\n423 1880 1927.0\n424 795 901.0\n425 660 785.0\n425 1020 1105.0\n426 568 710.0\n427 1464 1525.0\n427 1836 1885.0\n429 460 629.0\n429 572 715.0\n429 700 821.0\n429 728 845.0\n429 880 979.0\n430 1032 1118.0\n430 1824 1874.0\n432 495 657.0\n432 576 720.0\n432 665 793.0\n432 810 918.0\n432 924 1020.0\n432 1260 1332.0\n432 1426 1490.0\n432 1701 1755.0\n432 1920 1968.0\n434 912 1010.0\n434 1488 1550.0\n435 580 725.0\n435 1044 1131.0\n435 1224 1299.0\n438 584 730.0\n440 462 638.0\n440 525 685.0\n440 825 935.0\n440 918 1018.0\n440 1056 1144.0\n440 1170 1250.0\n440 1911 1961.0\n441 588 735.0\n441 1160 1241.0\n441 1512 1575.0\n441 1960 2009.0\n444 592 740.0\n444 1295 1369.0\n444 1333 1405.0\n445 1068 1157.0\n447 596 745.0\n448 720 848.0\n448 840 952.0\n448 975 1073.0\n448 1536 1600.0\n448 1764 1820.0\n450 544 706.0\n450 600 750.0\n450 1080 1170.0\n450 1848 1902.0\n450 2000 2050.0\n451 780 901.0\n453 604 755.0\n455 504 679.0\n455 528 697.0\n455 1092 1183.0\n455 1560 1625.0\n456 608 760.0\n456 650 794.0\n456 855 969.0\n456 1035 1131.0\n456 1330 1406.0\n456 1408 1480.0\n459 612 765.0\n459 1260 1341.0\n459 2040 2091.0\n460 483 667.0\n460 1008 1108.0\n460 1104 1196.0\n462 616 770.0\n462 784 910.0\n462 1040 1138.0\n462 1584 1650.0\n464 777 905.0\n464 870 986.0\n464 1650 1714.0\n464 1827 1885.0\n465 620 775.0\n465 1116 1209.0\n465 1404 1479.0\n468 595 757.0\n468 624 780.0\n468 960 1068.0\n468 1001 1105.0\n468 1365 1443.0\n468 1485 1557.0\n468 2001 2055.0\n469 1608 1675.0\n470 1128 1222.0\n471 628 785.0\n472 885 1003.0\n473 864 985.0\n474 632 790.0\n475 840 965.0\n475 1140 1235.0\n476 480 676.0\n476 765 901.0\n476 1107 1205.0\n476 1632 1700.0\n476 1995 2051.0\n477 636 795.0\n477 1364 1445.0\n480 504 696.0\n480 550 730.0\n480 640 800.0\n480 693 843.0\n480 728 872.0\n480 836 964.0\n480 900 1020.0\n480 1102 1202.0\n480 1152 1248.0\n480 1235 1325.0\n480 1400 1480.0\n480 1564 1636.0\n480 1768 1832.0\n480 1890 1950.0\n481 600 769.0\n483 644 805.0\n483 720 867.0\n483 1656 1725.0\n483 1820 1883.0\n484 1287 1375.0\n485 1164 1261.0\n486 648 810.0\n488 915 1037.0\n489 652 815.0\n490 1176 1274.0\n490 1680 1750.0\n492 656 820.0\n492 1435 1517.0\n492 1645 1717.0\n495 660 825.0\n495 840 975.0\n495 952 1073.0\n495 1188 1287.0\n495 1472 1553.0\n495 1596 1671.0\n496 897 1025.0\n496 930 1054.0\n496 1890 1954.0\n496 1953 2015.0\n497 1704 1775.0\n498 664 830.0\n500 525 725.0\n500 1200 1300.0\n501 668 835.0\n504 550 746.0\n504 672 840.0\n504 703 865.0\n504 810 954.0\n504 945 1071.0\n504 1078 1190.0\n504 1122 1230.0\n504 1247 1345.0\n504 1275 1371.0\n504 1470 1554.0\n504 1728 1800.0\n505 1212 1313.0\n507 676 845.0\n507 1040 1157.0\n510 680 850.0\n510 792 942.0\n510 1224 1326.0\n510 1400 1490.0\n511 1752 1825.0\n512 960 1088.0\n512 2016 2080.0\n513 684 855.0\n513 1584 1665.0\n515 1236 1339.0\n516 688 860.0\n516 1505 1591.0\n516 1813 1885.0\n517 1044 1165.0\n518 1320 1418.0\n518 1776 1850.0\n519 692 865.0\n520 546 754.0\n520 576 776.0\n520 765 925.0\n520 975 1105.0\n520 1248 1352.0\n520 1302 1402.0\n520 1650 1730.0\n522 696 870.0\n522 760 922.0\n525 700 875.0\n525 864 1011.0\n525 1040 1165.0\n525 1260 1365.0\n525 1800 1875.0\n528 605 803.0\n528 630 822.0\n528 704 880.0\n528 896 1040.0\n528 990 1122.0\n528 1025 1153.0\n528 1404 1500.0\n528 1540 1628.0\n528 1900 1972.0\n530 1272 1378.0\n531 708 885.0\n531 1700 1781.0\n532 624 820.0\n532 855 1007.0\n532 1395 1493.0\n532 1824 1900.0\n533 756 925.0\n534 712 890.0\n535 1284 1391.0\n536 1005 1139.0\n537 716 895.0\n539 1140 1261.0\n539 1848 1925.0\n540 567 783.0\n540 629 829.0\n540 720 900.0\n540 819 981.0\n540 897 1047.0\n540 1155 1275.0\n540 1296 1404.0\n540 1408 1508.0\n540 1575 1665.0\n540 1989 2061.0\n543 724 905.0\n544 1020 1156.0\n544 1092 1220.0\n545 1308 1417.0\n546 728 910.0\n546 1120 1246.0\n546 1472 1570.0\n546 1872 1950.0\n549 732 915.0\n549 1820 1901.0\n550 1320 1430.0\n552 736 920.0\n552 986 1130.0\n552 1035 1173.0\n552 1539 1635.0\n552 1610 1702.0\n553 1896 1975.0\n555 572 797.0\n555 740 925.0\n555 1332 1443.0\n555 2016 2091.0\n558 744 930.0\n558 880 1042.0\n559 840 1009.0\n560 588 812.0\n560 684 884.0\n560 702 898.0\n560 900 1060.0\n560 1050 1190.0\n560 1161 1289.0\n560 1344 1456.0\n560 1518 1618.0\n560 1551 1649.0\n560 1920 2000.0\n561 748 935.0\n561 952 1105.0\n561 1240 1361.0\n561 1540 1639.0\n564 752 940.0\n564 1645 1739.0\n565 1356 1469.0\n567 756 945.0\n567 1020 1167.0\n567 1944 2025.0\n568 1065 1207.0\n570 760 950.0\n570 1008 1158.0\n570 1368 1482.0\n570 1760 1850.0\n572 1521 1625.0\n572 1815 1903.0\n573 764 955.0\n574 1632 1730.0\n574 1968 2050.0\n575 1260 1385.0\n575 1380 1495.0\n576 660 876.0\n576 768 960.0\n576 943 1105.0\n576 1080 1224.0\n576 1232 1360.0\n576 1482 1590.0\n576 1680 1776.0\n579 772 965.0\n580 609 841.0\n580 741 941.0\n580 1392 1508.0\n580 1632 1732.0\n581 1992 2075.0\n582 776 970.0\n583 1344 1465.0\n584 1095 1241.0\n585 648 873.0\n585 780 975.0\n585 928 1097.0\n585 1200 1335.0\n585 1404 1521.0\n588 784 980.0\n588 945 1113.0\n588 1309 1435.0\n588 1715 1813.0\n588 2016 2100.0\n590 1416 1534.0\n591 788 985.0\n592 1110 1258.0\n592 1305 1433.0\n594 608 850.0\n594 792 990.0\n594 1008 1170.0\n595 600 845.0\n595 924 1099.0\n595 1428 1547.0\n597 796 995.0\n600 630 870.0\n600 800 1000.0\n600 910 1090.0\n600 1045 1205.0\n600 1125 1275.0\n600 1178 1322.0\n600 1440 1560.0\n600 1750 1850.0\n600 1827 1923.0\n600 1955 2045.0\n602 1800 1898.0\n603 804 1005.0\n605 1452 1573.0\n606 808 1010.0\n608 1140 1292.0\n608 1380 1508.0\n609 812 1015.0\n609 1188 1335.0\n610 1464 1586.0\n611 1020 1189.0\n612 759 975.0\n612 816 1020.0\n612 1075 1237.0\n612 1309 1445.0\n612 1680 1788.0\n612 1785 1887.0\n615 728 953.0\n615 820 1025.0\n615 1476 1599.0\n616 663 905.0\n616 735 959.0\n616 870 1066.0\n616 990 1166.0\n616 1155 1309.0\n616 1638 1750.0\n616 1887 1985.0\n618 824 1030.0\n620 651 899.0\n620 861 1061.0\n620 1488 1612.0\n620 1872 1972.0\n621 672 915.0\n621 828 1035.0\n624 715 949.0\n624 832 1040.0\n624 918 1110.0\n624 1170 1326.0\n624 1280 1424.0\n624 1457 1585.0\n624 1820 1924.0\n624 1980 2076.0\n625 1500 1625.0\n627 836 1045.0\n627 1064 1235.0\n627 1564 1685.0\n627 1936 2035.0\n630 840 1050.0\n630 1144 1306.0\n630 1248 1398.0\n630 1512 1638.0\n630 1976 2074.0\n632 1185 1343.0\n633 844 1055.0\n635 1524 1651.0\n636 848 1060.0\n636 1855 1961.0\n637 1116 1285.0\n638 720 962.0\n639 852 1065.0\n640 672 928.0\n640 924 1124.0\n640 1200 1360.0\n640 1536 1664.0\n640 1998 2098.0\n642 856 1070.0\n644 960 1156.0\n644 1035 1219.0\n645 812 1037.0\n645 860 1075.0\n645 1548 1677.0\n648 864 1080.0\n648 1215 1377.0\n648 1386 1530.0\n648 1890 1998.0\n649 1680 1801.0\n650 720 970.0\n650 1560 1690.0\n651 868 1085.0\n651 1368 1515.0\n654 872 1090.0\n655 1572 1703.0\n656 1230 1394.0\n656 1617 1745.0\n657 876 1095.0\n660 693 957.0\n660 779 1021.0\n660 880 1100.0\n660 989 1189.0\n660 1001 1199.0\n660 1120 1300.0\n660 1377 1527.0\n660 1584 1716.0\n660 1755 1875.0\n660 1925 2035.0\n663 884 1105.0\n663 1216 1385.0\n663 1360 1513.0\n663 1820 1937.0\n664 1245 1411.0\n665 780 1025.0\n665 1176 1351.0\n665 1596 1729.0\n666 888 1110.0\n666 1288 1450.0\n669 892 1115.0\n670 1608 1742.0\n671 1800 1921.0\n672 754 1010.0\n672 770 1022.0\n672 896 1120.0\n672 1054 1250.0\n672 1080 1272.0\n672 1260 1428.0\n672 1496 1640.0\n672 1700 1828.0\n672 1729 1855.0\n672 1960 2072.0\n675 816 1059.0\n675 900 1125.0\n675 1620 1755.0\n675 1760 1885.0\n678 904 1130.0\n680 714 986.0\n680 1056 1256.0\n680 1275 1445.0\n680 1365 1525.0\n680 1632 1768.0\n681 908 1135.0\n682 840 1082.0\n684 912 1140.0\n684 975 1191.0\n684 1363 1525.0\n684 1463 1615.0\n684 1995 2109.0\n685 1644 1781.0\n687 916 1145.0\n688 1290 1462.0\n688 1785 1913.0\n689 1320 1489.0\n690 920 1150.0\n690 1512 1662.0\n690 1656 1794.0\n693 924 1155.0\n693 1176 1365.0\n693 1560 1707.0\n693 1924 2045.0\n695 1668 1807.0\n696 697 985.0\n696 928 1160.0\n696 1305 1479.0\n696 1610 1754.0\n699 932 1165.0\n700 735 1015.0\n700 855 1105.0\n700 1125 1325.0\n700 1152 1348.0\n700 1680 1820.0\n702 936 1170.0\n702 1440 1602.0\n704 840 1096.0\n704 903 1145.0\n704 1320 1496.0\n704 1872 2000.0\n705 940 1175.0\n705 992 1217.0\n705 1692 1833.0\n708 944 1180.0\n710 1704 1846.0\n711 948 1185.0\n712 1335 1513.0\n714 720 1014.0\n714 952 1190.0\n714 1960 2086.0\n715 792 1067.0\n715 1428 1597.0\n715 1716 1859.0\n717 956 1195.0\n720 756 1044.0\n720 825 1095.0\n720 960 1200.0\n720 1092 1308.0\n720 1196 1396.0\n720 1254 1446.0\n720 1350 1530.0\n720 1519 1681.0\n720 1540 1700.0\n720 1653 1803.0\n720 1728 1872.0\n720 1961 2089.0\n723 964 1205.0\n725 1740 1885.0\n726 968 1210.0\n726 1232 1430.0\n728 1071 1295.0\n728 1170 1378.0\n728 1254 1450.0\n728 1365 1547.0\n729 972 1215.0\n730 1752 1898.0\n731 780 1069.0\n732 976 1220.0\n735 980 1225.0\n735 1088 1313.0\n735 1456 1631.0\n735 1764 1911.0\n736 930 1186.0\n736 1380 1564.0\n738 984 1230.0\n738 1600 1762.0\n740 777 1073.0\n740 1269 1469.0\n740 1776 1924.0\n741 988 1235.0\n741 1520 1691.0\n741 1540 1709.0\n744 817 1105.0\n744 992 1240.0\n744 1395 1581.0\n744 1850 1994.0\n745 1788 1937.0\n747 996 1245.0\n748 1035 1277.0\n750 1000 1250.0\n750 1800 1950.0\n752 1410 1598.0\n753 1004 1255.0\n755 1812 1963.0\n756 825 1119.0\n756 1008 1260.0\n756 1215 1431.0\n756 1360 1556.0\n756 1617 1785.0\n756 1683 1845.0\n759 1012 1265.0\n759 1288 1495.0\n760 798 1102.0\n760 1344 1544.0\n760 1425 1615.0\n760 1725 1885.0\n760 1824 1976.0\n762 1016 1270.0\n765 868 1157.0\n765 1020 1275.0\n765 1188 1413.0\n765 1836 1989.0\n767 1656 1825.0\n768 880 1168.0\n768 1024 1280.0\n768 1440 1632.0\n770 1104 1346.0\n770 1848 2002.0\n771 1028 1285.0\n774 1032 1290.0\n774 1768 1930.0\n775 1860 2015.0\n776 1455 1649.0\n777 1036 1295.0\n780 819 1131.0\n780 864 1164.0\n780 1040 1300.0\n780 1183 1417.0\n780 1421 1621.0\n780 1600 1780.0\n780 1872 2028.0\n780 1953 2103.0\n783 1044 1305.0\n783 1140 1383.0\n784 1260 1484.0\n784 1470 1666.0\n785 1884 2041.0\n786 1048 1310.0\n789 1052 1315.0\n790 1896 2054.0\n792 806 1130.0\n792 945 1233.0\n792 1056 1320.0\n792 1175 1417.0\n792 1344 1560.0\n792 1485 1683.0\n792 1694 1870.0\n792 1855 2017.0\n793 1776 1945.0\n795 1060 1325.0\n795 1292 1517.0\n795 1908 2067.0\n798 936 1230.0\n798 1064 1330.0\n799 960 1249.0\n800 840 1160.0\n800 1122 1378.0\n800 1155 1405.0\n800 1500 1700.0\n800 1920 2080.0\n801 1068 1335.0\n804 1072 1340.0\n805 1200 1445.0\n805 1764 1939.0\n805 1932 2093.0\n807 1076 1345.0\n808 1515 1717.0\n810 1080 1350.0\n810 1944 2106.0\n812 1305 1537.0\n812 1584 1780.0\n813 1084 1355.0\n814 1248 1490.0\n816 935 1241.0\n816 1012 1300.0\n816 1088 1360.0\n816 1530 1734.0\n816 1638 1830.0\n819 1092 1365.0\n819 1680 1869.0\n819 1900 2069.0\n820 861 1189.0\n820 1581 1781.0\n822 1096 1370.0\n824 1545 1751.0\n825 1100 1375.0\n825 1400 1625.0\n828 896 1220.0\n828 1104 1380.0\n828 1479 1695.0\n828 1771 1955.0\n831 1108 1385.0\n832 855 1193.0\n832 1224 1480.0\n832 1560 1768.0\n833 840 1183.0\n833 1056 1345.0\n834 1112 1390.0\n836 1323 1565.0\n837 1116 1395.0\n837 1320 1563.0\n840 882 1218.0\n840 1026 1326.0\n840 1053 1347.0\n840 1081 1369.0\n840 1120 1400.0\n840 1274 1526.0\n840 1350 1590.0\n840 1463 1687.0\n840 1575 1785.0\n840 1664 1864.0\n840 1702 1898.0\n840 1870 2050.0\n843 1124 1405.0\n845 936 1261.0\n846 1128 1410.0\n848 1590 1802.0\n849 1132 1415.0\n850 1320 1570.0\n852 1136 1420.0\n855 1140 1425.0\n855 1512 1737.0\n856 1605 1819.0\n858 920 1258.0\n858 1144 1430.0\n858 1400 1642.0\n858 1456 1690.0\n858 1760 1958.0\n860 903 1247.0\n860 1749 1949.0\n861 1148 1435.0\n864 990 1314.0\n864 1152 1440.0\n864 1330 1586.0\n864 1620 1836.0\n864 1848 2040.0\n867 1156 1445.0\n868 1395 1643.0\n868 1824 2020.0\n870 1160 1450.0\n872 1635 1853.0\n873 1164 1455.0\n875 1440 1685.0\n876 1168 1460.0\n879 1172 1465.0\n880 924 1276.0\n880 1050 1370.0\n880 1479 1721.0\n880 1650 1870.0\n880 1836 2036.0\n882 1176 1470.0\n884 987 1325.0\n885 1180 1475.0\n885 1628 1853.0\n888 1184 1480.0\n888 1225 1513.0\n888 1665 1887.0\n891 912 1275.0\n891 1188 1485.0\n891 1512 1755.0\n893 924 1285.0\n894 1192 1490.0\n896 1440 1696.0\n896 1680 1904.0\n897 1196 1495.0\n897 1840 2047.0\n900 945 1305.0\n900 1088 1412.0\n900 1200 1500.0\n900 1365 1635.0\n900 1495 1745.0\n900 1767 1983.0\n901 1260 1549.0\n902 1560 1802.0\n903 1204 1505.0\n904 1695 1921.0\n906 1208 1510.0\n909 1212 1515.0\n910 1008 1358.0\n910 1056 1394.0\n912 1045 1387.0\n912 1216 1520.0\n912 1300 1588.0\n912 1710 1938.0\n915 1220 1525.0\n915 1748 1973.0\n918 1224 1530.0\n920 966 1334.0\n920 1725 1955.0\n921 1228 1535.0\n924 1232 1540.0\n924 1305 1599.0\n924 1485 1749.0\n924 1568 1820.0\n924 1643 1885.0\n927 1236 1545.0\n928 1554 1810.0\n928 1740 1972.0\n930 1240 1550.0\n931 1020 1381.0\n931 1092 1435.0\n933 1244 1555.0\n935 1368 1657.0\n935 1452 1727.0\n936 1127 1465.0\n936 1190 1514.0\n936 1248 1560.0\n936 1377 1665.0\n936 1755 1989.0\n939 1252 1565.0\n940 987 1363.0\n942 1256 1570.0\n944 1770 2006.0\n945 1260 1575.0\n945 1700 1945.0\n945 1716 1959.0\n945 1872 2097.0\n946 1728 1970.0\n948 1264 1580.0\n950 1680 1930.0\n951 1268 1585.0\n952 960 1352.0\n952 1530 1802.0\n952 1785 2023.0\n954 1272 1590.0\n957 1080 1443.0\n957 1276 1595.0\n957 1624 1885.0\n960 1008 1392.0\n960 1100 1460.0\n960 1280 1600.0\n960 1386 1686.0\n960 1456 1744.0\n960 1672 1928.0\n960 1800 2040.0\n962 1200 1538.0\n963 1284 1605.0\n966 1288 1610.0\n966 1440 1734.0\n968 1155 1507.0\n968 1815 2057.0\n969 1120 1481.0\n969 1292 1615.0\n969 1480 1769.0\n972 1296 1620.0\n975 1080 1455.0\n975 1300 1625.0\n976 1830 2074.0\n978 1304 1630.0\n980 1029 1421.0\n980 1197 1547.0\n980 1575 1855.0\n981 1308 1635.0\n984 1312 1640.0\n984 1537 1825.0\n984 1845 2091.0\n987 1316 1645.0\n988 1275 1613.0\n990 1320 1650.0\n990 1680 1950.0\n992 1794 2050.0\n992 1860 2108.0\n993 1324 1655.0\n996 1328 1660.0\n999 1332 1665.0\n1000 1050 1450.0\n1002 1336 1670.0\n1003 1596 1885.0\n1005 1340 1675.0\n1007 1224 1585.0\n1008 1100 1492.0\n1008 1131 1515.0\n1008 1155 1533.0\n1008 1344 1680.0\n1008 1406 1730.0\n1008 1581 1875.0\n1008 1620 1908.0\n1011 1348 1685.0\n1014 1352 1690.0\n1017 1356 1695.0\n1020 1071 1479.0\n1020 1265 1625.0\n1020 1360 1700.0\n1020 1547 1853.0\n1020 1584 1884.0\n1023 1260 1623.0\n1023 1364 1705.0\n1023 1736 2015.0\n1026 1368 1710.0\n1029 1372 1715.0\n1032 1376 1720.0\n1032 1705 1993.0\n1035 1120 1525.0\n1035 1380 1725.0\n1036 1173 1565.0\n1036 1665 1961.0\n1037 1716 2005.0\n1038 1384 1730.0\n1040 1092 1508.0\n1040 1152 1552.0\n1040 1431 1769.0\n1040 1530 1850.0\n1041 1388 1735.0\n1044 1392 1740.0\n1044 1520 1844.0\n1045 1332 1693.0\n1047 1396 1745.0\n1050 1400 1750.0\n1050 1728 2022.0\n1053 1404 1755.0\n1056 1210 1606.0\n1056 1260 1644.0\n1056 1408 1760.0\n1056 1792 2080.0\n1059 1412 1765.0\n1060 1113 1537.0\n1062 1416 1770.0\n1064 1248 1640.0\n1064 1710 2014.0\n1065 1420 1775.0\n1066 1512 1850.0\n1068 1424 1780.0\n1071 1080 1521.0\n1071 1428 1785.0\n1074 1432 1790.0\n1077 1436 1795.0\n1080 1134 1566.0\n1080 1258 1658.0\n1080 1440 1800.0\n1080 1638 1962.0\n1080 1794 2094.0\n1083 1444 1805.0\n1086 1448 1810.0\n1089 1452 1815.0\n1092 1325 1717.0\n1092 1456 1820.0\n1092 1595 1933.0\n1092 1755 2067.0\n1095 1460 1825.0\n1098 1464 1830.0\n1100 1155 1595.0\n1101 1468 1835.0\n1104 1265 1679.0\n1104 1395 1779.0\n1104 1472 1840.0\n1105 1224 1649.0\n1105 1716 2041.0\n1107 1476 1845.0\n1110 1144 1594.0\n1110 1480 1850.0\n1113 1184 1625.0\n1113 1484 1855.0\n1116 1488 1860.0\n1116 1760 2084.0\n1118 1680 2018.0\n1119 1492 1865.0\n1120 1176 1624.0\n1120 1368 1768.0\n1120 1404 1796.0\n1120 1617 1967.0\n1121 1560 1921.0\n1122 1496 1870.0\n1125 1360 1765.0\n1125 1500 1875.0\n1127 1680 2023.0\n1128 1504 1880.0\n1131 1508 1885.0\n1134 1512 1890.0\n1137 1516 1895.0\n1140 1197 1653.0\n1140 1219 1669.0\n1140 1520 1900.0\n1140 1625 1985.0\n1140 1729 2071.0\n1143 1524 1905.0\n1144 1365 1781.0\n1144 1683 2035.0\n1144 1767 2105.0\n1146 1528 1910.0\n1148 1485 1877.0\n1149 1532 1915.0\n1152 1320 1752.0\n1152 1536 1920.0\n1155 1292 1733.0\n1155 1540 1925.0\n1155 1656 2019.0\n1158 1544 1930.0\n1159 1680 2041.0\n1160 1218 1682.0\n1160 1482 1882.0\n1161 1548 1935.0\n1164 1552 1940.0\n1167 1556 1945.0\n1170 1296 1746.0\n1170 1560 1950.0\n1173 1564 1955.0\n1176 1568 1960.0\n1179 1572 1965.0\n1180 1239 1711.0\n1182 1576 1970.0\n1185 1580 1975.0\n1188 1209 1695.0\n1188 1216 1700.0\n1188 1584 1980.0\n1190 1200 1690.0\n1191 1588 1985.0\n1194 1592 1990.0\n1197 1404 1845.0\n1197 1596 1995.0\n1200 1260 1740.0\n1200 1375 1825.0\n1200 1600 2000.0\n1200 1683 2067.0\n1203 1604 2005.0\n1204 1653 2045.0\n1206 1608 2010.0\n1209 1612 2015.0\n1212 1616 2020.0\n1215 1620 2025.0\n1218 1624 2030.0\n1220 1281 1769.0\n1221 1628 2035.0\n1224 1518 1950.0\n1224 1632 2040.0\n1227 1636 2045.0\n1230 1456 1906.0\n1230 1640 2050.0\n1232 1326 1810.0\n1232 1470 1918.0\n1233 1644 2055.0\n1235 1368 1843.0\n1236 1648 2060.0\n1239 1520 1961.0\n1239 1652 2065.0\n1240 1302 1798.0\n1242 1344 1830.0\n1242 1656 2070.0\n1245 1660 2075.0\n1248 1265 1777.0\n1248 1430 1898.0\n1248 1664 2080.0\n1251 1668 2085.0\n1254 1672 2090.0\n1257 1676 2095.0\n1260 1323 1827.0\n1260 1375 1865.0\n1260 1539 1989.0\n1260 1680 2100.0\n1263 1684 2105.0\n1266 1688 2110.0\n1276 1440 1924.0\n1280 1344 1856.0\n1281 1640 2081.0\n1287 1380 1887.0\n1290 1624 2074.0\n1296 1485 1971.0\n1300 1365 1885.0\n1300 1440 1940.0\n1309 1320 1859.0\n1311 1360 1889.0\n1312 1425 1937.0\n1320 1386 1914.0\n1320 1558 2042.0\n1320 1575 2055.0\n1330 1560 2050.0\n1340 1407 1943.0\n1344 1508 2020.0\n1344 1540 2044.0\n1357 1476 2005.0\n1360 1428 1972.0\n1365 1512 2037.0\n1365 1584 2091.0\n1376 1593 2105.0\n1380 1449 2001.0\n1392 1394 1970.0\n1400 1470 2030.0\n1420 1491 2059.0\n1428 1440 2028.0\n1428 1475 2053.0\n1440 1512 2088.0"
        self.assertEqual(wynik, oczekiwany_wynik)
