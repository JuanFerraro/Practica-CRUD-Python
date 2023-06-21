

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


# Funcion para listar personas:
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

# Funcion para buscar persona por id:
def buscar_persona(personas: list):
    print('\n* BUSCAR PERSONA POR ID *')
    while True:
        id_buscar = input('Ingrese ID de la persona: ')
        if len(id_buscar) >= 7 and len(id_buscar) <= 10:
            break

    encontrado = next((persona for persona in personas if persona['Identificacion'] == id_buscar), None)
    if encontrado is not None:
        print('\nPersona encontrada: ')
        print('Nombre: ', encontrado['Nombre'])
        print('Apellido: ', encontrado['Apellido'])
        print('ID: ', encontrado['Identificacion'])
        print('Edad: ', encontrado['Edad'])
        print('Estudios: ', encontrado['Estudios/Cursos'])
        print('Puntaje: ', encontrado['Puntaje'])
        print('*' * 25)
    else:
        print('Persona no encontrada.\n')

# Funcion para eliminar una persona:
def eliminar_persona(personas: list):
    while True:
        print('\n* ELIMINAR PERSONA *')
        persona_eliminar = input('Ingrese la ID de la persona a eliminar: ')
        if len(persona_eliminar) >= 7 and len(persona_eliminar) <= 10:
            break
    
    encontrado = next((persona for persona in personas if persona['Identificacion'] == persona_eliminar), None)
    if encontrado is not None:
        while True:
            try:
                print(f'Seguro que quieres eliminar a {encontrado["Nombre"]} {encontrado["Apellido"]} del registro?')
                print('1.Si\n2.No')
                opcion = int(input('Elige una opcion: '))
                if opcion in [1,2]:
                    break
            except ValueError as error:
                print('Error critico: ', error)
        if opcion == 1:
            for persona in personas: 
                if persona_eliminar == persona['Identificacion']:
                    personas.remove(persona)
                    print('Persona eliminada correctamente. \n')
    else:
        print('Persona no encontrada')   
            
