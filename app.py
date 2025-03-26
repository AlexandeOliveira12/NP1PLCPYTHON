import os

# LIMPAR TERMINAL
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# SISTEMA DE ESCOLHAS DE CURSOS
def menu_escolha():
        print("\n🧠 Bem vindo ao Menu do Estudante")
        print("1️⃣  - Cursos Python")
        print("2️⃣  - Logica Programção")
        print("3️⃣  - Infraestrutura Computacional - Hardware")
        print("4️⃣  - Sair")
        escolha = int(input("Escolha alguma das opções acima (somente numeros): "))

        if escolha == 4:
            return
        else:
            print("")
        
        return
    
menu_escolha()

        
