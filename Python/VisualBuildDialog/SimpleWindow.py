import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
 QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
 QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout)


class Dialog(QDialog):
    
    def slot_method(self):
        print('slot method called.')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton("Click")
        button.clicked.connect(self.slot_method)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())