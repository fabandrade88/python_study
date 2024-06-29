qty = int(input('qual quantidade de kWn foi consumido: '))

print('tipos de instalacao: ')
print('R - Residencia')
print('I - Industrias')
print('C - Comercio')

tipo_instalacao = input('digite a letra que representa a instalacao: ')

if(( tipo_instalacao == 'R') <= 500):
  valor_final1 = qty * 0.40
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
elif (( tipo_instalacao == 'R') > 500):
  valor_final1 = qty * 0.65
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
elif(( tipo_instalacao == 'I') <= 1000):
  valor_final1 = qty * 0.55
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
elif(( tipo_instalacao == 'I') > 1000):
  valor_final1 = qty * 0.60
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
elif(( tipo_instalacao == 'C') <= 5000):
  valor_final1 = qty * 0.55
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
elif(( tipo_instalacao == 'C') > 5000):
  valor_final1 = qty * 0.60
  print('Voce consumiu {} kWh e vai ter que pagar {}'. format(qty,valor_final1))
else:
  print('escolha uma opcao disponivel na lista')