#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ExperiNurse preAlpha v.1.0.0
Left panel with board
author: Konrad "Ironus" Zierek
website: github.com/Ironus/DSZI
last edited: March 2016
"""

import sys
import random
import os
import time
import collections
import heapq
import threading
from random import randint
from helpers import Searcher
from object_class import Object
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QBasicTimer, pyqtSlot, pyqtSignal,QPoint, Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QImage, QBrush, QTransform, \
    QPicture, QPixmap
from knowledge_base.driver import *
from symp_scanner import SymptomLoader
from diag import Diagnosis
from check import *

dict = {}
class SquareGrid:
    """
    Grid used as a replacement for SimpleGraph
    """

    def __init__(self, width, height):
        """
        Initiate, set width and height of the grid
        and create holder for walls (impenetrable objects)
        """
        self.width = width
        self.height = height
        self.walls = []

    def setWalls(self, *objects):
        """
        Inserts correct values into walls
        """
        for obj in objects:
            position = obj.getPosition()
            dimensions = obj.getSize()

            for x in range(int(position[0]/80),
                           int((position[0] +
                                dimensions[0]) / 80)):
                for y in range(int(position[1] / 80),
                               int((position[1] +
                                    dimensions[1]) / 80)):
                    self.walls.append((x, y))

    def inBounds(self, id):
        """
        Check if id (x and y) are in greed boundaries
        """
        (x, y) = id

        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        """
        Check if id (x and y) is wall or not
        """
        return id not in self.walls

    def neighbours(self, id):
        """
        Return positions that are connected to id
        """
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

        if (x + y) % 2 == 0:
            results.reverse()

        results = filter(self.inBounds, results)
        results = filter(self.passable, results)

        return results


class GridWithWeights(SquareGrid):
    """
    Wrapper for basic square grid
    """
    def __init__(self, width, height):
        """
        Initiate and set weight holder
        """
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        """
        Return cost of going from 1st node to the 2nd one
        """
        return self.weights.get(to_node, 1)


class PriorityQueue:
    """
    Wrapper for binary heap
    """
    def __init__(self):
        """
        Create holder for elements
        """
        self.elements = []

    def empty(self):
        """
        Check if empty
        """
        return len(self.elements) == 0

    def put(self, item, priority):
        """
        Add to heap
        """
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """
        Retrieve from heap
        """
        return heapq.heappop(self.elements)[1]


class Object:
    """
    STATIC (!) object on map, like "bed", "curtain" - collider
    """

    def __init__(self, name, position, size, pixmap_id,
                 rotation_angle=0):
        """
        Instatiating object with basic information.
        Position and size are tuples.
        Angle as default is 0.
        """

        self.name = name
        self.position = position
        self.size = size
        self.pixmap_id = pixmap_id
        self.rotation_angle = rotation_angle

    def getAngle(self):
        """
        Returns rotation angle
        """

        return self.rotation_angle

    def getPixmap(self):
        """
        Return pixmap id
        """

        return self.pixmap_id

    def getState(self):
        """
        Returns four values: pos_x, pos_y, width, height
        """

        return \
            self.position[0], self.position[1], \
            self.size[0], self.size[1]

    def getPosition(self):
        """
        Returns tuple with current objets position
        """

        return self.position

    def getSize(self):
        """
        Return tuple with objects size
        """

        return self.size

    def getName(self):
        """
        Returns object name
        """

        return self.name

    def changePixmap(self, pixmap_id):
        self.pixmap_id = pixmap_id


class Board(QFrame):
    """
    Main board drawing ambulatory room + animation
    """

    emitText = pyqtSignal(str)

    refreshRate = 300
    board_width = 720
    board_height = 560
    graph_width = int(board_width / 80)
    graph_height = int(board_height / 80)
    tile_size = 80
    player_size = 80
    move_speed = 20
    debug_mode = False
    right_foot = False

    player_x = 0
    player_y = 160
    is_operating = False

    inference_method = "Regułowe"
    pathFinding = "aStar"

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent
        # self.initBoard()

        self.loadPixmaps()
        self.use_this_pixmap = self.nurse_pixmap

        # setting logical value for information about animation state
        self.isStopped = False
        self.isActive = False

        self.symptoms = []

        # creating empty list of points of size board_width x board_height
        self.board = [
            [
                ''
                for x in range(self.board_width)
            ]
            for y in range(self.board_height)
        ]

        # creating list of static map objects
        # PIXMAPs are declared in function self.loadPixmaps()

        self.objects = {
            Object("curtain1",  (0, 0),     (80, 160),  7),
            Object("bed1",      (80, 0),    (80, 160),  4),
            Object("curtain2",  (240, 0),   (80, 160),  7),
            Object("bed2",      (320, 0),   (80, 160),  4),
            Object("curtain3",  (480, 0),   (80, 160),  7),
            Object("bed3",      (560, 0),   (80, 160),  5),
            # Object("table_top", (640, 240), (80, 80),   8, 90),
            Object("table",     (640, 400), (80, 80),   9, 90),
            Object("curtain4",  (0, 240),   (160, 80),  7, 90),
            Object("bed4",      (0, 320),   (160, 80),  6, 270),
            Object("curtain5",  (0, 480),   (160, 80),  7, 90),
            # Object
        }

        for obj in self.objects:
            if obj.getName() == 'bed3' or obj.getName() == 'bed4':
                obj.changePixmap(4)

        """
        Creating graph to get paths
        """
        self.graph = GridWithWeights(self.graph_width,
                                     self.graph_height)
        self.graph.setWalls(*self.objects)
        self.path = []

        # drawing static objects on map
        # self.fillBoard(80, 0, 40, 80, 'bed')

        # creating timer
        self.timer = QBasicTimer()

    def diagnose(self):
        self.is_operating = True
        get_symptoms_disease_relation_from_rows()
        if self.inference_method == 'Regułowe':
            diseases_list = []
            symptom_list = []
            name = str(randint(0, 1000000))
            while (True):
                self.emitText.emit("Nurse: Co Ci dolega?")

                while not self.symptoms:
                    time.sleep(0.1)
                if (self.symptoms): symptom_list.append(self.symptoms)

                symp = check_knowledge(dict, self.symptoms)
                print(dict)
                if (check_knowledge(dict, self.symptoms)):
                    result = check_knowledge(dict, self.symptoms)
                    self.emitText.emit("masz %s ?" % result[0])
                    self.emitText.emit("Jeśli tak to cierpisz na %s" % result[1])
                    break
                diseases_list = Diagnosis.perform_diagnosis(name, self.symptoms)
                if (len(diseases_list) == 1):
                    break
                else:
                    self.emitText.emit("--Liczba możliwych chorób to: %s--" % len(diseases_list))
                self.symptoms = []

            if (diseases_list):
                self.emitText.emit("%s cierpi na: %s" % (name, diseases_list[0]))
                key = str(diseases_list[0])
                dict.setdefault(key, [])
                dict.update({key: symptom_list})

            self.getPatientOufOf(self.current_bed)
            self.is_operating = False
            self.symptoms = []

    @pyqtSlot(str)
    def inferenceEmitted(self, method):
        self.inference_method = method

    @pyqtSlot(str)
    def pathMethod(self, method):
        if method == "A Star":
            self.pathFinding = "aStar"
        elif method == "Dijkstra":
            self.pathFinding = "dijkstra"

    @pyqtSlot()
    def newPatient(self):
        emptyBeds = self.getEmptyBeds()

        if emptyBeds:
            index = randint(0, len(emptyBeds) - 1)
            self.putPatientInto(emptyBeds[index].getName())
        else:
            self.emitText.emit('Brak wolnych lóżek')

    @pyqtSlot(str)
    def textEmitted(self, symptoms):

        self.symptoms = SymptomLoader.scanInput(symptoms)

    def loadPixmaps(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = base_dir[:-4]

        # tiles = QImage(base_dir + r'/images/40_kafelki.gif')
        # tiles = QImage(base_dir + r'/images/podloga80x80.png')
        # tiles = QImage(base_dir + r'/images/podloga1_80x80.png')
        # tiles = QImage(base_dir + r'/images/podloga2_80x80.png')
        # tiles = QImage(base_dir + r'/images/podloga3_80x80.png')
        tiles = QImage(base_dir + r'/images/podloga4_80x80.png')
        # tiles = QImage(base_dir + r'/images/kafelki.gif')
        self.tiles_brush = QBrush(tiles)

        """
        self.nurse_pixmap = QPixmap(base_dir +
                                    r'/images/nurse_standing40x40.png')
        """

        self.nurse_pixmap = QPixmap(base_dir +
                                    r'/images/nurse_standing80x80.png')
        self.nurse_pixmap_base = self.nurse_pixmap

        """
        self.nurse_left_pixmap = QPixmap(base_dir +
                                         r'/images/nurse_left40x40.png')
        """
        self.nurse_left_pixmap = QPixmap(base_dir +
                                         r'/images/nurse_left80x80.png')
        self.nurse_left_pixmap_base = self.nurse_left_pixmap

        """
        self.nurse_right_pixmap = QPixmap(base_dir +
                                            r'/images/nurse_right40x40.png')
        """
        self.nurse_right_pixmap = QPixmap(base_dir +
                                          r'/images/nurse_right80x80.png')

        # self.nurse_pixmap = QPixmap(base_dir +
        # r'/images/nurse_standing40x40.png')
        # self.nurse_pixmap = QPixmap(base_dir +
        # r'/images/nurse_standing80x80.png')
        self.nurse_pixmap = QPixmap(base_dir +
        r'/images/pigula_koczek80x80.png')
        self.nurse_pixmap_base = self.nurse_pixmap

        # self.nurse_left_pixmap = QPixmap(base_dir +
        # r'/images/nurse_left40x40.png')
        # self.nurse_left_pixmap = QPixmap(base_dir +
        # r'/images/nurse_left80x80.png')
        self.nurse_left_pixmap = QPixmap(base_dir +
        r'/images/pigula_koczek_lewa80x80.png')
        self.nurse_left_pixmap_base = self.nurse_left_pixmap

        # self.nurse_right_pixmap = QPixmap(base_dir +
        # r'/images/nurse_right40x40.png')
        # self.nurse_right_pixmap = QPixmap(base_dir +
        # r'/images/nurse_right80x80.png')
        self.nurse_right_pixmap = QPixmap(base_dir +
        r'/images/pigula_koczek_prawa80x80.png')

        self.nurse_right_pixmap_base = self.nurse_right_pixmap

        """
        self.empty_bed_pixmap = QPixmap(base_dir +
                                        r'/images/lozko40x80.gif')
        """

        self.empty_bed_pixmap = QPixmap(base_dir +
                                        r'/images/lozko80x160.gif')

        """
        self.girl_alarm_pixmap = QPixmap(base_dir +
                                           r'/images/girlAlarm40x80.gif')
        """

        self.girl_alarm_pixmap = QPixmap(base_dir +
                                         r'/images/girlAlarm80x160.gif')

        # self.empty_bed_pixmap = QPixmap(base_dir +
        # r'/images/lozko40x80.gif')
        # self.empty_bed_pixmap = QPixmap(base_dir +
        # r'/images/lozko80x160.gif')
        self.empty_bed_pixmap = QPixmap(base_dir +
        r'/images/lozko7_80x160.png')

        """
        self.girl_sleeping_pixmap = QPixmap(base_dir +
                                            r'/images/girlSleeping40x80.gif')
        """

        self.girl_sleeping_pixmap = QPixmap(base_dir +
                                            r'/images/girlSleeping80x160.gif')
        # self.girl_sleeping_pixmap = QPixmap(base_dir +
        # r'/images/girlSleeping40x80.gif')
        # self.girl_sleeping_pixmap = QPixmap(base_dir +
        # r'/images/girlSleeping80x160.gif')
        self.girl_sleeping_pixmap = QPixmap(base_dir +
        r'/images/lozko7_asleep_80x160.png')

        # self.table_top_pixmap = QPixmap(base_dir + r'/images/blat40x40.png')
        self.table_top_pixmap = QPixmap(base_dir + r'/images/blat80x80.png')

        # self.table_pixmap = QPixmap(base_dir + r'/images/szafka40x40.png')
        self.table_pixmap = QPixmap(base_dir + r'/images/szafka80x80.png')

        """
        self.curtain_pixmap = QPixmap(base_dir +
                                      r'/images/CurtainOnly40x80.gif')
        self.curtain_pixmap = QPixmap(base_dir +
                                      r'/images/CurtainOnly40x160.gif')
        """

        self.curtain_pixmap = QPixmap(base_dir +
                                      r'/images/CurtainOnly80x160.gif')

        # creating dictionary of brushes!
        self.pixmaps = {
            1: self.nurse_pixmap,
            2: self.nurse_left_pixmap,
            3: self.nurse_right_pixmap,
            4: self.empty_bed_pixmap,
            5: self.girl_alarm_pixmap,
            6: self.girl_sleeping_pixmap,
            7: self.curtain_pixmap,
            8: self.table_top_pixmap,
            9: self.table_pixmap
        }

    @pyqtSlot()
    def start(self):
        """
        Function responsible for preparing animation when
        start button has been pressed
        """

        if self.isActive:
            return

        if self.isStopped:
            self.isStopped = False

        self.isActive = True

        self.timer.start(self.refreshRate, self)

    @pyqtSlot()
    def stop(self):
        """
        Function responsible for stoping animation when
        stop button pressed
        """
        if not self.isActive:
            return

        self.isStopped = True
        self.isActive = False

        self.timer.stop()

        self.update()

    @pyqtSlot(str)
    def move(self, direction):
        """
        Function responsible for moving main character up.
        """

        self.rotatePlayer(direction)
        self.fillRealBoard(self.player_x, self.player_y,
                           self.player_size, self.player_size, '')

        if direction == 'up' and not self.collision(direction):
            self.makeStep(direction, -self.move_speed)

        elif direction == 'right' and not self.collision(direction):
            self.makeStep(direction, self.move_speed)

        elif direction == 'down' and not self.collision(direction):
            self.makeStep(direction, self.move_speed)

        elif direction == 'left' and not self.collision(direction):
            self.makeStep(direction, -self.move_speed)

        self.fillRealBoard(self.player_x, self.player_y,
                           self.player_size, self.player_size, 'player')

    def makeStep(self, direction, distance):
        # print('distance: ' + str(distance) + '\t 1/4th: ' + str(distance/4))

        # determining size of first step (can't be float)
        half_of_distance = int(distance / 2)

        # determinig which foot now
        if self.right_foot:
            foot_pixmap = self.nurse_left_pixmap
        else:
            foot_pixmap = self.nurse_right_pixmap

        # next time it will be another foot
        self.right_foot = not self.right_foot

        if direction in ['up', 'down']:
            # changing POS_Y
            self.player_y += half_of_distance
            self.use_this_pixmap = foot_pixmap
            self.repaint()

            time.sleep(0.05)

            self.player_y += half_of_distance
            self.use_this_pixmap = self.nurse_pixmap
            self.repaint()

        elif direction in ['left', 'right']:
            # changing POS_X
            self.player_x += half_of_distance
            self.use_this_pixmap = foot_pixmap
            self.repaint()

            time.sleep(0.05)

            self.player_x += half_of_distance
            self.use_this_pixmap = self.nurse_pixmap
            self.repaint()

    @pyqtSlot()
    def debug(self):
        """
        PyQt slot for signal to change map-drawing-mode
        debug   - black background & red objects
        normal  - normal :P
        """

        self.debug_mode = not self.debug_mode

    def getEmptyBeds(self):
        emptyBeds = []

        for obj in self.objects:
            if ((obj.getName() == 'bed1' or
                    obj.getName() == 'bed2' or
                    obj.getName() == 'bed3' or
                    obj.getName() == 'bed4') and
                    (obj.getPixmap() is 4)):
                emptyBeds.append(obj)

        return emptyBeds

    def getTakenBeds(self):
        takenBeds = []

        for obj in self.objects:
            if ((obj.getName() == 'bed1' or
                    obj.getName() == 'bed2' or
                    obj.getName() == 'bed3' or
                    obj.getName() == 'bed4') and
                    (obj.getPixmap() is not 4)):
                takenBeds.append(obj)

        return takenBeds

    def putSleepingPatientInto(self, bed_name):
        for obj in self.objects:
            if obj.getName() == bed_name and obj.getPixmap() != 6:
                obj.changePixmap(6)

    def putPatientInto(self, bed_name):
        for obj in self.objects:
            if obj.getName() == bed_name and obj.getPixmap() != 5:
                obj.changePixmap(5)

    def getPatientOufOf(self, bed_name):
        for obj in self.objects:
            if obj.getName() == bed_name and obj.getPixmap() != 4:
                obj.changePixmap(4)

    def rotatePlayer(self, direction):
        """
        Function responsible for rotating players icon.
        """

        rotation = QTransform()

        if direction == 'up':
            rotation.rotate(0)
        elif direction == 'right':
            rotation.rotate(90)
        elif direction == 'down':
            rotation.rotate(180)
        elif direction == 'left':
            rotation.rotate(270)

        self.use_this_pixmap = \
            self.nurse_pixmap_base.transformed(rotation)
        self.nurse_pixmap = \
            self.nurse_pixmap_base.transformed(rotation)
        self.nurse_left_pixmap = \
            self.nurse_left_pixmap_base.transformed(rotation)
        self.nurse_right_pixmap = \
            self.nurse_right_pixmap_base.transformed(rotation)

        """
        self.player_left_brush =
        QBrush(self.player_left_base.transformed(rotation))
        self.player_right_brush =
        QBrush(self.player_right_base.transformed(rotation))
        self.player_brush =
        QBrush(self.player_image_base.transformed(rotation))
        """

    def collision(self, direction):
        """
        Main function responsible for collision detection.
        """

        # These -/+ 1 comes from the fact, that we aren't checking
        # corners but pixels diagonally to the inside of player icon
        # @@@@@@@@@@@@
        # @*@@@@@@@@*@
        # @@@@@@@@@@@@
        # @@@@@@@@@@@@
        # @@@@@@@@@@@@
        # @*@@@@@@@@*@
        # @@@@@@@@@@@@

        # (x1, y1) - TOP LEFT
        # (x2, y2) - TOP RIGHT
        if direction == 'up':
            x1 = self.player_x + 1
            y1 = self.player_y - self.move_speed + 1

            x2 = self.player_x + self.player_size - 1
            y2 = y1

        # (x1, y1) - TOP RIGHT
        # (x2, y2) - BOTTOM RIGHT
        elif direction == 'right':
            x1 = self.player_x + self.player_size + self.move_speed - 1
            y1 = self.player_y + 1

            x2 = x1
            y2 = self.player_y + self.player_size - 1

        # (x1, y1) - BOTTOM LEFT
        # (x2, y2) - BOTTOM RIGHT
        elif direction == 'down':
            x1 = self.player_x + 1
            y1 = self.player_y + self.player_size + self.move_speed - 1

            x2 = self.player_x + self.player_size - 1
            y2 = y1

        # (x1, y1) - TOP LEFT
        # (x2, y2) - BOTTOM LEFT
        elif direction == 'left':
            x1 = self.player_x - self.move_speed + 1
            y1 = self.player_y + 1

            x2 = x1
            y2 = self.player_y + self.player_size - 1

        try:
            # no collision if value is "" (empty string)
            if self.board[y1][x1] or self.board[y2][x2]:
                print("Collision! There is: {0} or \
                      {1}".format(self.board[y1][x1], self.board[y2][x2]))
                return True
            elif direction == 'up' and y1 < 0:
                return True
            elif direction == 'right' and x1 > self.board_width:
                return True
            elif direction == 'down' and y1 > self.board_height:
                return True
            elif direction == 'left' and x1 < 0:
                return True
            else:
                return False
        except IndexError:
            return True

    def paintEvent(self, event):

        painter = QPainter(self)

        if self.debug_mode:
            self.drawRealBoard(painter)
        else:
            self.drawBoard(painter)
            self.drawPlayer(painter)

        self.update()

    def timerEvent(self, event):
        """
        Overwritten function of timer event
        """

        if event.timerId() == self.timer.timerId():
            takenBeds = self.getTakenBeds()

            if not self.is_operating and takenBeds:
                self.goToPatient(takenBeds)

        else:
            super(Board, self).timerEvent(event)

    def goToPatient(self, takenBeds):
        if takenBeds:
            index = randint(0, len(takenBeds) - 1)
            x, y = takenBeds[index].getPosition()
            sizeX, sizeY = takenBeds[index].getSize()

            pointX = int(x / 80)
            pointY = int(y / 80)

            if takenBeds[index].getName() == 'bed4':
                pointY = int(pointY + sizeY / 80)
            else:
                pointX = int(pointX + sizeX / 80)

            self.current_bed = takenBeds[index].getName()

            playerX = int(self.player_x / 80)
            playerY = int(self.player_y / 80)

            if self.pathFinding == "aStar":
                cameFrom, costSoFar = self.aStarSearch(self.graph,
                                                      (playerX, playerY),
                                                      (pointX, pointY))
            elif self.pathFinding == "dijkstra":
                cameFrom, costSoFar = self.dijkstraSearch(self.graph,
                                                         (playerX, playerY),
                                                         (pointX, pointY))

            self.path = self.reconstructPath(cameFrom,
            (playerX, playerY),
            (pointX, pointY))

            if playerX is pointX and playerY is pointY:
                self.is_operating = True
                diagnoseThread = threading.Thread(target=self.diagnose)
                diagnoseThread.start()
            else:
                self.movePlayer()

    def movePlayer(self):
        pathToMove = self.path[1:]

        for nextPointX, nextPointY in pathToMove:
            nextPointX = nextPointX * 80
            nextPointY = nextPointY * 80

            if self.player_x < nextPointX:
                while self.player_x < nextPointX:
                    self.move('right')
            elif self.player_x > nextPointX:
                while self.player_x > nextPointX:
                    self.move('left')
            elif self.player_y < nextPointY:
                while self.player_y < nextPointY:
                    self.move('down')
            elif self.player_y > nextPointY:
                while self.player_y > nextPointY:
                    self.move('up')


    def drawBoard(self, painter):
        """
        Main function for QPainter
        """

        # drawing tiles
        painter.setBrush(self.tiles_brush)
        painter.drawRect(
            0,
            0,
            self.board_width,
            self.board_height
        )

        self.drawObjects(painter)

    def drawObjects(self, painter):
        """
        Drawing objects like bed or curtain on map.
        """

        # reminder:
        # obj = [(pos_x, pos_y), (width, height), PIXMAP, ROTATION_ANGLE]
        for obj in self.objects:
            if obj.getAngle() != 0:
                rotation = QTransform()
                rotation.rotate(obj.getAngle())
                pixmap = self.pixmaps[obj.getPixmap()].transformed(rotation)
            else:
                pixmap = self.pixmaps[obj.getPixmap()]

            state = obj.getState()
            painter.drawPixmap(
                state[0],   # pos_x
                state[1],   # pos_y
                state[2],   # width
                state[3],   # height
                pixmap
            )

            # Drawing path - delete when not needed
            for (x, y) in self.path:
                painter.setPen(Qt.red)
                painter.drawRect(x * 80, y * 80, 80, 80)

            self.fillRealBoard(
                state[0],   # pos_x
                state[1],   # pos_y
                state[2],   # width
                state[3],   # height
                obj.getName()
            )

    def fillRealBoard(self, start_x, start_y, width, height, content):
        for y in range(start_y, start_y + height):
            for x in range(start_x, start_x + width):
                self.board[y][x] = content

        """
        print('filling board from {0} to {1} and \
              from {2} to {3} with {4}'.format(start_x, width,
                                               start_y, height, content))
        """

    def drawRealBoard(self, painter):
        """
        Only for debug, prints self.board pixel by pixel
        """
        for y in range(self.board_height):
            for x in range(self.board_width):
                if self.board[y][x] != '':
                    print(str(x) + 'x' + str(y) +
                          ' - ' + str(self.board[y][x]))
                    painter.setPen(Qt.red)
                    painter.drawRect(x, y, 1, 1)
                else:
                    painter.setPen(Qt.black)
                    painter.drawRect(x, y, 1, 1)

        self.update()

    def drawPlayer(self, painter):

        painter.drawPixmap(
            self.player_x,
            self.player_y,
            self.player_size,
            self.player_size,
            self.use_this_pixmap
        )

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def dijkstraSearch(self, graph, start, goal):
        """
        Algorytm Dijkstry
        """
        steps = PriorityQueue()
        steps.put(start, 0)
        cameFrom = {}
        costSoFar = {}
        cameFrom[start] = None
        costSoFar[start] = 0

        # dopoki cos w liscie krokow
        while not steps.empty():
            # pozyskaj miejsce, w ktorym jestes
            current = steps.get()

            # jesli dotarles do celu, to przerwij
            if current == goal:
                break

            # dla kazdego z sasiadow
            for next in graph.neighbours(current):
                # oblicz nowy koszt dojscia (dotychczasowy + do sasiada)
                newCost = costSoFar[current] + graph.cost(current, next)
                # jezeli koszt nie istnial wczesniej
                # lub jest nizszy niz poprzednik
                # to umiesc go w liscie kosztow do nastepnego kroku
                if next not in costSoFar or newCost < costSoFar[next]:
                    costSoFar[next] = newCost
                    # jako priorytet ustaw koszt
                    priority = newCost
                    steps.put(next, priority)
                    cameFrom[next] = current

        # zwroc koszt dojscia i liste krokow (lista od konca)
        return cameFrom, costSoFar

    def aStarSearch(self, graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbours(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far

    def reconstructPath(self, came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def draw_tile(self, graph, id, style, width):
        r = "."
        if 'number' in style and id in style['number']:
            r = "%d" % style['number'][id]
        if ('point_to' in style and
                style['point_to'].get(id, None) is not None):
            (x1, y1) = id
            (x2, y2) = style['point_to'][id]
            if x2 == x1 + 1:
                r = "\u2192"
            if x2 == x1 - 1:
                r = "\u2190"
            if y2 == y1 + 1:
                r = "\u2193"
            if y2 == y1 - 1:
                r = "\u2191"
        if 'start' in style and id == style['start']:
            r = "A"
        if 'goal' in style and id == style['goal']:
            r = "Z"
        if 'path' in style and id in style['path']:
            r = "@"
        if id in graph.walls:
            r = "#" * width
        return r

    def draw_grid(self, graph, width=2, **style):
        for y in range(graph.height):
            for x in range(graph.width):
                print("%%-%ds" % width % self.draw_tile(graph, (x, y),
                      style, width), end="")
            print()

    @pyqtSlot(str)
    def goTo(self, position):
        x, y = position.split()

        pointX = int(int(x) / 80)
        pointY = int(int(y) / 80)

        playerX = int(self.player_x / 80)
        playerY = int(self.player_y / 80)

        if self.pathFinding == "aStar":
            cameFrom, costSoFar = self.aStarSearch(self.graph,
                                                  (playerX, playerY),
                                                  (pointX, pointY))
        elif self.pathFinding == "dijkstra":
            cameFrom, costSoFar = self.dijkstraSearch(self.graph,
                                                     (playerX, playerY),
                                                     (pointX, pointY))

        self.path = self.reconstructPath(cameFrom,
            (playerX, playerY),
            (pointX, pointY))
        self.movePlayer()
