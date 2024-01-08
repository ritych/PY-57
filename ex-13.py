def main():
    for i in range(1, 6):
        print(f"Факториал числа {i} = {fact(i)}")


def fact(i):
    factorial = 1
    count = 1
    while count <= i:
        factorial *= count
        count += 1
    return factorial


if __name__ == "__main__":
    main()
