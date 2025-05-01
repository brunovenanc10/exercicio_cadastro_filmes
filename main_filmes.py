import time

bd_filmes = []

def cadastra_filmes(bd, título, ano):
    filme = [título, ano]
    bd.append(filme)
    return bd

def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd
while True:
    print('1 - Cadastrar Filme')
    print('2 - Listar Filmes')
    print('3 - Alterar Filme')
    op = int(input('Digite sua Opção: '))

    if op == 1:
        título = input('Digite o título do filme:')
        ano = int(input('Digite o ano do filme:'))
        bd_filmes = cadastra_filmes(
            bd=bd_filmes,
            título=título,
            ano=ano
        )
        print('Filme Cadastrado!')

    elif op == 2:
        listar_filmes(bd_filmes)
        print('Filmes Listados!')

    elif op == 3:
        listar_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar? '))
        titulo = input('Digite o novo título: ')
        ano = int(input('Digite o novo ano: '))
        bd_filmes = altera_filme(
            bd=bd_filmes,
            indice=(i-1),
            titulo=titulo,
            ano=ano
        )

        print('Filme Alterado!')
    else:
        print(f'Opção {op} Inválida!')

    time.sleep(3)