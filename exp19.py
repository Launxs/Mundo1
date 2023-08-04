#bissexto
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False  
        else:
            return True  
    else:
        return False  
ano = int(input("Digite um ano: "))
if is_leap_year(ano):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

#outra forma

from calendar import isleap

ano = int(input('Digite o ano: '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')