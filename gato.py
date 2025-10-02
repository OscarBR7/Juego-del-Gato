import random #Se importa la libería random para generar numeros aleatorios
import math #Se importa la libería math para poder aplicar el algoritmo minmax
import os #Se importa la librería os, para temas esteticos del programa

class Gato: #Se crea la clase gato, donde estarán los objetos que se utilizaran para el juego
    def __init__(self): #Se crea el constructor principal de la clase gato
        self.tablero = ['-' for _ in range(9)] #Se crea la variable tablero, inicializada con guiones
        #en un rango de 9, para crear el tablero caracteristico del gato
        if random.randint(0, 1) == 1: #Se escoge un número aleatorio entre 1 y 0 para escoger el caracter a 
            #usar por cada jugador
            self.humano = 'X' #Se crea el objeto humano inicializado con X si el aleatorio es 1
            self.maquina = "O" #Se crea el objeto maquina inicializado con O si el aleatorio es 1
        else:
            self.humano = "O" #Se crea el objeto humano inicializado con O si el aleatorio es 0
            self.maquina = "X" #Se crea el objeto maquina inicializado con X si el aleatorio es 0

    def mostrar_tablero(self): #Se crea la función mostrar tablero
        print("")
        for i in range(3): #Por medio de un for se realizan 3 iteraciones para pintar el tablero
            print("  ",self.tablero[0+(i*3)]," | ",self.tablero[1+(i*3)]," | ",self.tablero[2+(i*3)])
            #se utiliza el print, el objeto tablero y se hacer las multiplicaciones necesarias, para 
            #este se pueda pintar en el siguiente formato " " | " " | y se hace el recorrido tres veces
            #para tener el formato del gato
            print("")
            
    def tablero_lleno(self,estado): #Se crea la función tablero_lleno, que recibe como parametro un estado
        #Este estado será para verificar si existen celdas vacías 
        return not "-" in estado #Esta comparación devuelve verdadero si ya no existen celdas vacías

    def ganar_juego(self,estado,jugador): # se crea la función ganar_juego, que recibe el estado y el jugador
        if estado[0]==estado[1]==estado[2] == jugador: return True #Hace la comparación de cada celda para 
        #verificar que estan sean iguales y así poder determinar el ganador, se hace tres veces, debido a que
        #se necesita juntar 3 caracteres iguales de manera horizontal, vertical o en diagonal
        if estado[3]==estado[4]==estado[5] == jugador: return True #Lo mismo pero para las celdas posteriores
        if estado[6]==estado[7]==estado[8] == jugador: return True
        if estado[0]==estado[3]==estado[6] == jugador: return True
        if estado[1]==estado[4]==estado[7] == jugador: return True
        if estado[2]==estado[5]==estado[8] == jugador: return True
        if estado[0]==estado[4]==estado[8] == jugador: return True
        if estado[2]==estado[4]==estado[6] == jugador: return True

        return False #Retorna falso en caso de no coincidir con ninguna opción

    def verificar_victoria(self):#Se crea la función verificar victoria
        if self.ganar_juego(self.tablero,self.humano):#SE le pasan los parametros a la función ganar_juego
            #los parametros son el tablero, y el humano, que es el simbolo que esta jugando
            #Si la función devuelve verdadero el humano es el ganador
            os.system("cls")
            print(f"El humano con el simbolo {self.humano} ganó el juego!") #Mensaje de salida de ganador
            return True #Retorna verdadero si es que el humano es el ganador
            
        if self.ganar_juego(self.tablero,self.maquina):
            #SE le pasan los parametros a la función ganar_juego
            #los parametros son el tablero, y la maquina, que es el simbolo que esta jugando
            #Si la función devuelve verdadero la maquina es el ganador
            os.system("cls")
            print(f"La {self.maquina} ganó el juego!")#Mensaje de salida de ganador
            return True #Retorna verdadero si es que la maquina es el ganador

        if self.tablero_lleno(self.tablero):
            #SE le pasa el parametro a la función tablero_lleno
            #el pareametro es el tablero, si la funcón devuelve verdadero signfica que ya no hay celdas
            #disponibles, por lo tanto ya nadie puede ganar y es un empate
            os.system("cls")
            print("El juego termino en empate!") #mensaje de salida de empate
            return True #Retorna verdadero en empate
        return False #Se retorna falso en caso de que no encuentre ninguna opción

    def inicio(self):#se crea la función inicio
        jugador_maquina = JugadorMaquina(self.maquina) #Se crea la variable jugador_maquina
        #Donde se le pasan los metodos de los que dispone el objeto maquina de la clase
        #JugadorMaquina
        jugador_humano = JugadorHumano(self.humano)
        #Se crea la variable jugador_humano
        #Donde se le pasan los metodos de los que dispone el objeto humano de la clase
        #JugadorHumano
        while True: #Se crea un bucle while que siempre es verdadero hasta que se cumpla una
            #función que rompa el ciclo
            os.system("cls")
            print(f"Es el turno del humano con el caracter {self.humano}") #mensaje de salida que indica
            #Cuando es turno del humano para colocar su caracter
            self.mostrar_tablero() #se muestra el tablero, para que el humano vea cuales celdas estan vacías
            
            cuadro = jugador_humano.movimiento_humano(self.tablero)
            #se crea la variable cuadro, que es el número de celda donde se colocará el caracter del humano
            #esta celda recibirá la información de la varibale jugador_humano, que se le aplica el metodo
            #movimiento_humano donde se le pasa como parametro el tablero
            self.tablero[cuadro] = self.humano
            #al objeto tablero en la posición de la celda se le asigna el caracter del humano
            if self.verificar_victoria():#Se verifica si gana el humano
                break #Si gana se rompe el ciclo
            
            cuadro = jugador_maquina.movimiento_maquina(self.tablero)
            #se crea la variable cuadro, que es el número de celda donde se colocará el caracter de maquina
            #esta celda recibirá la información de la varibale jugador_maquina, que se le aplica el metodo
            #movimiento_maquina donde se le pasa como parametro el tablero
            self.tablero[cuadro] = self.maquina
            #al objeto tablero en la posición de la celda se le asigna el caracter de maquna
            if self.verificar_victoria():#Se verifica si gana la maquina
                break #Si gana se rompe el ciclo

        print()
        self.mostrar_tablero() #se muestra el tablero final

class JugadorHumano: #Se crea la clase JugadorHumano
    def __init__(self,caracter): #Se declara el constructor principal de la clase
        self.caracter = caracter #Se inicializa el objeto caracter
    
    def movimiento_humano(self,estado): #Se crea el metodo movimiento_humano que recibe como parametro el estado
        while True: #Se crea un bucle infinito
            cuadro =  int(input("Ingresa el número del cuadro donde quieres colocar tu caracter (1-9): "))
            #Se crea la variable cuadro, que espera un número del 1 al 9 por parte del usuario, que será
            #la posición donde desea colocar su caracter el humano
            print()
            if estado[cuadro-1] == "-": #se verifica que la celda este vacía
                break #se rompre el buclre y se retorna el valor de la celda
        return cuadro-1

class JugadorMaquina(Gato):#Se crea la clase JugadorMaquina, que hereda de la clase Gato
    def __init__(self,caracter): #Se crea el constructor principal
        self.maquina = caracter #Se inicializa el objeto maquina
        self.humano = "X" if caracter == "O" else "O" #Se inicializa el objeto humano

    def jugadores(self,estado): #Se crea el metodo jugadores
        n = len(estado) #Se crea la variable n, que contendra el largo del tablero
        x = 0 #Se inicializa la varible x en 0
        o = 0 #Se inicializa la varible o en 0
        for i in range(9): #se crea un bucle for que recorre las 9 celdas del tablero
            if(estado[i] == "X"): #Se compara el estado en la posición i con la x, para llevar un conteo
                #del número de jugadas que se lleva hasta el momento
                x = x+1 # se suma 1 al contador
            if(estado[i] == "O"):
                #Se compara el estado en la posición i con la o, para llevar un conteo
                #del número de jugadas que se lleva hasta el momento
                o = o+1 #Se suma 1 al contador
        
        if(self.humano == "X"): #se compara el caracter X con X si es así retorna X y luego compara x == o
            #esto se hace para saber si se hace el mismo número de jugadas
            return "X" if x==o else "O"
        if(self.humano == "O"):
            #se compara el caracter O con O si es así retorna O y luego compara x == o
            #esto se hace para saber si se hace el mismo número de jugadas
            return "O" if x==o else "X"
    
    def acciones(self,estado):#se crea el metodo acciones
        return [i for i, x in enumerate(estado) if x == "-"]
    #se retorna las posibles acciones que pueden ejecutar los jugadores, es decir, que solo puedan poner
    #los caracteres donde esten las celdas vacías el if x == "-" es el ecargado de la filtración
    
    def resultados(self,estado,accion): #Se crea el metodo resultados, que recibe como parametros, el estado
        #y la accion que se puede realizar
        nuevoEstado = estado.copy() #se crea un nuevo estado y se hace una copia del estado orginal, para
        #no modificar el estado original
        jugador = self.jugadores(estado) #Se crea la variable jugador que almacena el jugador actual que
        #le tocaría hacer la jugada
        nuevoEstado[accion] = jugador #Se asigna el caracter del jugador al nuevo estado
        return nuevoEstado #Se retorna el estado
    
    def final(self,estado): #Se crea el metodo final que recibe el estado
        if(self.ganar_juego(estado,"X")): #Se crea la condición que verifica si X gana el juego
            return True #retorna verdadero
        if(self.ganar_juego(estado,"O")): #Se crea la condición que verifica si O gana el juego
            return True #retorna verdadero
        return False #retorna falso en caso de que no haya ganado ninguno

    def minimax(self, estado, jugador): #se crea el metodo minimax el cual es un algoritmo 
        #recursivo que explora los posibles movimientos futuros de los jugadores
        max_jugador = self.humano #se crea la variable max_jugador a la cual se le asgina el valor 
        #del caracter del humano
        otro_jugador = 'O' if jugador == 'X' else 'X' #Se asigna el caracter a la maquina dependiendo de 
        #cual es el caracter que esta usando el humano
        if self.final(estado):#se crea la condición para saber quien gana el juego tomando en cuenta 
            #el estado del tablero
            return {'posicion': None, 'puntuacion': 1 * (len(self.acciones(estado)) + 1) if otro_jugador == max_jugador else -1 * (
                        len(self.acciones(estado)) + 1)}
        #Se retorna 1 si el jugador humano gana, se retorna -1 si la maquina gana
        elif self.tablero_lleno(estado):#se verifica si el tablero esta lelno
            return {'posicion': None, 'puntuacion': 0}
        #Se retorna 0 si existe el empate

        if jugador == max_jugador:#se crea la condición del si jugador actual es el humano
            mejor = {'posicion': None, 'puntuacion': -math.inf} #si es el humano se crea la puntuación
            #mejor inicializandola muy baja con el metodo -math.inf para maximizar la variable
        else:
            mejor = {'posicion': None, 'puntuacion': math.inf} #si es la maquina se crea la puntuación
            #mejor inicializandola muy alta con el metodo math.inf para minimizar la variable
        for posible_movimiento in self.acciones(estado): #se crea un bucle for para analizar los posibls
            #movimientos que se pueden realizar
            nuevoEstado = self.resultados(estado,posible_movimiento)
            #se crea un nuevo estado para cada movimiento y se evalua con resultados
            sim_score = self.minimax(nuevoEstado, otro_jugador)#actualiza el estado con el valor simulado
            #para poder compararlo

            sim_score['posicion'] = posible_movimiento 

            if jugador == max_jugador: 
                if sim_score['puntuacion'] > mejor['puntuacion']:
                    #Si el jugador actual es el jugador humano, se busca maximizar la puntuación.
                    mejor = sim_score#Se actualiza mejor con sim_score si la
                    # puntuación simulada es mejor que la mejor conocida hasta ahora.
            else:
                if sim_score['puntuacion'] < mejor['puntuacion']:
                    #Si el jugador actual es el oponente, se busca minimizar la puntuación.
                    mejor = sim_score #Se actualiza mejor con sim_score si la
                    # puntuación simulada es mejor que la mejor conocida hasta ahora.
        return mejor #Se retorna el mejor movimiento encontrado, con su posición y puntuación asociada.

    def movimiento_maquina(self,estado): #Se crea el metodo movimiento_maquina que recibe el estado
        cuadro = self.minimax(estado,self.maquina)['posicion'] #se crea la variable cuadro
        #que será la celda donde se guarde el valor de donde se podná la posición del caracter 
        #de la maquina, se se aplica el metodo minimax el cual recibe el estado y el caracter que esta 
        #usando la maquina, y además la posición que determino el algoritmo minimax que es la mejor
        #jugada
        return cuadro #se retorna el valor del cuadro

gato = Gato() #Se crea la variable gato que es una instancia de Gato
gato.inicio() #Se le aplica el metodo inicio a la instancia gato para comenzar el juego