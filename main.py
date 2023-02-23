
course = "  Python Programming  "
print(course.upper()) # upper robi cpslock ze wszystkiego
print(course.lower()) # wszystko z małej
print(course.title()) # robi pierwsze litery z duzą litera
print(course.lstrip()) # usuwa spacje
print(course.find("Pro")) # znajduje na ktorej pozycji jest
print(course.replace("P", "j")) # zamienia literke p na j
print("Pro" in course) # czy wystepuje w zdaniu Pro
print("Swift" not in course) # czy nie znajduje sie swift w zdaniu

print(10/3)    #dzieli
print(10//3)  # dzieli i obcina wszystko po przecinku
print(10 % 3) # ile wynosi reszta z dzielenia
print(10 ** 3) # robi do potegi

import math  # importujesz matme do pythona( jest to specjalna biblioteka)

print(round(2.9)) # zaookragla
print(abs(-2.9)) # wartosc bezwzgledna

print(math.ceil(2.2)) # zaogragla do gory
print(math.floor(2.9)) # zoogragla w dol

print("bag" > "apple")  # pierwsza litera "b" jest na 2 pozycji "a" a na 1 2>1 true

print(ord("d")) # jaka wartosc ma dana litera
print(ord("B"))


zmienna = 120
if zmienna :
    print("gonwo")
elif zmienna == 130:    # inaczej else if
    print("kakaka")
else:
    print("cos innego");


wiek = int(input("podaj wiek: "))
if wiek >= 18:
    print("ulala legalne")
else:
    print("sory nielegalne")

for zmienna in range(3):
    print(zmienna)