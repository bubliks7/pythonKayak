
TRASY = {
    "1": 7,
    "2": 10,
    "3": 16,
    "4": 22,
    "5": 7,
    "6": 15
}

class Trasy:
    def wybor_trasy(self):
        while True:
            print("\n Wybierz trasę którą chcesz przepłynąć")
            print("\n 1. Babice - Krzywcza (7km)")
            print("\n 2. Bachów - Krzywcza (10km)")
            print("\n 3. Iskań - Krzywcza (16km)")
            print("\n 4. Wybrzeże - Krzywcza (22km)")
            print("\n 5. Krzywcza - Reczpol (7km)")
            print("\n 6. Krzywcza - Krasiczyn (15km)")
            
            num_trasy = input('Wybierz numer trasy którą chcesz popłynąć: ')
                
            if num_trasy in TRASY:
                odleglosc = TRASY[num_trasy]
                self.jakiKajak(odleglosc)
                break
            else:
                print('Podaj liczbę od 1 do 6!!!!!!!!!')

    def jakiKajak(self, odleglosc):
        print('\nDostępne kajaki: \n - jednoosobowe \n - dwuosobowe')
        kajak = input('\nJeśli wybierasz kajak jednoosobowy wpisz 1, a jeśli dwuosobowy wpisz 2: ')

        if kajak == "1":
            pierwszy_obiekt = KajakiJednoosobowe(odleglosc=odleglosc)
            pierwszy_obiekt.pokaz()
            przekieruj = input('Wpisz 2 jeśli chcesz zobaczyć też dwuosobowe kajaki: ')
            if przekieruj == "2":
                drugi_obiekt = KajakiDwuosobowe(odleglosc=odleglosc)
                drugi_obiekt.pokaz()
        elif kajak == "2":
            drugi_obiekt = KajakiDwuosobowe(odleglosc=odleglosc)
            drugi_obiekt.pokaz()
            przekieruj = input('Wpisz 1 jeśli chcesz zobaczyć też jednoosobowe kajaki: ')
            if przekieruj == "1":
                pierwszy_obiekt = KajakiJednoosobowe(odleglosc=odleglosc)
                pierwszy_obiekt.pokaz()
        else:
            print('Musisz wybrać 1 albo 2!!')


class KajakiJednoosobowe:
    def __init__(self, odleglosc):
        self.odleglosc = odleglosc
        self.koszt_wycieczki = self.odleglosc * 7

    def pokaz(self):
        print(f'\nDługość trasy: {self.odleglosc} km')
        print("ZA KAJAKI JEDNOOSOBOWE!")
        print(f'Koszt trasy: {self.koszt_wycieczki} zł')


class KajakiDwuosobowe:
    def __init__(self, odleglosc):
        self.odleglosc = odleglosc
        self.koszt_wycieczki = self.odleglosc * 10

    def pokaz(self):
        print(f'\nDługość trasy: {self.odleglosc} km')
        print("ZA KAJAKI DWUOSOBOWE!")
        print(f'Koszt trasy: {self.koszt_wycieczki} zł')

Trasy().wybor_trasy()
