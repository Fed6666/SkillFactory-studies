spisok = '6 1 3 8 9 2 7 22 18 14 26 30 '
at = [int(x) for x in spisok.split()]

try:
    user = int(input("Введите целое число от 1 до 29: "))
    if user % 1 == 0:
        at.append(user)
        print("Список до сортировки: ", at)
        at.sort()
        print("Список после сортировки по возрастанию: ", at)
    else:
        print("введите корректное число")
except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")

def binary_search(at, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if at[middle] == user:
            return middle
        elif user < at[middle]:
            return binary_search(at, user, left, middle - 1)
        else:
            return binary_search(at, user, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


print("Индекс введенного числа в списке: ", binary_search(at, user, 0, -1))