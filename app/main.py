import crud

#Variables globales
personas = [
    {
        'Nombre': 'Juan',
        'Apellido': 'Barrios',
        'Identificacion': '10203040',
        'Edad': 26,
        'Estudios/Cursos': 'Fundamentos de Python y mas',
        'Puntaje': 5.4
    },
    {
        'Nombre': 'Sebastian',
        'Apellido': 'Ferraro',
        'Identificacion': '50607080',
        'Edad': 26,
        'Estudios/Cursos': 'Fundamentos de JS',
        'Puntaje': 9.8
    },
    {
        'Nombre': 'Cristo',
        'Apellido': 'Padre',
        'Identificacion': '90102030',
        'Edad': 33,
        'Estudios/Cursos': 'Ingeniero Industrial',
        'Puntaje': 3.3
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
            print('5. Ver grafico de puntajes')
            print('6. Salir')
            opcion = int(input('Elige una opción: '))
            if opcion in [1, 2, 3, 4, 5, 6]:
                break
        except ValueError as error:
            print('Error critico: ',error)
    
    if opcion == 1: crud.agregar_persona(personas); sub_menu()
    elif opcion == 2: crud.actualizar_persona(personas); sub_menu()
    elif opcion == 3: ver_personas()
    elif opcion == 4: crud.eliminar_persona(personas); sub_menu()
    elif opcion == 5: crud.grafica_puntajes(personas); sub_menu()
    elif opcion == 6: menu()

#funcion para menu de ver listas
def ver_personas():
    while True:
        try: 
            print('\n* LISTAR PERSONAS *')
            print('1. Ver lista de todas las personas')
            print('2. Buscar persona por identificacion')
            print('3. Salir')
            opcion = int(input('Elige una opcion: '))
            if opcion in [1,2]:
                break
        except ValueError as error:
            print('Error critico: ', error)
    if opcion == 1: crud.listar_personas(personas); sub_menu()
    elif opcion == 2: crud.buscar_persona(personas); sub_menu()
    elif opcion == 3: sub_menu()  

# Principal -- Principal -- Principal
if __name__ == '__main__':
    menu()
