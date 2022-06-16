#Matias Tapia
#ejercicio 1

def comparador_de_palabras(cadena_palabras):
  #print(cadena_palabras)
  palabra_extensa_maxima = {'no ingreso palabra(s)'}
  cantidad_extensa_maxima = 0
  for x in cadena_palabras:
    #print(x)
    cantidad = len(x)
    if(cantidad > cantidad_extensa_maxima):
      for y in range(len(palabra_extensa_maxima)):
        palabra_extensa_maxima.pop()
      palabra_extensa_maxima.add(x)
      cantidad_extensa_maxima = cantidad
    elif(cantidad == cantidad_extensa_maxima):
      palabra_extensa_maxima.add(x)
      cantidad_extensa_maxima = cantidad

  return palabra_extensa_maxima, cantidad_extensa_maxima

#Función principal
def main():
  print("####################")
  print("Determinar la palabra mas extensa")
  print("ingrese cantidad de palabras a comparar:")
  print("####################")
  dicionario = []
  cantidad = int(input("cantidad: "))
  print("####################")
  while(cantidad != 0):
    palabra = input("Ingrese palabra: ")
    cantidad -= 1
    dicionario.append(palabra)
  palabra_extensa,cantidad_maxima = comparador_de_palabras(dicionario)
  print("####################")
  
  if(len(palabra_extensa) > 1 ):
    print("Las palabras mas extensa son: ")
    for x in palabra_extensa:
      print("'" + x + "'")
    print("con una longitud de " + str(cantidad_maxima) + " letra(s)")
  else:
    print("La palabra mas extensa es: ")
    for x in palabra_extensa:
      print("'" + x + "'")
    print("con una longitud de " + str(cantidad_maxima) + " letra(s)")

#Punto de entrada
if __name__ == "__main__":
    main()
