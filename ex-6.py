def main():
    spisok = [1, 2, 3, 'string', [2, 3, 2], 'other string']
    for element in spisok:
        print(element)

    slovar = {
        'name': 'John',
        'soname': 'Smith',
        'age': '33',
        'weight': '80',
        'height': '175',
    }
    print()
    for element in slovar:
        print(element, slovar[element])


if __name__ == "__main__":
    main()
