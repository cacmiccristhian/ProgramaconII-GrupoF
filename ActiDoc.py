import tkinter as tk
from tkinter import ttk, messagebox

# Función para registrar doctor
def registrarDoctor():
    nombre = entryNombreD.get()
    especialidad = especialidadD.get()
    anios_servicio = entryAniosServicioD.get()
    sexo = sexoD.get()
    hospital = hospitalD.get()

    if not nombre or not especialidad or not anios_servicio or not sexo or not hospital:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        return

    # Insertar en Treeview
    treeviewD.insert("", "end", values=(nombre, especialidad, anios_servicio, sexo, hospital))

    # Guardar en archivo TXT
    with open("doctores_registrados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}, {especialidad}, {anios_servicio} años, {sexo}, {hospital}\n")

    # Limpiar campos
    entryNombreD.delete(0, tk.END)
    comboEspecialidadD.set("")
    entryAniosServicioD.delete(0, tk.END)
    entryAniosServicioD.insert(0, "0")
    sexoD.set("Masculino")
    comboHospitalD.set("")

# Crear ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Doctores")
ventanaPrincipal.geometry("890x600")

# Crear contenedor NoteBook (pestañas)
pestañas = ttk.Notebook(ventanaPrincipal)
frameDoctores = ttk.Frame(pestañas)
pestañas.add(frameDoctores, text="Doctores")
pestañas.pack(expand=True, fill="both")

# Nombre
labelNombreD = tk.Label(frameDoctores, text="Nombre:")
labelNombreD.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entryNombreD = tk.Entry(frameDoctores)
entryNombreD.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Especialidad
labelEspecialidadD = tk.Label(frameDoctores, text="Especialidad:")
labelEspecialidadD.grid(row=1, column=0, padx=5, pady=5, sticky="w")
especialidadD = tk.StringVar()
comboEspecialidadD = ttk.Combobox(
    frameDoctores,
    values=["Cardiología", "Dermatología", "Neurología", "Pediatría", "Ginecología", "Ortopedia"],
    textvariable=especialidadD,
    state="readonly"
)
comboEspecialidadD.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Años de servicio
labelAniosServicioD = tk.Label(frameDoctores, text="Años de servicio:")
labelAniosServicioD.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entryAniosServicioD = tk.Spinbox(frameDoctores, from_=0, to=100, width=5)
entryAniosServicioD.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Sexo con Radiobuttons
labelSexoD = tk.Label(frameDoctores, text="Sexo:")
labelSexoD.grid(row=3, column=0, padx=5, pady=5, sticky="w")
sexoD = tk.StringVar(value="Masculino")
radioMasculino = tk.Radiobutton(frameDoctores, text="Masculino", variable=sexoD, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, pady=2, sticky="w")
radioFemenino = tk.Radiobutton(frameDoctores, text="Femenino", variable=sexoD, value="Femenino")
radioFemenino.grid(row=3, column=2, padx=5, pady=2, sticky="w")

# Hospital donde trabaja
labelHospitalD = tk.Label(frameDoctores, text="Hospital donde trabaja:")
labelHospitalD.grid(row=4, column=0, padx=5, pady=5, sticky="w")
hospitalD = tk.StringVar()
comboHospitalD = ttk.Combobox(
    frameDoctores,
    values=["Caja Nacional de Salud", "Hospital El Bajio", "Caja Bancaria"],
    textvariable=hospitalD,
    state="readonly"
)
comboHospitalD.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Botones
btnFrameD = tk.Frame(frameDoctores)
btnFrameD.grid(row=5, column=1, columnspan=2, pady=5, sticky="w")
btnRegistrarD = tk.Button(btnFrameD, text="Registrar", bg="green", fg="white", command=registrarDoctor)
btnRegistrarD.grid(row=0, column=0, padx=5)
btnEliminarD = tk.Button(btnFrameD, text="Eliminar", bg="red", fg="white")
btnEliminarD.grid(row=0, column=1, padx=5)

# Treeview
treeviewD = ttk.Treeview(
    frameDoctores,
    columns=("Nombre", "Especialidad", "Años de servicio", "Sexo", "Hospital"),
    show="headings"
)
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Años de servicio", text="Años de servicio")
treeviewD.heading("Sexo", text="Sexo")
treeviewD.heading("Hospital", text="Hospital")
treeviewD.column("Nombre", width=180)
treeviewD.column("Especialidad", width=140)
treeviewD.column("Años de servicio", width=120)
treeviewD.column("Sexo", width=100)
treeviewD.column("Hospital", width=180)
treeviewD.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Scrollbar
scrollbarD = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscroll=scrollbarD.set)
scrollbarD.grid(row=6, column=4, sticky="ns")

ventanaPrincipal.mainloop()

