#Se importa la libreria 'random' para usarla a la hora de generar las contraseñas
import random
#Se importa la libreria 'string' para facilitar la creación de variables que contendran los alfabetos, números y simbolos
import string

#Se declara la función que contiene el script e inmediatamente se imprime el mensaje de comienzo del script
def pass_generator(welcome_message):
    print(welcome_message)
        
    #Variables que almacenan las diferentes posibilidades de la contraseña(alfabeto de minusculas y mayusculas, números y/o simbolos)
    #Minúsculas
    lowercase = string.ascii_lowercase
    #Minusculas + mayusculas
    lower_upper = string.ascii_lowercase + string.ascii_uppercase
    #Minusculas + mayusculas + numeros
    lower_upper_numbers = string.ascii_lowercase + string.ascii_uppercase + string.digits
    #Minusculas + mayusculas + numeros + simbolos
    lower_upper_numbers_simbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    #Minusculas + mayusculas + simbolos
    lower_upper_simbols = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    #Minusculas + numeros
    lower_numbers = string.ascii_lowercase + string.digits
    #Minusculas + numeros + simbolos
    lower_numbers_simbols = string.ascii_lowercase + string.digits + string.punctuation
    #Minusculas + simbolos
    lower_simbols = string.ascii_lowercase + string.punctuation

    #Variable que almacena el resultado final con la contraseña
    final_password = ""
    
    #Input para pedir la lóngitud de la contraseña deseada y que almacena en la variable 'pass_len'
    pass_len = input("¿Quieres una contraseña corta (8 caracteres) o larga (16 caracteres) (indique 'corta' o 'larga')?")
    #El valor de la variable se pasa a minúsculas para facilitar el siguiente 'if', que cambia el valor de 'pass_len' a un integer de 8 o 16 y además incorpora un control para validar el dato introducido.
    pass_len = pass_len.lower()
    if pass_len == "corta":
        pass_len = 8
    elif pass_len == "larga":
        pass_len = 16
    else:
        print("Valor incorrecto")
        pass_generator("Por favor, indique de nuevo los parámetros que desea para la contraseña.")
        
    #Input para indicar si se quieren incluir letras en mayúsculas y que almacena el resultado en la variable 'pass_cap'
    pass_cap = input("¿Quieres que tenga letras mayúsculas? (indique 'si' o 'no')")
    #Flujo de control que solo acepta 'si' o 'no' como respuestas
    if pass_cap.lower() == "si" or pass_cap.lower() == "no":
        pass
    else:
        print("Valor incorrecto")
        pass_generator("Por favor, indique de nuevo los parámetros que desea para la contraseña.")
    
    #Input para indicar si se quieren incluir números y que almacena el resultado en la variable 'pass_numbers'
    pass_numbers = input("¿Quieres que tenga números (indique 'si' o 'no'?")
    #Flujo de control que solo acepta 'si' o 'no' como respuestas
    if pass_numbers.lower() == "si" or pass_numbers.lower() == "no":
        pass
    else:
        print("Valor incorrecto")
        pass_generator("Por favor, indique de nuevo los parámetros que desea para la contraseña.")
    
    #Input para indicar si se quieren incluir simbolos y que almacena el resultado en la variable 'pass_simbols'
    pass_simbols = input("¿Quieres que tenga simbolos (indique 'si' o 'no'?")
    #Flujo de control que solo acepta 'si' o 'no' como respuestas
    if pass_simbols.lower() == "si" or pass_simbols.lower() == "no":
        pass
    else:
        print("Valor incorrecto")
        pass_generator("Por favor, indique de nuevo los parámetros que desea para la contraseña.")
    
    #Se imprime por pantalla los parámetros seleccionados para la contraseña que se va a generar
    print("----------------------------------------------------------")
    print("Su contraseña tendrá los siguientes parámetros:\n"
          "Longitud: "+str(pass_len)+" caracteres\n"
          "Mayúsculas: "+str(pass_cap.lower())+"\n"
          "Números: "+str(pass_numbers.lower())+"\n"
          "Simbolos: "+str(pass_simbols.lower()))
    print("----------------------------------------------------------")
    
    #Se pregunta si estos datos son correctos a través del input que lo almacena en la variable 'generate_pass'
    generate_pass = input("¿Es correcto? (indique 'si' o 'no')")
    generate_pass = generate_pass.lower()
    #Flujo de control para una respuesta afirmativa (procede a generar la contraseña) o negativa (vuelve a comenzar el script llamando de nuevo a la funcion 'pass_generator')
    if generate_pass == "si":
        #Flujo de control que va a generar la contraseña en base a las diferentes variables de minúsculas, mayúsculas, números y símbolos
        #Minúsculas
        if pass_cap == "no" and pass_numbers == "no" and pass_simbols == "no":
            final_password = random.choices(lowercase, k = pass_len)
            print(final_password)
        #Minusculas + mayusculas
        elif pass_cap == "si" and pass_numbers == "no" and pass_simbols == "no":
            final_password = random.choices(lower_upper, k = pass_len)
            print(final_password)
        #Minusculas + mayusculas + numeros
        elif pass_cap == "si" and pass_numbers == "si" and pass_simbols == "no":
            final_password = random.choices(lower_upper_numbers, k = pass_len)
            print(final_password)            
        #Minusculas + mayusculas + numeros + simbolos
        elif pass_cap == "si" and pass_numbers == "si" and pass_simbols == "si":
            final_password = random.choices(lower_upper_numbers_simbols, k = pass_len)
            print(final_password)                
        #Minusculas + mayusculas + simbolos
        elif pass_cap == "si" and pass_numbers == "no" and pass_simbols == "si":
            final_password = random.choices(lower_upper_simbols, k = pass_len)
            print(final_password) 
        #Minusculas + numeros
        elif pass_cap == "no" and pass_numbers == "si" and pass_simbols == "no":
            final_password = random.choices(lower_numbers, k = pass_len)
            print(final_password)            
        #Minusculas + numeros + simbolos
        elif pass_cap == "no" and pass_numbers == "si" and pass_simbols == "si":
            final_password = random.choices(lower_numbers_simbols, k = pass_len)
            print(final_password)       
        #Minusculas + simbolos
        elif pass_cap == "no" and pass_numbers == "no" and pass_simbols == "si":
            final_password = random.choices(lower_simbols, k = pass_len)
            print(final_password)
    else:
        pass_generator("Por favor, indique de nuevo los parámetros que desea para la contraseña.")
    
#Llamada a la función. 
pass_generator("Se va a generar una contraseña aleatoria.")
