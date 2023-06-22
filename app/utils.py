#Funcion para validar string (a-z y espacios)
def validar_string(string):
    if all((i.isalpha() or i.isspace()) for i in string):
        return True
    else:
        return False