# momcomepickmeupimscared
import modulo as ma
def main():
    
    if __name__ == "__main__":
        #copilot eu juro POR DEUS PARA-
        print("== Calculadora ==")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Limpar Terminal")

    opcao = input("Digite a opção desejada: ")
    while True:
        match opcao:
            #soma
            case "1":

                print(4*"-", "SOMA", 4*"-")  
                num1 = int(input("Digite o primeiro número para somar: "))
                num2 = int(input("Digite o segundo número para somar: "))

                print (f'Resultado = {ma.soma(num1, num2)}')
                break

            #subtração
            case "2":

                print(4*"-", "SUBTRAÇÃO", 4*"-")
                num1 = int(input("Digite o primeiro número para subtrair: "))
                num2 = int(input("Digite o segundo número para subtrair: "))

                print (f'Resultado = {ma.subtracao(num1, num2)}')
                break
            #multiplicação
            case "3":

                print(4*"-", "MULTIPLICAÇÃO", 4*"-")
                num1 = int(input("Digite o primeiro número para multiplicar: "))
                num2 = int(input("Digite o segundo número para multiplicar: "))

                print (f'Resultado = {ma.multiplicacao(num1, num2)}')
                break

            #divisão
            case "4":

                print(4*"-", "DIVISÃO", 4*"-")
                num1 = int(input("Digite o primeiro número para dividir: "))
                num2 = int(input("Digite o segundo número para dividir: "))

                print (f'Resultado = {ma.divisao(num1, num2)}')
                break

            #limpar terminal         
            case "5":

                ma.limpar_terminal()
                break

            case _:
                print("Opção inválida!")
                break