import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QTime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize the label first so initUI can use it
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 400, 200) # Increased size for 150px font

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        # Apply styles
        self.time_label.setStyleSheet("font-size: 100px;" # Adjusted to fit window
                                       "color: black;"
                                       "background-color: white;"
                                       "border: 2px solid black;"
                                       "border-radius: 10px;"
                                       "padding: 10px;"
                                       "font-family: 'Arial';")
        self.setStyleSheet("background-color: white;")

        # Connect the timer to the showTime function
        self.timer.timeout.connect(self.showTime)
        # Update every 1000 milliseconds (1 second)
        self.timer.start(1000)

        # Show time immediately on startup
        self.showTime()

    def showTime(self):
        # Use QTime.currentTime() to get the system time
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())