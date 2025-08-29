#importacion de librerias
import tkinter as tk 
from tkinter import ttk, messagebox
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")

#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames (uno por pestaña)
frame_pacientes = ttk.Frame(pestañas)
#agregar pestañas al notebook
pestañas.add(frame_pacientes, text="Pacientes")
pestañas.add(ttk.Frame(pestañas), text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nompreP=tk.Entry(frame_pacientes)
nompreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
FechaN=tk.Entry(frame_pacientes)
FechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
#Grupo Sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#Tipo de Seguro
labelTipodeSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro")
labelTipodeSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#Tipo de Centros Medicos
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud")
labelCentroMedico.grid(row=7, column=0, sticky="w", pady=5, padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", pady=5, padx=5)



ventana_principal.mainloop()