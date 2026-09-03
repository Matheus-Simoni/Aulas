def pesquisa_sequencial(lista, item):
    for i, j in enumerate(lista):
        if j == item:
          return i

def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) - 1

  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute == item:
      return meio
    elif chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None
