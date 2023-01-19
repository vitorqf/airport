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
            menuLogin()
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
            CadastroOperador()
            
        elif choice == '6':
            clear()
            print("Saindo do programa...")
            break
        else:
            clear()
            Iniciar()


    

def menuUserLogado():
    clear()
    print("===============================================")
    print("|                    MENU                     |")
    print("===============================================")
    print("| Opções:                                     |")
    print("|            1. Criar reserva                 |")
    print("|            2. Pagamento                     |")
    print("|            3. Cancelar reserva              |")
    print("|            4. informações                   |") 
    print("|            5. Sair                          |")
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

def menuLogin():
    clear()
    print("===============================================")
    print("|                 Autenticação                |")
    print("===============================================")
    print("| Opções:                                     |")
    print("|               1. Cadastrar-se               |")
    print("|               2. Login                      |")
    print("|               3. Sair                       |")
    print("===============================================")
    choice = input("Entre com sua escolha [1-5]: ")
    while True:
        if choice == '1':
            clear()
            CadastroPassageiro()
            break
            
        elif choice == '2':
            clear()
            FazerLogin()
            
        elif choice == '3':
            clear()
            print("Saindo do programa...")
            break
        else:
            clear()
            print("Opção inválida. Escolha novamente.")
            break





Airport_list = []
City_list = []
Crew_list = []
Seat_list = []
Flight_list = []
Operator_list = []
Passenger_list = []


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


        # arrumar o append do Flight
        Flight_list.append(Flight(tipo, Airport_list[0], Airport_list[1]), datetime.now().time(), datetime.now().date(), Seat_list, Crew_list)
        print("===============================================")
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break

def CadastroOperador():
    while True:
        clear() 
        print("===============================================")
        print("|              Cadastrar Operador             |")
        print("===============================================")
        nome = input("              Nome:  ")
        voo = input("  Insira o Voo relacionado ao operador: ")
        # arrumar o input do voo

        Operator_list.append(Operator(nome, voo))
        print("===============================================")
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            continue
        else:
            clear()
            menuAdmin()
            break





def CadastroPassageiro():
    while True:
        clear() 
        print("===============================================")
        print("|             Cadastrar Passageiro            |")
        print("===============================================")
        nome = input("              Nome: ")
        Passenger_list.append(Passenger(nome))
        print("===============================================")
        next = input('Continuar cadastrando? (s/n):  ')
        if next == 's':
            CadastroPassageiro()
        if nome:
            clear()
            menuUserLogado()
            break    
        else:
            print("Cadastro inválida. Pressione Enter para caso queira voltar")
            if nome == '':
                clear()
                Iniciar()
            continue

def FazerLogin():
    while True:
        clear() 
        print("===============================================")
        print("|                 Fazer Login                 |")
        print("===============================================")
        nome = input("              Nome: ")
        if nome in Passenger_list:
            clear()
            menuUserLogado()
            break
        else:
            print("Login inválido. Tente novamente")
            FazerLogin()
            break
# Iniciar()
# CadastroCidade()
# CadastroAeroporto()
# CadastroTripulacao()
# menuLogin()
# FazerLogin()
print(Passenger_list)