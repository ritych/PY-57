def main():
    numbers = []
    i = 0
    summa = 0
    num = int(input("Введите число. (Для окончания ввода и подсчета среднего введите 0) "))
    while num != 0:
        numbers.append(num)
        i += 1
        summa += num
        print('Группа чисел', numbers)
        num = int(input("Введите число. (Для окончания ввода и подсчета среднего введите 0) "))

    try:
        average = summa / i
        print(f"Среднее значение: {average}")
    except:
        print('Вы не ввели ни одного числа')


if __name__ == "__main__":
    main()
