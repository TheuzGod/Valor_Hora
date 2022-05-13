print('''Digite o "Salário Mensal" em Real e Centavos 
Por exemplo: 1000.00''')

sm = float(input('Salário Mensal: '))

print('''Digite o "Horas Trabalho por mês" em número inteiro 
por exemplo: 300''')

ht = int(input('Horas Trabalho por mês: '))

vh = sm / ht

print('Seu Valor Hora é {:.2f}'.format(vh))
