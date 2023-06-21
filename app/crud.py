

#Funcion para agregar nueva persona
def agregar_persona(personas: list):
    data = {}
    print("\n** REGISTRO NUEVA PERSONA **")
    while True:
        try:
            nombre = input('Nombre: ')
            data['Nombre'] = nombre

            apellido = input('Apellido: ')
            data['Apellido'] = apellido

            while True:
                id = input('Identificacion: ')
                if len(id) < 7 or len(id) > 10:
                    print('Dato incorrecto, reingreselo.')
                else:
                    data['Identificacion'] = id
                    break
            
            while True:
                edad = int(input('Edad: '))
                if edad < 15 or edad > 99:
                    print('Dato incorrecto, resingreselo.')
                else:
                    data['Edad'] = edad
                    break
            
            while True:
                estudios = input('Estudios/Cursos: ')
                if len(estudios) < 7:
                    print('No valido, reingrese los datos.')
                else:
                    data['Estudios/Cursos'] = estudios
                    break
            
            while True:
                puntaje = float(input('Puntaje: '))
                if puntaje < 0 or puntaje > 10:
                    print('Dato incorrecto, reingreselo.')
                else:
                    data['Puntaje'] = puntaje
                    break
            
            personas.append(data)
            break
        except ValueError as error:
            print('Error critico: ',error)
        except TypeError as error:
            print('Error critico: ',error)


# Funcion para listar personas
def listar_personas(personas: list):
    print('\n* LISTADO DE PERSONAS *')
    for persona in personas:
        print('Nombre: ', persona['Nombre'])
        print('Apellido: ', persona['Apellido'])
        print('ID: ', persona['Identificacion'])
        print('Edad: ', persona['Edad'])
        print('Estudios: ', persona['Estudios/Cursos'])
        print('Puntaje: ', persona['Puntaje'])
        print('*' * 25)