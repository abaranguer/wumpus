#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import math

class Room:
    xc = 0
    yc = 0
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    doors = []

if __name__ == "__main__":
    # initialize map
    rooms = [Room() for i in range(0, 20)]
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
    
    root = tk.Tk()
    canvas = tk.Canvas(root, width=600, height=600, borderwidth=0, highlightthickness=0, bg="grey")
    j = 0
    R = 20
    for i in range(0, 5):
        x = 300 + int(80.0 * math.cos( (2.0 * math.pi / 5.0) * i)) 
        y = 300 + int(80.0 * math.sin( (2.0 * math.pi / 5.0) * i))

        rooms[j].xc = x
        rooms[j].yc = y
        rooms[j].x0 = x - R
        rooms[j].y0 = y - R
        rooms[j].x1 = x + R
        rooms[j].y1 = y + R
        j = j + 1

    for i in range(0, 10):
        x = 300 + int(180.0 * math.cos( (math.pi / 5.0) * i)) 
        y = 300 + int(180.0 * math.sin( (math.pi / 5.0) * i))

        rooms[j].xc = x
        rooms[j].yc = y
        rooms[j].x0 = x - R
        rooms[j].y0 = y - R
        rooms[j].x1 = x + R
        rooms[j].y1 = y + R
        j = j + 1

    for i in range(0, 5):
        x = 300 + int(280.0 * math.cos( (2.0 * math.pi / 5.0) * i - (math.pi / 5.0)))
        y = 300 + int(280.0 * math.sin( (2.0 * math.pi / 5.0) * i - (math.pi / 5.0)))

        rooms[j].xc = x
        rooms[j].yc = y
        rooms[j].x0 = x - R
        rooms[j].y0 = y - R
        rooms[j].x1 = x + R
        rooms[j].y1 = y + R
        j = j + 1

    for i in range(0, 20):
        canvas.create_line(rooms[i].xc, \
                           rooms[i].yc, \
                           rooms[rooms[i].doors[0]].xc, \
                           rooms[rooms[i].doors[0]].yc)

        canvas.create_line(rooms[i].xc, \
                           rooms[i].yc, \
                           rooms[rooms[i].doors[1]].xc, \
                           rooms[rooms[i].doors[1]].yc)
        
        canvas.create_line(rooms[i].xc, \
                           rooms[i].yc, \
                           rooms[rooms[i].doors[2]].xc, \
                           rooms[rooms[i].doors[2]].yc)

    for i in range(0, 20):
        canvas.create_oval(rooms[i].x0, rooms[i].y0, rooms[i].x1, rooms[i].y1, fill='white')
        canvas.create_text(rooms[i].xc, rooms[i].yc, text='%d' % i, fill='black')
        
    canvas.grid()
    root.wm_title("El Castell del Wumpus!")
    root.mainloop()
