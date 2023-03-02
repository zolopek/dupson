succesful = True
for number in range(3):    # robisz zeby ci petle 3 razy napisal
    print("attempt")
    if succesful:
        print("succesfuLL")
        break                # przerwya petle
else:
    print("Attempt 4 times and failed ")


for x in range(5):
    for y in range(3):

        print(f"( {x}, {y})")       # wypisuje wyszystkie kombinacje


#for x in [1, 2, 3, 4]:    # wypisuje liczby po kolei
   # print(x)


y = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        y = y + 1



def dodowanie(x, y):
    print(x+y)

dodowanie(2, 3)

def dodowanie2(x, y, z = 0):
    print(x+y+z)

dodawanie2(2, 3 , 5)
dodawanie2(5, 6)
dodowanie2(9, 5)


