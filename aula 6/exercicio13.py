palavras = ('mario', 'luigi', 'Peach', 'Yoshi', 'Browser')

for palavra in palavras:
  print(f'\nPalavra: {palavra.upper()}. Vograis: ')
  for letra in palavra:
    if letra.lower() in 'aeiou':
      print(letra.upper(), end='')