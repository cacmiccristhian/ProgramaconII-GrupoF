import tkinter as tk
from tkinter import messagebox
# Pacientes
def nuevoPaciente():
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Pacientes")
    ventanaRegistro.geometry("600x450")
    ventanaRegistro.configure(bg="#8D8C8C")
    #Nombre
    nombreLabel = tk.Label(ventanaRegistro, text="Nombre: ",bg="#8D8C8C")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5,sticky="w") # n=norte, s=sur, e=este, w=oeste
    entradaNombre = tk.Entry(ventanaRegistro)
    entradaNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #Dirección
    direccionLabel = tk.Label(ventanaRegistro, text="Dirección: ",bg="#8D8C8C")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entradaDireccion = tk.Entry(ventanaRegistro)
    entradaDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #Teléfono
    telefonoLabel = tk.Label(ventanaRegistro, text="Teléfono: ",bg="#8D8C8C")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entradaTelefono = tk.Entry(ventanaRegistro)
    entradaTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    #sexo
    sexoLabel = tk.Label(ventanaRegistro, text="Sexo: ",bg="#8D8C8C")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5,sticky="w")
    Sexo = tk.StringVar(value="Masculino")# Es una variable especial de Tkinter que se utiliza para enlazar widgets como RadioButtons
    rbMasculino = tk.Radiobutton(ventanaRegistro, text="Masculino", variable=Sexo, value="Masculino")
    rbMasculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    rbFemenino = tk.Radiobutton(ventanaRegistro, text="Femenino", variable=Sexo, value="Femenino")
    rbFemenino.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    #Enfermedades
    enfLabel = tk.Label(ventanaRegistro, text="Enfermedades base: ",bg="#8D8C8C")
    enfLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes = tk.BooleanVar()
    hipertension = tk.BooleanVar()
    asma = tk.BooleanVar()
    cbDiabetes = tk.Checkbutton(ventanaRegistro, text="Diabetes", variable=diabetes, bg="#8D8C8C")      
    cbDiabetes.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    cbHipertension = tk.Checkbutton(ventanaRegistro, text="Hipertensión", variable=hipertension, bg="#8D8C8C")
    cbHipertension.grid(row=6, column=1, padx=10, pady=5, sticky="w") 
    cbAsma = tk.Checkbutton(ventanaRegistro, text="Asma", variable=asma, bg="#8D8C8C")
    cbAsma.grid(row=7, column=1, padx=10, pady=5, sticky="w")
    # Cadena para mostrar todos los datos del formulario
    def registrarDatos():
        enfermedades = []
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertensión")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades) > 0:
            enfermedadesTexto = ", ".join(enfermedades)
        else:
            enfermedadesTexto = "Ninguna"
        info = (
            f"Nombre: {entradaNombre.get()}\n"
            f"Dirección: {entradaDireccion.get()}\n"
            f"Teléfono: {entradaTelefono.get()}\n"
            f"Sexo: {Sexo.get()}\n"
            f"Enfermedades: {enfermedadesTexto}\n"
        )
        messagebox.showinfo("Datos Registrados", info,)
        ventanaRegistro.destroy() #Cierra la ventana tras el mensaje
    btnRegistrar = tk.Button(ventanaRegistro, text="Registrar", command=registrarDatos)
    btnRegistrar.grid(row=9, columnspan=2, pady=15,)
def BuscarPaciente():
    messagebox.showinfo("BuscarPaciente","Busqueda de Paciente")
def EliminarPaciente():
    messagebox.showinfo("EliminarPaciente","Eliminación de Paciente")
# Doctores
def nuevoDoctor():
    ventanaDoctor = tk.Toplevel(ventanaPrincipal)
    ventanaDoctor.title("Registro de Doctores")
    ventanaDoctor.geometry("550x500")
    ventanaDoctor.configure(bg="#50CDFF")
    tk.Label(ventanaDoctor, text="Nombre completo:",bg="#50CDFF").grid(row=0, column=0, sticky="w", pady=5, padx=10)
    entry_nombre = tk.Entry(ventanaDoctor)
    entry_nombre.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=5)

    tk.Label(ventanaDoctor, text="Dirección:",bg="#50CDFF").grid(row=1, column=0, sticky="w", pady=5, padx=10)
    entry_direccion = tk.Entry(ventanaDoctor)
    entry_direccion.grid(row=1, column=1, columnspan=3, sticky="w", padx=10, pady=8)

    def solo_numeros(char):
        return char.isdigit() or char == ""
    vcmd = ventanaDoctor.register(solo_numeros)
    tk.Label(ventanaDoctor, text="Teléfono:",bg="#50CDFF").grid(row=2, column=0, sticky="w", pady=8, padx=10)
    entry_telefono = tk.Entry(ventanaDoctor, validate="key", validatecommand=(vcmd, '%P'))
    entry_telefono.grid(row=2, column=1, columnspan=3, sticky="w", padx=10, pady=8)

    tk.Label(ventanaDoctor, text="Especialidad:",bg="#50CDFF").grid(row=3, column=0, sticky="w", pady=8, padx=10)
    especialidad_var = tk.StringVar(value="Pediatría")
    tk.Radiobutton(ventanaDoctor, text="Pediatría",bg="#50CDFF", variable=especialidad_var, value="Pediatría").grid(row=4, column=1, sticky="w", padx=10, pady=4)
    tk.Radiobutton(ventanaDoctor, text="Cardiología",bg="#50CDFF", variable=especialidad_var, value="Cardiología").grid(row=5, column=1, sticky="w", padx=10, pady=4)
    tk.Radiobutton(ventanaDoctor, text="Neurología",bg="#50CDFF", variable=especialidad_var, value="Neurología").grid(row=6, column=1, sticky="w", padx=10, pady=4)
    tk.Radiobutton(ventanaDoctor, text="Otro:",bg="#50CDFF", variable=especialidad_var, value="Otro").grid(row=7, column=1, sticky="w", padx=10, pady=4)
    entry_otro = tk.Entry(ventanaDoctor, state="disabled")
    entry_otro.grid(row=7, column=2, sticky="w", padx=10, pady=4)
    def actualizar_otro(*args):
        if especialidad_var.get() == "Otro":
            entry_otro.config(state="normal")
        else:
            entry_otro.delete(0, tk.END)
            entry_otro.config(state="disabled")
    especialidad_var.trace_add("write", actualizar_otro)

    tk.Label(ventanaDoctor, text="Disponibilidad:",bg="#50CDFF").grid(row=8, column=0, sticky="w", pady=8, padx=10)
    var_manana = tk.BooleanVar()
    var_tarde = tk.BooleanVar()
    var_noche = tk.BooleanVar()
    tk.Checkbutton(ventanaDoctor, text="Mañana",bg="#50CDFF", variable=var_manana).grid(row=9, column=1, sticky="w", padx=10, pady=5)
    tk.Checkbutton(ventanaDoctor, text="Tarde",bg="#50CDFF", variable=var_tarde).grid(row=10, column=1, sticky="w", padx=10, pady=5)
    tk.Checkbutton(ventanaDoctor, text="Noche",bg="#50CDFF", variable=var_noche).grid(row=11, column=1, sticky="w", padx=10, pady=5)

    def registrarDoctor():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        especialidad = especialidad_var.get()
        if especialidad == "Otro":
            especialidad = entry_otro.get()
        disponibilidad = []
        if var_manana.get():
            disponibilidad.append("Mañana")
        if var_tarde.get():
            disponibilidad.append("Tarde")
        if var_noche.get():
            disponibilidad.append("Noche")
        datos = (
            f"Nombre completo: {nombre}\n"
            f"Dirección: {direccion}\n"
            f"Teléfono: {telefono}\n"
            f"Especialidad: {especialidad}\n"
            f"Disponibilidad: {', '.join(disponibilidad)}"
        )
        messagebox.showinfo("Datos Registrados", datos)
        ventanaDoctor.destroy()

    frame_botones = tk.Frame(ventanaDoctor, bg="#50CDFF")
    frame_botones.grid(row=12, column=0, columnspan=4, pady=20)
    tk.Button(frame_botones, text="Registrar", command=registrarDoctor, width=15).pack(side="left", padx=10)
    tk.Button(frame_botones, text="Salir", command=ventanaDoctor.destroy, width=15).pack(side="left", padx=10)
def BuscarDoctor():
    messagebox.showinfo("BuscarDoctor","Busqueda de Doctor")
def EliminarDoctor():
    messagebox.showinfo("EliminarDoctor","Eliminación de Doctor")
    
#Ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x450")
ventanaPrincipal.configure(bg="#BBBBBB")

#Barra de menu
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)

#Barra de pacientes
menuPacientes = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente",command=BuscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command=EliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir",command=ventanaPrincipal.quit)

#Barra de doctores
menuDoctores = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command=nuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor",command=BuscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor",command=EliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=ventanaPrincipal.quit)
#Barra de Ayuda
menuAyuda = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de...",command=lambda:messagebox.showinfo("Acerca de...","V: Prueba 1.0\nby: Bcrra_"))
menuAyuda.add_separator()
menuAyuda.add_command(label="Salir",command=ventanaPrincipal.quit)
ventanaPrincipal.mainloop()