#algoritmo cadastrar jogos por nome e videogame

#validacao

def valida_int(pergunta, min, max):
 while True: #loop infinito ate receber um valor inteiro valido
    try:
      x = int(input(pergunta)) #tenta converter a entrada para inteiro
      if (x < min)or (x > max): #verifica se esta dentro do intervalo
        print(f'Erro: O valor deve estar entre {min} e {max}.')
      else:
        return x #retorna o valor inteiro valido
    except ValueError:
      print('Erro: Digite um valor inteiro válido.') #mensagem de erro caso nao seja um inteiro valido


def existeArquivo(nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
  
  #criar arquivo

def criarArquivo(nomeArquivo):
   try:
     a = open(nomeArquivo, 'wt+')
     a.close()
   except:
    print('erro na criacao do arquivo')
   else:
     print(f'Arquivo {nomeArquivo} criado com sucesso.\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
   try:
     a = open(nomeArquivo, 'at')
   except:
     print('error abrir arquivo')
   else:
      a.write(f'{nomeJogo};{nomeVideogame}\n')
   finally:
      a.close()
#programa principal: menu

arquivo = 'games.txt'
if existeArquivo(arquivo):
  print('arquivo localizado')
else:
  print('arquivo Inexistente')
  criarArquivo(arquivo)

def listarArquivo(nomeArquivo):
   try:
     a = open(nomeArquivo, 'rt')
   except:
     print('erro ao ler arquivo')
   else:
     print(a.read())

   finally:
     a.close()

while True:
  print('MENU')
  print('1 - Cadastrar novo item')
  print('2 - listar cadastros')
  print('3 - Sair')

  op = valida_int('Escolha a opcao desejada: ', 1, 3)
  if(op == 1): #novo item
    print('opcao de cadastar novo item selecionada...\n')
    nomeJogo = input('nome do jogo: ')
    nomeVideogame = input('nome do video game: ')
    cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

  elif (op == 2): #listar
      print('opcao de listar selecionada...\n')
      listarArquivo(arquivo)

  elif (op == 3):
       print('encerrrando o programa...')
       break
