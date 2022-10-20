#Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała
litera = input("podaj litere:" )
 if litera >= 'a' and <= 'z':
     print("litera jest mała")
elif litera >='A' and <= 'Z':
    print("litera jest duża")
else :
     print("to nie jest litera")
