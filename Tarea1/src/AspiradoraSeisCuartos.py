#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AspiradoraSeisCuartos_f.py
----------------
"""

import entornos_f
from random import choice



class SeisCuartos(entornos_f.Entorno):
    """
    Clase para un entorno de seis cuartos.

    El estado se define como (robot, a, b, c, d, e, f)
    donde robot puede tener los valores "A", "B", "C", "D", "E", "F"
    indicando el cuarto en el que esta.
    
    a, b, c, d, e, f pueden tener los valores "limpio", "sucio"
    Las acciones válidas en el entorno son 
        ("subir", "bajar", "ir_der", "ir_izq", "limpiar", "nada").
    
    Algunas acciones son invalidas en algunas casillas:
    En a, no se puede subir ni ir_izq.
    En b, no se puede subir ni bajar.
    En c, no se puede subir, ni ir_der.
    En d, no se puede bajar ni ir_der.
    En e, no se puede bajar ni subir.
    En f, no se puede bajar ni ir_izq.

    Los sensores es una tupla (robot, limpio?)
    con la ubicación del robot y el estado de limpieza
    """
    def acción_legal(self, acción):

        return acción in ("subir", "bajar", "ir_der", "ir_izq", "limpiar", "nada")

    def transición(self, estado, acción):
        robot, a, b, c, d, e, f = estado

        c_local = 0 if a == b == c == d == e == f == "limpio" and acción is "nada" else 2 if acción is "subir" else 1

        return ((estado, c_local) if acción is "nada" else
                (("A", a, b, c, d, e, f), c_local) if acción is "subir" and robot == "F" else
                (("A", a, b, c, d, e, f), c_local) if acción is "ir_izq" and robot == "B" else
                (("B", a, b, c, d, e, f), c_local) if acción is "ir_izq" and robot == "C" else
                (("B", a, b, c, d, e, f), c_local) if acción is "ir_der" and robot == "A" else
                (("C", a, b, c, d, e, f), c_local) if acción is "subir" and robot == "D" else
                (("C", a, b, c, d, e, f), c_local) if acción is "ir_der" and robot == "B" else
                (("D", a, b, c, d, e, f), c_local) if acción is "bajar" and robot == "C" else
                (("D", a, b, c, d, e, f), c_local) if acción is "ir_der" and robot == "E" else
                (("E", a, b, c, d, e, f), c_local) if acción is "ir_izq" and robot == "D" else
                (("E", a, b, c, d, e, f), c_local) if acción is "ir_der" and robot == "F" else
                (("F", a, b, c, d, e, f), c_local) if acción is "ir_izq" and robot == "E" else
                (("F", a, b, c, d, e, f), c_local) if acción is "bajar" and robot == "A" else
                ((robot, "limpio", b, c, d, e, f), c_local) if robot is "A" else
                ((robot, a, "limpio", c, d, e, f), c_local) if robot is "B" else
                ((robot, a, b, "limpio", d, e, f), c_local) if robot is "C" else
                ((robot, a, b, c, "limpio", e, f), c_local) if robot is "D" else
                ((robot, a, b, c, d, "limpio", f), c_local) if robot is "E" else
                ((robot, a, b, c, d, e, "limpio"), c_local))

    def percepción(self, estado):

        return estado[0], estado[" ABCDEF".find(estado[0])]


class AgenteAleatorio(entornos_f.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales
    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, p):
        return ((choice(["bajar", "ir_der", "limpiar", "nada"])) if p == "A" else
                (choice(["ir_izq", "ir_der", "limpiar", "nada"])) if p == "B" else
                (choice(["bajar", "ir_izq", "limpiar", "nada"])) if p == "C" else
                (choice(["subir", "ir_izq", "limpiar", "nada"])) if p == "D" else
                (choice(["ir_der", "ir_izq", "limpiar", "nada"])) if p == "E" else
                (choice(["subir", "ir_der", "limpiar", "nada"])))


class AgenteReactivoSeisCuartos(entornos_f.Agente):
    """
    Un agente reactivo simple
    """
    def programa(self, percepción):
        robot, situación = percepción
        return ('limpiar' if situación == 'sucio' else
                'ir_der' if robot == 'A' else
                'ir_der' if robot == 'B' else
                'bajar' if robot == 'C' else
                'ir_izq' if robot == 'D' else
                'ir_izq' if robot == 'E' else 'subir')


class AgenteReactivoModeloSeisCuartos(entornos_f.Agente):
    """
    Un agente reactivo basado en modelo
    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos
        """
        self.modelo = ['A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio']

    def programa(self, percepción):
        robot, situación = percepción

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[' ABCDEF'.find(robot)] = situación

        # Decide sobre el modelo interno
        a, b, c, d, e, f = self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
        return ('nada' if a == b == c == d == e == f == 'limpio' else
                'limpiar' if situación == 'sucio' else
                'ir_der' if robot == 'A' else
                'ir_der' if robot == 'B' else
                'bajar' if robot == 'C' else
                'ir_izq' if robot == 'D' else
                'ir_izq' if robot == 'E' else 'subir')


def prueba_agente(agente):
    entornos_f.imprime_simulación(
        entornos_f.simulador(
            SeisCuartos(),
            agente,
            ['A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'],
            100
        ),
        ['A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio']
    )

def test():
    """
    Prueba del entorno y los agentes
    """
    print("Prueba del entorno con un agente aleatorio")
    prueba_agente(AgenteAleatorio(['subir', 'bajar', 'ir_der', 'ir_izq', 'limpiar', 'nada']))

    print("Prueba del entorno con un agente reactivo")
    prueba_agente(AgenteReactivoSeisCuartos())

    print("Prueba del entorno con un agente reactivo con modelo")
    prueba_agente(AgenteReactivoModeloSeisCuartos())
    

if __name__ == "__main__":
    test()