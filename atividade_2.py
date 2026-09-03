#Qual o nome associado ao número 256 e quantas tentativas foram feitas? Quantas tentativas seriam em uma pesquisa sequencial?

lista = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'), (122, 'Vanessa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]

def pesquisa_binaria(lista, item): 
  baixo = 0
  alto = len(lista) - 1
  contagem = 1
  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute[0] == item:
      return meio, contagem
    elif chute[0] > item:
      alto = meio - 1
      contagem += 1 
    else:
      baixo = meio + 1
      contagem += 1
  return None

def pesquisa_sequencial(lista, item):
    contagem = 1
    for i, j in enumerate(lista):
        if j[0] == item:
            return i, contagem
        else:
            contagem += 1
    return None

x, y = pesquisa_binaria(lista, 256)
a, b = pesquisa_sequencial(lista, 256)

print('\nPesquisa Binaária:')
print(f'\nO nome é: {lista[x][1]}')
print(f'Numero de tentativas: {y}')
print('\n==========================')
print('\nPesquisa sequencial:')
print(f'\nO nome é: {lista[a][1]}')
print(f'Numero de tentativas: {b}')