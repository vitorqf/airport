import os

from airport import Airport, City
from crew import Crew
from flight import Flight
from person_with_reservation import Operator, Passenger
from reservation import Reservation
from seat import Seat


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Iniciar():
    clear()
    print("===============================================")
    print("|              ADMIN OU USUARIO               |")
    print("===============================================")
    print("| Opções:                                     |")
    print("|                 1. Admin                    |")
    print("|                 2. Usuario                  |")
    print("|                 3. Sair                     |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-3]: ")
    
    senhaAdmin = 'admin'

    while True:
        if choice == '1':
            senha = input("Senha: ")
            if senha == senhaAdmin:
                clear()
                menuAdmin()
                break
            else:
                print("Senha inválida. Pressione Enter para caso queira voltar")
                if senha == '':
                    clear()
                    Iniciar()
                continue

            
        elif choice == '2':
            clear()
            menuUser()
            break
            
        elif choice == '3':
            clear()
            print("Saindo do programa...")
            break
        else:
            clear()
            Iniciar()


def menuAdmin():
    clear()
    print("===============================================")
    print("|                 MENU ADMIN                  |")
    print("===============================================")
    print("| Opções:                                     |")
    print("|         1. Cadastrar Cidade                 |")
    print("|         2. Cadastrar Aeroporto              |")
    print("|         3. Cadastrar Tripulação             |")
    print("|         4. Cadastrar Lista de Assentos      |")
    print("|         5. Cadastrar Voô                    |")
    print("|         6. Cadastrar Operador               |")
    print("|         7. Sair                             |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-7]: ")

    
    while True:
        if choice == '1':
            clear()
            CadastroCidade()
            break
            
        elif choice == '2':
            clear()
            
        elif choice == '3':
            clear()
            
        elif choice == '4':
            clear()

        elif choice == '5':
            clear()

        elif choice == '6':
            clear()
            
        elif choice == '7':
            clear()
            print("Saindo do programa...")
            break
        else:
            clear()
            print("Opção inválida. Escolha novamente.")

    

def menuUser():
    clear()
    print("===============================================")
    print("|                    MENU                     |")
    print("===============================================")
    print("| Opções:                                     |")
    print("|                 1. opcao                    |")
    print("|                 2. opcao                    |")
    print("|                 3. opcao                    |")
    print("|                 4. opcao                    |")
    print("|                 5. Sair                     |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-5]: ")

    while True:
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

def CadastroCidade():
    clear()
    print("===============================================")
    print("|               Cadastrar Cidade              |")
    print("===============================================")
    pais = input("              País: ")
    estado = input("              Estado: ")
    cidade = input("              Cidade: ")

    instance = City(pais, estado, cidade)
    City_list.append(instance)
    print("===============================================")

def CadastroAeroporto():
    clear()
    print("===============================================")
    print("|             Cadastrar Aeroporto             |")
    print("===============================================")
    nome = input("              Nome: ")
    decolagens = int(input("              Decolagens suportadas: "))
    

    instance = Airport(City_list[0], nome, decolagens)
    Airport_list.append(instance)

    print("===============================================")

    if instance.name != '' and instance.max_departures != '':
        print('Aeroporto cadastrado com sucesso!')
    else:
        print('Aeroporto não cadastrado!')

# CadastroCidade()
Airport_list = []
City_list = [City('dasd', 'dasijdias', 'duas')]
CadastroAeroporto()