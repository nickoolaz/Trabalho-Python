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


def listar(aluno):
    print('\n--- Listagem Alunos ---')

    for i in aluno:
        print( 'Id: ' + str(i['id']) + '\n' +
               'Cpf: ' + i['cpf'] + '\n' +
               'Nome: ' + i['nome'] + '\n' +
               'Idade: ' + str(i['idade']) + '\n' +
               'Turma: ' + i['turma'] + '\n' +
               '-----------------------' )

    opcao = int(input('\nDeseja atualizar algum aluno? [1-Sim/2-Não]: '))
    if opcao == 1:
        print('\n--- Atualizar Aluno ---')
        print('1 - Editar')
        print('2 - Deletar')
        print('3 - Menu')
        print('-----------------------\n')

        opcao = int(input('Informe a Opção: '))
        if opcao == 1:
            editar(aluno)

        elif opcao == 2:
            deletar(aluno)

        elif opcao == 3:
            menu(aluno)

        else:
            print('\nOpção inválida!')
            return menu(aluno)

    else:
        opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
        if opcao == 1:
            menu(aluno)

        else:
            exit()

