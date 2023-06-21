
#Función para Menú principal:
def menu():
    while True:
        try:
            print('-' * 13, ' MENU ', '-' * 14)
            print('1. Ingresar')
            print('2. Salir')
            opcion = int(input('Elige una opcion: '))
            if opcion in [1,2]:
                break
        except ValueError as error:
            print(error)
    if opcion == 1:
            sub_menu()

#Función para sub menú:
def sub_menu():
    
    while True:
        try:
            print('-' * 12, ' SUB MENU ', '-' * 12)
            print('1. Añadir nueva persona')
            print('2. Actualizar datos de persona')
            print('3. Ver datos de persona')
            print('4. Elimar registros de una persona')
            opcion = int(input('Elige una opción: '))
            if opcion in [1, 2, 3, 4]:
                break
        except ValueError as error:
            print(error)
    # return opcion


if __name__ == '__main__':
    menu()
