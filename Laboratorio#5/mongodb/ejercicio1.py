from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escuela"]
coleccion = db["estudiantes"]

estudiantes = [
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]

coleccion.insert_many(estudiantes)

todos_estudiantes = coleccion.find()
for estudiante in todos_estudiantes:
    print(estudiante)

estudiantes_bogota = coleccion.find({"ciudad": "Bogotá"})
for estudiante in estudiantes_bogota:
    print(estudiante)

estudiantes_mayores_20 = coleccion.find({"edad": {"$gt": 20}})
for estudiante in estudiantes_mayores_20:
    print(estudiante)