#Matias Tapia
#ejercicio 2

def riman(cadena_palabras):
  palabra_a = cadena_palabras[0]
  palabra_b = cadena_palabras[1]

  #print(palabra_a)
  #print(palabra_b)

  largo_a = len(palabra_a)
  #print(palabra_a[(largo_a - 3):])
  extremo_a = palabra_a[(largo_a - 3):]
  extremo_a_a = palabra_a[(largo_a - 2):]
  #print(extremo_a_a)

  largo_b = len(palabra_b)
  #print(palabra_b[0:3])
  extremo_b = palabra_b[(largo_b - 3):]
  extremo_b_b = palabra_b[(largo_b - 2):]
  #print(extremo_b_b)

  if(extremo_a == extremo_b):
    print("las palabras " + palabra_a + " con la palabra " + palabra_b + " RIMAN")
  elif(extremo_a_a == extremo_b_b):
    print("las palabras " + palabra_a + " con la palabra " + palabra_b + " RIMAN un poco")
  else:
    print("las palabras " + palabra_a + " con la palabra " + palabra_b + " no RIMAN")

  
def main():
  dicionario = []
  print("####################")
  print("ingrese palabras para determinar si riman")
  print("####################")
  cantidad = 2
  while(cantidad != 0):
    palabra = input("Ingrese palabra: ")
    validar_longitud = len(palabra)
    if(validar_longitud < 3):
      print("####################")
      print("ingrese una palabra que tenga mas de 3 letras.")
      print("####################")
      cantidad += 1
    else:
      dicionario.append(palabra)
    cantidad -= 1
  #print(dicionario)
  riman(dicionario)

#Punto de entrada
if __name__ == "__main__":
    main()
