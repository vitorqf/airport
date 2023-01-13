import os

from airport import Airport, City
from crew import Crew
from flight import Flight
from person_with_reservation import Operator, Passenger
from reservation import Reservation
from seat import Seat

from datetime import datetime

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
    print("|         4. Cadastrar Voô                    |")
    print("|         5. Cadastrar Operador               |")
    print("|         6. Sair                             |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-6]: ")

    
    while True:
        if choice == '1':
            clear()
            CadastroCidade()
            break
            
        elif choice == '2':
            clear()
            CadastroAeroporto()
            break
            
        elif choice == '3':
            clear()
            CadastroTripulacao()
            break

        elif choice == '4':
            clear()
            CadastroVoo()
            break

        elif choice == '5':
            clear()
            
        elif choice == '6':
            clear()
            print("Saindo do programa...")
            break
        else:
            clear()
            Iniciar()

    

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






Airport_list = []
City_list = []
Crew_list = []
Seat_list = []
Flight_list = []


def CadastroCidade():
    while True:
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
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break

def CadastroAeroporto():
    while True:
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
        
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break

def CadastroTripulacao():
    while True:
        clear() 
        print("===============================================")
        print("|             Cadastrar Tripulação            |")
        print("===============================================")
        nome = input("              Nome: ")
        funcao = input("              Função: ")

        instance = Crew(nome, funcao)
        Crew_list.append(instance)
        print("===============================================")
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break


def CadastroVoo():
    while True:
        clear() 
        print("===============================================")
        print("|                 Cadastrar Voô               |")
        print("===============================================")
        tipo = input("              Tipo(Nacional|Internacional): ")
        assentos = int(input("  Quantidade de assentos: "))
        for i in range(0, assentos):
            assento = input("              ID do assento: ")
            Seat_list.append(assento)

        Flight_list.append(Flight(tipo, Airport_list[0], Airport_list[1]), datetime.now().time(), datetime.now().date(), Seat_list, Crew_list)
        print("===============================================")
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break

# Iniciar()
# CadastroCidade()
# CadastroAeroporto()
# CadastroTripulacao()