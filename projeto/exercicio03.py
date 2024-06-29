#Abertura do programa

print('Bem-vindo a Fábrica de Camisetas do Fabrício Oliveira de Andrade')

def escolha_modelo (): #Funcao de escolha dos modelos e de alocacao de valor.
  while True:
    print('Entre com o modelo desejado')
    print('  MCS - Manga Curta Simples')
    print('  MLS - Manga Longa Simples')
    print('  MCE - Manga Curta Com Estampa')
    print('  MLE - Manga Longa Com Estampa')

    modelo = input('>> ')
    if modelo not in [ 'MCS', 'MLS', 'MCE', 'MLE']:
      print('Escolha invalida, entre com o modelo novamente')

    elif modelo == 'MCS':
      modelo = 1.80
      return modelo
    
    elif modelo == 'MLS':
      modelo = 2.10
      return modelo
    
    elif modelo == 'MCE':
      modelo = 2.90
      return modelo
    
    elif modelo == 'MLE':
      modelo = 3.20
      return modelo
  

def num_camisetas (): #Funcao para selecao de quantidade de camisas dentro do limite
  while True:
    try:
     numeroDeCamisetas = int(input('Entre com o numero de camisetas: '))

     if numeroDeCamisetas < 20:
      return numeroDeCamisetas
    
     elif numeroDeCamisetas <= 20 and numeroDeCamisetas < 200:
      desconto = numeroDeCamisetas * (1 - 0.05)
      return desconto
    
     elif numeroDeCamisetas >= 200 and numeroDeCamisetas < 2000:
      desconto = numeroDeCamisetas * (1 - 0.07)
      return desconto
    
     elif numeroDeCamisetas >= 2000 and numeroDeCamisetas<= 20000:
       desconto = numeroDeCamisetas * (1 - 0.12)
       return desconto
     else:
       print('Nao aceitamos tantas camisetas de uma vez')
       print('Por favor, entre com o numero de camisetas novamente')
     
    except ValueError:
        print('Por favor, entre com o numero de camisetas novamente')

def frete (): # Selecao de frente e alocacao de valores.
  while True:
    print('Escolha o tipo de frete:')
    print('  1 - Frete por transportadora - R$100.00')
    print('  2 - Frete por Sedex - R$ 200.00')
    print('  0 - Retirar pedido na fabrica - R$ 0.00')

    opcaoDeFrete = int(input('>> '))
    if opcaoDeFrete not in [0, 1, 2]:
      print('Escolha o tipo de frete')
    
    elif opcaoDeFrete == 0:
      opcaoDeFrete = 0.00
      return opcaoDeFrete
    
    elif opcaoDeFrete == 1:
      opcaoDeFrete = 100.00
      return opcaoDeFrete
    
    elif opcaoDeFrete == 2:
      opcaoDeFrete = 200.00
      return opcaoDeFrete

modelo = escolha_modelo()
quantidade = num_camisetas()
entrega = frete()


total = (modelo * quantidade) + entrega #calculo de custo total com frente

print(f'total: {total} (Modelo: R$ {modelo} * Quantidade (com desconto): {quantidade} + frente: {entrega})')

