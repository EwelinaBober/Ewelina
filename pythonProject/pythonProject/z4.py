litera = input("podaj literę:" )
roznica = ord('a')- ord('A')

if 'a' <= litera <= 'z' :
    print(char(ord(litera)- roznica))

elif 'A' <= litera <= 'Z':
    nowa = ord(litera)+ roznica
    znak = chr(nowa)
    print(znak)
else :
    print("to nie jest litera")

''' Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości) i wypisuje
ją na ekranie
rekord(znak)- zwraca ascii'''