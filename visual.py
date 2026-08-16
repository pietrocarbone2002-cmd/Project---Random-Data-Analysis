from edited_frontend import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import csv
from matplotlib .figure import Figure
from random_data import random_mean_reverting, random_walk
from secondary_window import Ui_Dialog
import arrow
from pathlib import Path
import os

class DataCreationWindow(QDialog):

    parameter_submitted = Signal(str, int, int, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Data Generation Window")

        #Generate Data Button
        self.ui.generate_data.clicked.connect(lambda: self.generate_data_click())

    def generate_data_click(self):
        
        #Random Walk
        if self.ui.random_walk_radio.isChecked():
            start_text = self.ui.start_value_enter.text()
            steps_text = self.ui.steps_enter.text()
            bias_text = self.ui.bias_value_enter.text()

            start = int(start_text)
            steps = int(steps_text)
            bias = float(bias_text)

            self.parameter_submitted.emit("random_walk",start, steps, bias)

        #Random Mean Reverting
        elif self.ui.mean_reverting_radio.isChecked():
            start_text = self.ui.start_point_enter.text()
            steps_text = self.ui.steps_mr_enter.text()
            sigma_text = self.ui.sigma_value_enter.text()

            start = int(start_text)
            steps = int(steps_text)
            sigma = float(sigma_text)

            self.parameter_submitted.emit("random_mean_reverting",start, steps, sigma)

        #No Method Selected
        else:
            QMessageBox.information(self,"Info", "Enter all required information!")
            return

        self.close()

#-------------------------------------------------------------------------------------------------
# MAIN WINDOW
#-------------------------------------------------------------------------------------------------

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

        self.data_list = os.listdir("Data")
        self.ui.listWidget.addItems(self.data_list)

        self.ui.DeleteButton.clicked.connect(self.delete_data)

        self.data = ([],[])
        self.axes = self.figure.add_subplot()

        self.axes.clear()

        self.axes.plot(self.data[0], self.data[1], color = "purple", linewidth = 0.7)
        self.axes.set_title("Random Data Series")
        self.axes.set_xlabel("Steps")
        self.axes.set_ylabel("Values")
        self.axes.grid()

        self.canvas.draw()

    def delete_data(self):
        item = self.ui.listWidget.currentItem()

        if item is not None:
            os.remove(f"Data/{item.text()}")
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        else:
            QMessageBox.information(self,"Info", "You must select a file to delete!")
            return
        

    def update_plot(self):

        self.axes.clear()

        self.axes.plot(self.data[0], self.data[1], color = "purple", linewidth = 0.7)
        self.axes.set_title("Random Data Series")
        self.axes.set_xlabel("Steps")
        self.axes.set_ylabel("Values")
        self.axes.grid()

        self.canvas.draw()

    def generate_data(self, method, start, steps, parameter):

        if method == "random_walk":
            self.data = random_walk(start, steps, parameter)

        if method == "random_mean_reverting":
            self.data = random_mean_reverting(start, steps, parameter)

        data_path = Path("Data")
        data_path.mkdir(parents=True, exist_ok=True)

        now = arrow.now()
        name = f"{method}_{now.format('YYYY_MM_DD_HHmmss')}.csv"
        data_file = data_path / name

        with data_file.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Value"])

            for value in self.data:
                writer.writerow([value])

        self.ui.listWidget.addItem(f"{name}")

        self.update_plot()

    def open_data_window(self):

        if self.secondary_wind is None: 
            self.secondary_wind = DataCreationWindow(self)
            self.secondary_wind.parameter_submitted.connect(self.generate_data)
            self.secondary_wind.destroyed.connect(lambda: setattr(self, "secondary_wind", None))
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