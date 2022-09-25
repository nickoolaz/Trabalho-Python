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

