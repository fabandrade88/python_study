print('Bem-vindo a Fábrica de Camisetas do Fabrício Oliveira de Andrade')

total = 0

def escolha_modelo ():
  while True:
    print('Entre com o modelo desejado')
    print('  MCS - Manga Curta Simples')
    print('  MLS - Manga Longa Simples')
    print('  MCE - Manga Curta Com Estampa')
    print('  MLE - Manga Longa Com Estampa')

    modelo = input('>> ')
    if modelo not in [ 'MCS', 'MLS', 'MCE', 'MLE']:
      print('Escolha invalida, entre com o modelo novamente')
      
    else:
     return modelo

def num_camisetas ():
  while True:
    numeroDeCamisetas = int(input('Entre com o numero de camisetas: '))

    if numeroDeCamisetas < 20:
      return numeroDeCamisetas
    
    elif 20 <= numeroDeCamisetas < 200:
      desconto = numeroDeCamisetas * (1 - 0.05)
      return desconto
    
    elif 200 >= numeroDeCamisetas < 2000:
      desconto = numeroDeCamisetas * (1 - 0.07)
      return desconto
    
    elif 2000 >= numeroDeCamisetas <= 20000:
      desconto = numeroDeCamisetas * (1 - 0.12)
      return desconto
    
    elif numeroDeCamisetas > 20000:
      print('Nao aceitamos tantas camisetas de uma vez')
      print('Por favor, entre com o numero de camisetas novamente')

escolha_modelo ()
num_camisetas ()