import math
result = None



def get_numbers():
    num_list = []
    while True:
        num = float(input("Wprowadz cyfre (Napisz 0 aby zakonczyc): "))
        if num == 0:
            zapytanie_o_zapis = input("czy chcesz zapisać wynik? (y/n): ")
            if zapytanie_o_zapis == "y":
                get_result()
                filename = input("Wprowadz nazwe pliku w którym mają być zapisywane wyniki (np. wyniki.txt): ")
                with open(filename, "w") as file:
                    file.write(str(result))
                    print("Wynik został zapisany w pliku: ", filename)
                    break
            else:
                break
        num_list.append(num)
    return num_list


def get_result():
    global result
    return result


def main():
    while True:
        print("\nMenu:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Modulo")
        print("6. Pierwiastek")
        print("7. Silnia")
        print("8. Zapamiętanie wyniku")
        print("9. Wyjście z programu")

        choice = int(input("\nWybierz opcję: "))

        if choice == 1:
            print("\nDodawanie:")
            num_list = get_numbers()
            result = sum(num_list)
            print(f"Wynik: {result}")
        elif choice == 2:
            print("\nOdejmowanie:")
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
            result = num1 - num2
            print(f"Wynik: {result}")
        elif choice == 3:
            print("\nMnożenie:")
            num_list = get_numbers()
            result = 1
            for num in num_list:
                result *= num
            print(f"Wynik: {result}")
        elif choice == 4:
            print("\nDzielenie:")
            num1 = float(input("Podaj dzielną: "))
            num2 = float(input("Podaj dzielnik: "))
            if num2 == 0:
                print("Dzielenie przez 0 jest niedozwolone.")
                continue
            result = num1 / num2
            print(f"Wynik: {result}")
        elif choice == 5:
            print("\nModulo:")
            num1 = int(input("Podaj liczbę: "))
            num2 = int(input("Podaj modulo: "))
            if num2 <= 0:
                print("Modulo musi być liczbą dodatnią i całkowitą.")
                continue
            result = num1 % num2
            print(f"Wynik: {result}")
        elif choice == 6:
            print("\nPierwiastek:")
            num = float(input("Podaj liczbę: "))
            if num < 0:
                print("Nie można wyznaczać pierwiastka z liczby ujemnej.")
                continue
            result = math.sqrt(num)

            print(f"Wynik: {result}")
        elif choice == 7:
            wynik = 1
            liczba = int(input("Wprowadź dodatnią liczbę całkowitą, aby znaleźć jej silnię: "))
            if liczba >= 0:
                for i in range(1, liczba + 1):
                    wynik = wynik * i
                print("Silnia z liczby", liczba, "wynosi", wynik)
            else:
                print("Wprowadź dodatnią liczbę całkowitą.")
        elif choice == 8:
            result = get_result()
            filename = input("Wprowadz nazwe pliku w którym mają być zapisywane wyniki (np. wyniki.txt): ")
            with open(filename, "w") as file:
                file.write(str(result))
                print("Wynik został zapisany w pliku: ", filename)
        elif choice == 9:
            break


main()
