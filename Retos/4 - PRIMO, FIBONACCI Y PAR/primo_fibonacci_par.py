#Se declara la función que contiene el script e inmediatamente se imprime el mensaje de comienzo del script
def number_checker(number):
    result = ""
    counter = []
    
    #PRIMO
    for index in range(1,number+1):
        if number % index == 0:
            counter.append(index)
        else:
            pass  
    #Se comprueba si es Primo. Un número primo solo es divisible entre 1 y si mismo. Si len(counter) es mayor de 2 números almacenados en la lista, no es primo.
    if len(counter) <= 2:
        result += str(number) + " es un número primo, "
    else:
        result += str(number) + " no es un número primo, "
    
    #FIBONACCI
    fibonacci = [0,1]
    #Bucle 'while' para generar la sucesión Fibonacci hasta llegar al número 10.000. Si es necesario, aumentar este valor.
    while fibonacci[-1] <= 100:
        for index in range(1):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    #Se comprueba si está en el listado de la sucesión Fibonacci y añade el string a la variable 'result'
    if number in fibonacci:
        result += "fibonacci y "
    else:
        result += "no es fibonacci y "
    
    #PAR/IMPAR
    #Se comprueba si es par o impar y se añade el resultado a la variable 'result'. Un numero es par cuando, al dividirlo entre 2, el resto (operación python -> %) es 0. Si el resto (%) no es 0, es impar.
    if number % 2 == 0:
        result += "es par."
    else:
        result += "es impar."
    
    
    #Se imprime el resultado completo del script con una frase en la que indica si/no es primo, fibonacci y par/impar.
    print(result)
    

#Llamadas a la función para comprobar los números
number_checker(2)
number_checker(7)
number_checker(8)
number_checker(9)
number_checker(13)
number_checker(15)
number_checker(21)
