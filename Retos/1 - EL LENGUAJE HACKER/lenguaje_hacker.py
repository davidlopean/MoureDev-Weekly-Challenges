#Se declara la función que contiene el script 
def hacker_language(string):
    #Se crea el diccionario con la clave:valor, donde clave es el caracter introducido en la frase y el valor es su homologo en lenguaje hacker (leet)
    leet_alphabet = {"a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":",_|","k":">|","l":"1","m":"^^","n":"^/","o":"0","p":"|*","q":"(_,)","r":"I2","s":"5","t":"7","u":"(_)","v":"\/","w":"\/\/","x":"><","y":"j","z":"2"," ":" "}
    
    #Se crea la variable de tipo string que va a formar la frase convertida a lenguaje hacker (leet)
    phrase = ""
    
    #Bucle for que va a interactuar por cada caracter introducido en la frase
    for letter in string:
        #Se convierte a lowercase y se almacena en la variable 'lower'
        lower = letter.lower()
        #Variable que toma el caracter en lowercase y lo busca en el diccionario, devolviendo el valor correspondiente del lenguaje hacker (leet).
        leet_leter = leet_alphabet.get(lower)
        #Cada valor encontrado en el diccionario se va sumando al string de la variable 'phrase'
        phrase = phrase + str(leet_leter)
    #Se imprime el string en lenguaje hacker (leet)
    print(phrase)

#Test: llamada a la función para probar que funciona correctamente, pasando a lenguaje hacker (leet) el clásico "Hola mundo".
hacker_language("Hola mundo")

#Llamada a la función con un input que nos pedirá una frase para convertirla a lenguaje hacker (leet).
hacker_language(input("Indique una frase:"))
