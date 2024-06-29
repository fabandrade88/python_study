pergunta = int(input('coloque primeiro valor: '))
pergunta2 = int(input('coloque segundo valor: '))

print('qual conta quer fazer')
print('1 = soma')
print('2 = subtracao')
print('3 = multiplicacao')
print('4 = divisao')

conta = int(input('digite o numero correspondente da lista a cima: '))

if (conta == 1):
  print(pergunta + pergunta2)
elif (conta == 2):
  print(pergunta - pergunta2)
elif( conta == 3):
  print(pergunta * pergunta2)
elif (conta == 4):
  print(pergunta / pergunta2)
else:
  print('digite um valor valido')