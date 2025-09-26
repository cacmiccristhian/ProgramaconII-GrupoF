# Importación de librerías necesarias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Lista para almacenar los datos de pacientes en memoria
pacienteDataP = []

# Función para enmascarar y validar la fecha de nacimiento
def enmascarar_fecha(texto):
    limpio = ''.join(filter(str.isdigit, texto))  # Elimina caracteres no numéricos
    formato_final = ""

    # Limita la longitud a 8 dígitos (ddmmaaaa)
    if len(limpio) > 8:
        limpio = limpio[:8]

    # Aplica formato dd-mm-aaaa
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio 

    # Actualiza el campo si el formato cambió
    if fechaN.get() != formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)

    # Calcula la edad si la fecha es válida
    if len(fechaN.get()) == 10:
        fecha_actual = datetime.now().date()
        fecha_nacimiento = datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        edad = fecha_actual.year - fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True

# Función para guardar todos los pacientes en un archivo .txt
def guardarEnArchivoP():
    with open("EstaturaPaciente.txt", "w", encoding="utf-8") as archivo:
        for pacienteP in pacienteDataP:
            archivo.write(
                f"{pacienteP['Nombre']}|"
                f"{pacienteP['Fecha de Nacimiento']}|"
                f"{pacienteP['Edad']}|"
                f"{pacienteP['Estatura']}|"
                f"{pacienteP['Género']}|"
                f"{pacienteP['Grupo Sanguíneo']}|"
                f"{pacienteP['Tipo de Seguro']}|"
                f"{pacienteP['Centro Médico']}\n"
            )

# Función para registrar un nuevo paciente
def registrarPaciente():
    # Obtiene los valores ingresados
    nombre = nombreP.get()
    fecha = fechaN.get()
    edad = edadVar.get()
    estatura = entryEstatura.get()
    genero_valor = genero.get()
    grupo = entryGrupoS.get()
    seguro = tipoSeguro.get()
    centro = centroM.get()

    # Verifica que los campos obligatorios estén completos
    if not nombre or not fecha or not edad or not estatura:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos obligatorios.")
        return

    # Crea un diccionario con los datos del paciente
    paciente = {
        "Nombre": nombre,
        "Fecha de Nacimiento": fecha,
        "Edad": edad,
        "Estatura": estatura,
        "Género": genero_valor,
        "Grupo Sanguíneo": grupo,
        "Tipo de Seguro": seguro,
        "Centro Médico": centro
    }

    # Agrega el paciente a la lista y actualiza el archivo
    pacienteDataP.append(paciente)
    guardarEnArchivoP()

    # Muestra el paciente en el Treeview
    treeview.insert("", "end", values=(nombre, fecha, edad, estatura, genero_valor, grupo, seguro, centro))
    messagebox.showinfo("Registro exitoso", "Datos guardados correctamente.")

# Función para eliminar paciente seleccionado
def eliminarPaciente():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione un paciente para eliminar.")
        return

    for item in seleccionado:
        valores = treeview.item(item, "values")
        nombre = valores[0]
        fecha = valores[1]

        # Elimina del Treeview
        treeview.delete(item)

        # Elimina de la lista interna
        pacienteDataP[:] = [p for p in pacienteDataP if not (p["Nombre"] == nombre and p["Fecha de Nacimiento"] == fecha)]

    # Actualiza el archivo
    guardarEnArchivoP()
    messagebox.showinfo("Eliminado", "Paciente eliminado correctamente.")

# Configuración de la ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Registro de Pacientes")
ventanaPrincipal.geometry("890x600")

# Crea pestaña de pacientes
pestañas = ttk.Notebook(ventanaPrincipal)
framePacientes = ttk.Frame(pestañas)
pestañas.add(framePacientes, text="Pacientes")
pestañas.pack(expand=True, fill="both")

# Campos de entrada
labelNombre = tk.Label(framePacientes, text=" Nombre Completo:")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP = tk.Entry(framePacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")

labelFechaN = tk.Label(framePacientes, text=" Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w")
validacion_fecha = ventanaPrincipal.register(enmascarar_fecha)
fechaN = ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")

labelEdad = tk.Label(framePacientes, text=" Edad:")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar = tk.StringVar()
edadP = tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")

labelEstatura = tk.Label(framePacientes, text=" Estatura (cm):")
labelEstatura.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entryEstatura = tk.Entry(framePacientes)
entryEstatura.grid(row=3, column=1, padx=5, pady=5, sticky="w")

labelGenero = tk.Label(framePacientes, text=" Género:")
labelGenero.grid(row=4, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino")
radioMasculino = ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=4, column=1, padx=5, sticky="w")
radioFemenino = ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=5, column=1, padx=5, sticky="w")

labelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:")
labelGrupoS.grid(row=6, column=0, padx=5, pady=5, sticky="w")
entryGrupoS = tk.Entry(framePacientes)
entryGrupoS.grid(row=6, column=1, padx=5, pady=5, sticky="w")

labelTipoS = tk.Label(framePacientes, text=" Tipo de Seguro:")
labelTipoS.grid(row=7, column=0, padx=5, pady=5, sticky="w")
tipoSeguro = tk.StringVar()
tipoSeguro.set("Público")
comboTipoS = ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoS.grid(row=7, column=1, padx=5, pady=5, sticky="w")

labelCentroM = tk.Label(framePacientes, text=" Centro Médico:")
labelCentroM.grid(row=8, column=0, padx=5, pady=5, sticky="w")
centroM = tk.StringVar()
centroM.set("Hospital Central")
comboCentroM = ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Salud Sur"], textvariable=centroM)
comboCentroM.grid(row=8, column=1, padx=5, pady=5, sticky="w")

# Botones de acción
btnFrame = tk.Frame(framePacientes)
btnFrame.grid(row=9, column=1, columnspan=2, pady=5, sticky="w")

btnRegistrar = tk.Button(btnFrame, text="Registrar", bg="#007BFF", fg="white", command=registrarPaciente)
btnRegistrar.grid(row=0, column=0, padx=5)
btnEliminar = tk.Button(btnFrame, text="Eliminar", bg="#C82333", fg="white", command=eliminarPaciente)
btnEliminar.grid(row=0, column=1, padx=5)

# Tabla para mostrar pacientes
treeview = ttk.Treeview(framePacientes, columns=("Nombre", "FechaN", "Edad", "Estatura", "Género", "GrupoS", "TipoS", "CentroM"), show="headings")
# Configuración de columnas del Treeview
treeview.heading("Nombre", text="Nombre")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Estatura", text="Estatura (cm)")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.column("Nombre", width=200)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50)
treeview.column("Estatura", width=80)
treeview.column("Género", width=100)
treeview.column("GrupoS", width=100)
treeview.column("TipoS", width=100)
treeview.column("CentroM", width=150)

# Ubicación del Treeview en la cuadrícula
treeview.grid(row=10, column=0, columnspan=4, padx=5, pady=5)

# Scrollbar vertical para el Treeview
scrollbar = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=10, column=4, sticky="ns")

# Ejecuta el bucle principal de la aplicación
ventanaPrincipal.mainloop()
