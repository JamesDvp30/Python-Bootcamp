import time as tm
import datetime as dt
""" REPASO DE CONCATENACION, FUNCIONES FECHA Y TIEMPO, Conversion de datos
print('Estes es el primer progrmama que realizo despues de tanto tiempo')
print('Inserta tu nombre')
nombre = input()
print('Ingresa tu apellido')
apellido =input()
print('Bienvenido, ' + nombre + ' ' + apellido )
total= len(nombre + apellido)
print('Tu nombre tiene:  %d '  % total + ' Caracteres ')
tm.sleep(3)


print('Bien, ahora inserta tu año de nacimiento')
nacimiento = int(input())
fecha_actual = dt.datetime.now()
anio = int(fecha_actual.year)

#print(anio)

edad = anio-nacimiento 
print('Mi hermano, tu tienes o tendras %d ' % edad + ' años')"""

#Trabajar con booleanos y 
""" 
nombre = input()
if nombre == 'Jose':
    print('Te conozco, Hola!')
else:
    print('No te conozco')
"""
"""
#loop while
while True:
    print("Dime quien tu ere!")
    nombre= input()
    if(nombre != 'jose'):
        continue # el continue hace que yo vuelva arriba a ejecutar nuevamente pa eso sirve
    print('Mi loco pon la clave ahi(Es un peje)')
    clave =input()
    if clave == 'peje':
        break
print('Iniciaste sesion compadre!')
"""

"""
#login de una red social en paiton
while True:
    print('Ingrese su usuario')
    usuario = input()
    if(usuario !='jgiacomor'):
        print('Socio usted no está aqui, intentelo nuevamente')
        continue
    else: 
        print('Ponga su clave ahora') 
        clave= input()
        if (clave != 'Lila2020'):        
            print('Lo sentimos, Vuelva a iniciar sesion')
        else:
            print('Bienvenido mi hermanaso, tu eres duro ' +usuario )
            break
"""

#Loops
"""
print('Mi nombre es ')
for i in range(6):
    print('Jose  seis veces (' + str(i) +')')



total =0 
for num in range(101):
    total= total+num
print(total)

for i in range(0,22,2):
    print(i)


for i in range(5,-1,-1):
    print(i)


#importando modulos
import random as rnd # un for con numeros randoms por cada iteraccion

for i in range(5):
    print(rnd.randint(1,10))


#jueguito de  adivina el numero inventado por mi

print('Bienvenidos a mi juego, vamo a ver si eres duro!')
i = 0
valor = 15
while(i==0):
    print('Ingresa un numero del 1 al 25')
    numerito=  int(input())
    if (numerito >= 25 or numerito  <= 9):
        print('Ta friooo pinguino')
        continue
    elif(numerito >= 10 and  numerito <= 14 ):
        print('Ta calientico')
        continue
    elif( numerito >= 16 and numerito <= 19 ):
        print('Ta calientico')
        continue
    elif( numerito == 15 ):
        print('PIPO LOCO!, LA PEGASTE')
        break


#juego de piedra papel o tijera a la criolla
import random, sys

print('Bienvenido!, Veamos si eres duro en esta vaina...')
print('Esto es piedra papel y tijeras, ')
victorias=0
derrotas=0
empates=0
while True:
    print('%s Victorias %s Derrotas %s Empates' % (victorias, derrotas,empates))
    while True:
        print('Elige tu movimiento (p)iedra, (pa)pel y (t)ijeras')
        jugada =input()
        if jugada== 'q':
            sys.exit() #cierra el programa
        if jugada == 'p'or jugada == 'pa' or jugada =='t':
            break
        print('pon una de las opciones: p pa t')
        #elecciones del jugador

        if jugada == 'p':
            print('Piedra versus...')
        elif(jugada== 'pa'):
            print('papel versus...')
        elif(jugada =='t'):
            print('Tijera versus...')

        

        numero_random = random.randint(1,3)
        if numero_random == 1:
            computadora ='p'
            print('la maquina eligio PIEDRA!')
        elif numero_random == 2:
            computadora = 'pa'
            print('PAPEL!')
        elif numero_random == 3:
            computadora = 't'
            print('la maquina eligio TIJERAS!')

        if(jugada ==computadora):
            empates= empates+1
            print('Empate carajo!')
        elif(jugada == 'pa' and computadora == 't'):
            derrotas = derrotas+1
            print('Perdiste!!')      
        elif(jugada == 'p' and computadora == 'pa'):
            derrotas =derrotas+1
            print('Perdiste!!')
        elif(jugada == 't' and computadora == 'p'):
            derrotas =derrotas+1
            print('Perdiste!!')
        elif(jugada == 't' and computadora == 'pa'):
            victorias = victorias+1
            print('Ganaste palomo!!')
        elif(jugada == 'p' and computadora == 't'):
            victorias =victorias+1
            print('Ganaste palomo!!')
        elif(jugada== 'pa' and computadora == 'p'):
            victorias = victorias+1
            print('Ganaste palomo!!')




import random, sys

print('¡Bienvenido! Veamos si eres duro en esta vaina...')
print('Esto es piedra, papel y tijeras.')
victorias = 0
derrotas = 0
empates = 0

while True:
    print('%s Victorias %s Derrotas %s Empates' % (victorias, derrotas, empates))
    while True:
        print('Elige tu movimiento: (p)iedra, (pa)pel o (t)ijeras (o presiona q para salir)')
        jugada = input()
        if jugada == 'q':
            sys.exit() # Cierra el programa
        if jugada in ['p', 'pa', 't']:
            break
        print('Pon una de las opciones: p, pa, t')

    # Elecciones del jugador
    if jugada == 'p':
        print('Piedra versus...')
    elif jugada == 'pa':
        print('Papel versus...')
    elif jugada == 't':
        print('Tijera versus...')

    numero_random = random.randint(1, 3)
    if numero_random == 1:
        computadora = 'p'
        print('¡La máquina eligió PIEDRA!')
    elif numero_random == 2:
        computadora = 'pa'
        print('¡La máquina eligió PAPEL!')
    elif numero_random == 3:
        computadora = 't'
        print('¡La máquina eligió TIJERAS!')

    if jugada == computadora:
        empates += 1
        print('¡Empate carajo!')
    elif (jugada == 'pa' and computadora == 't') or (jugada == 'p' and computadora == 'pa') or (jugada == 't' and computadora == 'p'):
        derrotas += 1
        print('¡Perdiste!')
    else:
        victorias += 1
        print('¡Ganaste palomo!')"""


"""

#exception handling manejo de excepciones para evitar que un codigo completo te crashee




def spam(dividepor):
    try: 
        return 42 / dividepor
    except ZeroDivisionError:
        print('Compay ta dividiendo entre 0 kllk!?')

print(spam(2))
print(spam(12))
print(spam(10))
print(spam(0))


#Juego del ZigZag usando try


import time, sys
indent= 0
indentcreciente= True
try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.3)
        if indentcreciente:
            indent=indent+1
            if indent== 20:
                indentcreciente =False
        
        else:
            indent=indent-1
            if indent==0:
                indentcreciente= True
except KeyboardInterrupt:
    sys.exit()
 """


#LISTAS PAPUAAA
#spam = [['gato' , 'Perro', ], [1,2,2]]
#spam[0]

#spam = ['gato' , 'Perro', 'Lila']
#print(spam [0])

#spam = ['gato' , 'Perro', 'Lila','epoi','quale', 'idea']
#print(spam[1:4])  perro, lila, epoi


# print(spam[:2]) solo los 2 primeros... imprimira gato perro

# print(spam[1:]) imprime todos menos el primero
#print(spam[:]) imprime todo lo que tenga

#print(spam[1:])

"""
gatos = []
while True:
    print('Ingresa el nombre del gato Numero ' + str(len(gatos)+1) + ' o NO PONGA DATA PA DETENERME')
    nombre= input()   
    if nombre == '':
        break
    gatos = gatos + [nombre]
print('Los gatos se llaman: ')
for nombre in gatos:
    print(' ' +nombre)



productos= ['pera','zapato','manzana','yuca']
for i in range(len(productos)):
    print('En el indice ' + str(i) + ' el producto que tenemos es: ' + productos[i])

    #En el indice 0 el producto que tenemos es: pera
    #En el indice 1 el producto que tenemos es: zapato 
    #En el indice 2 el producto que tenemos es: manzana
    #En el indice 3 el producto que tenemos es: yuca 
"""
#'perro' in ['perro','gato','chucho','raton']
# RESULTADO SERA TRUE


#metodos de las listas 
#.append, .insert, .index, . remove, .sort, .reverse    

#TUPLAS, lo mismo que las listas solo que en vez de [] son (), y su data no se altera como en las listas
#para indicar una tupla de 1 solo valor seria ponerle una coma, por ej.  producto=("perro",)

