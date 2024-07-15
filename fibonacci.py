def fibonacci_recursivo(num):
    if num == 0:
        return 1
    else:
        return num + fibonacci(num-1)

#0, 1, 1, 2, 3, 5, 8, 13

def fibonacci(num):
    numero_anterior = 0
    numero_posterior = 0
    contador = 0

    for i in range(num):
        if numero_anterior == 0:
            numero_posterior+=1

        numero_posterior = numero_anterior + numero_posterior
        numero_anterior = numero_posterior - numero_anterior

    return numero_posterior

print(fibonacci_recursivo(5))