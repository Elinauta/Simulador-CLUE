#ALTA DE CARTAS
cartas = {
    "personajes":[
                "Prof. Moradillo",
                "Srita. Scarlata",
                "Sr. Verdi",
                "Coronel Mostaza",
                "Sra. Blanco",
                "Sra. Azulino"],
    "armas":[
           "tubo",
           "cuchillo",
           "pistola",
           "candelabro",
           "soga"],
    "habitaciones":[
                  "cocina",
                  "comedor",
                  "bibloioteca",
                  "sala",
                  "estudio"]
}
#-----------------------------------------------------------------------------------
import random
import os
import time
borrarPantalla = lambda: os.system ("cls")
#-----------------------------------------------------------------------------------
    #SELECCION DE LA VICTIMA
victima = random.choice(cartas["personajes"])

#Dialogo------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
borrarPantalla()
print("BIENVENIDO A CLUE\n\n¿Quién es el culpable?")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nPara poder resolver este caso tienes derecho a hacer 5 preguntas sobre un personaje, un arma o una habitacion en especifico")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nPodrás saber lo que dice el acusado y lo que lograron captar las camaras de seguridad de la mansión dandote pistas sobre el homicidio")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nUna vez terminadas tus 5 oportunidades de generar pistas, podrás hacer una acusación sobre quién es el culpable, con qué objeto mató a la victima y en cuál habitación fue ejecutado")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("¡¿LISTO PARA INICIAR EL CASO?!")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("\n-¡NO PUEDE SER! Encontraron el cuerpo muerto de " + victima)
time.sleep(2)
print("\n-¡Quién pudo haber hecho algo tan terrible?!")
input("\n\nPress Enter to continue...")
borrarPantalla()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #elimina a la victima de la lista personajes
cartas["personajes"].remove(victima)
#print(cartas["personajes"])

#--------------------------------------------------------------------------------------------------------------------------
    #SELECCION DEL HOMICIDIO
    #Culpable, arma y habitacion
 
homicidio = [random.choice(cartas["personajes"]),random.choice(cartas["armas"]), random.choice(cartas["habitaciones"])]
#print(homicidio)
#--------------------------------------------------------------------------------------------------------------------------
    #GENERACION DE PISTAS PARA CREAR LAS HISTORIAS

random.shuffle(cartas["personajes"])
lista_Historias = []                              

for i in range(5):
  p = cartas["personajes"][i]
  a = cartas["armas"][i]
  h = cartas["habitaciones"][i]
  lista_Historias.append((p,a,h))
#print(lista_Historias)
#-------------------------------------------------------------------------------------------------------------------
    #SELECCION PARA MOSTRAR HISTORIAS

print("ENCONTREMOS PISTAS...")
#ciclo para 5 preguntas
for p in range(5):
  #Menú 1
  print("\nSelecciona una opcion para hacer una pregunta:\n1 Personaje\n2 Arma\n3 Habitacion")
  opcion = int(input())

  #Opciones
  if opcion == 1:
    #Menu 2 
    print("\nSelecciona el personaje por el que quieres preguntar:")
    for i in range(len(cartas["personajes"])):
      print(i+1, cartas["personajes"][i])
    op2 = int(input())

    #busca la pista dentro de la lista de lista_Historias y poder mostrar la historia
    eleccion = cartas["personajes"][op2-1]

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n\n",historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    #busca las listas en homicidio para mostrar si hay o no registro 
    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)
    input("\n\nPress Enter to continue...")
    borrarPantalla()


  if opcion == 2:
    print("\nSelecciona el arma por la que quieres preguntar:")
    for i in range(len(cartas["armas"])):
      print(i+1, cartas["armas"][i])
    op2 = int(input())

    eleccion = cartas["armas"][op2-1]

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n", historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)      
    input("\n\nPress Enter to continue...")
    borrarPantalla()


  if opcion == 3:
    print("\nSelecciona la habitacion por la que quieres preguntar:")
    for i in range(len(cartas["habitaciones"])):
      print(i+1, cartas["habitaciones"][i])
    op2 = int(input())  

    eleccion = cartas["habitaciones"][op2-1] 

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n", historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)      
    input("\n\nPress Enter to continue...")
    borrarPantalla()       
#------------------------------------------------------------------------------------
    #SUPOSICIÓN

print("ES MOMENTO DE HACER UNA ACUSACIÓN.\nRecuerda que debes escoger un personaje, un arma y una habitación con las pistas que haz recolectado hasta ahora\n")
time.sleep(3)
print("\nSelecciona al culpable:")
for i in range(len(cartas["personajes"])):
  print(i+1, cartas["personajes"][i])
culp = int(input())
culpable = cartas["personajes"][culp-1]    

print("\nSelecciona el arma homicida:")
for i in range(len(cartas["armas"])):
  print(i+1, cartas["armas"][i])
ah = int(input())
arm_hom = cartas["armas"][ah-1]  

print("\nSelecciona la habitacion:")
for i in range(len(cartas["habitaciones"])):
  print(i+1, cartas["habitaciones"][i])
ha = int(input())  
habit = cartas["habitaciones"][ha-1]   

suposicion = [culpable,arm_hom,habit]
#------------------------------------------------------------------------------------------
    #RESULTADOS

borrarPantalla()
print("¿QUIÉN ES EL CULPABLE?")
time.sleep(3)
print("Los resultados de tu acusación son los siguientes...\n\n")
time.sleep(3)
for x in range(3):
  frase2 = ""
  if suposicion[x] not in homicidio[x]:
    frase2 += suposicion[x] + ": No es correcta"
    print(frase2)
  else:
    frase2 += suposicion[x] + ": Es correcta"
    print(frase2)  

time.sleep(3)
print("\n\nEl culpable a sido",homicidio[0],"con", homicidio[1], "en",homicidio[2])  