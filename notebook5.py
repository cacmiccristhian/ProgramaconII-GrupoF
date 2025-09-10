# Importación de librerías
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox

# Lista para almacenar datos de pacientes y doctores
pacienteDataP = []
doctorDataD = []

# Función para enmascarar fecha
def enmascararFecha(texto):
    limpio = "".join(filter(str.isdigit, texto))  # Limpio = 123456
    formatoFinal = ""  # Variable que guardará la fecha en formato válido
    if len(limpio) > 8:  # 01-12-2012
        limpio = limpio[:8]  # Si limpio tiene más de 8 números, solamente tomará en cuenta los primeros 8
    if len(limpio) > 4:  # 12112  12  -      11-2
        formatoFinal = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}" 
    elif len(limpio) > 2:  # Limpio = 121 12-1
        formatoFinal = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formatoFinal = limpio
    if fechaN.get() != formatoFinal:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formatoFinal)
    if len(fechaN.get()) == 10:
        fechaActual = datetime.now().date()
        fechaNacimiento = datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        edad = fechaActual.year - fechaNacimiento.year  # 2025 - 2012
        edadVar.set(edad)
    else:
        edadVar.set("")

    return True
# Función para guardar en archivo (Pacientes)
def guardarEnArchivoP():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for pacienteP in pacienteDataP:
            archivo.write(
                f"{pacienteP['Nombre']}|"
                f"{pacienteP['Fecha de Nacimiento']}|"
                f"{pacienteP['Edad']}|"
                f"{pacienteP['Género']}|"
                f"{pacienteP['Grupo Sanguíneo']}|"
                f"{pacienteP['Tipo de Seguro']}|"
                f"{pacienteP['Centro Médico']}\n"
            )

# Función para guardar en archivo (Doctores)
def guardarEnArchivoD():
    with open("Doctores.txt", "w", encoding="utf-8") as archivo:
        for doctorD in doctorDataD:
            archivo.write(
                f"{doctorD['Nombre']}|"
                f"{doctorD['Especialidad']}|"
                f"{doctorD['Edad']}|"
                f"{doctorD['Teléfono']}\n"
            )

def cargaDesdeArchivo():
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            pacienteDataP.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6]
                    }
                    pacienteDataP.append(paciente)
        cargarTreeview()
    except FileNotFoundError:
        open("paciente.txt", "w", encoding="utf-8").close()
# Función para registrar paciente
def registrarPaciente():
    # Crear un diccionario con los datos ingresados
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Género": genero.get(),
        "Grupo Sanguíneo": entryGrupoS.get(),
        "Tipo de Seguro": tipoSeguro.get(),
        "Centro Médico": centroM.get()
    }
    # Agregar paciente a la lista
    pacienteDataP.append(paciente)
    # Guardar en archivo
    guardarEnArchivoP()
    # Cargar el Treeview
    cargarTreeview()
def eliminarPaciente():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showinfo("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
        return

    indice = int(seleccionado[0])
    idItem = seleccionado[0]
    if messagebox.askyesno("Eliminar Paciente", f"¿Estás seguro de que deseas eliminar este paciente '{treeview.item(idItem, 'values')[0]}'?"):
        del pacienteDataP[indice]
        guardarEnArchivoP()  # Guardar los cambios en el archivo
        cargarTreeview()
        messagebox.showinfo("Paciente Eliminado", "El paciente ha sido eliminado exitosamente.")
# Función para cargar datos en el Treeview
def cargarTreeview():
    # Limpiar el Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    # Insertar cada paciente
    for i, item in enumerate(pacienteDataP):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"]
            )
        )

# Función para cargar datos desde archivo (Doctores)
def cargarDesdeArchivoD():
    try:
        with open("Doctores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:  # Validar que haya 4 campos
                    doctorD = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Teléfono": datos[3]
                    }
                    doctorDataD.append(doctorD)
        cargarTreeviewD()
    except FileNotFoundError:
        messagebox.showwarning("Archivo no encontrado", "El archivo Doctores.txt no existe. Se creará uno nuevo al guardar datos.")


# Actualización de la función registrarDoctor para guardar en archivo y actualizar el Treeview
def registrarDoctor():
    # Crear un diccionario con los datos ingresados
    doctorD = {
        "Nombre": nombreD.get(),
        "Especialidad": especialidad.get(),
        "Edad": edadD.get(),
        "Teléfono": telefono.get()
    }
    # Agregar doctor a la lista
    doctorDataD.append(doctorD)
    # Guardar en archivo
    guardarEnArchivoD()
    # Cargar el Treeview
    cargarTreeviewD()

# Función para cargar datos en el Treeview (Doctores)
def cargarTreeviewD():
    # Limpiar el Treeview
    for doctorD in treeviewD.get_children():
        treeviewD.delete(doctorD)
    # Insertar cada doctor
    for i, itemD in enumerate(doctorDataD):
        treeviewD.insert(
            "", "end", iid=str(i),
            values=(
                itemD["Nombre"],
                itemD["Especialidad"],
                itemD["Edad"],
                itemD["Teléfono"]
            )
        )

# Crear ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("1430x600")
ventanaPrincipal.configure(bg="#3ADBFB")

# Crear contenedor NoteBook (pestañas)
pestañas = ttk.Notebook(ventanaPrincipal)

# Crear frames (uno por pestaña)
framePacientes = ttk.Frame(pestañas)
frameDoctores = ttk.Frame(pestañas)

# Agregar pestañas al NoteBook
pestañas.add(framePacientes, text="Pacientes")
pestañas.add(frameDoctores, text="Doctores")

# Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

# Nombre
labelNombre = tk.Label(framePacientes, text=" Nombre Completo:")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP = tk.Entry(framePacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Fecha de nacimiento
labelFechaN = tk.Label(framePacientes, text=" Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w")
fechaN = tk.Entry(framePacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
fechaN.bind('<KeyRelease>', lambda event: enmascararFecha(fechaN.get()))

# Edad (readonly)
labelEdadP = tk.Label(framePacientes, text=" Edad:")
labelEdadP.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar = tk.StringVar()
edadP = tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Género
labelGenero = tk.Label(framePacientes, text=" Género:")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino")  # Valor por defecto
radioMasculino = ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")
radioFemenino = ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")

# Grupo sanguíneo
labelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:")
labelGrupoS.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entryGrupoS = tk.Entry(framePacientes)
entryGrupoS.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Tipo de seguro
labelTipoS = tk.Label(framePacientes, text=" Tipo de Seguro:")
labelTipoS.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipoSeguro = tk.StringVar()
tipoSeguro.set("Público")  # Valor por defecto
comboTipoS = ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoS.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Tipo de centro médico
labelCentroM = tk.Label(framePacientes, text=" Centro Médico:")
labelCentroM.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centroM = tk.StringVar()
centroM.set("Hospital Central")  # Valor por defecto
comboCentroM = ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Salud Sur"], textvariable=centroM)
comboCentroM.grid(row=7, column=1, padx=5, pady=5, sticky="w")

# Frame para los botones
btnFrame = tk.Frame(framePacientes)
btnFrame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")

# Botón Registrar
btnRegistrar = tk.Button(btnFrame, text="Registrar", bg="#45D042", fg="white", command=registrarPaciente)
btnRegistrar.grid(row=0, column=0, padx=5)

# Botón Eliminar
btnEliminar = tk.Button(btnFrame, text="Eliminar", bg="#E83333", fg="White", command=eliminarPaciente)
btnEliminar.grid(row=0, column=1, padx=5)

# Treeview para mostrar los pacientes
treeview = ttk.Treeview(framePacientes, columns=("Nombre", "FechaN", "Edad", "Género", "GrupoS", "TipoS", "CentroM"), show="headings")
treeview.heading("Nombre", text="Nombre")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.grid(row=9, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# Scrollbar vertical
scrollY = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scrollY.set)
scrollY.grid(row=9, column=2, sticky="ns")

# Frame para Doctores 
# Nombre
labelNombreD = tk.Label(frameDoctores, text=" Nombre Completo:")
labelNombreD.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreD = tk.Entry(frameDoctores)
nombreD.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Especialidad
labelEspecialidad = tk.Label(frameDoctores, text=" Especialidad:")
labelEspecialidad.grid(row=1, column=0, padx=5, pady=5, sticky="w")
especialidad = tk.StringVar()
comboEspecialidad = ttk.Combobox(frameDoctores, textvariable=especialidad, values=["Cardiología", "Neurología", "Dermatología", "Ginecología"])
comboEspecialidad.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad
labelEdadD = tk.Label(frameDoctores, text=" Edad:")
labelEdadD.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadD = tk.Spinbox(frameDoctores, from_=18, to=100, width=5)
edadD.grid(row=2, column=1, padx=5, pady=5, sticky="w")
# Teléfono
labelTelefono = tk.Label(frameDoctores, text=" Teléfono:")
labelTelefono.grid(row=3, column=0, padx=5, pady=5, sticky="w")
telefono = tk.Entry(frameDoctores)
telefono.grid(row=3, column=1, padx=5, pady=5, sticky="w")
# Frame para los botones
btnFrameD = tk.Frame(frameDoctores)
btnFrameD.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")
# Botón registrar 
btnRegistrarD = tk.Button(btnFrameD, text="Registrar",bg="#45D042", fg="white", command=registrarDoctor)
btnRegistrarD.grid(row=0, column=0, padx=5)
# Botón Eliminar
btnEliminarD = tk.Button(btnFrameD, text="Eliminar", bg="#E83333", fg="White", command="")
btnEliminarD.grid(row=0, column=1, padx=5)
# Treeview para mostrar los doctores
treeviewD = ttk.Treeview(frameDoctores, columns=("Nombre","Especialidad","Edad", "Teléfono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Teléfono", text="Teléfono")
treeviewD.grid(row=9, column=2, columnspan=2, padx=5, pady=10, sticky="nsew")

scrollYD = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scrollYD.set)
scrollYD.grid(row=9, column=4, sticky="ns")
# Cargar datos desde archivo al iniciar la aplicación
cargaDesdeArchivo()
cargarDesdeArchivoD()
ventanaPrincipal.mainloop()