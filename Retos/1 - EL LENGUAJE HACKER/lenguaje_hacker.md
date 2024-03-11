# Reto #1: EL LENGUAJE HACKER"

## Enunciado

```
Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337").
Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
```

## Soluciones
#### Python (enlace al código: [código](https://github.com/davidlopean/MoureDev-Weekly-Challenges/blob/604d47d5e638d9c21371919f6ce980375ca734a5/Retos/1%20-%20EL%20LENGUAJE%20HACKER/lenguaje_hacker.py))

```
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
```

[Volver a la página inicial del repositorio de retos](https://github.com/davidlopean/MoureDev-Weekly-Challenges/tree/main)
