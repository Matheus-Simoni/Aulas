#usar o algoritmo de fatorial, mas fazer soma acumulada (ex: 5 + 4 + 3 + 2 + 1)

def cumsum(n):
  if n <= 1:
    return 1
  else:
    return n + cumsum(n - 1)

print(cumsum(5))

#mesma solução, mas com while/for 

def cumsum2(n):
    resultado = 0
    while n:
        resultado = resultado + n 
        n -= 1
    return resultado

print(cumsum2(5))

def cumsum3(n):
    soma = 0
    for n in range(n + 1):
        soma += n
        n = n - 1
    return soma

print(cumsum3(5))

#ordenar numeros de forma descrecente 

def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[0]
    menores = [i for i in arr[1:] if i >= pivo]
    maiores = [i for i in arr[1:] if i < pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))