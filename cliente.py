import tabla as tbl

tabla = int(input("Ingresa un numero?"))

mi_objeto = tbl.Tabla(tabla)

print("Tabla normal:")
mi_objeto.mostrarNormal()
print("Tabla invertida:")
mi_objeto.mostarInvertido()
