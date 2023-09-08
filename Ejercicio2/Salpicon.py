print("Preparar salpicon")
print("*****")
print("0. SALIR")
print("1. Registrar frutas")
print("2. Mostrar frutas ordenadas de mayor a menor precio")
print("3. Mostrar fruta más barata y la más cara")
print("4. Mostrar costo toal de un salpicón")
print("****-****")

opcion=-1
frutas=[]

while opcion!=0:
    fruta={}
    opcion=int(input("Digite una opción: "))
    if opcion==1:
        fruta["id"]=input("Digite el ID de la fruta: ")
        fruta["nombre"]=input("Digite el nombre de la fruta: ")
        fruta["precioUnitario"]=float(input("Digite el precio unitario de la fruta: "))
        fruta["cantidad"]=int(input("Digite la cantidad de frutas: "))
        
        frutas.append(fruta)
        print("Fruta registrada con éxito")
    elif opcion==2:
        # Ordena la lista de frutas por precio unitario en orden descendente (de mayor a menor)
        frutas_ordenadas = sorted(frutas, key=lambda x: x["precioUnitario"], reverse=True)
        
        # Muestra las frutas ordenadas
        print("Frutas ordenadas de mayor a menor precio:")
        for fruta in frutas_ordenadas:
            print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: ${fruta['precioUnitario']}")        
        
    elif opcion == 3:
        
        if len(frutas) == 0:
            print("Aún no se han registrado frutas.")
        else:
            fruta_mas_costosa = max(frutas, key=lambda x: x["precioUnitario"])
            fruta_mas_barata = min(frutas, key=lambda x: x["precioUnitario"])

            print("Fruta más costosa:")
            print(f"ID: {fruta_mas_costosa['id']}, Nombre: {fruta_mas_costosa['nombre']}, Precio Unitario: ${fruta_mas_costosa['precioUnitario']}")

            print("Fruta más barata:")
            print(f"ID: {fruta_mas_barata['id']}, Nombre: {fruta_mas_barata['nombre']}, Precio Unitario: ${fruta_mas_barata['precioUnitario']}")
            
    elif opcion == 4:
        costo_total = 0  # Inicializamos el costo total en cero
        for fruta in frutas:
            costo_fruta = fruta["precioUnitario"] * fruta["cantidad"]
            costo_total += costo_fruta

        print(f"El costo total del salpicón es: ${costo_total}")
        
        