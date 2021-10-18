



clients = 'Daniel,ricardo,'

def crear_cliente(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else :
        print('El cliente ya esta en la lista de clientes')

def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients+=','

def _print_welcome():
    print('Vienvenidos a platziventas')
    print('*'*50)
    print('Que te gustaria hacer hoy')
    print('[C]reate client')
    print('[D]elete client')

if __name__ == '__main__':
    _print_welcome()
    #crear_cliente('rossi')
    #list_clients()
    command = input ()

    if command == 'C':
        client_name = input('Cual es el nombre del cliente?: \n')
        crear_cliente(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:('Comando invalido')
    

