import re
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    def replace(self,expression):
        # print(expression)
    # Replace the sqrt symbol with the sqrt funcion from the math module
        return eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', expression))
    
        # The Press_it Functions determines the work of the button press
    def press_it(self, pressed):
        if pressed == "C":
            self.OutputDisplay.setText("0")
        else:
            if self.OutputDisplay.text() == "0":
                self.OutputDisplay.setText("")
        



            self.OutputDisplay.setText(f'{self.OutputDisplay.text()}{pressed}')


# The evaluation Function.

    def Equals_key(self):
        # It grabs what is written on the screen.
        mystr = self.OutputDisplay.text()
        screen=mystr
        patt = re.compile(r'√')
        matches = patt.finditer(mystr)
        for match in matches:
            # print(match)
            if match !="":
                answere = self.replace(mystr)
                self.OutputDisplay.setText(str(round(answere,5)))
            else:
                
                self.OutputDisplay.setText("ERROR!!")

    def Decimal_key(self):
        screen = self.OutputDisplay.text()
        if screen[-1] == ".":
            pass
        else:
            self.OutputDisplay.setText(f'{screen}.')


#     def Root_key(self): 
#                screen = self.OutputDisplay.text()
#                self.OutputDisplay.setText(f'{screen[-1]}** 0.5') 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 605)
        MainWindow.setMinimumSize(QtCore.QSize(285, 605))
        MainWindow.setSizeIncrement(QtCore.QSize(1290, 3045))
        MainWindow.setBaseSize(QtCore.QSize(285, 605))
        MainWindow.setStyleSheet("background-color:rgb(0, 170, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputDisplay = QtWidgets.QLabel(self.centralwidget)
        self.OutputDisplay.setGeometry(QtCore.QRect(0, 0, 285, 209))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.OutputDisplay.sizePolicy().hasHeightForWidth())
        self.OutputDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.OutputDisplay.setFont(font)
        self.OutputDisplay.setMouseTracking(True)
        self.OutputDisplay.setTabletTracking(True)
        self.OutputDisplay.setFocusPolicy(QtCore.Qt.TabFocus)
        self.OutputDisplay.setStyleSheet("background-color:rgb(35, 37, 48);\n"
                                         "color:rgb(255, 255, 255);\n"
                                         "")
        self.OutputDisplay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OutputDisplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OutputDisplay.setTextFormat(QtCore.Qt.AutoText)
        self.OutputDisplay.setScaledContents(True)
        self.OutputDisplay.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.OutputDisplay.setWordWrap(True)
        self.OutputDisplay.setIndent(-5)
        self.OutputDisplay.setObjectName("OutputDisplay")
        self.C_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("C"))
        self.C_BUtton.setGeometry(QtCore.QRect(1, 210, 69, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.C_BUtton.setFont(font)
        self.C_BUtton.setMouseTracking(False)
        self.C_BUtton.setToolTip("")
        self.C_BUtton.setStatusTip("")
        self.C_BUtton.setAutoFillBackground(False)
        self.C_BUtton.setStyleSheet("QPushButton{\n"
                                    "    border-radius:5px;\n"
                                    "    background-color:rgb(53, 54, 70);\n"
                                    "    color:rgb(218, 160, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    background-color:rgb(71, 72, 94);\n"
                                    "    color:rgb(218, 160, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:rgb(82, 83, 108);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")
        self.C_BUtton.setObjectName("C_BUtton")
        self.Devide_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("/"))
        self.Devide_BUtton.setGeometry(QtCore.QRect(71, 210, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Devide_BUtton.setFont(font)
        self.Devide_BUtton.setStyleSheet("QPushButton{\n"
                                         "    border-radius:5px;\n"
                                         "    background-color:rgb(53, 54, 70);\n"
                                         "    color:rgb(218, 160, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color:rgb(71, 72, 94);\n"
                                         "    color:rgb(218, 160, 0);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color:rgb(82, 83, 108);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.Devide_BUtton.setObjectName("Devide_BUtton")
        self.Multiply_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("*"))
        self.Multiply_BUtton.setGeometry(QtCore.QRect(142, 210, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Multiply_BUtton.setFont(font)
        self.Multiply_BUtton.setStyleSheet("QPushButton{\n"
                                           "    border-radius:5px;\n"
                                           "    background-color:rgb(53, 54, 70);\n"
                                           "    color:rgb(218, 160, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color:rgb(71, 72, 94);\n"
                                           "    color:rgb(218, 160, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color:rgb(82, 83, 108);\n"
                                           "}\n"
                                           "")
        self.Multiply_BUtton.setObjectName("Multiply_BUtton")
        self.Delete_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("√"))
        self.Delete_BUtton.setGeometry(QtCore.QRect(213, 210, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Delete_BUtton.setFont(font)
        self.Delete_BUtton.setStyleSheet("QPushButton{\n"
                                         "    border-radius:5px;\n"
                                         "    background-color:rgb(53, 54, 70);\n"
                                         "    color:rgb(218, 160, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color:rgb(71, 72, 94);\n"
                                         "    color:rgb(218, 160, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color:rgb(82, 83, 108);\n"
                                         "}\n"
                                         "")
        self.Delete_BUtton.setObjectName("Delete_BUtton")
        self.Seven_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("7"))
        self.Seven_BUtton.setGeometry(QtCore.QRect(0, 261, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Seven_BUtton.setFont(font)
        self.Seven_BUtton.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "    background-color:rgb(35, 37, 48);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius:6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(48, 51, 66);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:rgb(82, 83, 108);\n"
                                        "}\n"
                                        "")
        self.Seven_BUtton.setObjectName("Seven_BUtton")
        self.One_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("1"))
        self.One_BUtton.setGeometry(QtCore.QRect(0, 363, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.One_BUtton.setFont(font)
        self.One_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.One_BUtton.setObjectName("One_BUtton")
        self.Four_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("4"))
        self.Four_BUtton.setGeometry(QtCore.QRect(0, 312, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Four_BUtton.setFont(font)
        self.Four_BUtton.setStyleSheet("QPushButton{\n"
                                       "\n"
                                       "    background-color:rgb(35, 37, 48);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    border-radius:6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color:rgb(48, 51, 66);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:rgb(82, 83, 108);\n"
                                       "}\n"
                                       "")
        self.Four_BUtton.setObjectName("Four_BUtton")
        self.sin_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("sin"))
        self.sin_BUtton.setGeometry(QtCore.QRect(0, 465, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sin_BUtton.setFont(font)
        self.sin_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.sin_BUtton.setObjectName("sin_BUtton")
        self.Power_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("**"))
        self.Power_BUtton.setGeometry(QtCore.QRect(0, 516, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Power_BUtton.setFont(font)
        self.Power_BUtton.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "    background-color:rgb(35, 37, 48);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius:6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(48, 51, 66);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:rgb(82, 83, 108);\n"
                                        "}\n"
                                        "")
        self.Power_BUtton.setObjectName("Power_BUtton")
        self.Zero_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("0"))
        self.Zero_BUtton.setGeometry(QtCore.QRect(0, 414, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Zero_BUtton.setFont(font)
        self.Zero_BUtton.setStyleSheet("QPushButton{\n"
                                       "\n"
                                       "    background-color:rgb(35, 37, 48);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    border-radius:6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color:rgb(48, 51, 66);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:rgb(82, 83, 108);\n"
                                       "}\n"
                                       "")
        self.Zero_BUtton.setObjectName("Zero_BUtton")
        self.DoubleZero_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("00"))
        self.DoubleZero_BUtton.setGeometry(QtCore.QRect(71, 414, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DoubleZero_BUtton.setFont(font)
        self.DoubleZero_BUtton.setStyleSheet("QPushButton{\n"
                                             "\n"
                                             "    background-color:rgb(35, 37, 48);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border-radius:6px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color:rgb(48, 51, 66);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color:rgb(82, 83, 108);\n"
                                             "}\n"
                                             "")
        self.DoubleZero_BUtton.setObjectName("DoubleZero_BUtton")
        self.Eight_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("8"))
        self.Eight_BUtton.setGeometry(QtCore.QRect(71, 261, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Eight_BUtton.setFont(font)
        self.Eight_BUtton.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "    background-color:rgb(35, 37, 48);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius:6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(48, 51, 66);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:rgb(82, 83, 108);\n"
                                        "}\n"
                                        "")
        self.Eight_BUtton.setObjectName("Eight_BUtton")
        self.LOG_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("log"))
        self.LOG_BUtton.setGeometry(QtCore.QRect(71, 516, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LOG_BUtton.setFont(font)
        self.LOG_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.LOG_BUtton.setObjectName("LOG_BUtton")
        self.Two_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("2"))
        self.Two_BUtton.setGeometry(QtCore.QRect(71, 363, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Two_BUtton.setFont(font)
        self.Two_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.Two_BUtton.setObjectName("Two_BUtton")
        self.Cos_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("cos"))
        self.Cos_BUtton.setGeometry(QtCore.QRect(71, 465, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Cos_BUtton.setFont(font)
        self.Cos_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.Cos_BUtton.setObjectName("Cos_BUtton")
        self.Five_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("5"))
        self.Five_BUtton.setGeometry(QtCore.QRect(71, 312, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Five_BUtton.setFont(font)
        self.Five_BUtton.setStyleSheet("QPushButton{\n"
                                       "\n"
                                       "    background-color:rgb(35, 37, 48);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    border-radius:6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color:rgb(48, 51, 66);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:rgb(82, 83, 108);\n"
                                       "}\n"
                                       "")
        self.Five_BUtton.setObjectName("Five_BUtton")
        self.Equals_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Equals_key())
        self.Equals_BUtton.setGeometry(QtCore.QRect(213, 414, 71, 153))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Equals_BUtton.setFont(font)
        self.Equals_BUtton.setStyleSheet("QPushButton{\n"
                                         "\n"
                                         "    background-color:rgb(230, 169, 0);\n"
                                         "    border-radius:6px;\n"
                                         "    color:rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color:rgb(176, 129, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color:rgb(172, 126, 0);\n"
                                         "}\n"
                                         "")
        self.Equals_BUtton.setObjectName("Equals_BUtton")
        self.Substraction_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("-"))
        self.Substraction_BUtton.setGeometry(QtCore.QRect(213, 261, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Substraction_BUtton.setFont(font)
        self.Substraction_BUtton.setStyleSheet("QPushButton{\n"
                                               "    border-radius:5px;\n"
                                               "    background-color:rgb(53, 54, 70);\n"
                                               "    color:rgb(218, 160, 0);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background-color:rgb(71, 72, 94);\n"
                                               "    color:rgb(218, 160, 0);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color:rgb(82, 83, 108);\n"
                                               "}\n"
                                               "")
        self.Substraction_BUtton.setObjectName("Substraction_BUtton")
        self.Decimal_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Decimal_key())
        self.Decimal_BUtton.setGeometry(QtCore.QRect(142, 414, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Decimal_BUtton.setFont(font)
        self.Decimal_BUtton.setStyleSheet("QPushButton{\n"
                                          "\n"
                                          "    background-color:rgb(35, 37, 48);\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    border-radius:6px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color:rgb(48, 51, 66);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color:rgb(82, 83, 108);\n"
                                          "}\n"
                                          "")
        self.Decimal_BUtton.setObjectName("Decimal_BUtton")
        self.Addition_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("+"))
        self.Addition_BUtton.setGeometry(QtCore.QRect(213, 312, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Addition_BUtton.setFont(font)
        self.Addition_BUtton.setStyleSheet("QPushButton{\n"
                                           "    border-radius:5px;\n"
                                           "    background-color:rgb(53, 54, 70);\n"
                                           "    color:rgb(218, 160, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color:rgb(71, 72, 94);\n"
                                           "    color:rgb(218, 160, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color:rgb(82, 83, 108);\n"
                                           "}\n"
                                           "")
        self.Addition_BUtton.setObjectName("Addition_BUtton")
        self.Nine_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("9"))
        self.Nine_BUtton.setGeometry(QtCore.QRect(142, 261, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Nine_BUtton.setFont(font)
        self.Nine_BUtton.setStyleSheet("QPushButton{\n"
                                       "\n"
                                       "    background-color:rgb(35, 37, 48);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    border-radius:6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color:rgb(48, 51, 66);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:rgb(82, 83, 108);\n"
                                       "}\n"
                                       "")
        self.Nine_BUtton.setObjectName("Nine_BUtton")
        self.Percentage_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("/100"))
        self.Percentage_BUtton.setGeometry(QtCore.QRect(213, 363, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Percentage_BUtton.setFont(font)
        self.Percentage_BUtton.setStyleSheet("QPushButton{\n"
                                             "    border-radius:5px;\n"
                                             "    background-color:rgb(53, 54, 70);\n"
                                             "    color:rgb(218, 160, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color:rgb(71, 72, 94);\n"
                                             "    color:rgb(218, 160, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color:rgb(82, 83, 108);\n"
                                             "}\n"
                                             "")
        self.Percentage_BUtton.setObjectName("Percentage_BUtton")
        self.ln_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("ln"))
        self.ln_BUtton.setGeometry(QtCore.QRect(142, 516, 70, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ln_BUtton.setFont(font)
        self.ln_BUtton.setStyleSheet("QPushButton{\n"
                                     "\n"
                                     "    background-color:rgb(35, 37, 48);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    border-radius:6px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgb(48, 51, 66);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color:rgb(82, 83, 108);\n"
                                     "}\n"
                                     "")
        self.ln_BUtton.setObjectName("ln_BUtton")
        self.Three_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("3"))
        self.Three_BUtton.setGeometry(QtCore.QRect(142, 363, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Three_BUtton.setFont(font)
        self.Three_BUtton.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "    background-color:rgb(35, 37, 48);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius:6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(48, 51, 66);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:rgb(82, 83, 108);\n"
                                        "}\n"
                                        "")
        self.Three_BUtton.setObjectName("Three_BUtton")
        self.Tan_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("tan"))
        self.Tan_BUtton.setGeometry(QtCore.QRect(142, 465, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Tan_BUtton.setFont(font)
        self.Tan_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.Tan_BUtton.setObjectName("Tan_BUtton")
        self.Six_BUtton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("6"))
        self.Six_BUtton.setGeometry(QtCore.QRect(142, 312, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Six_BUtton.setFont(font)
        self.Six_BUtton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Six_BUtton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "    background-color:rgb(35, 37, 48);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border-radius:6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(48, 51, 66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(82, 83, 108);\n"
                                      "}\n"
                                      "")
        self.Six_BUtton.setObjectName("Six_BUtton")
        self.ChangColor_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("Theme"))
        self.ChangColor_Button.setGeometry(QtCore.QRect(70, 570, 151, 31))
        self.ChangColor_Button.setStyleSheet("QPushButton{\n"
                                             "\n"
                                             "    background-color:rgb(255, 255, 255);\n"
                                             "    border-radius:6px;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color:rgb(227, 227, 227);\n"
                                             "}")
        self.ChangColor_Button.setObjectName("ChangColor_Button")
        self.OutputDisplay.raise_()
        self.Devide_BUtton.raise_()
        self.Multiply_BUtton.raise_()
        self.Delete_BUtton.raise_()
        self.Seven_BUtton.raise_()
        self.One_BUtton.raise_()
        self.Four_BUtton.raise_()
        self.sin_BUtton.raise_()
        self.Power_BUtton.raise_()
        self.Zero_BUtton.raise_()
        self.DoubleZero_BUtton.raise_()
        self.Eight_BUtton.raise_()
        self.LOG_BUtton.raise_()
        self.Two_BUtton.raise_()
        self.Cos_BUtton.raise_()
        self.Five_BUtton.raise_()
        self.Equals_BUtton.raise_()
        self.Substraction_BUtton.raise_()
        self.Decimal_BUtton.raise_()
        self.Addition_BUtton.raise_()
        self.Nine_BUtton.raise_()
        self.Percentage_BUtton.raise_()
        self.ln_BUtton.raise_()
        self.Three_BUtton.raise_()
        self.Tan_BUtton.raise_()
        self.Six_BUtton.raise_()
        self.C_BUtton.raise_()
        self.ChangColor_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.OutputDisplay.setText(_translate("MainWindow", "0"))
        self.C_BUtton.setText(_translate("MainWindow", "C"))
        self.Devide_BUtton.setText(_translate("MainWindow", "÷"))
        self.Multiply_BUtton.setText(_translate("MainWindow", "X"))
        self.Delete_BUtton.setText(_translate("MainWindow", "√"))
        self.Seven_BUtton.setText(_translate("MainWindow", "7"))
        self.One_BUtton.setText(_translate("MainWindow", "1"))
        self.Four_BUtton.setText(_translate("MainWindow", "4"))
        self.sin_BUtton.setText(_translate("MainWindow", "sin"))
        self.Power_BUtton.setText(_translate("MainWindow", "x^y"))
        self.Zero_BUtton.setText(_translate("MainWindow", "0"))
        self.DoubleZero_BUtton.setText(_translate("MainWindow", "00"))
        self.Eight_BUtton.setText(_translate("MainWindow", "8"))
        self.LOG_BUtton.setText(_translate("MainWindow", "log"))
        self.Two_BUtton.setText(_translate("MainWindow", "2"))
        self.Cos_BUtton.setText(_translate("MainWindow", "cos"))
        self.Five_BUtton.setText(_translate("MainWindow", "5"))
        self.Equals_BUtton.setText(_translate("MainWindow", "="))
        self.Substraction_BUtton.setText(_translate("MainWindow", "-"))
        self.Decimal_BUtton.setText(_translate("MainWindow", "."))
        self.Addition_BUtton.setText(_translate("MainWindow", "+"))
        self.Nine_BUtton.setText(_translate("MainWindow", "9"))
        self.Percentage_BUtton.setText(_translate("MainWindow", "%"))
        self.ln_BUtton.setText(_translate("MainWindow", "ln"))
        self.Three_BUtton.setText(_translate("MainWindow", "3"))
        self.Tan_BUtton.setText(_translate("MainWindow", "tan"))
        self.Six_BUtton.setText(_translate("MainWindow", "6"))
        self.ChangColor_Button.setText(
            _translate("MainWindow", "Change color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
