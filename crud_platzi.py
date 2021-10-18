import sys


#clients = 'pablo,ricardo,'
clients = ['pablo','ricardo']


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in client\'s list')


def list_clients():
    global clients
    print(clients)

def Update_client(client_name, Updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', Updated_client_name+ ',')
    else:
        _not_exist()

def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name+',','')
        
    else:
        _not_exist()


def _get_client_name():
    client_name = None
    while not client_name:
        client_name =  input('¿Cual es el nombre del cliente? \n')
        
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()
    return client_name


def _not_exist():
    print('El cliente ingresado no se encuentra en la lista\n Intente de nuevo o utilice un nombre valido')


def search_client(client_name):
    global clients
    client_list= clients.split(',')

    for client in client_list:
        if client != client_name:
            continue
        else:
            return True
     

def _add_comma():
    global clients

    clients += ','
"""
def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name
"""

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[L]ist clients')
    print('[S]earch client')



if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name=_get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        Updated_client_name = input('¿Cual es el nombre del cliente a actualizar? \n')
        Update_client(client_name, Updated_client_name)
        list_clients()

    elif command == 'D':
        client_name =_get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('El cliente esta en la lista de clientes')
        else:
            print('El cliente con el nombre {} no esta en la lista de clientes'.format(client_name))