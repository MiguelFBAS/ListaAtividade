'''
Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo passar o comando de abertura de arquivos, passar comando de ação

Modos de ação: 
-  "r": Leitura do arquivo
-  "w": escrita(sobrescrever o conteudo antigo)
-  "a": adiciona conteudo
-  "x": criar um arquivo 
-  "b": arquivos binarios
-  "t": texto

'''
#Criando e escrevendo arquivo

arquivo = open("primeiro_arquivo.txt", 'w')
arquivo.write('Hello monkeys')
arquivo.close()
