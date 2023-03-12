a = int(input())
b = int(input())

if a == 0 or b == 0:
    print(0)
else:
    mon = 1
    n = 1
    k = 1

    while a != 0 and b != 0: #Сравниваем текущие элементы и в зависимости от результата увеличиваем либо n, либо k
        if a < b:
            k += 1 
        elif a > b:
            n += 1
        else:
            n = k = 1

        if k > mon: #Проверяем, не превышает ли k или n максимальную длину монотонного фрагмента n_max
            mon = k
        elif n > mon:
            mon = n

        a = b
        b = int(input())

    print(mon) #Выводим максимальную длину монотонного фрагмента
