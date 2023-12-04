#print jest funkcją
print("Witaj")

#definiowanie własnej funkcji
def funkcja_test():
    print("Funkcja... ")
#wywołanie funkcji
funkcja_test()

#deklaracja funkcji z argumentem
def dodaj(x):
    print(x + 1)

dodaj(5)

def dodaj(x, y):
    print(x + y)

dodaj(4, 7)

#nie działa funkcja, która została przeciążona. Ona nie jest przeciązona tylko nadpisana...
# dodaj(3)

#prawidłowe dokonanie przeciążenia
def dodaj(x, y = 1):
    print(x + y)

dodaj(2, 3)
dodaj(2) #tu domyślnie jest pod y = 1 więc wynikiem będzie 3
print("---")


#funkcja z return
def dodaj(x, y = 1, z = 0):
    return x + y + z

# po stworzeniu funkcji z return, aby ją wyświetlić trzeba zrobić np jak poniżej
print(dodaj(5, 3, 2))
suma = dodaj(5, 3, 2)
print(suma)

#Przeskoczenie drugiego argumentu
print(dodaj(2, z = 5))

# #można zwracać wiele wartości
def fn(a, b):
    return a + b, a - b, a * b
#zwracana jest krotka
print(fn(3,4))
print(fn(3,4)[1])