aluno = []
def menu(aluno):
    print('\n--- Menu Aluno ----')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Editar')
    print('4 - Deletar')
    print('5 - Sair')
    print('-------------------\n')

    opcao = int(input('Informe a Opção: '))
    if opcao == 1:
        cadastrar(aluno)

    elif opcao == 2:
        listar(aluno)

    elif opcao == 3:
        editar(aluno)

    elif opcao == 4:
        deletar(aluno)

    elif opcao == 5:
        sair(aluno)

    else:
        print('\nOpção inválida!')
        return menu(aluno)


def cadastrar(aluno):
    print('\n--- Cadastrar Aluno ---')
    id = int(input('Id: '))
    cpf = input('Cpf: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    turma = input('Turma: ')


    aluno.append({
        'id': id,
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'turma': turma

    })
    print('-----------------------\n')
    print('Cadastro concluído!')

    opcao = int(input ('\nDeseja cadastrar um novo aluno? [1-Sim/2-Não]: '))
    if opcao == 1:
        cadastrar(aluno)

    elif opcao == 2:
        menu(aluno)

    else:
        print('\nOpção inválida!')
        menu(aluno)


