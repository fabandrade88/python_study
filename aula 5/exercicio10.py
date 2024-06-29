#fatorial

def valida_int(pergunta, min, max):
  x = int(input(pergunta))
  while((x < min)or (x > max)):
    x = int(input(pergunta))

    return x

def fatorial (num):

  """
  funcao para calcular fatorial

  """

  fat = 1

  if num == 0:
    return fat
  #esta parte apenas executa num > 0
  for i in range(1, num + 1, 1):
    fat *= i
  
  return fat

x = validade_int('digite um valor para calcular fatorial: ', 0, 9999)

print(f'{x}! = {fatorial(x)}')