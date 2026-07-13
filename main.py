from agenda import Agenda

def main():
    agd = Agenda()
    while True:
        print('''
            1 - Agregar ctc
            2 - Borrar ctc
            3 - Mostrar ctcs
            4 - Buscar ctc
            5 - Salir''')

        opc = int(input("-> "))
        match(opc):
            case 1: 
                agd.agregar_contaco()
            case 2: 
                agd.mostrar_contacto()
                indice = int(input("-> "))
                agd.borrar_contacto(indice)
            case 3: 
                agd.mostrar_contacto()
            case 4: 
                nombre = input("Coincidencia x nombre:  ")
                agd.buscar_contacto(nombre)
            case 5: break
            
if __name__ == "__main__":
    main()