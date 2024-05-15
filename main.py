import jogo
import sys

def mostrar_menu():
    print("Menu:")
    print("1. Jogar")
    print("2. Sair")
    print() # Adiciona uma linha em branco
    
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        print()  # Adiciona uma quebra de linha após escolha

        if opcao == "1":
            jogo.jogar()
        elif opcao == "2":
            print("Obrigado por jogar!")
            sys.exit()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida. \n")

if __name__ == "__main__":
    main()
    