'''
Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''


#Se crea una función que contiene el script para el programa "Fizzbuzz"
def fizzbuzz():
    #Bucle 'for' que, a través de la variable 'i', va a generar números de 0 al 100, en pasos de 1 en 1
    for i in range(0,101,1):
        #Si la variable 'i' es múltiplo de 3 y de 5 devuelve el string "fizzbuss"
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        #Si la variable 'i' es múltiplo de 3 devuelve el string 'fizz'
        elif i % 3 == 0:
            print("fizz")
        #Si la variable 'i' es múltiplo de 5 devuelve el string 'buzz'
        elif i % 5 == 0:
            print("buzz")
        #Si la variable 'i' no es múltiplo de 3 ni de 5 solamente imprimi el valor de 'i'.
        else: 
            print(i)

#Llamada a la función
fizzbuzz()
