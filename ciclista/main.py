from Ciclista import Ciclista

ciclista1 = Ciclista()
ciclista1.ingresar()

ciclista2 = Ciclista()
ciclista2.ingresar()

ciclista3 = Ciclista()
ciclista3.ingresar()
if(ciclista1.tiempo > ciclista2.tiempo and ciclista3.tiempo > ciclista2.tiempo):
    print("El Ganador es:")
    print(ciclista2.nombre)
    print(ciclista2.edad)
    print(ciclista2.pais)
    print(ciclista2.tiempo)
elif(ciclista1.tiempo < ciclista2.tiempo and ciclista3.tiempo > ciclista1.tiempo):
    print("El Ganador es:")
    print(f"Nombre: {ciclista1.nombre} ")
    print(f"Edad: {ciclista1.edad} ")
    print(f"País: {ciclista1.pais} ")
    print(f"Tiempo: {ciclista1.tiempo} ")
elif(ciclista3.tiempo < ciclista2.tiempo and ciclista1.tiempo > ciclista3.tiempo):
    print("El Ganador es:")
    print(f"Nombre: {ciclista3.nombre} ")
    print(f"Edad: {ciclista3.edad} ")
    print(f"País: {ciclista3.pais} ")
    print(f"Tiempo: {ciclista3.tiempo} ")
elif(ciclista1.tiempo == ciclista2.tiempo and ciclista3.tiempo == ciclista1.tiempo):
    print("Los ciclistas quedaron empatados")
else:
    print("Errooooor")