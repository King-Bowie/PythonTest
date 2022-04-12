quant = maior = menor = 0
for numero in range(0,5):
    num = int(input('Digite um numero: '))    
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(f'Menor valor: {menor}   Maior valor: {maior}')
