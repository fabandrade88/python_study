valor = int(input('escreva o valor desejado: '))

while True:
  if valor >= 100:
    cont100 = valor // 100
    valor = valor - cont100 * 100
    print (f'cedulas de 100: {cont100}')
    print(valor)
    if not valor:
      break

  if valor >= 50:
    cont50 = valor // 50
    valor = valor - cont50 * 50
    print (f'cedulas de 50: {cont50}')
    print(valor)
    if not valor:
      break

  if valor >= 2:
    cont20 = valor // 20
    valor = valor - cont20 * 20
    print (f'cedulas de 20: {cont20}')
    print(valor)
    if not valor:
      break

  if valor >= 10:
    cont10 = valor // 10
    valor = valor - cont10 * 10
    print (f'cedulas de 10: {cont10}')
    print(valor)
    if not valor:
      break

  if valor >= 5:
    cont5 = valor // 5
    valor = valor - cont5 * 5
    print (f'cedulas de 5: {cont5}')
    print(valor)
    if not valor:
      break

  if valor:
    cont1 = valor
    print(f'celudas de 1: {cont1}')
    break