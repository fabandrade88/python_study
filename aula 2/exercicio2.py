km = float(input('Quantos km vc percorreu: '))
dias = float(input('Por quantos dias vc ficou com o carro: '))

calculode_km = km * 0.15
calculo_locacao = dias * 60

valor_total = calculode_km + calculo_locacao

print('O custo de total de km foi de {}, as diarias ficaram em {}, e o valor total a pagar e de {}'. format(calculode_km, calculo_locacao, valor_total))
