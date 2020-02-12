#Павлюк Владислав
#Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
#цієї ж суми в гривнях.
from enum import Enum
while True:
    while True:
        try:
            class converter (Enum):
               USD = 1
               EUR = 2
               CZK = 3
               PLN = 4
            x = float (input ( 'amount of money:'))
            p = converter (int (input ("Введите номер валюты")))
            break
        except ValueError:
            print('Введите число')
    if p==converter.USD:
       print(x*26)
    elif p==converter.EUR:
       print(x*28)
    elif p==converter.CZK:
       print(x*1.08)
    elif p==converter.PLN:
       print(x*6)
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
