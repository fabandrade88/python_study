print('Bem-vindo a Empresa do Fabricio Oliveira de Andrade')

lista_funcionario = {'nome':[], 'setor':[], 'salario':[]}

id_global = 4622693

cadastrar_funcionario (id)

for i in range(3):
  nome = input('Qual o nome do funcionario? ')
  setor = input('Qual o setor do funcionario? ')
  salario = int(input('Qual salario do funcionario? '))

  lista_funcionario['nome'].append(nome)
  lista_funcionario['setor'].append(setor)
  lista_funcionario['salario'].append(salario)

