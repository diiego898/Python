print(__name__)

if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)

if __name__ == "__main__":
    producto = Producto([args])
    print(producto)
    print(producto.agregar_impuesto(0.18))