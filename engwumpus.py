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
    
    print "\nThe hunter is in the room number %d" % hunterRoom

    if wumpusRoom == hunterRoom:
        print "The wumpus is in the room! He eats you!"    
        continueGame = False

    if continueGame and (hunterRoom in (pit1Room, pit2Room)):
        print "There's an acid pit in the room! You fall there!"
        continueGame = False

    if continueGame and (hunterRoom in (bat1Room, bat2Room)):
        print "There's a bat in the room!"
        newHunterRoom = rnd.randint(0, 19)
        newBat1Room = rnd.randint(0, 19)
        newBat2Room = rnd.randint(0, 19)
        gameObjects.get("hunter").roomNumber = newHunterRoom
        gameObjects.get("bat1").roomNumber = newBat1Room
        gameObjects.get("bat2").roomNumber = newBat2Room
        print "It takes you to the room number %d" % newHunterRoom
        continueGame = enterRoom(gameObjects)

    if not continueGame:
        print "You die!"

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
    
    print "The room %d connects rooms number %d, %d and %d" % (hunterRoom, door0, door1, door2)

    print "You have %d arrows" % arrows
    
    if wumpusRoom in rooms[hunterRoom].doors:
        print "I smell a Wumpus!"

    if (bat1Room in rooms[hunterRoom].doors) or (bat2Room in rooms[hunterRoom].doors):
        print "Bats nearby!"

    if (pit1Room in rooms[hunterRoom].doors) or (pit2Room in rooms[hunterRoom].doors):
        print "I feel a draft!"
    
def actionsHunter(gameObjects):
    continueGame = True
    wumpusMove = False
    hunterRoom = gameObjects.get("hunter").roomNumber
    wumpusRoom = gameObjects.get("wumpus").roomNumber
    arrows = gameObjects.get("arrows")
    rooms = gameObjects.get("rooms")
    [door0, door1, door2] = rooms[hunterRoom].doors

    while True:
        action = raw_input("Move 'm' or Shoot 's' ? ")
        if action in ('m','s','M','S'):
            break

    while True:
        try:
            door = int(raw_input("Room %d, %d or %d ? " % (door0, door1, door2)))
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
            print "The arrow kills the Wumpus!"
            print "You win!"
            continueGame = False

    if ((action=='s' or action=='S') and \
        ((wumpusRoom <> door0) and \
         (wumpusRoom <> door1) and \
         (wumpusRoom <> door2))):
            print "You have failed!"

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
                aux = "arrow"
            else:
                aux = "arrows"
            print "Now you have %d %s" % (arrows, aux)

            if arrow == 0:
                print "You can't kill the Wumpus, and he will eat you"
                print "You die..."
            continueGame = False

            if continueGame and wumpusMove:
                print "Wumpus has moved!"

    return continueGame

def gameLoop(gameObjects):
    continueGame = True

    while continueGame:
        continueGame = enterRoom(gameObjects)
        if continueGame:
            examineRoom(gameObjects)
            continueGame = actionsHunter(gameObjects)

instructions = '''
Hunt the Wumpus
---------------
A player of the game enters commands to move through the rooms or to shoot arrows along a tunnel into one of the adjoining rooms.
There are twenty rooms, each connecting to three others, arranged like the vertices of a dodecahedron or the faces of an icosahedron (which are identical in layout).
Hazards include bottomless pits, super bats (which drop the player in a random location.
The Wumpus is described as having sucker feet (to escape the bottomless pits) and being too heavy for a super bat to lift.
When the player has deduced from hints which chamber the Wumpus is in without entering the chamber, he fires an arrow into the Wumpus's chamber to kill it.
The player wins the game if he kills the Wumpus.
However, firing the arrow into the wrong chamber startles the Wumpus, which may cause it to move to an adjacent room.
The player loses if he or she is in the same room as the Wumpus (which then eats him or her) or a bottomless pit.

Objects:
    Wumpus: your target; a beast that eats you if you ever end up in the same room.
    Bats (2): creatures that instantly carry you to a random room.
    Pits (2): fatal to you if you enter the room.

Actions: There are two possible actions:
    Move: to one of the three rooms connected to your current one.
    Shoot: fire an arrow to one of the three rooms connected to your current one.

Warning messages: Give you information about the contents of adjacent rooms.
    Wumpus: "I smell a wumpus"
    Bat: "Bats nearby"
    Pit: "I feel a draft"
'''

if __name__ == "__main__":

    print instructions

    # gameObjects = [rooms, hunter, wumpus, bat1, bat2, pit1, pit2]
    gameObjects = initializeObjects()
    
    gameLoop(gameObjects)
