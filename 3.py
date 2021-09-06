#Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

number = int(input("Enter your number"))
while number >14:
  if number % 10 == 0:
    print(number,'процентов')
  elif number % 10 == 1:
    print (number,'процент')
  elif number % 10 < 5:
    print(number,'процента')
  else:
    print(number,'процентов')
  break

else:
    if number % 10 == 0:
        print(number, 'процентов')
    elif number % 100 == 11:
        print(number,"процентов")
    elif number % 10 == 1:
        print(number, 'процент')
    elif number % 10 < 5:
        print(number, 'процента')
    else:
        print(number, 'процентов')
