#Questão 2. Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas. Exiba, as notas, seus respectivos pesos e a média.

notas = []
pesos = []
notasPeso = []

def recebeNotas():
    n = 1
    while True:
        qtdeNota = int(input('Deseja adicionar quantas notas?\nR: '))
        
        for i in range(qtdeNota):
            notas.append(int(input(f'Nota {n}: ')))
            pesos.append(float(input('Insira o peso dessa nota: ')))
            n += 1
        
        maisNota = input('Deseja continuar adicionando notas?\nR: ').lower()
    
        if maisNota == 'nao':
            print('Fazendo o cálculo da média')
            break
    return notas, pesos 

def calculaMedia(notas, pesos):
    for i in range(len(notas)):
        notasPeso.append(notas[i] * pesos[i])

    media = sum(notasPeso)/len(notas)
    return media

def exibeNotas(media):
    n = 1
    for i in range(len(notas)):
        print(f'Nota {n} = {notas[i]}')
        print(f'Peso {n} = {pesos[i]}\n')
        n += 1

    print('Média aritmética = %.2f' % media)

recebeNotas()
media = calculaMedia(notas, pesos)
exibeNotas(media)