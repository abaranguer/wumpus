#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as rnd

class Room:
    doors = []

class GameObject:
    roomNumber = -1

    def __init__(self, roomNumber):
        self.roomNumber = roomNumber

def initializeObjects():
    # map
    rooms = [Room() for i in range(0, 20)]

    # initialize map
    rooms[ 0].doors = [1, 4, 5]
    rooms[ 1].doors = [0, 2, 7]
    rooms[ 2].doors = [1, 3, 9]
    rooms[ 3].doors = [2, 4, 11]
    rooms[ 4].doors = [0, 3, 13]
    rooms[ 5].doors = [0, 6, 14]
    rooms[ 6].doors = [5, 7, 16]
    rooms[ 7].doors = [1, 6, 8]
    rooms[ 8].doors = [7, 9, 17]
    rooms[ 9].doors = [2, 8, 10]
    rooms[10].doors = [9, 11, 18]
    rooms[11].doors = [3, 10, 12]
    rooms[12].doors = [11, 13, 19]
    rooms[13].doors = [4, 12, 14]
    rooms[14].doors = [5, 13, 15]
    rooms[15].doors = [14, 16, 19]
    rooms[16].doors = [6, 15, 17]
    rooms[17].doors = [8, 16, 18]
    rooms[18].doors = [10, 17, 19]
    rooms[19].doors = [12, 15, 18]

    # initialize characters and objects
    wumpusRoom = -1
    bat1Room = -1
    bat2Room = -1
    pit1Room = -1
    pit2Room = -1
    hunterRoom = -1
    arrows = 5

    while (hunterRoom == wumpusRoom) or \
          (hunterRoom == bat1Room) or   \
          (hunterRoom == bat2Room) or   \
          (hunterRoom == pit1Room) or   \
          (hunterRoom == pit2Room) or   \
          (pit1Room == pit2Room) or     \
          (bat1Room == bat2Room):
        
        hunterRoom = rnd.randint(0, 19)
        wumpusRoom = rnd.randint(0, 19)
        bat1Room = rnd.randint(0, 19)
        bat2Room = rnd.randint(0, 19)
        pit2Room = rnd.randint(0, 19)
        pit2Room = rnd.randint(0, 19)

    hunter = GameObject(hunterRoom)
    wumpus = GameObject(wumpusRoom)
    bat1 = GameObject(bat1Room)
    bat2 = GameObject(bat2Room)
    pit1 = GameObject(pit1Room)
    pit2 = GameObject(pit2Room)

    return {"rooms":rooms, "hunter":hunter, "wumpus":wumpus,
            "bat1":bat1, "bat2":bat2, "pit1":pit1, "pit2":pit2, "arrows":arrows}

def enterRoom(gameObjects):
    continueGame = True
    rooms = gameObjects.get("rooms")
    hunterRoom = gameObjects.get("hunter").roomNumber
    wumpusRoom = gameObjects.get("wumpus").roomNumber
    bat1Room = gameObjects.get("bat1").roomNumber
    bat2Room = gameObjects.get("bat2").roomNumber
    pit1Room = gameObjects.get("pit1").roomNumber
    pit2Room = gameObjects.get("pit2").roomNumber
    
    print "\nEts a l'habitació número %d" % hunterRoom

    if wumpusRoom == hunterRoom:
        print "El wumpus és a l'habitació!"
        print "T'ha atrapat i comença a devorar-te!" 
        print "No és que sigui dolent... Et menja perquè és la seva natura de Wumpus..."    
        continueGame = False

    if continueGame and (hunterRoom in (pit1Room, pit2Room)):
        print "Hi ha un pou amb acid a l'habitació!"
        print "Has caigut dins i comences a dissoldre't de forma lenta i dolorosament agònica!"
        continueGame = False

    if continueGame and (hunterRoom in (bat1Room, bat2Room)):
        print "I un rat penat gegant a l'habitació! T'ha agafat i se t'emporta volant!"
        newHunterRoom = rnd.randint(0, 19)
        newBat1Room = rnd.randint(0, 19)
        newBat2Room = rnd.randint(0, 19)
        gameObjects.get("hunter").roomNumber = newHunterRoom
        gameObjects.get("bat1").roomNumber = newBat1Room
        gameObjects.get("bat2").roomNumber = newBat2Room
        print "El rat penat t'ha deixat caure a l'habitació número %d" % newHunterRoom
        continueGame = enterRoom(gameObjects)

    if not continueGame:
        print "Has mort de forma horrible!" 
        print "..." 
        print "Però altres vindran a intentar triomfar allà on tu has fracassat tan lamentablement "

    return continueGame

def examineRoom(gameObjects):
    rooms = gameObjects.get("rooms")
    hunterRoom = gameObjects.get("hunter").roomNumber
    arrows = gameObjects.get("arrows")
    wumpusRoom = gameObjects.get("wumpus").roomNumber
    bat1Room = gameObjects.get("bat1").roomNumber
    bat2Room = gameObjects.get("bat2").roomNumber
    pit1Room = gameObjects.get("pit1").roomNumber
    pit2Room = gameObjects.get("pit2").roomNumber
    [door0, door1, door2] = rooms[hunterRoom].doors
    
    print "L'habitació %d es connecta amb les habitacions %d, %d i %d" % (hunterRoom, door0, door1, door2)

    if arrows > 1:
        aux = "fletxes"
    else:
        aux = "fletxa"
    print "Encara tens %d %s" % (arrows, aux) 
    
    if wumpusRoom in rooms[hunterRoom].doors:
        print "Fa una insuportable fortor de wumpus!"
        print "Hi ha un wumpus pudent a una de les habitacions que es connecten des d'aquí!"

    if (bat1Room in rooms[hunterRoom].doors) or (bat2Room in rooms[hunterRoom].doors):
        print "Se sent soroll d'ales!"
        print "Hi ha almenys un rat penat gegant a les habitacions que es connecten des d'aquí"

    if (pit1Room in rooms[hunterRoom].doors) or (pit2Room in rooms[hunterRoom].doors):
        print "Se sent el soroll d'àcid bullint!"
        print "Hi ha almenys un pou ple d'àcid a les habitacions que es connecten des d'aquí"
    
def actionsHunter(gameObjects):
    continueGame = True
    wumpusMove = False
    hunterRoom = gameObjects.get("hunter").roomNumber
    wumpusRoom = gameObjects.get("wumpus").roomNumber
    arrows = gameObjects.get("arrows")
    rooms = gameObjects.get("rooms")
    [door0, door1, door2] = rooms[hunterRoom].doors

    while True:
        action = raw_input("Moure's 'm' o Tirar una fletxa 's' ? ")
        if action in ('m','s','M','S'):
            break

    while True:
        try:
            door = int(raw_input("A quina habitació %d, %d or %d ? " % (door0, door1, door2)))
            if door in (door0, door1, door2):
              break
        except:
            None

    if (action=='m' or action=='M'):
        gameObjects.get("hunter").roomNumber = door

    if ((action=='s' or action=='S') and \
        ((wumpusRoom == door0) or \
         (wumpusRoom == door1) or \
         (wumpusRoom == door2))):
            print "La fletxa ha matat al Wumpus!"
            print "La protectora d'animals et denunciarà si et descobreixen!"
            print "Ets l'assassí del wumpus!"
            print "Un altre sàdic que mata pobres bestioletes indefenses!"
            print "Suposo que estaràs content, criminal!"
            print "En fi. Suposo que t'he de felicitar perquè has guanyat."
            continueGame = False

    if ((action=='s' or action=='S') and \
        ((wumpusRoom <> door0) and \
         (wumpusRoom <> door1) and \
         (wumpusRoom <> door2))):
            print "has fallat! No hi havia cap wumpus a l'habitació!"

            # move wumpus
            doorsWumpus = doors[wumpusRoom].doors
            randomDoor = rnd.random()
            if randomDoor < 0.75 :
                wumpusMove= True
            if randomDoor >= 0 and randomDoor < 0.25:
                gameObjects.get("wumpus").roomNumber = doorsWumpus[0]
            if randomDoor >= 0.25 and randomDoor < 0.50:
                gameObjects.get("wumpus").roomNumber = doorsWumpus[1]
            if randomDoor >= 0.50 and randomDoor < 0.75:
                gameObjects.get("wumpus").roomNumber = doorsWumpus[2]

            arrows = arrows - 1

            if arrow == 1:
                aux = "fletxa"
            else:
                aux = "fletxes"
            print "Ara tens %d %s" % (arrows, aux)

            if arrow == 0:
                print "No tens fletxes i, per tant, ja no pots matar el Wumpus."
                print "No trigarà a descobrir-te i, aleshores, et menjarà."
                print "Serà molt dolorós i horrible..."
                print "Ja se sent com ve!"
                print "Ara entra per la porta i es llença sobre teu!"
                print "La resistència és inútil.."
                print "Encara ets conscient quan se t'empassa!"
                print "Els àcids de la seva digestio fan la resta. Has mort."
                print "Però recorda que no és que el wumpus sigui dolent..." 
                print "Et menja perquè és la seva natura de Wumpus..."
            continueGame = False

            if continueGame and wumpusMove:
                print "La fletxa ha alertat el Wumpus i es mou! espero que no vingui cap aquí!"

    return continueGame

def gameLoop(gameObjects):
    continueGame = True

    while continueGame:
        continueGame = enterRoom(gameObjects)
        if continueGame:
            examineRoom(gameObjects)
            continueGame = actionsHunter(gameObjects)

instructions = '''
Caçar el Wumpus
---------------
El Wumpus és un monstre enorme i pesat amb la pell plena de ventoses 
que s'alimenta de tot allò que cau a les seves urpes. 
Tu ets un caçador que vol aconseguir el cap del Wumpus com a trofeu 
i ets a un castell on se sap que n'hi ha un.  
El castell té vint habitacions, cada habitació es connecta amb 
altres tres habitacions.
Si entres a l'habitació on és el Wumpus, et menjarà.
Al castell hi ha un parell d'habitacions que tenen un fals terra. 
Només entrar s'ensorra el terra i caus a un pou amb un potent àcid al fons. 
Tothom que entra a una habitació amb pou, mor. 
Menys el Wumpus. El Wumpus no hi cau perquè amb les seves ventoses 
s'enganxa a les parets i no toca l'àcid.
Al castell també hi ha un parell de rats penats gegants. 
Si entres a una habitació amb un rat penat, t'agafarà, se t'emportarà volant 
i et deixarà caure a una habitació qualsevol del castell. 
Els rats penats no poden endur-se al Wumpus perquè pesa massa per ells 
i el Wumpus no es pot menjar als rats penats perquè són massa ràpids 
per atrapar-los.
Saps que a alguna de les habitacions adjacents hi ha el Wumpus
perquè mai s'ha banyat i fa molta pudor, i el pots ensumar.
Saps que a les habitacions adjacents hi poden haver rats-penats
perquè sents el soroll del batec de les seves ales,
I, finalment, saps que a les habitacions adjacents poden haver pous 
perquè sents el soroll de l'acid bullint.
Tens cinc fletxes. Has de moure't pel castell 
i quan dedueixis a quina habitació està el Wumpus, pots tirar-li 
una fletxa des d'una de les habitacions adjacents. 
Si l'habitació a la que has tirat la fletxa és la del Wumpus, 
el mataràs i hauràs guanyat. 
Però si el Wumpus no és a l'habitació, el soroll de la fletxa 
potser el posarà en alerta i farà que es mogui a alguna habitació 
contigua a la que ocupa.
Si esgotes totes les fletxes, aleshores ja no tens defensa 
possible contra el Wumpus, que et trobarà i et menjarà.
'''

if __name__ == "__main__":

    print instructions

    # gameObjects = [rooms, hunter, wumpus, bat1, bat2, pit1, pit2]
    gameObjects = initializeObjects()
    
    gameLoop(gameObjects)
