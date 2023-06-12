import sys
from PySide6 import QtCore, QtWidgets, QtGui

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

model = load_model("nn_dutch_eng.h5")

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create labels and text inputs
        self.label1 = QtWidgets.QLabel("Offer supplier #1",
                                       alignment=QtCore.Qt.AlignLeft)
        self.label2 = QtWidgets.QLabel("Offer supplier #2",
                                       alignment=QtCore.Qt.AlignLeft)
        self.input1 = QtWidgets.QLineEdit()
        self.input1.setValidator(QtGui.QDoubleValidator())
        self.input2 = QtWidgets.QLineEdit()
        self.input1.setValidator(QtGui.QDoubleValidator())

        # Create grid layout to add labels and text inputs
        self.grid = QtWidgets.QGridLayout()

        self.grid.addWidget(self.label1, 0, 0, QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.input1, 0, 1)
        self.grid.addWidget(self.label2, 1, 0, QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.input2, 1, 1)

        # Create button to call model with text input values
        self.button = QtWidgets.QPushButton("Calculate")

        # Create font for result label
        self.font = QtGui.QFont()
        self.font.setPixelSize(40)

        # Create result label
        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.text.setFont(self.font)

        # Create vertical layout and add the grid, button, and result label
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addLayout(self.grid)
        self.layout.addWidget(self.button)

        self.layout.addWidget(self.text)

        # Connect clicked signal form button with magic slot
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        # Predict returns an array of arrays
        result = model.predict([[int(self.input1.text()),
                                 int(self.input2.text())]])[0][0]

        print("Model result {}".format(result))

        # 0 - English auction
        # 1 - Dutch auction
        self.text.setText("Model result {:.3f}\n{} auction".format(result, "Dutch" if round(result) else "English"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(640, 480)
    widget.show()

    sys.exit(app.exec())