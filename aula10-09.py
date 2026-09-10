#fatorial 

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(10))

#Fibonacci (cada número é a soma dos dois números anteriores)

def fibonacci(n):
  if n <= 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))