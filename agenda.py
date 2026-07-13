from contactos import Contactos

class Agenda:
    def __init__(self):
        self.lista_contacto = []
        
    def agregar_contaco(self):
        nombre = input("Nombre: ")
        nombre = nombre.capitalize()
        telefono = self.validar_numero()
        contacto = Contactos(nombre,telefono)
        self.lista_contacto.append(contacto)
        
    def borrar_contacto(self, indice):
        self.lista_contacto.pop(indice-1)
        
    def buscar_contacto(self, nombre):
        encontrados = []
        for contac in self.lista_contacto:
            if nombre.lower() in contac.nombre.lower():
                encontrados.append(contac)

        if encontrados:
            for c in encontrados:
                print(c.mostrar_info())
        else:
            print("No se encontraron coincidencias.")
            
    def validar_numero(self):
        while True:
            numero = input("Telefono: ")
            if numero.isdigit() and len(numero) >= 8:
                return int(numero)
            else:
                print("Numero de 8 digitos")
                
    def mostrar_contacto(self):    
        for i, contac in enumerate(self.lista_contacto , start=1):
            print(f"{i} - Nombre: {contac.nombre} Telefono: {contac.telefono}")
