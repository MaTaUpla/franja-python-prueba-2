#Matias Tapia
#ejercicio 3

#formula del area de un circulo A = pi * R^2
def calculo_area_circulo(radio):
  pi = 3.14
  area = (pi * pow(radio,2))
  print("El area del circulo de radio " + str(radio) + " cm, es de " + str(area) + " cm2")
  return round(area,1)

#formula del volumen del cilindro V = area * altura 
#uso la funcion del area en el volumen
def calculo_volumen_cilindro(radio, altura):
  area = calculo_area_circulo(radio)
  volumen = area * altura
  print("El volumen del cilindro de radio " + str(radio) + " cm y altura " + str(altura) + " cm, es de " + str(volumen) + " cm3")
  return round(volumen,1)


#Función principal
def main():
  #Inicio de variables input, opciones para uso de una funcion o ambas
  print("#########################################################")
  print("Calculador de areade un circulo o volumen de un cilindro")
  print("Coloque 1 para area del circulo")
  print("Coloque 2 para volumen del cilindro")
  print("#########################################################")
  opcion = int(input("Ingrese opcion: "))
  if(opcion == 1):
    radio_circulo = input("Ingrese valor del radio del circulo: ")
    print("")
    area = calculo_area_circulo(int(radio_circulo))
  else:
    radio_cilindro = input("Ingrese valor del radio de la base del cilindro: ")
    altura_cilindro = input("Ingrese valor de la altura del cilindro: ")
    print("")
    #uso funciones para calculos
    volumen = calculo_volumen_cilindro(int(radio_cilindro), int(altura_cilindro))

#Punto de entrada
if __name__ == "__main__":
    main()
