import matplotlib.pyplot as plt

#Funcion para validar string (a-z y espacios)
def validar_string(string):
    if all((i.isalpha() or i.isspace()) for i in string): # .isalpha (a-z) .isspace(space)
        return True
    else:
        return False
    
# Funcion para obtener los datos a graficar
def obtener_datos(personas: list):
    people = list(map(lambda persona: persona['Nombre'] +' '+ persona['Apellido'], personas)) 
    puntaje = list(map(lambda persona: persona['Puntaje'], personas))
    return people, puntaje

#Funcion para graficar nombre y puntaje
def grafico_barras(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)  
    plt.show()