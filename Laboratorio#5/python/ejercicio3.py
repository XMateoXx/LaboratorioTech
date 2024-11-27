estudiantes = ["Mateo", "Alejandro"]
print("Lista de estudiantes")
for estudiante in estudiantes:
    print(estudiante)
nombre_nuevo = input("¿Qué estudiante desea agregar, a la lista estudiante? ")
estudiantes.append(nombre_nuevo)
print("Lista de estudiantes actualizada:", estudiantes)

print(f"Esta es la informacion que tenemos del nuevo estudiante {nombre_nuevo}")
contacto = {
    "nombre": nombre_nuevo,
    "correo": "@gmail.co"
}
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

actualizar_correo = input("Ups, hubo un error al obtener el correo del estudiante, por favor actualizalo => ")
contacto["correo"] = actualizar_correo
print("Contacto actualizado:", contacto)
