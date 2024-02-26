# Created: August 2022
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QSizePolicy, QLabel, QFormLayout, QRadioButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import math
class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 500)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setStyleSheet("background-color: black; color: white;")
        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        font = QtGui.QFont("Courier New", 14)  
        self.display.setFont(font)
        self.base_label = QLabel('Base:', self)
        self.base_label.setStyleSheet("color: white;")
        self.base_input = QLineEdit(self)
        self.base_input.setFixedWidth(50)
        self.root_degree_label = QLabel('Root Degree:', self)
        self.root_degree_label.setStyleSheet("color: white;")
        self.root_degree_input = QLineEdit(self)
        self.root_degree_input.setFixedWidth(50)
        self.degree_button = QRadioButton('Degrees', self)
        self.radian_button = QRadioButton('Radians', self)
        self.degree_button.toggled.connect(self.on_deg_radian_toggle)
        self.radian_button.toggled.connect(self.on_deg_radian_toggle)
        self.degree_button.setChecked(True)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', '+/-', 'AC', '%', '⌫',
            'log', 'ln', '^', 'sqrt', 'cbrt', 'ⁿ√', 'x!', 'π', 'e',
            'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', '(', ')'
        ]
        grid_layout = QGridLayout()
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            button.clicked.connect(self.on_button_click)
            font = QtGui.QFont("Courier New", 11)
            font.setBold(True)
            button.setFont(font)
            if button_text.isdigit():
                button.setStyleSheet("background-color: rgb(153, 255, 255); color: black; border-radius: 15px;")
            elif button_text in ['AC', '%', '+/-', '.', 'log', 'ln', 'sqrt', 'cbrt', 'ⁿ√', '^', 'x!', 'π', 'e']:
                button.setStyleSheet("background-color: rgb(255, 255, 153); color: black; border-radius: 15px;")
            elif button_text in ['/', '*', '+', '-', '=']:
                button.setStyleSheet("background-color: rgb(255, 255, 153); color: black; border-radius: 15px;")
            elif button_text == '⌫':
                button.setStyleSheet("background-color: rgb(102, 255, 178); color: black; border-radius: 15px;")
            elif button_text in ['Deg/Rad', '(', ')']:
                button.setStyleSheet("background-color: rgb(255, 153, 153); color: black; border-radius: 15px;")
            elif button_text in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan']:
                button.setStyleSheet("background-color: rgb(255, 255, 153); color: black; border-radius: 15px;")
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        form_layout = QFormLayout()
        form_layout.addRow(self.base_label, self.base_input)
        form_layout.addRow(self.root_degree_label, self.root_degree_input)
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.degree_button)
        radio_layout.addWidget(self.radian_button)
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)
        layout.addLayout(form_layout)
        layout.addLayout(radio_layout)
        self.setLayout(layout)
        self.degrees_mode = True
    def on_button_click(self):
        button = self.sender()
        current_text = self.display.text()
        if button.text() == '=':
            try:
                expression = current_text.replace('÷', '/').replace('×', '*').replace('π', str(math.pi)).replace('e', str(math.e))
                result = str(eval(expression))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'AC':
            self.display.clear()
        elif button.text() == '%':
            try:
                result = str(eval(current_text) / 100)
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == '⌫':
            new_text = current_text[:-1]
            self.display.setText(new_text)
        elif button.text() == '+/-':
            if current_text and current_text[0] == '-':
                new_text = current_text[1:]
            else:
                new_text = '-' + current_text
            self.display.setText(new_text)
        elif button.text() == 'log':
            base = float(self.base_input.text()) if self.base_input.text() else 10.0
            try:
                result = str(math.log(float(current_text), base))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'ln':
            try:
                result = str(math.log(float(current_text)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == '^':
            self.display.setText(current_text + '^')
        elif button.text() == 'sqrt':
            try:
                result = str(math.sqrt(float(current_text)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'cbrt':
            try:
                result = str(math.pow(float(current_text), 1/3))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'ⁿ√':
            base = float(self.base_input.text()) if self.base_input.text() else 10.0
            root_degree = float(self.root_degree_input.text()) if self.root_degree_input.text() else 2.0
            try:
                result = str(math.pow(float(current_text), 1/root_degree))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'x!':
            try:
                result = str(math.factorial(int(current_text)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'π':
            new_text = current_text + 'π'
            self.display.setText(new_text)
        elif button.text() == 'e':
            new_text = current_text + 'e'
            self.display.setText(new_text)
        elif button.text() in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan']:
            try:
                angle = float(current_text)
                if self.degrees_mode and button.text() in ['sin', 'cos', 'tan']:
                    angle = math.radians(angle)
                elif not self.degrees_mode and button.text() in ['arcsin', 'arccos', 'arctan']:
                    angle = math.degrees(angle)
                if button.text() == 'sin':
                    result = str(math.sin(angle))
                elif button.text() == 'cos':
                    result = str(math.cos(angle))
                elif button.text() == 'tan':
                    result = str(math.tan(angle))
                elif button.text() == 'arcsin':
                    result = str(math.asin(angle))
                elif button.text() == 'arccos':
                    result = str(math.acos(angle))
                elif button.text() == 'arctan':
                    result = str(math.atan(angle))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif button.text() == 'Deg/Rad':
            self.degrees_mode = not self.degrees_mode
            button_text = 'Degrees' if self.degrees_mode else 'Radians'
            button.setText(button_text)
        elif button.text() in ['(', ')']:
            new_text = current_text + button.text()
            self.display.setText(new_text)
        else:
            new_text = current_text + button.text()
            self.display.setText(new_text)
    def on_deg_radian_toggle(self):
        if self.degree_button.isChecked():
            self.degrees_mode = True
        elif self.radian_button.isChecked():
            self.degrees_mode = False
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec_())
