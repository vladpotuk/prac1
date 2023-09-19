a = int(input("Діаметр кола: "))

operation = input("Введіть  'plosha' або 'perimetr':")

if operation == 'plosha':
    result = 3.14*(a/2)*(a/2)
    print("Площа дорівнює:", result)
elif operation == 'perimetr':
    result = 3.14*a
    print("Періметр дорівнює:", result)



