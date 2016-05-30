#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ExperiNurse preAlpha v.1.0.0

Main script to graphic engine

author: Konrad "Ironus" Zierek
website: github.com/Ironus/DSZI
last edited: March 2016
"""

import sys
import os
import random
from buttons import RightPanel, PatientAlert
from board import Board
from console import Console
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        """
        board:   rightPanel:
        |-------|-------|
        |       |       |
        |       |       |
        |       |       |
        | board | btns  |
        |       |       |
        |       |       |
        |       |       |
        |-------|-------|
        |               |
        | console_outpt |
        |               |
        |---------------|
        | console_input |
        |---------------|
        """

        # widths
        mainWindowWidth = 1000
        rightPanelWidth = 280
        boardWidth = 720

        # heights
        mainWindowHeight = 700
        panelsHeight = 560
        consoleHeight = 140

        # application icon
        base_dir = os.path.dirname(os.path.abspath(__file__))
        iconPath = base_dir[:-4] + r'/images/redCross.png'
        self.setWindowIcon(QIcon(iconPath))

        # window resize and centering
        self.resize(mainWindowWidth, mainWindowHeight)
        self.setMinimumSize(mainWindowWidth, mainWindowHeight)
        self.setMaximumSize(mainWindowWidth, mainWindowHeight)
        self.center()
        self.setWindowTitle('ExperiNurse')

        # ambulatory board
        self.board = Board(self)
        self.board.setGeometry(0, 0, boardWidth, panelsHeight)

        # right panel for buttons and comboBox
        self.rightPanel = RightPanel(self)
        self.rightPanel.setGeometry(boardWidth, 0,
                                    rightPanelWidth, panelsHeight)

        # console
        self.console = Console(self)
        self.console.setGeometry(0, panelsHeight,
                                 mainWindowWidth, consoleHeight)

        self.rightPanel.start.connect(self.board.start)
        self.rightPanel.stop.connect(self.board.stop)
        self.rightPanel.move.connect(self.board.move)
        self.rightPanel.debug.connect(self.board.debug)
        self.rightPanel.inference.connect(self.board.inferenceEmitted)
        self.rightPanel.pathMethod.connect(self.board.pathMethod)
        self.console.textEmitted.connect(self.board.textEmitted)
        self.console.newPatient.connect(self.board.newPatient)
        self.console.goTo.connect(self.board.goTo)
        self.board.emitText.connect(self.console.printText)

        # horizontal layout
        horizontalBox = QHBoxLayout()

        # adding widgets to layout
        horizontalBox.addWidget(self.board)
        horizontalBox.addWidget(self.rightPanel)
        horizontalBox.addWidget(self.console)

        self.show()

    def center(self):
        """
        Centering main window relative to screen geometry
        """

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
