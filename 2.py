total = 0
i = 0
while True:
    i += 1
    if i >= 1000:
        break
    if i % 2 == 0:
        continue
    number = i ** 3
    cube = i ** 3
    sum = 0
    while number != 0:
        sum = sum + number % 10  # здесь суммируется остаток: напр., 1234 : сначала 4 + 3 + 2 + 1, за счет того, что в конце цикла число меняется: 1234, 123, 12, 1, а при 0 цикл прекращается по условию выше
        number = number // 10  # вот за счет этого число меняется


    if sum % 7 != 0:
        pass
    else:
        print(sum) #для проверки логики
        total = total + cube
print(total)
