x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))

operacja = input("Wybierz operację arytmetyczną (+, -, *, /, **, %): ")


if operacja == "+":
    wynik = x + y
elif operacja == "-":
    wynik = x - y
elif operacja == "*":
    wynik = x * y
elif operacja == "/":
    wynik = x / y
elif operacja == "**":
    wynik = x ** y
elif operacja == "%":
    wynik = x % y
else:
    wynik = "Nieprawidłowa operacja"

print(x, operacja, y, "=", wynik)