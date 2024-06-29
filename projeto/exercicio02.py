#Abertura do sistema
print('-' * 2, 'Bem-vindos a loja de Marmitas do Fabricio Oliveira de Andrade', '-' * 2)

# Menu com opcoes do cardapio
print('-' * 25, ' Cardápio ','-' * 25)
print('-' * 3, '|', 'Tamanho','|', 'Bife Acebolado(BA)','|','File de Frango(FF)','|','-' * 3)
print('-' * 3, '|', '   P   ','|', '    R$ 16.00      ','|','     R$ 15.00     ','|','-' * 3)
print('-' * 3, '|', '   M   ','|', '    R$ 18.00      ','|','     R$ 17.00     ','|','-' * 3)
print('-' * 3, '|', '   G   ','|', '    R$ 22.00      ','|','     R$ 21.00     ','|','-' * 3)
print('-' * 61)

def order ():
    total = 0

    while True:
        while True:
            sabor = input('Entre com sabor desejado (BA/FF): ')
            if sabor not in ['BA', 'FF']:#tamanho nao estiver dentro da lista
                print('Sabor invalido. Tente Novamente')
            else:
                break
        
        while True:
            tamanho = input('Entre com o tamanho desejado (P, M, G): ')
            if tamanho in ['P', 'M', 'G']: #tamanho nao estiver dentro da lista
                break
            else:
                print('Tamanho invalido. Tente Novamente')
        
        # Valor baseado no Tamanho e Sabor.
        if tamanho == 'P' and sabor == 'BA':
            valor = 16.00
        elif tamanho == 'M' and sabor == 'BA':
            valor = 18.00
        elif tamanho == 'G' and sabor == 'BA':
            valor = 22.00
        elif tamanho == 'P' and sabor == 'FF':
            valor = 15.00
        elif tamanho == 'M' and sabor == 'FF':
            valor = 17.00
        elif tamanho == 'G' and sabor == 'FF':
            valor = 21.00
        
        total += valor #Incrementando o total
        print(f'Você pediu um {"Bife Acebolado" if sabor == "BA" else "Filé de Frango"} no tamanho {tamanho}: R$ {"%.2f" % valor}')
        
        orderMore = input('Deseja mais alguma coisa? (S/N): ').upper() #sempre UpperCase
        if orderMore == 'N':
            break

    print(f'O valor total a ser pago: R$ {"%.2f" % total}')

order()