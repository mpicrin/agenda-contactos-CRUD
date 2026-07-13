class Contactos:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Telefono: {self.telefono}"