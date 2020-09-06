

# Diccionario de las notas de fisica
notas_fisica = {

	"Sofia": 10.0,
	"Sebastian": 5.0,
	"Benjamin": 9.0,
	"Francisca": 10.0,
}

# Diccionario de las notas de Programacion

notas_programacion = {

	"Sofia": 10.0,
	"Sebastian": 4.0,
	"Francisca": 10.0,
	"Benjamin": 1.0,
}

# Todos los alumnos
alumnos = ("Sofia", "Francisca", "Sebastian", "Benjamin")

# Recorriendo todos los alumnos

print("  Notas en programacion")
for alumno in alumnos:
	print(f"Nota de {alumno} en programacion es {notas_programacion[alumno]}") 

print("  Notas en fisica")
for alumno in alumnos:
	print(f"Nota de {alumno} en fisica es {notas_fisica[alumno]}")
