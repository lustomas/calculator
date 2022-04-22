import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def dodaj(x, y): return x+y
def odejmij(x, y): return x-y
def pomnoz(x, y): return x*y
def podziel(x, y): return x/y

choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

num1 = float(input("Podaj składnik pierwszy: "))

num2 = float(input("Podaj składnik drugi: "))

if choice == '1': logging.info(f"Dodaję {num1} i {num2}"), print("Wynik to", dodaj(num1,num2)),
elif choice == '2': logging.info(f"Odejmuję  {num1} i {num2}"), print("Wynik to", odejmij(num1, num2))
elif choice == '3': logging.info(f"Mnożę {num1} i {num2}"), print("Wynik to", pomnoz(num1, num2))
elif choice == '4': logging.info(f"Dzielę {num1} i {num2}"), print("Wynik to", podziel(num1, num2))
