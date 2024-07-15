def fatorial(elementos):

    if elementos == 0:
        return 1
    else:
        return elementos * fatorial(elementos-1)

print(fatorial(5))