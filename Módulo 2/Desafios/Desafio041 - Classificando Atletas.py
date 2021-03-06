print('='*100)
print('''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
→ Até 9 anos: MIRIM
→ Até 14 anos: INFANTIL
→ Até 19 anos: JÚNIOR
→ Até 20 anos: SÊNIOR
→ Acima: MASTER ''')
print('='*100)

#Resolução

#Importando datetime
from datetime import date

#Capturando a entrada do usuário e calculando sua idade
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print(f'Você tem {idade} anos.')

#Informando a categoria
if idade <= 9:
    print('Sua categoria é a MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é a INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é a JÚNIOR')
elif idade > 19 and idade <= 20:
    print('Sua categoria é a SÊNIOR')
else:
    print('Sua categoria é a MASTER')