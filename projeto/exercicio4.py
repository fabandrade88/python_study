import copy #importando o copy da biblioteca

print('Bem-vindo a Empresa do Fabricio Oliveira de Andrade')

lista_funcionario = []

id_global = 4622693

#funcao para cadastrar um novo funcionario
def cadastrar_funcionario(id):
  nome = input('Qual o nome do funcionario? ')
  setor = input('Qual o setor do funcionario? ')
  salario = float(input('Qual salario do funcionario? '))

  funcionario = {"id": id,"nome": nome, "setor": setor, "salario": salario}

  lista_funcionario.append(copy.deepcopy(funcionario)) #chamando o copy que foi importado
  print('cadastro feito')

#funcao para consultar os funcionarios cadastrados
def consultar_funcionarios ():
  while True:
    print('Menu - Consultar Funcionarios')
    print('1 - Consultar Todos')
    print('2 - Consultar por id')
    print('3 - Consultar por Setor')
    print('4 - Retornar ao menu')

    escolha = int(input('Escolha a opcao: '))

    if escolha == 1:
      print('Lista de todos os funcionarios: ')
      for i in lista_funcionario:
        print(i)
    elif escolha == 2:
      id_consulta = int(input('Digite o id do funcionario: '))
      funcionario = next( i for i in lista_funcionario if i['id'] == id_consulta) #busca id dentro de lista ate encontrar dentro das opcoes
      if funcionario:
        print(funcionario)
      else:
        print('Funcionario nao encontrado.')
    elif escolha == 3:
      consulta = input('Digite o setor: ')
      funcionario_setor = [i for i in lista_funcionario if i['setor'] == consulta]
      if funcionario_setor:
        for i in funcionario_setor:
          print(i)
      else:
          print('Nenhum funcionario encontrado neste setor.')
    elif escolha == 4:
      return
    else:
      print('Opcao invalida')

#funcao para remover funcionarios

def remover_funcionario():
  while True:
    id_remover = int(input('Digite o id do funcionario a ser removido: '))
    funcionario = next(i for i in lista_funcionario if i['id'] == id_remover)
    if funcionario:
      lista_funcionario.remove(funcionario) #remove funcionario
      print('Funcionario removido com sucesso')
      break
    else:
      print('id invalido')

#menu principal

while True:
  print('Menu Principal')
  print(' 1 - Cadastrar Funcionario')
  print(' 2 - Consultar Funcionario')
  print(' 3 - Remover Funcionario')
  print(' 4 - Encerrar o Programa')

  escolha = int(input('Escolha a opcao: '))

  if escolha == 1:
    id_global += 1 #incrementa de 1 em 1 o id global
    cadastrar_funcionario(id_global)
  elif escolha == 2:
    consultar_funcionarios()
  elif escolha == 3:
    remover_funcionario()
  elif escolha == 4:
    print('Programa encerrado')
    break
  else:
    print('Opcao invalida')


