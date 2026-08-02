from edited_frontend import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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