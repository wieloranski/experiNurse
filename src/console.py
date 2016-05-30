#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ExperiNurse preAlpha v.1.0.0

Widget with console used for getting user input and showing results

author: Konrad "Ironus" Zierek
website: github.com/Ironus/DSZI
last edited: March 2016
"""

import sys
import random
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit,
                             QScrollArea)
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QMargins


class Console(QWidget):

    # signals
    newPatient = pyqtSignal()
    goTo = pyqtSignal([str])
    textEmitted = pyqtSignal([str])

    def __init__(self, parent):

        super().__init__(parent)
        self.initConsole()

    def initConsole(self):

        # vertical layout
        verticalBox = QVBoxLayout()
        verticalBox.setContentsMargins(QMargins(0, 0, 0, 0))
        verticalBox.setSpacing(0)

        # output QLabel wrapped in QScrollArea
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)

        self.consoleOutput = QLabel(self)
        self.consoleOutput.setStyleSheet(
            "background-color: rgb(50, 50, 50);\
             border: none;\
             color: white;\
             padding: 0;"
        )
        self.consoleOutput.setWordWrap(True)
        self.textEmitted[str].connect(self.printText)

        self.scrollArea.setWidget(self.consoleOutput)

        # input QLineEdit
        self.consoleInput = QLineEdit(self)
        self.consoleInput.setStyleSheet(
            "background-color: rgb(50, 50, 50); \
             border: none;\
             color: white;\
             padding: 0;"
        )
        self.consoleInput.setFocus()
        self.consoleInput.returnPressed.connect(self.readText)

        # adding elements to layout
        verticalBox.addWidget(self.scrollArea)
        verticalBox.addWidget(self.consoleInput)

        # setting layout
        self.setLayout(verticalBox)

    @pyqtSlot(str)
    def readText(self):
        """
        Function responsible for retreiving text from QLineEdit
        and emitting it
        """

        # retreive text
        inputText = str(self.consoleInput.text())

        # clear QLineEdit
        self.consoleInput.setText('')

        # if new patient
        if inputText == 'Nowy pacjent':
            # emit new patient signal
            self.newPatient.emit()
        elif inputText.split()[0] == 'Idź':
            self.goTo.emit(inputText.split(None, 1)[1])
        elif inputText != '':
            # emit symptoms in signal
            self.textEmitted.emit(inputText)

    @pyqtSlot(str)
    def printText(self, text):
        """
        Function responsible for printing text into QLabel
        """

        # print text in console
        textToPrint = self.consoleOutput.text() + '\n' + text
        self.consoleOutput.setText(textToPrint)

        # move slider to the bottom
        verticalScrollBar = self.scrollArea.verticalScrollBar()
        consoleOuputHeight = self.consoleOutput.geometry().height()
        verticalScrollBar.setMaximum(consoleOuputHeight)
        verticalScrollBar.setValue(verticalScrollBar.maximum())
