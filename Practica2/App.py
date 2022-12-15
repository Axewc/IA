# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App Main


import sys
from Node import Node
from AStarAlgorithm import AStarAlgorithm

class App(object):
    
    def __init__(self, objetivo):

        self.cero = Node("0", abs(objetivo - 0))
        self.uno = Node("1", abs(objetivo - 1))
        self.dos = Node("2", abs(objetivo - 2))
        self.veinte = Node("20", abs(objetivo - 20))
        self.veintiuno = Node("21", abs(objetivo - 21))
        self.veintidos = Node("22", abs(objetivo - 22))
        self.cuarenta = Node("40", abs(objetivo - 40))
        self.cuarentayuno = Node("41", abs(objetivo - 41))
        self.cuarentaydos = Node("42", abs(objetivo - 42))

        self.cero.addChild(self.uno, 1 - 0)
        self.cero.addChild(self.veintiuno, 21 - 0)
        self.cero.addChild(self.veinte, 20 - 0)

        self.uno.addChild(self.cero, 1 - 0)
        self.uno.addChild(self.veintiuno, 21 - 1)
        self.uno.addChild(self.veinte, 20 - 1)
        self.uno.addChild(self.veintidos, 22 - 1)
        self.uno.addChild(self.dos, 2 - 1)

        self.dos.addChild(self.uno, 2 - 1)
        self.dos.addChild(self.veintiuno, 21 - 2)
        self.dos.addChild(self.veintidos, 22 - 2)

        self.veinte.addChild(self.cero, 20 - 0)
        self.veinte.addChild(self.uno, 20 - 1)
        self.veinte.addChild(self.veintiuno, 21 - 20)
        self.veinte.addChild(self.cuarenta, 40 - 20)
        self.veinte.addChild(self.cuarentayuno, 41 - 20)

        self.veintiuno.addChild(self.cero, 21 - 0)
        self.veintiuno.addChild(self.uno, 21 - 1)
        self.veintiuno.addChild(self.dos, 21 - 2)
        self.veintiuno.addChild(self.veinte, 21 - 20)
        self.veintiuno.addChild(self.veintidos, 22 - 21)
        self.veintiuno.addChild(self.cuarenta, 40 - 21)
        self.veintiuno.addChild(self.cuarentayuno, 41 - 21)
        self.veintiuno.addChild(self.cuarentaydos, 42 - 21)

        self.veintidos.addChild(self.dos, 22 - 2)
        self.veintidos.addChild(self.uno, 22 - 1)
        self.veintidos.addChild(self.veintiuno, 22 - 21)
        self.veintidos.addChild(self.cuarentayuno, 41 - 22)
        self.veintidos.addChild(self.cuarentaydos, 42 - 22)

        self.cuarenta.addChild(self.veinte, 40 - 20)
        self.cuarenta.addChild(self.veintiuno, 40 - 21)
        self.cuarenta.addChild(self.cuarentayuno, 41 - 40)

        self.cuarentayuno.addChild(self.veinte, 41 - 20)
        self.cuarentayuno.addChild(self.veintiuno, 41 - 21)
        self.cuarentayuno.addChild(self.cuarenta, 41 - 40)
        self.cuarentayuno.addChild(self.veintidos, 41 - 22)
        self.cuarentayuno.addChild(self.cuarentaydos, 42 - 41)

        self.cuarentaydos.addChild(self.veintidos, 42 - 20)
        self.cuarentaydos.addChild(self.veintiuno, 42 - 21)
        self.cuarentaydos.addChild(self.cuarentayuno, 42 - 41)

    def searchAStarAlgorithm(self):
        print("\nBuscando ruta optima con Algoritmo A*")
        astar = AStarAlgorithm(self.cero, self.cuarentaydos)
        print("Nodo Inicial: %s -----> Nodo Final %s" % (self.cero.name, self.cuarentaydos.name))
        res= astar.run()
        return res

def bueno():
    try:
        app = App(42)
        res = app.searchAStarAlgorithm()
        return res
    except (ValueError, FileNotFoundError, AttributeError) as ex:
        print(ex)
    

