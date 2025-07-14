#producto={"model":["marca","pantalla","RAM","disco","GB de DD","procesador ", "video"]}
productos = {'8D475H': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}
#stoc={"modelo":["precio,stock"]}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 }



def agregar_items_a_la_lista():
    print("agregar cosas a la lista")
def elimnar_producto(modelo):
    modelo=input('ingrese el modelo que desea eliminar: ').capitalize()
    for productos in stock:
        if modelo in productos :
            del modelo["model"]
        print('se ha eliminado con exito!!!!')
        return    
    else:
        print('no existe dicha marca')
def stock_marca(marca):    
        while True:
            marca=input("ingrese marca a consultar: ").capitalize()
            if marca in productos:
                break
            else:
                print("no existe dicha marca")
                if marca in stock:
                    marca["stock"]==stock.items()
                    return(marca)

while True:
    print("===MENU PRINCIPAL====")
    print("1.-STOCK marca")
    print("2.-busqueda por RAM")
    print("3.-Eliminar producto")
    print("4.-Salir")
    opc=input("ingrese las siguiente opciones: ")
    if opc=="1":
        stock_marca(stock)
    elif opc=="2":
        busqueda_RAM_precio()
    elif opc=="3":
        elimnar_producto(productos)
    elif opc=="4":
        print("programa finalizado")
        break
    else:
        print("seleccione una de las opciones")    