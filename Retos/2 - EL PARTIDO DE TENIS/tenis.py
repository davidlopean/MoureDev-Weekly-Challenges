#Se declara la función que contiene el script 
def tenis(string):
    
    #Se llama a la frase (string) pasada a través de la función. En este caso para indicar el comienzo del partido
    print(string)
    
    #Variable de valor booleano 'False' que cambiará a True cuando el jugador gane el set, indicando el final del partido.
    game_end = False
    
    #Variables para guardar la puntuación de cada jugador durante el partido
    player_1_points = "Love"
    player_2_points = "Love"
    
    #Bucle while que nos solicitará el jugador que ha ganado el set hasta que el valor booleano de la variable 'game_end' pase a 'True', indicando que el partido ya ha sido ganado por algún jugador.
    while game_end == False:
        #Variable que almacena el jugador que ha ganado el set tras preguntarnoslo con el input()
        player_winner_set = input("¿Quien ha ganado este set, P1 o P2?")
        
        #Flujo condicional del 'player_1' que ira sumando puntos al marcador tras realizar comparaciones contra el marcador actual
        if player_winner_set == "P1":
            if player_1_points == "Love":
                player_1_points = "15"
            elif player_1_points == "15":
                player_1_points = "30"
            elif player_1_points == "30" and player_2_points != "40":
                player_1_points = "40"
            elif player_1_points == "30" and player_2_points == "40":
                player_1_points = "Deuce"
                player_2_points = "Deuce"
            elif player_1_points == "Deuce" and player_2_points == "Deuce":
                player_1_points == "Ventaja"
                player_2_points == "40"
            elif player_1_points == "40" and player_2_points == "Ventaja":
                player_1_points = "Deuce"
                player_2_points = "Deuce"
            elif player_1_points == "40" and player_2_points != "Deuce" or player_2_points != "40" or player_2_points != "Ventaja":
                player_1_points = "Ganador"
                game_end = True
                print("Ha ganado el jugador 1")
            elif player_1_points == "Ventaja":
                game_end = True
                print("Ha ganado el jugador 1")
            else:
                game_end = True
                print("Ha ganado el jugador 1") 
                
        #Flujo condicional del 'player_2' que ira sumando puntos al marcador tras realizar comparaciones contra el marcador actual
        if player_winner_set == "P2":
            if player_2_points == "Love":
                player_2_points = "15"
            elif player_2_points == "15":
                player_2_points = "30"
            elif player_2_points == "30" and player_1_points != "40":
                player_2_points = "40"
            elif player_2_points == "30" and player_1_points == "40":
                player_1_points = "Deuce"
                player_2_points = "Deuce"
            elif player_2_points == "Deuce" and player_1_points == "Deuce":
                player_2_points == "Ventaja"
                player_1_points == "40"
            elif player_2_points == "40" and player_1_points == "Ventaja":
                player_1_points = "Deuce"
                player_2_points = "Deuce"
            elif player_2_points == "40" and player_1_points != "Deuce" or player_1_points != "40" or player_1_points != "Ventaja":
                player_2_points = "Ganador"
                game_end = True
                print("Ha ganado el jugador 2")
            elif player_2_points == "Ventaja":
                game_end = True
                print("Ha ganado el jugador 2")
            else:
                game_end = True
                print("Ha ganado el jugador 2") 
                
        #Else para controlar que solo se pueda introducir 'P1' o 'P2'
        else:
            print('Solo es posible indicar: P1 o P2')
            
        #String y su impresión por consola con el marcador del partido para mostrarlo por pantalla cada vez que se indique el ganador del set
        marcador =  "Marcador:\n"+"P1: "+player_1_points+"\n"+"P2: "+player_2_points
        print(marcador)
                   
    
#Llamada a la función. 
#¡Comienza el partido de tenis!
tenis("¡Comienza el partido de tenis!")
