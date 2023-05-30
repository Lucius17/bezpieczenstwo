def szyfrowanie_znaku(char,key):
    # chr zwracana nam znak kiedy podamy mu jego numer w tablicy znaków ASCII
	# ord zwraca nam numer w tablicy ASCII podanego znaku
	# w tablicy ASCII a to 97 znak ponieważ ta tablica zwiera nie tylko litery, ale też inne znaki używane do interfejsów
	# dlatego cofamy numer znaku o długość alfabetu i przesuwamy o wartość naszego klucza
	# na koniec wiedząc, że alfabet (bez polskich znaków) ma 26 liter liczymy resztę z dzielenia oraz przesuwamy znowu do początku alfabetu i otrzymujemy zaszyfrowany znak
    return chr((ord(char)-97+key) %26+97)


def	szyfrowanie(text,key):
    temp = "" #tworzymy musty string jako zmienna pomocnicza
	#text to tablica znaków więc odliczamy od początku naszego tekstu
    for char in text:
        # do naszej zmiennej pomocniczej dodajemy zaszyfrowany znak
        temp += szyfrowanie_znaku(char,key)
    return temp #po zaszyfrowaniu wszystkich znaków zwracamy naszą zaszyfrowaną wiadomość


def	deszyfrowanie(text,key):
    return szyfrowanie(text, 26-key) #wiedząc, że alfabet ma 26 liter wystarczy, że podczas odszyfrowywania przesuniemy nasz klucz o 26 liter minus klucz wtedy otrzymamy odszyfrowaną wiadomość

menu = ["wyjdź z programu","szyfrowanie","odszyfrowywanie"]

def main():
    for index,option in enumerate(menu):
        print(f'{index}. {option}')
        
    user = input("wybierz opcję: ")
    if (user == "0"):
        quit()
    if ((user == "1") or (user == "2")):
        text = input("podaj tekst ")
        key = input("podaj klucz ")
        if (key.isdigit()):
            key=int(key)
        else:
            print("klucz musi być liczbą, spróbuj ponownie")
            main()
        if(user == "1"):
            print(szyfrowanie(text,key))
        else:
            print(deszyfrowanie(text,key))
    else:
        print("nie ma takiej opcji")
        main()
        

if (__name__ == "__main__"):
    while True:
        main()
            

    