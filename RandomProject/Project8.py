import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from PyQt5.QtCore import QTimer, QTime, QDateTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 100, 400, 200)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.time_label = QLabel('00:00:00', self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;"
                                       "color: black;"
                                       "background-color: white;"
                                       "border: 2px solid black;"
                                       "border-radius: 10px;"
                                       "padding: 10px;"
                                       "font-family: 'Arial';")
        vbox.addWidget(self.time_label)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start)
        vbox.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop)
        vbox.addWidget(self.stop_button)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset)
        vbox.addWidget(self.reset_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.elapsed_time = 0
        self.is_running = False
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = QDateTime.currentDateTime()
            self.timer.start(1000)
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.timer.stop()
            
    def reset(self):
        self.elapsed_time = 0
        self.update_time()
    def update_time(self):
        if self.is_running:
            current_time = QDateTime.currentDateTime()
            elapsed_time_ms = current_time.toMSecsSinceEpoch()
            start_time_ms = self.start_time.toMSecsSinceEpoch()
            self.elapsed_time = elapsed_time_ms - start_time_ms
            self.update_display()
    def update_display(self):
        elapsed_time_seconds = self.elapsed_time // 1000
        minutes = elapsed_time_seconds // 60
        seconds = elapsed_time_seconds % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.time_label.setText(time_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
