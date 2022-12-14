import tkinter as tk

basura = "#"
obstaculo = "@"
libre = "-"
botchita = "Q"

coordx = 0
coordy = 0
numlo = 0
Cuarto = {}
Simbolos = {}
pos = 0
prevPosition = 0

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
      
        print("posición anterior: " + str(pos))
        pos += 1
        print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=botchita, fg='pink')
        Cuarto[pos-1].config(text=pos-1, fg='black')
    else:
        print("no me puedo mover más a la derecha")

def izquierda():
    global pos
    par = pos / 10
    if par % 2 != 0:
        print("posición anterior: " + str(pos))
        pos -= 1
        print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=botchita,fg='pink')
        Cuarto[pos+1].config(text=pos+1, fg='black')
    else:
        print("no me puedo mover más a la izquierda")

def abajo():
    global pos

    if(pos + 20 <= 199):
        print("posición anterior: " + str(pos))
        pos += 20
        print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=botchita, fg='pink')
        Cuarto[pos-20].config(text=pos-20, fg='black')
    else:
        print("no me puedo ir más abajo")

def arriba():
    global pos

    if(pos - 20 >= 0):
        print("posición anterior: " + str(pos))
        pos -= 20
        print("posición nueva: " + str(pos))
        Cuarto[pos].config(text=botchita, fg='pink')
        Cuarto[pos+20].config(text=pos+20, fg='black')
    else:
        print("no me puedo ir más arriba")

window = tk.Tk()
window.title("Botchita simulacion")
window.resizable(width=False, height=False)

#Agregar basura a algun Loseta.
form = tk.Frame(master=window, width=200, height=258, borderwidth=1, bg="red")
form.pack(side=tk.LEFT)
#numLosetab = tk.Entry(master=form,width=12)
#numLosetab.place(x=50,y=20)
#bb = tk.Button(master=form, text="Resetear Loseta", relief=tk.RAISED)
#bb.place(x=40,y=50)

#Agregar obstaculos a algun Loseta.
#numLosetaobs = tk.Entry(master=form,width=12)
#numLosetaobs.place(x=50,y=120)
#bo = tk.Button(master=form, text="Agregar un Obstaculo", relief=tk.RAISED)
#bo.place(x=20,y=150)

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

for i in range(10):
    for j in range(20):
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
Cuarto[0].config(text=botchita, fg='pink')

window.mainloop()