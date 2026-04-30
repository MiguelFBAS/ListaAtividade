# for

#laço de for, ele e finito:  quando eu sei o numero de repetições

frutas = ['melancia', 'abacaxi', 'melao', 'pera']
fruta = 'melancia'

'''for f in frutas:
    print(fruta[0]) -- mmmmm
    print (f)'''

# for range (inicio, fim, salto) 

'''for i in range(1, 20, 2):
    print("repeti")'''

'''num = int(input("Digite o numero para saber a tabuada: "))
for i in range (11):
    print(f"{i} x {num} = {i * num}")'''

lista_nomes = ['George Joestar', 'Johnathan Joestar', 'Joseph Joestar', 'Jotaro Kujo', 'Josuke Higashikata', 
'Giorno Giovanna', 'Jolyne Cujoh', 'Johnny Joestar', "Josuke 'Gappy' Higashikata", 'Jorge Joestar', "Jodio Joestar"]

for i, nome in enumerate (lista_nomes):
    print (f' {i+1}º {nome}')

nome_buscar = input ("Digite um nome para buscar: ").title()

if 'Jorge Joestar' in lista_nomes:
     print ("WHAT THE HELL IS EVEN HAPPENING IN THIS DAMN NOVEL WHAT DO YOU MEAN THERE ARE TWENTY NINE KARS ON MARS--")