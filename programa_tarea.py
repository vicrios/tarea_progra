# -*- coding: utf-8 -*-
"""programa tarea

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/vicrios/d8d81c15f24137c4a166a74c67ec99c3/untitled3.ipynb
"""

class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()