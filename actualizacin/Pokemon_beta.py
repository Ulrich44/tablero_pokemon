from tkinter import *
from pueblo_paleta import mostrar_ventana_paleta
from utiles import limites


ventana = Tk()
ventana.title("Pokemon Go V.000000001")
ventana.update_idletasks()
ancho = ventana.winfo_screenwidth() - 560
alto = ventana.winfo_screenheight() - 560
ventana.geometry("%dx%d%+d%+d" % (560, 560, ancho / 2, alto / 2))


canvas = Canvas(ventana, width=560, height=560)
canvas.pack()
fondo = PhotoImage(file="oak1.gif")
ash = PhotoImage(file="ash_up.gif")
fondo_change = canvas.create_image(280, 280 , image = fondo)

nombre = 0
cajanombre = 0
ash_moves = 0
x_ini = 0
y_ini = 0
func = 1

def mover_ash(evento):
    global ventana, ash, x_ini, y_ini, func, fondo, ash_moves, nombre, shownombre, cajanombre, ventanaP
    if func == 1:
        fondo = PhotoImage(file="oak2.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        func = 2
    elif func == 2:
        fondo = PhotoImage(file="oak3.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        nombre = StringVar()
        nombre.set ("   Ash Ketchum")
        cajanombre = Entry(ventana, textvariable=nombre, bg = "lightgreen")
        cajanombre.pack()
        cajanombre.place(x=30, y=460)
        func = 3
    elif func == 3:
        cajanombre.destroy()
        fondo = PhotoImage(file="oak4.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        shownombre = Label(ventana, text=nombre.get())
        shownombre.pack()
        shownombre.place(x=30, y=400)
        func = 4
    elif func == 4:
        shownombre.destroy()
        fondo = PhotoImage(file="lab_oak.gif")
        canvas.itemconfig(fondo_change, image=fondo)
        ash_moves = canvas.create_image(280, 520, image=ash)
        func = 5
    elif evento.keysym == "Down" and limites(x_ini, y_ini, "Down"):
        ash = PhotoImage(file="ash_down.gif")
        canvas.itemconfig(ash_moves, image = ash)
        canvas.move(2,0,10)
        x_ini -= 10
        if y_ini == 0 and x_ini == 0:
            ventana.quit()
            return mostrar_ventana_paleta()
        print(str(x_ini), str(y_ini))
    elif evento.keysym == "Up" and limites(x_ini, y_ini, "Up"):
        ash = PhotoImage(file="ash_up.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2,0,-10)
        x_ini += 10
        print(str(x_ini), str(y_ini))
    elif evento.keysym == "Left" and limites(x_ini, y_ini, "Left"):
        ash = PhotoImage(file="ash_left.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2,-10,0)
        y_ini -= 10
        if y_ini == 0 and x_ini == 0:
            ventana.quit()
            return mostrar_ventana_paleta()
        print(str(x_ini), str(y_ini))
    elif evento.keysym == "Right" and limites(x_ini, y_ini, "Right"):
        ash = PhotoImage(file="ash_right.gif")
        canvas.itemconfig(ash_moves, image=ash)
        canvas.move(2,10,0)
        y_ini += 10
        if y_ini == 0 and x_ini == 0:
            ventana.quit()
            return mostrar_ventana_paleta()
        print(str(x_ini), str(y_ini))

ventana.bind_all("<Up>", mover_ash)
ventana.bind_all("<Left>", mover_ash)
ventana.bind_all("<Right>", mover_ash)
ventana.bind_all("<Down>", mover_ash)


ventana.mainloop()