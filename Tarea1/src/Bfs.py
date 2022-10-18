import sys


from Route import Route


class Bfs(object):
    

    def __init__(self, nodeStart, nodeEnd):
        """
        Parameters
        ----------
        nodeStart : Node Object, obligatorio
            Nodo de inicio de la ruta.

        nodeEnd : Node Object, obligatorio
            Nodo final de la ruta.
        """
        self.iteration = 0
        self.iterationList = {}
        self.routeList = []
        self.nodeStart = nodeStart
        self.nodeEnd = nodeEnd
        self.valueMin = 0
        self.routeMin = False
        self.exit = True

    def run(self):
        """ Método principal """
        while (self.exit):
            self.iteration += 1
            self.routeslist = []
            self.setRouteInitialNode() if (len(self.iterationList) == 0) else self.searchNode()
            self.printIterationList()

    def setRouteInitialNode(self):
        """
        Inicializar ruta con nodo de inicio.
        """
        route = Route(self.nodeStart.name, self.nodeStart.estimatedCost, 0, self.iteration, self.nodeStart)
        self.routeslist.append(route)
        self.iterationList[self.iteration] = self.routeslist

    def searchNode(self):
        """
        Buscar nodo por ruta óptima
        """
        self.evaluateMininiumRoute()
        
        for r in self.iterationList[self.iteration-1]:
            if (r.name == self.routeMin):
                self.checkingRouteChildNodes(r)

        self.iterationList[self.iteration] = self.routeslist

    def checkingRouteChildNodes(self, route):
        """
        Evaluando la ruta optima de los nodos hijos
        Parameters:
        -----------
        route: Ruta, obligatorio
        """
        childrens = route.node.getChildrenNodes()
        self.validateResultFound(route.node.name, self.nodeEnd.name)
        for child in childrens:
            nameRoute = self.routeMin + "->" + child.name
            estimatedCost = route.node.estimatedCost 
            value = child.estimatedCost
            route = Route(nameRoute, value, estimatedCost, self.iteration, child)
            self.routeslist.append(route)


    def validateResultFound(self, routeName, nodeSearch):
        """
        Validar si llegamos al nodo final.

        Parameters
        -----------
        routeName : str, obligatorio
            nombre del nodo actual que tiene el recorrido (ruta).

        nodeSearch : str, obligatorio
            nombre del nodo destino final.

        """
        if (routeName == nodeSearch):
            self.exit = False


    def printIterationList(self):
        """
        Imprimir en pantalla la lista de rutas seleccionadas.
        """
        print("[%s] " % (self.iteration), end='')
        counter = 0
        total = len(self.iterationList[self.iteration])
        for r in self.iterationList[self.iteration]:
            counter += 1
            print("%s: %s" % (r.name, r.value), end='') if (
                counter == total) else print("%s: %s, " % (r.name, r.value), end='')
        print("")

    def evaluateMininiumRoute(self):
        """
        Evaluar la ruta de menor esfuerzo
        """
        counter = 0
        for route in self.iterationList[self.iteration-1]:
            counter += 1
        if (counter == 1):
            self.valueMin = route.value
            self.routeMin = route.name
        else:
            for route in self.iterationList[self.iteration-1]:
                if (route.value < self.valueMin):
                    self.valueMin = route.value
                    self.routeMin = route.name

        self.print_highlight(self.routeMin, self.valueMin)

    def print_highlight(self, routeMin, valueMin):
        """
        Imprimir ruta optima en color amarillo.

        Parameters
        ----------
        routeMin : str, obligatorio
            Nombre de ruta optima (secuencia de nodos)

        valueMin : int, obligatorio
            Valor mínimo de la ruta óptima
        """
        CYELLOW = '\33[33m'
        CEND = '\033[0m'
        print("{}Recorrido Minimo : {} : {} {}\n".format(
            CYELLOW, routeMin, valueMin, CEND))
