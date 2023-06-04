#lista znaków naszych lister jakich chcemy użyć
alfabet = '''aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ0123456789,.?;:"[]{}|!@#$%^&*()_-=+'''

litery = list(alfabet)

def szyfrowanie_znaku(char,key):
    # jeśli litera nie będzie w naszym alfabecie zwrócimy ją taką jaka jest, co sprawi, że nie będzie można jej później odszyfrować

    if  char not in litery:
        return char
    i = litery.index(char) #przypisujemy index naszej litery do zmiennej
    
	#zwracamy znak przesunięty o wartość naszego klucza oraz liczymy resztę z dzielenia aby nie wyjść poza limit naszego alfabetu
    return litery[(i+key)% len(litery)]
    
		
    



def	szyfrowanie(text,key):
    temp = "" #tworzymy musty string jako zmienna pomocnicza
	#text to tablica znaków więc odliczamy od początku naszego tekstu
    for char in text:
        # do naszej zmiennej pomocniczej dodajemy zaszyfrowany znak
        temp += szyfrowanie_znaku(char,key)
    return temp #po zaszyfrowaniu wszystkich znaków zwracamy naszą zaszyfrowaną wiadomość


def	deszyfrowanie(text,key):
    return szyfrowanie(text, len(litery)-key) #robimy to samo co wcześniej tylko z inną długością naszego alfabetu


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