import crud

#Variables globales
personas = [
    {
        'Nombre': 'Juan',
        'Apellido': 'Barrios',
        'Identificacion': '1022036041',
        'Edad': 26,
        'Estudios/Cursos': 'Fundamentos de Python y mas',
        'Puntaje': 7.8
    }
]

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
            print('3. Ver lista de personas')
            print('4. Eliminar registros de una persona')
            print('5. Salir')
            opcion = int(input('Elige una opción: '))
            if opcion in [1, 2, 3, 4, 5]:
                break
        except ValueError as error:
            print(error)
    
    if opcion == 1: crud.agregar_persona(personas); sub_menu()
    elif opcion == 2: print('2')
    elif opcion == 3: crud.listar_personas(personas); sub_menu()
    elif opcion == 4: print('4')
    elif opcion == 5: menu()
    # return opcion


if __name__ == '__main__':
    menu()
