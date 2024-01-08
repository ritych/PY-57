def main():
    prime_numbers = []
    for num in range(2, 51):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
    print("Простые числа от 2 до 50:", prime_numbers)


if __name__ == "__main__":
    main()
