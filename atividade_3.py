#usar o algoritmo de fatorial, mas fazer soma acumulada (ex: 5 + 4 + 3 + 2 + 1)

def cumsum(n):
  if n <= 1:
    return 1
  else:
    return n + cumsum(n - 1)

#print(cumsum(4))

def fatorial(n):
    resultado = 1
    while n:
        resultado = resultado * n 
        n = n - 1
    return resultado

print(fatorial(4))