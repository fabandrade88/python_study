#Abertura do Software

print('Bem-vindo a loja do Fabricio Oliveira de Andrade')

#Input de valor do pedido e quantidade de parcelas

valorDoPedido = float(input('Entre o valor do pedido: R$ '))
quantidadeDeParcelas = int(input('Entre a quantidade de parcelas: '))

#Juros dependendo da quantidade de parcelas

if (quantidadeDeParcelas < 4):
  Juros = (0/100)
elif (quantidadeDeParcelas >= 4 and  quantidadeDeParcelas < 6):
  Juros = (4/100)
elif (quantidadeDeParcelas >= 6 and  quantidadeDeParcelas < 9):
  Juros = (8/100)
elif (quantidadeDeParcelas >= 9 and  quantidadeDeParcelas < 13):
  Juros = (16/100)
else:
  Juros = (32/100)

#calculo do valor da parcela considerando os juros

valorDaparcela = (valorDoPedido * (1 + Juros)) / quantidadeDeParcelas
print(f'O valor das parcelas é de: R${"%.2f" % valorDaparcela}')

#Valor total considerando valor da parcela final + quantidade de parcelas

valorTotalParcelado = valorDaparcela * quantidadeDeParcelas
print(f'O valor total parcelado é de: R${valorTotalParcelado}')
