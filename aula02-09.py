def pesquisa_sequencial(lista, item): 
#faz item a item, mais lento, porém interresante por ser simples para pequenos códigos
    for i, j in enumerate(lista):
        if j == item:
          return i

def pesquisa_binaria(lista, item): #Lista precisa estar obrigatoriamente em ordem
#testa sempre o termo do meio, verifica se o numero é maior ou menor e elimina o resto. Mas complexo, mais rápido em sistemas grandes
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


#Calculo de complexidade: Quantas tentativas leva para resolver no pior cenário
#calcular quantos passo a pesquisa binaria levará = log₂(n)