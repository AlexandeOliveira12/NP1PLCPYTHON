import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu_escolha():
        print("\n🧠 Bem vindo ao Menu do Estudante")
        print("1️⃣  - Cursos Python")
        print("2️⃣  - ")
        print("3️⃣  - ")
        print("4️⃣  - Biblioteca Digital")
        print("5️⃣  - Sair")
        escolha = int(input("Escolha alguma das opções acima (somente numeros): "))

        if escolha == 1:
            clear_screen()
            print("\n📚 Qual curso quer assistir? ")
            print("1️⃣  - Curso em Video - Python")
            print("2️⃣  - Curso Gratuito de Python - Pietro Martins")
            print("3️⃣  - Python for Beginners - (Curso m Inglês)")
            print("4️⃣  - Voltar para o Menu")
            print("5️⃣  - Sair")
            EscCurso = int(input("Escolha um curso (somente numeros): "))
            if  EscCurso == 1:
                os.system('start "https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0"')
            elif EscCurso == 2:
                os.system('start "https://www.youtube.com/watch?v=wC_mwNUT48s&list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip"')
            elif EscCurso == 3:
                os.system('start "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"')
            elif EscCurso == 4:
                clear_screen()
                menu_escolha()
            elif EscCurso == 5:
                clear_screen()
                return
        elif escolha == 5:
            return
        else:
            print("nada")
        
        return 
    
menu_escolha()

        
