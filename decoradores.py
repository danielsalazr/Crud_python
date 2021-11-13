


PASSWORD = '12345'


#Forma 1 de decorador 

def password_required(func):
    def wrapper():
        password = input('Cual es tu contrasena ? \n')

        if password == PASSWORD:
            return(func())
        else:
            print('La contrasena no es correcta')
    return wrapper

@password_required  #Este es el decorados
def needs_password():
    print('La contrasena es correcta')

#Con el decorador pudimos ejecutar una logica antess de la funcion y determinamos
#si  se iva a tener acceso a esa funcion

#forma 2 de decorador
def upper(func):
    def wrapper(*args,**kargs):
        result = func(*args, **kargs)

        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return('hola {}'.format(name))

#Aqui utilizamos el decorador para obtener el texto y convertirlo en mayuscula


if __name__ == '__main__':
    needs_password()
    print(say_my_name('David'))