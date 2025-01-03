from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32,1.65,2.31,3.22,1.22,1.99,2.05,2.65]
precios_bebida = [0.25,0.99,1.21,1.54,1.08,1.10,2.00,1.58]
precios_postres = [1.54,1.68,1.32,1.97,2.55,2.14,1.94,1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    for x, cuadro in enumerate(cuadros_comida):
        if variables_comida[x].get() == 1:
            cuadro.config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadro.delete(0, END)
            cuadro.focus()
        else:
            cuadro.config(state=DISABLED)
            texto_comida[x].set('0')

    for x, cuadro in enumerate(cuadros_bebida):
        if variables_bebida[x].get() == 1:
            cuadro.config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadro.delete(0, END)
            cuadro.focus()
        else:
            cuadro.config(state=DISABLED)
            texto_bebida[x].set('0')

    for x, cuadro in enumerate(cuadros_postres):
        if variables_postre[x].get() == 1:
            cuadro.config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadro.delete(0, END)
            cuadro.focus()
        else:
            cuadro.config(state=DISABLED)
            texto_postres[x].set('0')

def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get())* precios_comida[p])
        p += 1

    subtotal_bebidas = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebidas = subtotal_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postres = 0
    p = 0
    for cantidad in texto_postres:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = subtotal_comida + subtotal_bebidas + subtotal_postres
    impuestos= subtotal * 0.07
    total1 = subtotal + impuestos
    print(total1)

    var_costo_comida.set(f'$ {round(subtotal_comida,2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebidas, 2)}')
    var_costo_postres.set(f'$ {round(subtotal_postres,2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total1, 2)}')


def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# -{random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}' +'\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'* 75 +'\n')

    x = 0

    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{listas_comidas[x]}\t\t{comida.get()}\t${int(comida.get())* precios_comida[x]}\n')

        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{listas_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get())* precios_bebida[x]}\n')

        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{listas_postres[x]}\t\t{postre.get()}\t${int(postre.get())* precios_postres[x]}\n')

        x += 1

    texto_recibo.insert(END, f'-'* 75 +'\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-'* 75 +'\n')
    texto_recibo.insert(END, f'Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Los esperamos pronto!!')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1200x800+0+0')

#evitar maximizar la pantalla
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title('Mi restaurante -Sistema de Facturación')

#color de fondo de la ventana
aplicacion.config(bg='burlywood')

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief = FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text= 'Sistema de Facturación', fg='azure4',
                        font=('Dosis',58), bg='burlywood', width=0)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4',padx=80)
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas= LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                          bd =1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel Bebidas
panel_bebidas= LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                          bd =1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel Postres
panel_postres= LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                          bd =1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


#Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora= Frame(panel_derecha, bd=1, relief=FLAT, bg='white')
panel_calculadora.pack()


#Panel recibo
panel_recibo= Frame(panel_derecha, bd=1, relief=FLAT, bg='white')
panel_recibo.pack()

#Panel botones
panel_botones= Frame(panel_derecha, bd=1, relief=FLAT, bg='white')
panel_botones.pack()

#Lista de productos
listas_comidas =['Pollo','Cordero', 'Pescado', 'Pizza', 'Salmón','Cerdo', 'Empanadas','Ensalada']
listas_bebidas = ['Agua','Soda','Jugo', 'Coca Cola', 'Sprite', 'Vino', 'Fernet', 'Cerveza']
listas_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Torta','Cheescake', 'Tarta']

# generar items comida
variables_comida =[]
cuadros_comida = []
texto_comida = []
contador = 0

for comida in listas_comidas:

    #crear los checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue = 1,
                         offvalue= 0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador]=StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)



    contador += 1

# generar items bebida
variables_bebida =[]
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in listas_bebidas:

    # crear los checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue = 1,
                         offvalue= 0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada bebida
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador]=StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postre
variables_postre =[]
cuadros_postres = []
texto_postres = []
contador = 0

for postre in listas_postres:

    # crear los checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue = 1,
                         offvalue= 0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada postre
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador]=StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                  column=1)


    contador += 1

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto= StringVar()
var_total = StringVar()

#Etiquetas de costos y campos de entrada comida
etiqueta_costo_comida= Label(panel_costos,
                             text='Costo Comida',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_costo_comida.grid(row=0, column= 0)
#cuadro de entrada
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)

#Etiquetas de costos y campos de entrada bebida
etiqueta_costo_bebida= Label(panel_costos,
                             text='Costo Bebida',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_costo_bebida.grid(row=1, column= 0)
#cuadro de entrada
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)

#Etiquetas de costos y campos de entrada postres
etiqueta_costo_postres= Label(panel_costos,
                             text='Costo Postres',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_costo_postres.grid(row=2, column= 0)
#cuadro de entrada
texto_costo_postres = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1,padx=41)

#Etiquetas de costos y campos de entrada SUBTOTAL
etiqueta_subtotal= Label(panel_costos,
                             text='Subtotal',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_subtotal.grid(row=0, column= 2)
#cuadro de entrada
texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)

#Etiquetas de costos y campos de entrada bebida IMPUESTOS
etiqueta_impuestos= Label(panel_costos,
                             text='Impuetos',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_impuestos.grid(row=1, column= 2)
#cuadro de entrada
texto_impuestos = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuestos.grid(row=1,column=3,padx=41)

#Etiquetas de costos y campos de entrada Total
etiqueta_total= Label(panel_costos,
                             text='TOTAL',
                             font=('Dosis',12,'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_total.grid(row=2, column= 2)
#cuadro de entrada
texto_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)

#botones
botones= ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo =Text(panel_recibo,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=42,
                   height=10)
texto_recibo.grid(row=0, column=0)

#CALCULADORA
visor_calculadora= Entry(panel_calculadora,
                         font=('Dosis',16,'bold'),
                         width=32,
                         bd=1)

visor_calculadora.grid(row=0, column=0,columnspan=4)

botones_calculadora= ['7','8','9','+','4','5','6','-','1','2','3','x','=','Borrar','0','/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column= columna)
    if columna == 3:
        fila +=1

    columna += 1
    if columna == 4:
        columna = 0


botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))





#evitar que la pantalla se cierre
aplicacion.mainloop()