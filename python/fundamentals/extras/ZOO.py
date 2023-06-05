class Zoo:
    def __init__(self,name):
        self.name = name
        self.animals = []

    def agregar_leon(self, name, edad , atrib):
        self.animals.append(Leon(name, edad , atrib))
        return self

    def agregar_tigre(self, name , edad , atrib):
        self.animals.append(Tigre(name , edad , atrib))
        return self

    def agregar_tiburone(self, name , edad , atrib):
        self.animals.append(Tiburon(name , edad , atrib))
        return self

    def imprimir_toda_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.mostrar_info()
        return self
    def alimentar(self):
        print("-"*10, self.name, "-"*10)
        for animal in self.animals:
            animal.alimentacion()
        return self
    


class Animal:
    def __init__(self, zoo_name, zoo_edad ):
        self.name = zoo_name
        self.edad = zoo_edad
        self.salud = 100
        self.felicidad = 100

    def alimentacion(self):
        self.salud += 10
        self.felicidad += 10
        return self

class Leon(Animal):
    def __init__(self, zoo_name, zoo_edad, melena):
        super().__init__(zoo_name, zoo_edad)
        self.melena = melena

    def mostrar_info(self):
        print(f" Nombre = {self.name}  Edad = {self.edad} Atributo = {self.melena} Salud = {self.salud}  Felicidad = {self.felicidad} ")
        return self
class Tiburon(Animal):
    def __init__(self, zoo_name, zoo_edad, aleta):
        super().__init__(zoo_name, zoo_edad )
        self.aleta = aleta
    def mostrar_info(self):
        print(f" Nombre = {self.name}  Edad = {self.edad} Atributo = {self.aleta} Salud = {self.salud}  Felicidad = {self.felicidad} ")
        return self
class Tigre(Animal):
    def __init__(self, zoo_name, zoo_edad, fuerza):
        super().__init__(zoo_name, zoo_edad)
        self.fuerza = fuerza
    def mostrar_info(self):
        print(f" Nombre = {self.name}  Edad = {self.edad} Atributo = {self.fuerza} Salud = {self.salud}  Felicidad = {self.felicidad} ")
        return self






zoo1 = Zoo("El zoo de John")

zoo1.agregar_leon("Nala" , 22 ,1000)
zoo1.agregar_leon("Simba" , 22 ,1000)

zoo1.agregar_tigre("Rajah" , 22 ,1000)
zoo1.agregar_tigre("Shere Khan" , 22 ,1000 )

zoo1.agregar_tiburone("Shark" , 22 ,1000)
zoo1.agregar_tiburone("Martillo" , 22 ,1000)

zoo1.imprimir_toda_info()
zoo1.alimentar()
zoo1.imprimir_toda_info()
zoo1.imprimir_toda_info()
zoo1.alimentar()
zoo1.imprimir_toda_info()
zoo1.imprimir_toda_info()
zoo1.alimentar()
zoo1.imprimir_toda_info()
zoo1.imprimir_toda_info()
zoo1.alimentar()
zoo1.imprimir_toda_info()
zoo1.imprimir_toda_info()
zoo1.alimentar()
zoo1.imprimir_toda_info()