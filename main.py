#print() pisze po ekranie

#input() czeka na odpowiedz uzytkownika

x = "dududupson"
zmienna = "jakis ciag znakow"
print(len(x))   # liczy znaki w stringu i je wypluwa
print(x[0])   # pisze znak ze stringa na pozycji 0 (czyli s)
print(x[1:5])   # to samo co na gorze ale od 1 do 5 pozycji
print(x[2:]) # leci od 2 do końca
print(x[:5]) # od poczatku do 5
print(x[:])   # dziala tak samo jak print(x)
print(x[::2])  # co drugi element

# [x:y:z]
# x - poczatek
# y - koniec
# z - krok (co jeden albo dwa albo wiencej)

x = "konrad"
y = "dupson"
# print(x * 5, y, end="\n") #end na koncu robi wszytsko w jednej linijce
#print(x * 5, y, end="---")   # ctrl + d kopiowanie linijki (czacha wybucha)
#print(x * 5, y, end="---")   # ctrl + d kopiowanie linijki (czacha wybucha)

print(f"Witaj {x} jdsfjfsj sfjkf")   # f pozwala na ulatwienie i nie dodawanie plusow glupich

x = input("podaj swoj wiek")   # jak masz zdanie nie w cudzyslowie zaznacz je i kliknij cudzyslow samo sie zrobi
print(int(x)+2)

james_bond = 7
# nasz cel to 007
print(str(james_bond).zfill(3)) # wypelnia zerami



