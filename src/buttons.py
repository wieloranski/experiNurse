#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ExperiNurse preAlpha v.1.0.0

Right panel with control buttons
author: Konrad "Ironus" Zierek
website: github.com/Ironus/DSZI
last edited: May 2016
"""

import sys
from PyQt5.QtWidgets import (QFrame, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QPushButton, QLabel, QComboBox,
                             QTreeWidget, QTreeWidgetItem)
from PyQt5.QtCore import Qt, pyqtSignal


class RightPanel(QWidget):
    """
    Right panel with application control system
    """

    start = pyqtSignal()
    stop = pyqtSignal()
    move = pyqtSignal([str])
    debug = pyqtSignal()
    inference = pyqtSignal([str])
    pathMethod = pyqtSignal([str])

    def __init__(self, parent):

        super().__init__(parent)
        self.initRightPanel()

    def initRightPanel(self):

        # vertical layout
        verticalBox = QVBoxLayout()

        # adding components and positioning them properly
        verticalBox.addWidget(PatientAlert(self, self.inference, self.pathMethod))
        verticalBox.addStretch(1)
        verticalBox.addLayout(self.createSteeringWheel())
        verticalBox.addStretch(1)
        verticalBox.addLayout(self.createControlsButtons())

        self.setLayout(verticalBox)

    def createControlsButtons(self):
        """
        Creates start and stop buttons
        """

        # horizontal layout
        horizontalBox = QHBoxLayout()

        # buttons
        startButton = QPushButton("Start", self)
        stopButton = QPushButton("Stop", self)

        # signals
        startButton.clicked.connect(self.buttonClicked)
        stopButton.clicked.connect(self.buttonClicked)

        # adding stretches and buttons to layout
        horizontalBox.addWidget(startButton)
        horizontalBox.addWidget(stopButton)

        # returning layout
        return horizontalBox

    def createSteeringWheel(self):
        """
        Creates up/right/down/left button.
        """

        # grid layout
        gridLayout = QGridLayout()

        # buttons
        upButton = QPushButton("▲", self)
        rightButton = QPushButton("▶", self)
        downButton = QPushButton("▼", self)
        leftButton = QPushButton("◀", self)
        debugButton = QPushButton("debug", self)
        # debugLabel = QLabel("Ten tryb wymaga dużo cierpliwości! :D")

        # signals
        upButton.clicked.connect(self.buttonClicked)
        rightButton.clicked.connect(self.buttonClicked)
        downButton.clicked.connect(self.buttonClicked)
        leftButton.clicked.connect(self.buttonClicked)
        debugButton.clicked.connect(self.buttonClicked)

        gridLayout.addWidget(upButton, 0, 1)
        gridLayout.addWidget(rightButton, 1, 2)
        gridLayout.addWidget(downButton, 2, 1)
        gridLayout.addWidget(leftButton, 1, 0)
        gridLayout.addWidget(debugButton, 3, 0, 1, 3)
        # gridLayout.addWidget(debugLabel, 4, 0, 1, 3)

        return gridLayout

    def buttonClicked(self):
        """
        Function responsible for emitting signal when some button
        is pressed.
        """

        if not self.signalsBlocked():
            sender = self.sender()

            if sender.text() == "Start":
                self.start.emit()
            elif sender.text() == "Stop":
                self.stop.emit()
            elif sender.text() == "▲":
                self.move.emit('up')
            elif sender.text() == "▶":
                self.move.emit('right')
            elif sender.text() == "▼":
                self.move.emit('down')
            elif sender.text() == "◀":
                self.move.emit('left')
            elif sender.text() == "debug":
                self.debug.emit()


class PatientAlert(QWidget):
    """
    Part of right panel. Shows information about patients
    that requires immediate help.
    """

    def __init__(self, parent, inference, pathMethod):

        super().__init__(parent)
        self.inference = inference
        self.pathMethod = pathMethod
        self.initPatientAlert()

    def initPatientAlert(self):

        # vertical layout
        verticalBox = QVBoxLayout()

        # main label with information if any (and which one)
        # of patients asked for help
        mainLabel = QLabel(self)
        mainLabel.setAlignment(Qt.AlignCenter)

        # default value for main label - none of the patients
        lozko = '--'
        mainLabel.setText('Pacjent z łóżka ' + lozko +
                          '\nzgłosił prośbę o pomoc')

        # tree with list of tested medications
        medicationsTree = MedicationsTree(self)

        # label to combo box
        comboLabel = QLabel(self)
        comboLabel.setAlignment(Qt.AlignLeft)
        comboLabel.setText('Metoda wnioskowania:')

        # combo box with a list of possible learning methods
        comboBox = QComboBox(self)

        # adding learning methods
        comboBox.addItem('Regułowe')

        # connecting singal's function with combo box
        comboBox.activated[str].connect(self.onActivated)

        # label to combo box
        pathComboLabel = QLabel(self)
        pathComboLabel.setAlignment(Qt.AlignLeft)
        pathComboLabel.setText('Metoda szukania drogi:')

        # combo box with a list of possible learning methods
        pathComboBox = QComboBox(self)

        # adding learning methods
        pathComboBox.addItem('A Star')
        pathComboBox.addItem('Dijkstra')

        # connecting singal's function with combo box
        pathComboBox.activated[str].connect(self.pathAlg)

        # adding elements to layout
        verticalBox.addWidget(mainLabel)
        verticalBox.addWidget(medicationsTree)
        verticalBox.addWidget(comboLabel)
        verticalBox.addWidget(comboBox)
        verticalBox.addWidget(pathComboLabel)
        verticalBox.addWidget(pathComboBox)

        # connecting layout to widget
        self.setLayout(verticalBox)

    def onActivated(self, method):
        self.inference.emit(method)

    def pathAlg(self, method):
        self.pathMethod.emit(method)


class MedicationsTree(QWidget):
    """
    Tree with possibility to dynamically add and remove
    items via signals
    """

    def __init__(self, parent):

        super().__init__(parent)
        self.initMedicationsTree()

    def initMedicationsTree(self):

        # vertical layout
        verticalBox = QVBoxLayout()

        # create tree object
        self.tree = QTreeWidget(self)
        self.tree.setHeaderLabels(["Choroba", "Znam rozwiązanie?"])
        # self.tree.setHeaderHidden(True)

        # top most item
        # self.mainRoot = QTreeWidgetItem(["Choroby"])
        # self.tree.addTopLevelItem(self.mainRoot)

        # polygon
        self.addBranch("Gorączka", "Nie")
        self.addBranch("Ból zęba", "Tak")
        self.addBranch("Ból łokcia", "Tak")

        self.deleteBranchByName("Ból zęba")
        self.deleteBranchByIndex(1)
        # print(self.countTreeItems())

        # add tree to layout
        verticalBox.addWidget(self.tree)

        self.setLayout(verticalBox)

    def addBranch(self, illness, treatable):
        """
        Adds new objects to the tree.
        """
        QTreeWidgetItem(self.tree, [illness, treatable])

    def deleteBranchByName(self, illness, flag=1):
        """
        Finds objects with given "name" in the tree.
        Removes every matching object.
        Returns nothing.

        Qt.MatchFlags
            0 - exactly
            1 - contains (default)
            2 - startswith
            3 - endswith
        """

        objects = self.tree.findItems(illness, Qt.MatchFlags(1), 0)
        for obj in objects:
            index = self.tree.indexOfTopLevelItem(obj)
            self.tree.takeTopLevelItem(index)

    def deleteBranchByIndex(self, index):
        """
        Removes object at given index from the tree.
        Returns nothing.
        """

        self.tree.takeTopLevelItem(index)

    def countTreeItems(self):
        """
        Counts objects in the tree.
        Returns this number.
        """

        return self.tree.topLevelItemCount()
