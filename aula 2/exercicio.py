preco = float(input('valor de um produto: '))
desconto = float(input('desconto do produto: '))

calculo = (preco * desconto)/100
valor_final = preco - calculo

print ('O valor do produto e {} com desconto de {} o valor final fica {}'. format(preco,desconto, valor_final))