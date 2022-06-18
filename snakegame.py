import turtle as tortu
import time
import random as rn
import threading

posponer = 0.1

#Marcador
score = 0
highscore = 0
#Configuracion de la ventana
ventana = tortu.Screen()
ventana.title("Snake Game")
ventana.setup(width=600, height=600)
ventana.bgcolor("#a9c956")
ventana.tracer(0) #Si la snake aparece o no

#Cabeza serpierte
cabeza = tortu.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup() #si se mueve la snake no deja rastro
cabeza.goto(0,0) #Posicion de inicio
cabeza.color("#4b79e9")
cabeza.direction = "stop"

#Cabeza Tortuga (enemigo)
"""
malo = tortu.Turtle()
malo.speed(0)
malo.shape("turtle")
malo.penup()
malo.goto(100,100) #Posicion de inicio
malo.color("#be1cc9")
malo.direction = "stop"
"""

#Comida
comida = tortu.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup() #si se mueve la snake deja rastro o no
comida.goto(0,100)
comida.color("red")

#Cuerpo serpiente
segmentos = []

#Texto
texto = tortu.Turtle()
texto.speed(0) 
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0             High Score: 0" , align = "center", font= ("Arial", 24, "normal"))

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
    
def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20) #Velocidad para mover 
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)                    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)   

def morir():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"

    # Borrar los segmentos.
    if segmentos:
        for segmento in segmentos:
            segmento.hideturtle()
        segmentos.remove(nuevo_segmento)

    #Limpiar lista de segmentos
    segmentos.clear()

        
#Teclado
ventana.listen() #Para que la ventana este atenta a lo que tiene que hacer
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")

while True:
    ventana.update()

    #Movimiento de la tortuga (enemigo)
    """
    mov_random = rn.randint(1,4)
    if mov_random == 1:
        y_malo = malo.ycor()
        malo.sety(y_malo + 20)
    if mov_random == 2:
        y_malo = malo.ycor()
        malo.sety(y_malo - 20)
    if mov_random ==3:
        x_malo = malo.xcor()
        malo.setx(x_malo - 20) 
    if mov_random == 4:
        x_malo = malo.xcor()
        malo.setx(x_malo + 20)
    """
    

    #colisiones con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() >280 or cabeza.ycor() < -280:
        morir()
        #reset marcador
        score = 0
        texto.clear()
        texto.write(f"Score: {score}             High Score: {highscore}", align = "center", font= ("Arial", 24, "normal"))

    #colisiones con la comida
    if cabeza.distance(comida) < 20: #si colisiona la cabeza con comida (<20 porque la cabeza tiene por defecto 20px) se le asigna nueva posicion a la comida
        x = rn.randint(-14,14)
        y = rn.randint(-14,14)

        comida.goto(x*20,y*20) #asignacion ubicacion random a comida

        nuevo_segmento = tortu.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup() # si se mueve la snake deja rastro o no
        nuevo_segmento.color("#263d75")
        segmentos.append(nuevo_segmento)

        #Aumento marcador
        score += 10
        if score > highscore:
            highscore = score
        texto.clear()
        texto.write(f"Score: {score}             High Score: {highscore}", align = "center", font= ("Arial", 24, "normal"))
        
    #Mover el cuerpo de la serpiente
    totalsegmentos = len(segmentos)
    for index in range(totalsegmentos -1, 0, -1): #Itero hasta la cabeza de la serpiente
        x = segmentos[index -1].xcor() #Obtengo coordenadas del segmento anterior
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    if totalsegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    

    movimiento()  

    #colisiones con el cuerpo
    
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            morir()
            #reset marcador
            score = 0
            texto.clear()
            texto.write(f"Score: {score}             High Score: {highscore}", align = "center", font= ("Arial", 24, "normal"))

    time.sleep(posponer)    


##################################################################################


