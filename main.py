import sys 
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def dodaj(x, y): return x+y
def odejmij(x, y): return x-y
def pomnoz(x, y): return x*y
def podziel(x, y): return x/y
def czy_liczba(s):
    try:
        float(s)
        pass
    except ValueError:
        print("Podany składnik nie jest liczbą!")
        return sys.exit()

choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

num1 = input("Podaj składnik pierwszy: ")
czy_liczba(num1)

num2 = input("Podaj składnik drugi: ")
czy_liczba(num2)

if choice == '1': logging.info("Dodaję %s i %s" % (num1, num2)), print("Wynik to", dodaj(num1, num2)),
elif choice == '2': logging.info("Odejmuję %s i %s" % (num1, num2)), print("Wynik to",  odejmij(num1, num2))
elif choice == '3': logging.info("Mnożę %s i %s" % (num1, num2)), print("Wynik to", pomnoz(num1, num2))
elif choice == '4': logging.info("Dzielę %s i %s" % (num1, num2)), print("Wynik to", podziel(num1, num2))
