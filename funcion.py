#comenzamos poniendo una varibale que se llamara "pedido" que sera igual a una lista con "[]" que serian corchetes
 #
pedidos = []
dinero_recaudado = 0


def mostrar_detalles():
    print("===Detalles de pedidos===")
    for pedido in pedidos:
        print("cliente:", pedido["cliente"]) 
        print("plato:", pedido["platos"])
        print("bebida:", pedido["bebida"])
        print("total:", pedido["Total"])
        print("=============================")

cantidad_pedidos = int(input("cuántos pedidos se van a procesar en la ronda actual?: "))

for pedido in range (cantidad_pedidos):
    
    print("pedido ", pedido +1)
    cliente = input("Ingrese su nombre: ")
    print("=== MENU 1 - PLATO PRINCIPAL ===: ")
    print("1. perro caliente - $10500")
    print("2. hamburguesa")

    platos = int(input("seleccione el plato que desea comer: "))
    if platos == 1:
        platos = "perro caliente"
        precio_plato = 10500
    elif platos == 2:
        print("=== SUBMENU - TIPO DE HAMBURGUESA ===: ")
        print("1: haburguesa secilla - 20000")
        print("2: hamburguesa doble carne - 35000")
    
        tipo_de_hamburgues = int(input("seleccione el tipo de hamburguesa: "))

        if tipo_de_hamburgues == 1:
            platos = "hamburguesa sencilla"
            precio_plato = 20000
        elif tipo_de_hamburgues == 2:
            platos = "hamburguesa doble carne"
            precio_plato = 35000
        else:
         print("opcion invalida")
         continue
    else:
        print("opcion invalida")
        continue

    print("===MENU2 - BEBIDAS===: ")
    print("1. gaseosa - 5000")
    print("2. jugo natural - 10000 ")

    bebidas = int(input("seleccione la bebida que quiere tomar: "))
    if bebidas == 1:
        bebidas = "gaseosa"
        precio_bebida = 5000
    elif bebidas == 2:
        bebidas = "jugo natural"
        precio_bebida = 10000
    else:
         print("opcion invalida")
         continue
    Total = precio_plato + precio_bebida
    dinero_recaudado = dinero_recaudado + Total
    pedido = {
        "cliente": Cliente,
        "platos": platos,
        "bebida": bebidas,
        "Total": Total  
    }
    pedidos.append(pedido)
print("Total de dinero recaudado:", dinero_recaudado)

ver_detalle = input("Desea ver el detalle de los pedidos (si/no): ")

if ver_detalle.lower() == "si":
    mostrar_detalles()

elif ver_detalle.lower() == "no":
    print("===PEDIDOS FINALIZADOS===")





