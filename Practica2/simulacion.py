import tkinter as tk
from App import bueno

basura = "#"
obstaculo = "@"
libre = "-"
botchita = "Q"

coordx = 0
coordy = 0
numlo = 0
Cuarto = {}
Simbolos = {}
recBasura = {}
recObstaculos = {}
pos = 0
prevPosition = 0

contadorBasura = 0
contadorObstaculos = 0

def left_click(eve):
    Simbolos[int(eve.widget.cget('text').replace(" ","").replace("\n","").replace("-","").replace("@","").replace("#",""))] = basura
    eve.widget.config(text=eve.widget.cget('text').replace("-",basura).replace("@",basura))

def mid_click(eve):
    Simbolos[int(eve.widget.cget('text').replace(" ","").replace("\n","").replace("#","").replace("@","").replace("-",""))] = libre
    eve.widget.config(text=eve.widget.cget('text').replace("#",libre).replace("@",libre))

def right_click(eve):
    Simbolos[int(eve.widget.cget('text').replace(" ","").replace("\n","").replace("-","").replace("#","").replace("@",""))] = obstaculo
    eve.widget.config(text=eve.widget.cget('text').replace("-",obstaculo).replace("#",obstaculo))

def derecha():
    global pos
    par = (pos - 9) / 10

    if pos % 10 != 9 or pos == 0 or par % 2 == 0 or pos == 9 and pos <= 199:
      
        #print("posición anterior: " + str(pos))
        pos += 1
        #print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=inserta_botchita(pos), fg='orange')
        Cuarto[pos-1].config(text=paso_botchita(pos-1), fg='blue')
        return True
    else:
        #print("no me puedo mover más a la derecha")
        return False

def izquierda():
    global pos
    par = pos / 10
    if par % 2 != 0:
        #print("posición anterior: " + str(pos))
        pos -= 1
        #print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=inserta_botchita(pos),fg='orange')
        Cuarto[pos+1].config(text=paso_botchita(pos+1), fg='blue')
        return True
    else:
        #print("no me puedo mover más a la izquierda")
        return False

def abajo():
    global pos

    if(pos + 20 <= 199):
        #print("posición anterior: " + str(pos))
        pos += 20
        #print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=inserta_botchita(pos), fg='orange')
        Cuarto[pos-20].config(text=paso_botchita(pos-20), fg='blue')
        return True
    else:
        return False
        #print("no me puedo ir más abajo")

def arriba():
    global pos

    if(pos - 20 >= 0):
        #print("posición anterior: " + str(pos))
        pos -= 20
        #print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=inserta_botchita(pos), fg='orange')
        Cuarto[pos+20].config(text=paso_botchita(pos+20), fg='blue')
        return True
    else:
        return False
        #print("no me puedo ir más arriba")

def reconocimiento_der():
    global contadorBasura
    global contadorObstaculos
    if(Simbolos[pos+1] == '#'):
        recBasura[contadorBasura] = pos+1
        contadorBasura += 1
    if(Simbolos[pos+1] == '@'):
        recObstaculos[contadorObstaculos] = pos+1
        contadorObstaculos += 1

    while(derecha()):
        if(Simbolos[pos+1] == '#'):
            recBasura[contadorBasura] = pos+1
            contadorBasura += 1
        if(Simbolos[pos+1] == '@'):
            recObstaculos[contadorObstaculos] = pos+1
            contadorObstaculos += 1
def reconocimiento_izq():
    global contadorBasura
    global contadorObstaculos
    if(Simbolos[pos-1] == '#'):
        recBasura[contadorBasura] = pos-1
        contadorBasura += 1
    if(Simbolos[pos-1] == '@'):
        recObstaculos[contadorObstaculos] = pos-1
        contadorObstaculos += 1

    while(izquierda()):
        if(Simbolos[pos-1] == '#'):
            recBasura[contadorBasura] = pos-1
            contadorBasura += 1
        if(Simbolos[pos-1] == '@'):
            recObstaculos[contadorObstaculos] = pos-1
            contadorObstaculos += 1

def reconocimiento():

    global contadorBasura
    global contadorObstaculos
    global pos

    while(pos!=180):
        reconocimiento_der()
        abajo()
        reconocimiento_izq()
        if(pos!=180):
            abajo()

    if(Simbolos[pos] == '#'):
        recBasura[contadorBasura] = pos
        contadorBasura += 1
    if(Simbolos[pos] == '@'):
        recObstaculos[contadorObstaculos] = pos
        contadorObstaculos += 1

    print("Hay basura en las posiciones: ")
    for basura in recBasura:
        print(recBasura[basura])
    print("Hay obstaculos en las posiciones: ")
    for obstaculos in recObstaculos:
        print(recObstaculos[obstaculos])

    bsim = tk.Button(master=form, text="Limpiar", relief=tk.RAISED, command=algor)
    bsim.place(x=30,y=230)
    mueve(0)
    return recBasura

def mueve(nuevaPos):
    global pos

    Cuarto[int(nuevaPos)].config(text=inserta_botchita(int(nuevaPos)), fg='orange')
    Cuarto[int(pos)].config(text=paso_botchita(pos), fg='blue')
    pos = int(nuevaPos)

def algor():
    global pos
    avr = bueno()
    print("Ruta del roomba: "+avr)
    ruta = avr.split("-")
    print(ruta)
    for loseta in ruta:
        mueve(loseta)
    Simbolos[pos] = libre
    print("limpie la posición: " + str(pos))
    limpia_botchita(pos)

def inserta_botchita(n):
    info = Cuarto[n].cget('text')
    sim = Simbolos[n]
    lugar = info.find(sim)
    return info[:lugar] + botchita + "\n" + info[lugar:]

def paso_botchita(n):
    linea = Cuarto[n].cget('text').replace(botchita,"")
    linea = linea.replace("\n","").replace(" ","")
    linea = linea[:len(linea)-1] + "\n" + linea[len(linea)-1]
    return linea

def limpia_botchita(n):
    losetalimpia = Cuarto[n].cget('text').replace(basura,libre)
    losetalimpia = losetalimpia.replace("\n","").replace(" ","")
    losetalimpia = losetalimpia[:len(losetalimpia)-2] + "\n" + botchita + "\n" + losetalimpia[len(losetalimpia)-1]
    Cuarto[n].config(text=losetalimpia, fg='orange')

window = tk.Tk()
window.title("Botchita simulacion")
window.resizable(width=False, height=False)

#Agregar basura a algun Loseta.
form = tk.Frame(master=window, width=200, height=258, borderwidth=1, bg="red")
form.pack(side=tk.LEFT)

#Moverse derecha
bsim = tk.Button(master=form, text="►", relief=tk.RAISED, command= derecha)
bsim.place(x=110,y=100)

#Moverse izquierda
bsim = tk.Button(master=form, text="◄", relief=tk.RAISED, command= izquierda)
bsim.place(x=50,y=100)

#Moverse abajo
bsim = tk.Button(master=form, text="▼", relief=tk.RAISED, command= abajo)
bsim.place(x=80,y=130)

#Moverse arriba
bsim = tk.Button(master=form, text="▲", relief=tk.RAISED, command= arriba)
bsim.place(x=80,y=70)

#Generacion del mapa
mapa = tk.Frame(master=window, width=40*20, height=40*10, borderwidth=1)
mapa.pack()

#Inicio de la Simulacion.
bsim = tk.Button(master=form, text="Iniciar simulacion", relief=tk.RAISED, command=reconocimiento)
bsim.place(x=30,y=200)

for i in range(10):
    for j in range(20):
        if(numlo == 42):
            Loseta = tk.Button(master=mapa, width=4, height=2, text=f"{numlo} \n #", bg="grey", fg="green", relief=tk.RAISED)
        else:
            Loseta = tk.Button(master=mapa, width=4, height=2, text=f"{numlo} \n -", bg="grey", fg="black", relief=tk.RAISED)
        Loseta.bind("<Button-1>", left_click)
        Loseta.bind("<Button-2>", mid_click)
        Loseta.bind("<Button-3>", right_click)
        Loseta.place(x=coordx,y=coordy)
        Simbolos[numlo] = "-"
        Cuarto[numlo] = Loseta
        coordx+=40
        numlo+=1
    coordx=0
    coordy+=40
Cuarto[0].config(text=inserta_botchita(0), fg='orange')

Simbolos[42] = basura

window.mainloop()