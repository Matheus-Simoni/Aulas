#fatorial 
#usado na atividade 3

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(4))

#Fibonacci (cada número é a soma dos dois números anteriores)

def fibonacci(n):
  if n <= 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

#quicksort

def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[0]
    menores = [i for i in arr[1:] if i <= pivo]
    maiores = [i for i in arr[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))