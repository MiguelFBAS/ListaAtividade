'''
1. Crie um progrma que o usuario possa digitar quantos numeros quiser e ao terminar impirma a lista em ordem crescente

2. crie um programa que o usuario possa digitar a quantidade desejada de nots de um determinado aluno (nota minima 0 e nota maxima 10) 
e o programa calcula a media desse aluno, e ao final imprima se o aluno esta aprovado (>=7) ou reprovadoe/recuperação (>=5)'''

# Atividade 1.

l_num = []

while True:
    num = float(input("Digite um numero: "))
    i = num
    l_num.append(num)
        
    add = input ("Pressione +/= para adicionar mais um numero.\n Pressione enter sem nenhum dois dois escrito para continuar o programa.\n")
    if add != "=":
            break
    else:
          False

f_num = sorted([num])
print(f_num) 
