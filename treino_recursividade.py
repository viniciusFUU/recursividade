def soma_separado_parametros(num):
    valor = 0

    num = str(num)

    for i in range(len(num)):
        elemento_int = int(num[i])
        valor += elemento_int

    return valor

def soma_recursiva(num):
    if num < 10:
        return num
    else:
        ultimo_elemento = num % 10
        num_sem_ultimo_elemento = num // 10

        return ultimo_elemento + soma_recursiva(num_sem_ultimo_elemento)
    
def potencia_recursiva(num, potencia):
    if potencia == 0:
        return 1
    
    numero_potencia = num*potencia

    return numero_potencia + potencia_recursiva(num, potencia-1)

def fibonacci(qtd_elementos):
    if qtd_elementos == 0:
        return 0
    elif qtd_elementos == 1:
        return 1
    else:
        return fibonacci(qtd_elementos-1) + fibonacci(qtd_elementos-2)
    
def palindromo(palavra):
    if len(palavra) <= 0:
        return True
    elif palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False
    
def numeros_pares(valor):
    ultimo_elemento = valor % 10
    valor_sem_o_ultimo_elemento = valor // 10

    qtd_valor = str(valor)

    if ultimo_elemento == 0:
        return 0 + numeros_pares(valor_sem_o_ultimo_elemento)
    elif len(qtd_valor) == 1 and ultimo_elemento % 2 != 0:
        return 0
    elif len(qtd_valor) == 1 and ultimo_elemento % 2 == 0:
        return 1
    elif ultimo_elemento % 2 == 0:
        return 1 + numeros_pares(valor_sem_o_ultimo_elemento)
    else:
        return numeros_pares(valor_sem_o_ultimo_elemento)
    
def contagem_de_ocorrencias(palavra, letra):
    qtd_letras = len(palavra)

    if qtd_letras < 1: 
        return 0
    elif palavra[-1] == letra:
        palavra = palavra[0:-1]
        return 1+ contagem_de_ocorrencias(palavra, letra)
    else:
        palavra = palavra[0:-1]
        return contagem_de_ocorrencias(palavra, letra)
    
def soma_elementos_lista(lista):
    if len(lista) < 1:
        return 0
    if len(lista) >= 1:
        ultimo_elemento = lista[-1]
        lista_sem_ultimo_elemento = lista[:-1]
        return ultimo_elemento + soma_elementos_lista(lista_sem_ultimo_elemento)
    
def fatorial(numero):
    if numero < 1:
        return 1
    
    return numero * fatorial(numero-1)