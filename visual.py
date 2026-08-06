from edited_frontend import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from matplotlib .figure import Figure
from random_data import random_mean_reverting, random_walk
from secondary_window import Ui_Dialog


class DataCreationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Data Generation Window")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Random Data Generator")

        layout_chart = self.ui.WidgetCanvas.layout()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout_chart.addWidget(self.canvas)
        self.ui.DataButton.clicked.connect(self.open_data_window)
        self.secondary_wind = None

        data_walk = random_mean_reverting(0, 1000, 10)

        self.axes = self.figure.add_subplot()
        self.axes.plot(data_walk[0], data_walk[1], color = "purple", linewidth = 0.7)
        self.axes.set_title("Random Data Series")
        self.axes.set_xlabel("Steps")
        self.axes.set_ylabel("Values")
        self.axes.grid()
        self.canvas.draw()


    def open_data_window(self):

        if self.secondary_wind is None: 
            self.secondary_wind = DataCreationWindow(self)
            self.secondary_wind.destroyed.connect(lambda: setattr(self, "secondary_window", None))
            self.secondary_wind.show()
        else:
            self.secondary_wind.raise_()
            self.secondary_wind.activateWindow()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# start = int(input("Enter origin point: "))
# steps = int(input("Enter the amount of steps: "))
# bias = float(input("Enter the probability bias: "))

# data_random = rd.random_walk(start, steps, bias)

# plt.plot(data_random[0], data_random[1], '-', label="Random Walk Data", color = "orange", linewidth = 1)


# plt.title("Random Data Series")
# plt.xlabel("Steps")
# plt.ylabel("Position")
# plt.legend()
# plt.grid()
# plt.show()