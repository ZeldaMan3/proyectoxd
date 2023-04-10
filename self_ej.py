# Se inicia la clase con sus atributos
class Alumno:
    def inic(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

        #Se hace la funcion para imprimir los atributos
    def imprimir(self):
        print("Nombre: ",self.nombre, "\nNota: ", self.nota)

    #Se hace la funcion que verifica la nota
    def resultado(self):
        if self.nota >= 5:
            print("Aproaste")
        else:
            print("No aproaste")


#Se crea los objetos
alumno01 = Alumno()
alumno02 = Alumno()

#Da los valores a los objetos
#alumno01.inic("Matias", 4) llama a la funcion init para tomar los valores "nombre" y "nota"

alumno01.inic("Matias", 4)
alumno02.inic("Juan", 7)

#Imprime los resultados
alumno01.imprimir()
alumno01.resultado()
