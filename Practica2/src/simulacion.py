import tkinter as tk

basura = "#"
obstaculo = "@"

coordx = 0
coordy = 0
numlo = 0
Cuarto = {}

def left_click(eve):
    eve.widget.config(text=basura)

def right_click(eve):
    eve.widget.config(text=obstaculo)

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

#Inicio de la Simulacion.
bsim = tk.Button(master=form, text="Iniciar simulacion", relief=tk.RAISED)
bsim.place(x=30,y=200)

#Generacion del mapa
mapa = tk.Frame(master=window, width=40*20, height=40*10, borderwidth=1)
mapa.pack()

for i in range(10):
    for j in range(20):
        Loseta = tk.Button(master=mapa, width=4, height=2, text=f"{numlo}", bg="grey", fg="black", relief=tk.RAISED)
        Loseta.bind("<Button-1>", left_click)
        Loseta.bind("<Button-3>", right_click)
        Loseta.place(x=coordx,y=coordy)
        Cuarto[numlo] = Loseta
        coordx+=40
        numlo+=1
    coordx=0
    coordy+=40

window.mainloop()