import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuAdmin():
    clear()
    print("===============================================")
    print("|                    MENU                    |")
    print("===============================================")
    print("| Opções:                                    |")
    print("|                 1. opcao                   |")
    print("|                 2. opcao                   |")
    print("|                 3. opcao                   |")
    print("|                 4. opcao                   |")
    print("|                 5. Sair                    |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-5]: ")
    return choice

while True:
    choice = menuAdmin()
    if choice == '1':
        clear()
        
    elif choice == '2':
        clear()
        
    elif choice == '3':
        clear()
        
    elif choice == '4':
        clear()
        
    elif choice == '5':
        clear()
        print("Saindo do programa...")
        break
    else:
        clear()
        print("Opção inválida. Escolha novamente.")





def menuUser():
    clear()
    print("===============================================")
    print("|                    MENU                    |")
    print("===============================================")
    print("| Opções:                                    |")
    print("|                 1. opcao                   |")
    print("|                 2. opcao                   |")
    print("|                 3. opcao                   |")
    print("|                 4. opcao                   |")
    print("|                 5. Sair                    |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-5]: ")
    return choice

while True:
    choice = menuUser()
    if choice == '1':
        clear()
        
    elif choice == '2':
        clear()
        
    elif choice == '3':
        clear()
        
    elif choice == '4':
        clear()
        
    elif choice == '5':
        clear()
        print("Saindo do programa...")
        break
    else:
        clear()
        print("Opção inválida. Escolha novamente.")



def Iniciar():
    clear()
    print("===============================================")
    print("|              Admin ou Usuario              |")
    print("===============================================")
    print("| Opções:                                    |")
    print("|                 1. Admin                   |")
    print("|                 2. Usuario                 |")
    print("|                 3. Sair                    |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-3]: ")
    return choice

while True:
    choice = Iniciar()
    if choice == '1':
        clear()
        menuAdmin()
        
    elif choice == '2':
        clear()
        menuUser()
        
    elif choice == '3':
        clear()
        print("Saindo do programa...")
        break
    else:
        clear()
        print("Opção inválida. Escolha novamente.")