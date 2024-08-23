import tkinter as tk 

# Funcion para guardar datos 
def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        datos.append(dato)
        entrada.delete(0,tk.END)
        
def info_persona():
    seleccion = lista.curselection()
    if seleccion :
        ventana_secundaria = tk.Toplevel(ventana)
        ventana_secundaria.title("Agregar")
        ventana_secundaria.geometry("300x300")

ventana = tk.Tk()

ventana.title('Menú desplegable')

ventana.geometry('400x400')

#lista para guardar los datos
datos = {"Pereyra Sebastian" : {"DNI": "39313730", "correo": "sebasedotensei@gmail.com", "edad": 28}}

#marco para ver datos guardados
marco = tk.Frame(ventana,bg="red",bd=3)
marco.pack(padx= 20, pady= 20)

#Barra de desplazamiento
scroll = tk.Scrollbar(marco)
scroll.pack(side= tk.RIGHT,fill=tk.Y)

label = tk.Label(ventana,text="ingresar datos ")
label.pack()
#crea la barra donde ingresamos los datos
entrada = tk.Entry(ventana)
entrada.pack()

#crea la lista para agregar datos
lista = tk.Listbox(marco, yscrollcommand= scroll.set)

# agregamos elementos a la lista
for persona in datos():
   lista.insert(tk.END, persona)

lista.pack(side=tk.LEFT , fill= tk.BOTH)

scroll.config(command= lista.yview)

boton = tk.Button(ventana, text="agregar",command= agregar_dato)
boton.pack(pady=10)

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)

barra_menu.add_cascade(label =
'Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal,tearoff=0)

menu_principal.add_cascade(label =
'Agregar Informacion', menu=submenu)

submenu.add_command(label = 'Edad')

submenu.add_command(label = 'Nombre')

submenu.add_command(label = 'Apellido')

submenu.add_command(label = 'Correo')

ventana.mainloop()