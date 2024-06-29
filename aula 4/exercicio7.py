print('1 - Coxinha - RS 5,00')
print('2 - Pastel - RS 7,00')
print('3 - Cafe - RS 4,00')
print('4 - Suco - RS 6,00')
print('5 - sair')

total = 0

while True:
 op = int(input('qual item quer comprar: '))


 if (op == 1):
  qtd = int(input('qual a quantidade? '))
  total = total + qtd * 5.00

 elif(op == 2):
  qtd = int(input('qual a quantidade? '))
  total = total + qtd * 7.00

 elif(op == 3):
  qtd = int(input('qual a quantidade? '))
  total = total + qtd * 4.00

 elif(op == 4):
  qtd = int(input('qual a quantidade? '))
  total = total + qtd * 6.00

 elif(op == 5):
  break
 
 else:
  print('produto invalido selecione outro')

print(f'total a ser pago e igual {total}')
