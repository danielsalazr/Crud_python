import click

from tabulate import tabulate
#from click import decorators

from clients.services import ClientService
from clients.models import Client

@click.group() # Convertimos clients()en otro decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
            type = str,
            prompt=True,
            help='The client name')
@click.option('-c', '--company',
            type = str,
            prompt=True,
            help='The client company')
@click.option('-e', '--email',
            type = str,
            prompt=True,
            help='The client email')
@click.option('-p', '--position',
            type = str,
            prompt=True,
            help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)



@clients.command()
@click.pass_context
def list (ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    #click.echo (' ID  |  NAME  |  COMPANY |  EMAIL  |  POSITION') #ponmos click.echo como sustituto a print debido a que print se comprta diferencre en casa sistema operativo
    #click.echo('*'*100)

    headers = [field.capitalize() for field in Client.schema()]
    table = []

    print()

    for client in clients_list:
        """click.echo('{uid}  |  {name}  |  {email}  |  {company}  |  {position}'.format(
            uid = client['uid'],
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']

        
        ))"""

        table.append([client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid']])

    print(tabulate(table, headers))
    print()

@clients.command()
@click.pass_context
def uodate(ctx, client_uid):
    """Update a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    pass

all =  clients
