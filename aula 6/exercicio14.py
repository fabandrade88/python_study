import random

print('JOKENPO')

def valida_int(pergunta, min, max):
  x = int(input(pergunta))
  while((x < min) or (x >max)):
    x = int(input(pergunta))

    return x
  
  def vencedor (jogador1, jogador2):
    if jogador1 == 1:#Pedra
     if jogador2 == 1:
      empate

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
resultados = []

while True:
  j1 = valida_int('Escola sua jogada: ', 0, 3)
  if not j1:
    break

  j2 = random.randint(1,3)
  jogadas.append([j1, j2])
  resultados = vencedor(j1, j2)
