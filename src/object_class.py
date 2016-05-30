#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Object:
    """
    STATIC (!) object on map, like "bed", "curtain" - collider
    """

    def __init__(self, name, position, size, pixmap_id, 
        rotation_angle = 0):
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

    def changePixmap(self, id):
        self.pixmap_id = id

    def getState(self):
        """
        Returns four values: pos_x, pos_y, width, height
        """

        return self.position[0], self.position[1], \
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