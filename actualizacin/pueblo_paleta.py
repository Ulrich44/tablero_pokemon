from tkinter import *

def mostrar_ventana_paleta():
    global contenedor, ventanaB, mover_ash, fondo_change, nombre,\
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, ventanaP, ventana, pueblo_paleta
    ventanaP = Toplevel()
    ventanaP.title("Pueblo_Paleta")
    ventanaP.update_idletasks()

    ancho = ventanaP.winfo_screenwidth() - 660
    alto = ventanaP.winfo_screenheight() - 660
    ventanaP.geometry("%dx%d%+d%+d" % (660, 660, ancho / 2, alto / 2))

    canvas = Canvas(ventanaP, width=660, height=660)
    canvas.pack()
    fondo2 = PhotoImage(file="afueras_pic.gif")
    ash = PhotoImage(file="ash_down.gif")
    canvas.create_image(330, 310, image=fondo2)
    mover_ash = canvas.create_image(470, 420, image=ash)
    nombre = 0
    cajanombre = 0
    ash_moves = 0
    x_ini = 0
    y_ini = 0
    func = 1

    def pueblo_paleta(evento):
        global ventanaP, ventanaB, ash, x_ini, y_ini, func, fondo2, ash_moves, nombre, cajanombre, canvas, mover_ash, Pokemon_beta
        if evento.keysym == "Down":
            ash = PhotoImage(file="ash_down.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Up":
            ash = PhotoImage(file="ash_up.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Left":
            ash = PhotoImage(file="ash_left.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Right":
            ash = PhotoImage(file="ash_right.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))

    ventanaP.bind_all("<Up>", pueblo_paleta)
    ventanaP.bind_all("<Left>", pueblo_paleta)
    ventanaP.bind_all("<Right>", pueblo_paleta)
    ventanaP.bind_all("<Down>", pueblo_paleta)
    ventanaP.mainloop()

def mostrar_ventana_bosque():
    global contenedor, ventanaB, mover_ash, fondo_change, nombre, cajanombre, \
        ash_moves, x_ini, y_ini, func, canvas, ventana_up, ventanaP, ventanaB
    ventanaB = Toplevel()
    ventanaB.title("Bosque_Verde")
    ventanaB.update_idletasks()

    ancho = ventanaB.winfo_screenwidth() - 660
    alto = ventanaB.winfo_screenheight() - 800
    ventanaB.geometry("%dx%d%+d%+d" % (660, 700, ancho / 2, alto / 2))

    canvas = Canvas(ventanaB, width=500, height=700)
    canvas.pack()
    fondo3 = PhotoImage(file="bosque_verde.gif")
    ash = PhotoImage(file="ash_up_min.gif")
    canvas.create_image(250, 350, image=fondo3)
    mover_ash = canvas.create_image(250, 670, image=ash)
    nombre = 0
    cajanombre = 0
    ash_moves = 0
    x_ini = 0
    y_ini = 0
    func = 1

    def bosque_verde(evento):
        global ventanaP, ventanaB, ash, x_ini, y_ini, func, fondo3, ash_moves, nombre, \
            cajanombre, canvas, mover_ash, ventana_up
        if evento.keysym == "Down":
            ash = PhotoImage(file="ash_down_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            if x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                return mostrar_ventana_paleta_up()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Up":
            ash = PhotoImage(file="ash_up_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Left":
            ash = PhotoImage(file="ash_left_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            if x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                return mostrar_ventana_paleta_up()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Right":
            ash = PhotoImage(file="ash_right_min.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            if x_ini == -20 and -30 < y_ini < 30:
                ventanaB.destroy()
                return mostrar_ventana_paleta_up()
            print(str(x_ini), str(y_ini))

    ventanaB.bind_all("<Up>", bosque_verde)
    ventanaB.bind_all("<Left>", bosque_verde)
    ventanaB.bind_all("<Right>", bosque_verde)
    ventanaB.bind_all("<Down>", bosque_verde)
    ventanaB.mainloop()

def mostrar_ventana_paleta_up():
    global contenedor, ventanaB, mover_ash, fondo_change, nombre,\
        cajanombre, ash_moves, x_ini, y_ini, func, canvas, ventanaP, ventana, pueblo_paleta, ventana_up
    ventana_up = Toplevel()
    ventana_up.title("Pueblo_Paleta_up")
    ventana_up.update_idletasks()

    ancho = ventana_up.winfo_screenwidth() - 660
    alto = ventana_up.winfo_screenheight() - 660
    ventana_up.geometry("%dx%d%+d%+d" % (660, 660, ancho / 2, alto / 2))

    canvas = Canvas(ventana_up, width=660, height=660)
    canvas.pack()
    fondo2 = PhotoImage(file="afueras_pic.gif")
    ash = PhotoImage(file="ash_down.gif")
    canvas.create_image(330, 310, image=fondo2)
    mover_ash = canvas.create_image(340, 20, image=ash)
    nombre = 0
    cajanombre = 0
    ash_moves = 0
    x_ini = 0
    y_ini = 0
    func = 1

    def pueblo_paleta_up(evento):
        global ventanaP, ventanaB, ventana_up, ash, x_ini, y_ini, func, fondo2, ash_moves, nombre, cajanombre, canvas, mover_ash, Pokemon_beta
        if evento.keysym == "Down":
            ash = PhotoImage(file="ash_down.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, 10)
            x_ini -= 10
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Up":
            ash = PhotoImage(file="ash_up.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 0, -10)
            x_ini += 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Left":
            ash = PhotoImage(file="ash_left.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, -10, 0)
            y_ini -= 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))
        elif evento.keysym == "Right":
            ash = PhotoImage(file="ash_right.gif")
            canvas.itemconfig(mover_ash, image=ash)
            canvas.move(2, 10, 0)
            y_ini += 10
            if x_ini == 410 and -190 < y_ini < -90:
                ventanaP.destroy()
                return mostrar_ventana_bosque()
            print(str(x_ini), str(y_ini))

    ventana_up.bind_all("<Up>", pueblo_paleta_up)
    ventana_up.bind_all("<Left>", pueblo_paleta_up)
    ventana_up.bind_all("<Right>", pueblo_paleta_up)
    ventana_up.bind_all("<Down>", pueblo_paleta_up)
    ventana_up.mainloop()


