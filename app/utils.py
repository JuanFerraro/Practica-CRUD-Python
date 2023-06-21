#Funcion validar id:
def validar_id(id: int):
    if not id.isdigit() or len(id) < 7:
        return False
    else:
        return True