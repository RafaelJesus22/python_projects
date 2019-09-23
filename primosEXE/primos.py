def pega_divisores(num):
    #funçao que cria um objeto decorador com todos os diviores
    for i in range(1, int(num/2) +1):
        if num % i ==0:
            yield i 
    yield num


#cabeçalho do programa
print('==='*30, '\n                                   VERFICADOR DE PRIMOS\n', '==='*30)

while True:

    #variavel que conta os divisores
    total_divisores = 0

    #variavel de decisão
    resp = str() 

    #chama a função que gera um objeto gerador com todos os divisores
    numero_checar = pega_divisores(int(input('Qual numero quer saber se é primo: ')))
    print('==='*30)

    #mostar todos os divisores
    print('divisores: ', end='')

    for num in numero_checar:
        print(num, end=' ')
        total_divisores += 1

    #mostrar a quantidade de divisores
    print(f'\ntem {total_divisores} divisores,', end=' ')
    
    #revelar se é primo ou não
    if total_divisores == 2:
        print('portando ele é num numero primo')
    else:
        print('portanto ele não é um numero primo')

    print('==='*30)

    #decidir se vai verificar outro numero
    while True:
        resp = input('quer checar outro numero[s/n]: ')
        if resp == 'n' or resp == 's':
            break
    print('==='*30)        

    if resp == 'n':
        break

sair = input('tecle enter para sair do programa')
