from Ciclista import Ciclista

nombrePrimerCiclista=input("Ingrese el nombre del primer ciclista: ")
edadPrimerCiclista=int(input("Ingrese la edad del primer ciclista: "))
paisPrimerCiclista=input("Ingrese el pais del primer ciclista: ")
tiempoPrimerCiclista=int(input("Ingrese el tiempo que se demoro el primer ciclista: "))

ciclista1 = Ciclista()
ciclista1.nombre=nombrePrimerCiclista
ciclista1.edad=edadPrimerCiclista
ciclista1.pais=paisPrimerCiclista
ciclista1.tiempo=tiempoPrimerCiclista

nombreSegundoCiclista=input("Ingrese el nombre del segundo ciclista: ")
edadSegundoCiclista=int(input("Ingrese la edad del segundo ciclista: "))
paisSegundoCiclista=input("Ingrese el pais del segundo ciclista: ")
tiempoSegundoCiclista=int(input("Ingrese el tiempo que se demoro el segundo ciclista: "))

ciclista2 = Ciclista()
ciclista2.nombre=nombreSegundoCiclista
ciclista2.edad=edadSegundoCiclista
ciclista2.pais=paisSegundoCiclista
ciclista2.tiempo=tiempoSegundoCiclista

nombreTercerCiclista=input("Ingrese el nombre del tercer ciclista: ")
edadTercerCiclista=int(input("Ingrese la edad del tercer ciclista: "))
paisTercerCiclista=input("Ingrese el pais del tercer ciclista: ")
tiempoTercerCiclista=int(input("Ingrese el tiempo que se demoro el tercer ciclista: "))

ciclista3 = Ciclista()
ciclista3.nombre=nombreTercerCiclista
ciclista3.edad=edadTercerCiclista
ciclista3.pais=paisTercerCiclista
ciclista3.tiempo=tiempoTercerCiclista

if(ciclista1.tiempo > ciclista2.tiempo and ciclista3.tiempo > ciclista2.tiempo):
    print(f"El Ganador es:")
    print(ciclista2.nombre)
    print(ciclista2.edad)
    print(ciclista2.pais)
    print(ciclista2.tiempo)
elif(ciclista1.tiempo < ciclista2.tiempo and ciclista3.tiempo > ciclista1.tiempo):
    print(f"El Ganador es:")
    print(ciclista1.nombre)
    print(ciclista1.edad)
    print(ciclista1.pais)
    print(ciclista1.tiempo)
elif(ciclista3.tiempo < ciclista2.tiempo and ciclista1.tiempo > ciclista3.tiempo):
    print(f"El Ganador es:")
    print(ciclista3.nombre)
    print(ciclista3.edad)
    print(ciclista3.pais)
    print(ciclista3.tiempo)
elif(ciclista1.tiempo == ciclista2.tiempo or ciclista3.tiempo == ciclista1.tiempo):
    print("Los ciclistas quedaron empatados")
else:
    print("Errooooor")