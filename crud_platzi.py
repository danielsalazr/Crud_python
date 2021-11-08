import sys
import csv
import os
import os.path
from pathlib import Path
from typing import Dict

#clients = 'pablo,ricardo,'

"""
clients = [
    {
        'name':'Pablo',
        'company': 'Google',
        'email' : 'PabloGoogleano@google.com',
        'position': 'Software engineer',
    },
    {
        'name':'Richard',
        'company': 'Chibchombia',
        'email' : 'richardd@chibchombia.com',
        'position': 'data engineer',
    }
]
"""

#print(os.path.dirname(os.path.abspath(__file__)))

CLIENT_TABLE ='.clients.csv'  #Asi llamamo s un archivo oculto
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

creado = os.path.exists(CLIENT_TABLE)

def _initialize_clients_from_storage():

    if creado == False:
        return 

    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

        for row in reader :
            clients.append (row)
    print(clients)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames = CLIENT_SCHEMA)
        writer.writerows(clients)

        f.close()
        if creado == True:
            os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position} '.format(
        uid = idx, 
        name = client['name'],
        company = client['company'], 
        email = client['email'],
        position = client['position']))

def Update_client(client_id, updated_client):
    global clients
    clients[client_id] = updated_client



def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

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

def _get_client_field (field_name):
    field = None

    while not field:
        field = input('What is the client {}? \n'.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _not_exist():
    print('El cliente ingresado no se encuentra en la lista\n Intente de nuevo o utilice un nombre valido')


def search_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


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

    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = { 
            'name': _get_client_field('name'), 
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        #client_name=_get_client_name()
        create_client(client)
        #list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        if len(clients) -1 >= client_id:
            Updated_client = _get_client_from_user()
            Update_client(client_id, Updated_client)
            #list_clients()
        else:
            _not_exist()


    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        #list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('El cliente esta en la lista de clientes')
        else:
            print('El cliente con el nombre {} no esta en la lista de clientes'.format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()