print("Bienvenido al festival musical")
print("*******")
print("0. SALIR")
print("1. Registrar banda")
print("2. Ver lista de bandas")
print("3. Ver bandas que no se han presentado")
print("4. Cambiar hora de presentación")
print("5. Retirar banda que aún no se ha presentado")
print("****-****")

opcion=-1

bandas=[]

while opcion!=0:
    banda={}
    opcion=int(input("Digita una opción: "))
    
    if opcion==1:
        banda["id"]=input("Digite el id de la banda: ")
        banda["nombre"]=input("Digite el nombre de la banda: ")
        banda["genero"]=input("Digite el genero de la banda: ")
        banda["hora"]=input("Digite la hora a la que se presenta la banda: ")
        banda["pago"]=float(input("Digite el pago que se le realiza a la banda: "))
        estado_input=input("Se presentó o no / True-False: ")
        if estado_input.lower() == 'true':
            banda["estado"] = True
        else:
            banda["estado"] = False
            
        bandas.append(banda)
        print("Banda registrada con éxito")
    elif opcion==2:
        print("Lista de bandas registradas")
        for bandaIntegrante in bandas:
            print(f"Nombre Banda:{bandaIntegrante['nombre']}")
            print(f"ID banda:{bandaIntegrante['id']}")
            print(f"Hora presentacion:{bandaIntegrante['hora']}")
    elif opcion==3:
        print("Bandas que no se han presentado: ")
        
        for bandaIntegrante in bandas:
            if bandaIntegrante["estado"]==False:
                print(f"Nombre banda:{bandaIntegrante['nombre']}")
                
    elif opcion == 4:
        nombre_banda = input("Digite el nombre de la banda cuya hora desea cambiar: ")
        found = False
        for bandaIntegrante in bandas:
            if not bandaIntegrante["estado"] and bandaIntegrante["nombre"] == nombre_banda:
                nueva_hora = input("Digite la nueva hora de presentación: ")
                bandaIntegrante["hora"] = nueva_hora
                print("Hora de presentación actualizada con éxito.")
                found = True
                break
        if not found:
            print("No se encontró una banda con ese nombre o que no se haya presentado aún.")

    elif opcion == 5:
        nombre_banda = input("Digite el nombre de la banda que desea retirar: ")
        found = False
        for bandaIntegrante in bandas:
            if not bandaIntegrante["estado"] and bandaIntegrante["nombre"] == nombre_banda:
                bandas.remove(bandaIntegrante)
                print("Banda retirada con éxito.")
                found = True
                break
        if not found:
            print("No se encontró una banda con ese nombre o que no se haya presentado aún.")
            
                        